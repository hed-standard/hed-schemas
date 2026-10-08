#!/usr/bin/env python3
"""Keep ``schemas_latest_json/`` in sync with the latest *released* version of each schema.

``schemas_latest_json/`` holds one merged JSON copy of the newest released version of each schema:

    schemas_latest_json/HEDLatest.json          <- standard_schema/hedjson/HED<latest>.json (copied)
    schemas_latest_json/HED_score_Latest.json   <- library_schemas/score/hedxml/HED_score_<latest>.xml (converted)
    schemas_latest_json/HED_lang_Latest.json    <- library_schemas/lang/hedxml/HED_lang_<latest>.xml (converted)

The repository rule (README, "HED formats"): ``hedjson/`` is unmerged, ``hedxml/`` is merged, and
``schemas_latest_json/`` is merged. So a library's Latest copy cannot be copied from ``hedjson/``;
it is generated from the merged released XML with hedtools (``load_schema(xml).get_as_json_string()``).
The standard schema has no merged/unmerged distinction, so its copy is taken from ``hedjson/`` byte
for byte, with no hedtools dependency.

"Latest released" is determined from the canonical released set in ``<area>/hedxml/``. A standard
version whose ``hedjson/`` file is missing is reported as a problem (export the JSON first).

testlib is deliberately excluded: its versions are mutable "released" schemas used only for testing
and must never appear in ``schemas_latest_json/``. Any ``*_Latest.json`` found for an excluded
library is reported so it can be removed.

Generating a library's JSON needs hedtools (``pip install git+https://github.com/hed-standard/hed-python.git@main``).
The output depends on the hedtools version, so after hedtools changes its JSON writer ``--check`` can
report a library out of date; ``--update`` then rewrites the copy.

Usage::

    python scripts/update_latest_json.py --check     # exit 1 if anything is out of sync (CI gate)
    python scripts/update_latest_json.py --update     # write the latest released JSON into place
    python scripts/update_latest_json.py              # same as --check (read-only by default)
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections.abc import Callable
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

Converter = Callable[[Path], str]


def git_blob_sha(path: Path) -> str:
    """Return the git blob SHA-1 of a file's text, matching GitHub's contents-API ``sha``.

    CRLF line endings are normalized to LF before hashing, mirroring the repository's
    ``.gitattributes`` (``*.json text eol=lf``), so the comparison is stable regardless of a
    checkout's working-tree line endings (e.g. Windows CRLF vs Linux LF).
    """
    return text_blob_sha(path.read_bytes())


def text_blob_sha(data: bytes | str) -> str:
    """Return the git blob SHA-1 of text or bytes, with CRLF normalized to LF first."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    data = data.replace(b"\r\n", b"\n")
    hasher = sha1()
    hasher.update(f"blob {len(data)}\0".encode())
    hasher.update(data)
    return hasher.hexdigest()


def merged_json_with_hedtools(xml_path: Path) -> str:
    """Convert a released (merged) XML schema to its merged JSON text with hedtools.

    Raises ImportError when hedtools is not installed; schema load errors propagate as hedtools'
    ``HedFileError``.
    """
    from hed.schema import load_schema  # imported here so the rest of the script works without hedtools

    return load_schema(str(xml_path)).get_as_json_string(save_merged=True)


def _version_key(version: str) -> tuple:
    """Ascending sort key; a final release outranks its own prereleases.

    SemVer build metadata (the ``+...`` suffix) is stripped before parsing and ignored for
    ordering, per SemVer precedence rules. This is required because latest_released_version()
    extracts versions with a grammar (``_HED_VERSION_CORE``) that permits ``+...``; without this,
    such a version would fail to parse and sort as ``(-1, -1, -1, ...)``, wrongly ranking it lowest.
    """
    core = version.split("+", 1)[0]  # drop build metadata; it does not affect precedence
    match = re.match(r"^(\d+)\.(\d+)\.(\d+)(?:-(.+))?$", core)
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


def released_xml_name(library: str, version: str) -> str:
    """Filename of a specific released XML schema. ``library`` is '' for the standard schema."""
    return f"HED{version}.xml" if not library else f"HED_{library}_{version}.xml"


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


def latest_json_text(area: Path, library: str, version: str, converter: Converter) -> tuple[Path, str]:
    """Return (source path, text) for a schema's Latest copy.

    The standard schema's text is its ``hedjson/`` file as is. A library's text is the merged JSON
    generated from its released ``hedxml/`` file by ``converter``.

    Raises FileNotFoundError when the source file is missing.
    """
    if not library:
        source = area / "hedjson" / released_json_name(library, version)
        if not source.exists():
            raise FileNotFoundError(source)
        return source, source.read_text(encoding="utf-8")
    source = area / "hedxml" / released_xml_name(library, version)
    if not source.exists():
        raise FileNotFoundError(source)
    return source, converter(source)


