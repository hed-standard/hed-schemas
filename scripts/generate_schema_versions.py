#!/usr/bin/env python3
"""Generate ``schema_versions.json`` - a single manifest of every HED schema version.

The manifest is a *listing* only: it records, for the standard schema and every library, which
versions exist (released / prerelease / deprecated) together with each XML file's git blob SHA and
last-commit date. It never contains schema content.

Why this file exists
--------------------
hedtools (``hed.schema.get_available_hed_versions``) currently discovers versions by crawling the
GitHub *REST API* directory listings - one request for the standard schema, one to enumerate the
library folders, and two more (hedxml + prerelease) per library. Unauthenticated, that is dozens of
requests against GitHub's 60-per-hour anonymous cap. A consumer can instead fetch this one manifest
from ``raw.githubusercontent.com`` (CDN-served, not subject to the REST API rate limit) and get the
whole catalog in a single request, falling back to the API crawl only if the manifest is missing.

The blob SHAs recorded here are computed exactly the way git (and therefore the GitHub "contents"
API ``sha`` field, and hedtools' ``_calculate_sha1``) computes them, so a consumer can compare a
manifest SHA directly against a cached file's SHA to decide whether a re-download is needed. Line
endings are normalized to LF before hashing (matching the repo's ``.gitattributes`` ``eol=lf``), so
the manifest is identical whether generated on a Windows (CRLF) or Linux (LF) checkout.

What counts as what
-------------------
- released:   ``<area>/hedxml/*.xml``            (top level, excluding the ``deprecated`` subfolder)
- prerelease: ``<area>/prerelease/*.xml``
- deprecated: ``<area>/hedxml/deprecated/*.xml``  (best-effort; informational only)

where ``<area>`` is ``standard_schema`` (library key ``""``) or ``library_schemas/<name>``.

Only ``.xml`` files whose names match the HED version pattern are included; ``.xsd``/``.mediawiki``
files and the un-versioned ``HEDLatest.xml`` / ``HED_<lib>_Latest.xml`` pointers are ignored. Note
that a few very old deprecated files use non-semver names (e.g. ``HED1.3.xml``); those do not match
the pattern and are intentionally omitted from the deprecated listing.

Determinism and ``--check``
---------------------------
Output is sorted and stably ordered. ``--check`` compares only schema *content* - which versions
exist and each file's blob SHA - and ignores volatile git metadata (``generated``, ``repo_commit``,
and each entry's ``date``), so it never fails just because CI checked out a different commit (e.g. a
PR merge commit) than the one the file was generated on. When it does fail, it prints exactly which
entries were added, removed, or changed. Writing is likewise content-aware: if the committed manifest
already matches the current schema files, a normal run leaves it untouched instead of rewriting the
timestamp.

Usage::

    python scripts/generate_schema_versions.py            # write schema_versions.json at repo root
    python scripts/generate_schema_versions.py --check     # exit 1 if the committed file is stale
    python scripts/generate_schema_versions.py --repo-root /path/to/hed-schemas -o /tmp/out.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from hashlib import sha1
from pathlib import Path

# Mirrors hed.schema.hed_cache.HED_VERSION_FINAL so this script and hedtools agree on exactly
# which filenames are versioned schemas and how the (library, version) split is made.
_HED_VERSION_P1 = r"(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
_HED_VERSION_P2 = (
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
)
_HED_VERSION_P3 = r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
_HED_VERSION = _HED_VERSION_P1 + _HED_VERSION_P2 + _HED_VERSION_P3
_HED_VERSION_FINAL = r"^[hH][eE][dD](_([a-z0-9]+)_)?(" + _HED_VERSION + r")\.[xX][mM][lL]$"
_VERSION_RE = re.compile(_HED_VERSION_FINAL)

STANDARD_AREA = "standard_schema"
LIBRARY_AREA = "library_schemas"
STANDARD_LIBRARY_KEY = ""  # matches library_data.json's convention for the standard schema
OUTPUT_FILENAME = "schema_versions.json"
MANIFEST_FORMAT_VERSION = 1


def git_blob_sha(path: Path) -> str:
    """Return the git blob SHA-1 of a file's text, matching GitHub's contents-API ``sha``.

    CRLF line endings are normalized to LF before hashing, mirroring the repository's
    ``.gitattributes`` (``*.xml text eol=lf``). Git stores these files with LF, so its blob SHA -
    and therefore the value the GitHub API and raw host report - is the LF SHA regardless of a
    checkout's working-tree line endings. Hashing the raw bytes instead would make the manifest
    depend on whether it was generated on a CRLF (e.g. Windows) or LF (e.g. Linux CI) checkout,
    which would spuriously fail ``--check`` even though the committed content is identical.
    """
    data = path.read_bytes().replace(b"\r\n", b"\n")
    hasher = sha1()
    hasher.update(f"blob {len(data)}\0".encode())
    hasher.update(data)
    return hasher.hexdigest()


def git_iso_date(path: Path, repo_root: Path) -> str:
    """Return the ISO-8601 date of the last commit touching ``path``.

    Falls back to the file's modification time if git history is unavailable (e.g. running from a
    tarball rather than a checkout, or a shallow clone that doesn't include the file's last commit).
    """
    try:
        rel = path.relative_to(repo_root).as_posix()
        result = subprocess.run(
            ["git", "-C", str(repo_root), "log", "-1", "--format=%cI", "--", rel],
            capture_output=True,
            text=True,
            check=False,
        )
        date = result.stdout.strip()
        if date:
            return date
    except (OSError, ValueError):
        pass
    # Fallback: filesystem mtime as UTC ISO-8601.
    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    return mtime.isoformat()


def repo_head_sha(repo_root: Path) -> str | None:
    """Return the current HEAD commit SHA, or None if not in a git checkout."""
    result = subprocess.run(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        capture_output=True,
        text=True,
        check=False,
    )
    sha = result.stdout.strip()
    return sha or None


def _version_sort_key(version: str) -> tuple:
    """Sort key for HED versions, newest first when used with reverse=True.

    Released versions (no prerelease suffix) sort above prereleases of the same x.y.z, matching
    semantic-versioning precedence. SemVer build metadata (the ``+...`` suffix) is stripped and
    ignored for ordering. Anything unparsable sorts last.
    """
    core = version.split("+", 1)[0]  # drop SemVer build metadata; it does not affect precedence
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-(.+))?$", core)
    if not match:
        return (-1, -1, -1, 1, version)
    major, minor, patch, pre = match.groups()
    # pre is None for a final release -> (…, 1, "") sorts *after* a prerelease (…, 0, pre) when
    # reverse=True, i.e. the release is "newer" than its own prereleases. Correct.
    return (int(major), int(minor), int(patch), 0 if pre else 1, pre or "")


def _scan_folder(folder: Path, repo_root: Path) -> dict[str, list[dict]]:
    """Scan one flat folder of schema XML files, grouped by parsed library key.

    Returns ``{library_key: [ {version, file, sha, date}, ... ]}``. Non-matching files (``.xsd``,
    ``*Latest.xml``, prose, subdirectories) are silently skipped.
    """
    grouped: dict[str, list[dict]] = {}
    if not folder.is_dir():
        return grouped
    for name in sorted(os.listdir(folder)):
        path = folder / name
        if not path.is_file():
            continue
        match = _VERSION_RE.match(name)
        if match is None:
            continue
        library_key = match.group(2) or STANDARD_LIBRARY_KEY  # group(2) is the library name or None
        version = match.group(3)
        grouped.setdefault(library_key, []).append(
            {
                "version": version,
                "file": path.relative_to(repo_root).as_posix(),
                "sha": git_blob_sha(path),
                "date": git_iso_date(path, repo_root),
            }
        )
    for entries in grouped.values():
        entries.sort(key=lambda e: _version_sort_key(e["version"]), reverse=True)
    return grouped


def _merge(dest: dict[str, dict[str, list[dict]]], category: str, scanned: dict[str, list[dict]]) -> None:
    """Fold a scanned ``{library: [entries]}`` result into the manifest under ``category``."""
    for library_key, entries in scanned.items():
        dest.setdefault(library_key, {"released": [], "prerelease": [], "deprecated": []})
        dest[library_key][category] = entries


def build_manifest(repo_root: Path) -> dict:
    """Build the full manifest dictionary for the repository rooted at ``repo_root``."""
    libraries: dict[str, dict[str, list[dict]]] = {}

    # Standard schema (library key "").
    standard = repo_root / STANDARD_AREA
    _merge(libraries, "released", _scan_folder(standard / "hedxml", repo_root))
    _merge(libraries, "prerelease", _scan_folder(standard / "prerelease", repo_root))
    _merge(libraries, "deprecated", _scan_folder(standard / "hedxml" / "deprecated", repo_root))

    # Every library under library_schemas/.
    library_root = repo_root / LIBRARY_AREA
    if library_root.is_dir():
        for lib_name in sorted(os.listdir(library_root)):
            lib_dir = library_root / lib_name
            if not lib_dir.is_dir():
                continue
            _merge(libraries, "released", _scan_folder(lib_dir / "hedxml", repo_root))
            _merge(libraries, "prerelease", _scan_folder(lib_dir / "prerelease", repo_root))
            _merge(libraries, "deprecated", _scan_folder(lib_dir / "hedxml" / "deprecated", repo_root))

    # Drop libraries that turned out to have no versioned files at all (e.g. a folder that only
    # holds a stray .xsd), so the manifest lists only real schema libraries.
    libraries = {
        key: cats
        for key, cats in sorted(libraries.items())
        if cats["released"] or cats["prerelease"] or cats["deprecated"]
    }

    return {
        "manifest_format_version": MANIFEST_FORMAT_VERSION,
        "generated": datetime.now(tz=timezone.utc).isoformat(),
        "repo_commit": repo_head_sha(repo_root),
        "libraries": libraries,
    }


def _label(library_key: str) -> str:
    """Human-readable name for a library key ('' -> 'standard')."""
    return "standard" if library_key == "" else library_key


def _content_index(manifest: dict) -> dict:
    """Flatten a manifest to ``{(library, category, version): {"file", "sha"}}`` for diffing.

    Deliberately excludes the volatile / history-derived fields (``generated``, ``repo_commit``, and
    each entry's ``date``) so that a change in git metadata alone never counts as the manifest being
    "out of date" - only a real change to which schema files exist, or their content (SHA), does.
    This is what keeps the ``--check`` gate stable across different checkouts: a pull request's
    merge-commit checkout in CI has a different HEAD SHA (and can have different commit dates) than
    the commit the file was generated on, but the same schema content.
    """
    index: dict[tuple, dict] = {}
    for library_key, categories in manifest.get("libraries", {}).items():
        for category, entries in categories.items():
            for entry in entries:
                index[(library_key, category, entry.get("version"))] = {
                    "file": entry.get("file"),
                    "sha": entry.get("sha"),
                }
    return index


def _diff_manifests(existing: dict, fresh: dict) -> list[str]:
    """Return a human-readable list of the content differences between two manifests.

    An empty list means the two are equivalent for ``--check``/rewrite purposes.
    """
    diffs: list[str] = []

    old_fmt = existing.get("manifest_format_version")
    new_fmt = fresh.get("manifest_format_version")
    if old_fmt != new_fmt:
        diffs.append(f"manifest_format_version: {old_fmt} -> {new_fmt}")

    old_index = _content_index(existing)
    new_index = _content_index(fresh)

    def where(key: tuple) -> str:
        library_key, category, version = key
        return f"{_label(library_key)} / {category} / {version}"

    for key in sorted(new_index.keys() - old_index.keys()):
        entry = new_index[key]
        diffs.append(f"added:   {where(key)}  ({entry['file']}, sha {(entry['sha'] or '')[:10]})")
    for key in sorted(old_index.keys() - new_index.keys()):
        entry = old_index[key]
        diffs.append(f"removed: {where(key)}  (was {entry['file']}, sha {(entry['sha'] or '')[:10]})")
    for key in sorted(old_index.keys() & new_index.keys()):
        old_entry = old_index[key]
        new_entry = new_index[key]
        changed = []
        if old_entry["sha"] != new_entry["sha"]:
            changed.append(f"sha {(old_entry['sha'] or '')[:10]} -> {(new_entry['sha'] or '')[:10]}")
        if old_entry["file"] != new_entry["file"]:
            changed.append(f"file {old_entry['file']} -> {new_entry['file']}")
        if changed:
            diffs.append(f"changed: {where(key)}  ({'; '.join(changed)})")

    return diffs


def _serialize(manifest: dict) -> bytes:
    """Serialize manifest as JSON with LF line endings (not platform-specific)."""
    return (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Path to the hed-schemas repository root (default: parent of this script's directory).",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=None,
        help=f"Output path (default: <repo-root>/{OUTPUT_FILENAME}).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Do not write. Compare the committed manifest against the current schema files and, if "
        "they differ, exit 1 after listing exactly which entries were added/removed/changed. Only "
        "schema content is compared; volatile git metadata (generated/repo_commit/date) is ignored.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    output_path = Path(args.output) if args.output else repo_root / OUTPUT_FILENAME

    manifest = build_manifest(repo_root)

    if args.check:
        if not output_path.exists():
            print(f"CHECK FAILED: {output_path} does not exist. Run generate_schema_versions.py.", file=sys.stderr)
            return 1
        try:
            existing = json.loads(output_path.read_text(encoding="utf-8"))
        except ValueError as exc:
            print(f"CHECK FAILED: {output_path} is not valid JSON: {exc}", file=sys.stderr)
            return 1
        diffs = _diff_manifests(existing, manifest)
        if diffs:
            print(f"CHECK FAILED: {output_path} is out of date ({len(diffs)} difference(s)):", file=sys.stderr)
            for line in diffs:
                print(f"  {line}", file=sys.stderr)
            print("Run: python scripts/generate_schema_versions.py", file=sys.stderr)
            return 1
        print(f"CHECK OK: {output_path} matches the current schema files.")
        return 0

    # Write mode. Skip rewriting when the committed file already reflects the current schema content,
    # so repeated runs don't churn the generated/repo_commit/date fields (or the git history).
    if output_path.exists():
        try:
            existing = json.loads(output_path.read_text(encoding="utf-8"))
        except ValueError:
            existing = None
        if existing is not None and not _diff_manifests(existing, manifest):
            print(f"{output_path} already reflects the current schema files; not rewriting.")
            return 0

    output_path.write_bytes(_serialize(manifest))
    total = sum(
        len(c["released"]) + len(c["prerelease"]) + len(c["deprecated"]) for c in manifest["libraries"].values()
    )
    print(f"Wrote {output_path} ({len(manifest['libraries'])} libraries, {total} version entries).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
