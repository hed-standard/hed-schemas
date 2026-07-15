#!/usr/bin/env python3
"""Keep ``schemas_latest_json/`` in sync with the latest *released* JSON schema of each library.

``schemas_latest_json/`` holds one convenience copy of the newest released JSON schema per library:

    schemas_latest_json/HEDLatest.json          <- standard_schema/hedjson/HED<latest>.json
    schemas_latest_json/HED_score_Latest.json   <- library_schemas/score/hedjson/HED_score_<latest>.json
    schemas_latest_json/HED_lang_Latest.json    <- library_schemas/lang/hedjson/HED_lang_<latest>.json

These are currently maintained by hand. This script verifies (or fixes) that each ``*_Latest.json``
is a byte-for-byte copy of the current latest released JSON, by comparing git blob SHAs.

"Latest released" is determined from the canonical released set in ``<area>/hedxml/`` (the released
XML files), and the matching JSON is taken from ``<area>/hedjson/``. A library whose latest released
XML has no corresponding ``hedjson`` file is reported as a warning (the JSON has not been exported
yet) rather than silently skipped.

testlib is deliberately excluded: its versions are mutable "released" schemas used only for testing
and must never appear in ``schemas_latest_json/``. Any ``*_Latest.json`` found for an excluded
library is reported so it can be removed.

Usage::

    python scripts/update_latest_json.py --check     # exit 1 if anything is out of sync (CI gate)
    python scripts/update_latest_json.py --update     # copy the latest released JSON into place
    python scripts/update_latest_json.py              # same as --check (read-only by default)
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from hashlib import sha1
from pathlib import Path

STANDARD_AREA = "standard_schema"
LIBRARY_AREA = "library_schemas"
LATEST_JSON_DIR = "schemas_latest_json"

# Libraries that must never appear in schemas_latest_json/ (mutable test-only schemas).
EXCLUDED_LIBRARIES = {"testlib"}

# Released-XML version pattern (mirrors hed.schema.hed_cache). Used to find the latest released
# version from the canonical hedxml/ folder. group(2) = library name (or None for standard),
# group(3) = version.
_HED_VERSION_CORE = (
    r"(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)"
    r"(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?"
)
_XML_RE = re.compile(r"^[hH][eE][dD](_([a-z0-9]+)_)?(" + _HED_VERSION_CORE + r")\.[xX][mM][lL]$")


def git_blob_sha(path: Path) -> str:
    """Return the git blob SHA-1 of a file (identical to GitHub's contents-API ``sha``)."""
    data = path.read_bytes()
    hasher = sha1()
    hasher.update(f"blob {len(data)}\0".encode())
    hasher.update(data)
    return hasher.hexdigest()


def _version_key(version: str) -> tuple:
    """Ascending sort key; a final release outranks its own prereleases."""
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-(.+))?$", version)
    if not match:
        return (-1, -1, -1, 1, version)
    major, minor, patch, pre = match.groups()
    return (int(major), int(minor), int(patch), 0 if pre else 1, pre or "")


def latest_released_version(hedxml_dir: Path) -> str | None:
    """Return the newest released version string in a ``hedxml/`` folder, or None if empty."""
    if not hedxml_dir.is_dir():
        return None
    versions = []
    for name in os.listdir(hedxml_dir):
        if not (hedxml_dir / name).is_file():
            continue
        match = _XML_RE.match(name)
        if match is not None:
            versions.append(match.group(3))
    if not versions:
        return None
    return sorted(versions, key=_version_key)[-1]


def released_json_name(library: str, version: str) -> str:
    """Filename of a specific released JSON schema. ``library`` is '' for the standard schema."""
    return f"HED{version}.json" if not library else f"HED_{library}_{version}.json"


def latest_json_name(library: str) -> str:
    """Filename of the *_Latest.json copy. ``library`` is '' for the standard schema."""
    return "HEDLatest.json" if not library else f"HED_{library}_Latest.json"