def check_and_update(
    repo_root: Path, do_update: bool, converter: Converter | None = None
) -> tuple[list[str], list[str], list[str]]:
    """Compare (and optionally fix) every managed *_Latest.json.

    ``converter`` turns a library's released XML path into merged JSON text; the default uses
    hedtools. Tests pass their own.

    Returns (updated, in_sync, problems) as lists of human-readable messages.
    """
    if converter is None:
        converter = merged_json_with_hedtools
    latest_dir = repo_root / LATEST_JSON_DIR
    updated: list[str] = []
    in_sync: list[str] = []
    problems: list[str] = []
    expected_targets: set[str] = set()  # *_Latest.json filenames that are legitimately expected

    if do_update:
        latest_dir.mkdir(parents=True, exist_ok=True)

    for library in discover_libraries(repo_root):
        area = area_dir(repo_root, library)
        label = "standard" if not library else library

        version = latest_released_version(area / "hedxml")
        if version is None:
            # No released XML for this library (e.g. slam/mouse only have prereleases) -> it has
            # no "latest released JSON" to publish, so it correctly gets no *_Latest.json. Its name
            # is deliberately left out of expected_targets so a stray copy is caught by the scan below.
            continue
        # This library legitimately owns a *_Latest.json slot (even if its source turns out to be
        # unusable below); record it so the stray-file scan doesn't misreport it.
        expected_targets.add(latest_json_name(library))
        target = latest_dir / latest_json_name(library)

        try:
            source, text = latest_json_text(area, library, version, converter)
        except FileNotFoundError as e:
            missing = Path(str(e))
            problems.append(
                f"{label}: latest released version is {version} but {missing.relative_to(repo_root).as_posix()} "
                f"is missing - cannot update {target.name}. Export it for {version}."
            )
            continue
        except ImportError:
            problems.append(
                f"{label}: generating {target.name} needs hedtools "
                "(pip install git+https://github.com/hed-standard/hed-python.git@main)."
            )
            continue
        except Exception as e:  # noqa: BLE001 - a conversion failure is reported, not raised
            problems.append(f"{label}: cannot convert {released_xml_name(library, version)} to JSON: {e}")
            continue

        how = "copied from" if not library else "generated (merged) from"
        source_sha = text_blob_sha(text)
        target_sha = git_blob_sha(target) if target.exists() else None

        if source_sha == target_sha:
            in_sync.append(f"{label}: {target.name} matches {source.name} (sha {source_sha[:10]}).")
            continue

        if do_update:
            with open(target, "w", encoding="utf-8", newline="\n") as fp:
                fp.write(text.replace("\r\n", "\n"))
            verb = "created" if target_sha is None else "updated"
            updated.append(f"{label}: {verb} {target.name}, {how} {source.name} (sha {source_sha[:10]}).")
        else:
            detail = "missing" if target_sha is None else f"has sha {target_sha[:10]}"
            problems.append(
                f"{label}: {target.name} is out of date ({detail}; expected {source_sha[:10]}, {how} {source.name})."
            )

    # Flag any *_Latest.json in the directory that we do not expect to be there. Something is
    # expected only if a library legitimately owns that slot (standard, or a library with a
    # released version). Everything else is a stray: an excluded library (testlib), a
    # prerelease-only library (mouse, slam), or a leftover from a removed/renamed library.
    if latest_dir.is_dir():
        for name in sorted(os.listdir(latest_dir)):
            match = re.match(r"^HED(?:_([a-z0-9]+)_)?Latest\.json$", name)
            if not match or name in expected_targets:
                continue
            lib = match.group(1)
            if lib is None:
                reason = "the standard schema has no released version"
            elif lib in EXCLUDED_LIBRARIES:
                reason = f"the '{lib}' library is excluded from {LATEST_JSON_DIR}/"
            else:
                reason = f"'{lib}' has no released schema version (only prereleases, or it was removed)"
            problems.append(f"{name} should not be in {LATEST_JSON_DIR}/ ({reason}); remove it.")

    return updated, in_sync, problems


def main(converter: Converter | None = None) -> int:
    """CLI entry point. ``converter`` is for tests; the command line always uses hedtools."""
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parent.parent),
        help="Path to the hed-schemas repository root (default: parent of this script's directory).",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="Read-only. Exit 1 if anything is out of sync (default).")
    group.add_argument(
        "--update", action="store_true", help="Write the latest released JSON of each schema into schemas_latest_json/."
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    do_update = args.update

    updated, in_sync, problems = check_and_update(repo_root, do_update, converter)

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
            f"\nCHECK FAILED: {len(problems)} item(s) out of sync. "
            f"Run: python scripts/update_latest_json.py --update to write the latest released JSON "
            f"into place (then remove any stray files it reports and export any missing source JSON).",
            file=sys.stderr,
        )
        return 1
    print(f"\nCHECK OK: all {len(in_sync)} latest-JSON copies are in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