def discover_libraries(repo_root: Path) -> list[str]:
    """Return library keys to manage: '' (standard) plus every non-excluded library folder."""
    libraries = [""]  # standard schema
    library_root = repo_root / LIBRARY_AREA
    if library_root.is_dir():
        for name in sorted(os.listdir(library_root)):
            if name in EXCLUDED_LIBRARIES:
                continue
            if (library_root / name).is_dir():
                libraries.append(name)
    return libraries


def area_dir(repo_root: Path, library: str) -> Path:
    """Path to the schema area for a library key ('' -> standard_schema)."""
    return repo_root / STANDARD_AREA if not library else repo_root / LIBRARY_AREA / library


def check_and_update(repo_root: Path, do_update: bool) -> tuple[list[str], list[str], list[str]]:
    """Compare (and optionally fix) every managed *_Latest.json.

    Returns (updated, in_sync, problems) as lists of human-readable messages.
    """
    latest_dir = repo_root / LATEST_JSON_DIR
    updated: list[str] = []
    in_sync: list[str] = []
    problems: list[str] = []

    if do_update:
        latest_dir.mkdir(parents=True, exist_ok=True)

    for library in discover_libraries(repo_root):
        area = area_dir(repo_root, library)
        label = "standard" if not library else library

        version = latest_released_version(area / "hedxml")
        if version is None:
            # No released XML for this library (e.g. slam/mouse only have prereleases) -> it has
            # no "latest released JSON" to publish, so it correctly gets no *_Latest.json.
            continue

        source = area / "hedjson" / released_json_name(library, version)
        target = latest_dir / latest_json_name(library)

        if not source.exists():
            problems.append(
                f"{label}: latest released version is {version} but its JSON "
                f"({source.relative_to(repo_root).as_posix()}) is missing - cannot update "
                f"{target.name}. Export the JSON schema for {version}."
            )
            continue

        source_sha = git_blob_sha(source)
        target_sha = git_blob_sha(target) if target.exists() else None

        if source_sha == target_sha:
            in_sync.append(f"{label}: {target.name} matches {source.name} (sha {source_sha[:10]}).")
            continue

        if do_update:
            shutil.copyfile(source, target)
            verb = "created" if target_sha is None else "updated"
            updated.append(f"{label}: {verb} {target.name} from {source.name} (sha {source_sha[:10]}).")
        else:
            detail = "missing" if target_sha is None else f"has sha {target_sha[:10]}"
            problems.append(
                f"{label}: {target.name} is out of date ({detail}; expected {source_sha[:10]} from {source.name})."
            )

    # Flag any stray *_Latest.json that belongs to an excluded library (e.g. a testlib copy that
    # should not exist here).
    if latest_dir.is_dir():
        for name in sorted(os.listdir(latest_dir)):
            match = re.match(r"^HED_([a-z0-9]+)_Latest\.json$", name)
            if match and match.group(1) in EXCLUDED_LIBRARIES:
                problems.append(
                    f"{match.group(1)}: {name} should not be in {LATEST_JSON_DIR}/ "
                    f"({match.group(1)} is excluded); remove it."
                )

    return updated, in_sync, problems


def main() -> int:
    """CLI entry point."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Path to the hed-schemas repository root (default: parent of this script's directory).",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Read-only. Exit 1 if anything is out of sync (default).")
    group.add_argument("--update", action="store_true", help="Copy the latest released JSON into schemas_latest_json/.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    do_update = args.update

    updated, in_sync, problems = check_and_update(repo_root, do_update)

    for msg in in_sync:
        print(f"OK       {msg}")
    for msg in updated:
        print(f"UPDATED  {msg}")
    for msg in problems:
        print(f"PROBLEM  {msg}", file=sys.stderr)

    if do_update:
        print(f"\nDone: {len(updated)} updated, {len(in_sync)} already in sync, {len(problems)} problem(s).")
        # In update mode, a "problem" means something we could not fix (e.g. missing source JSON).
        return 1 if problems else 0

    # Check mode: any drift or problem is a failure.
    if problems:
        print(
            f"\nCHECK FAILED: {len(problems)} item(s) out of sync. Run update_latest_json.py --update.", file=sys.stderr
        )
        return 1
    print(f"\nCHECK OK: all {len(in_sync)} latest-JSON copies are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
