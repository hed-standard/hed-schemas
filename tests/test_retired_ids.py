#!/usr/bin/env python3
"""Consistency checks for the ``retired_ids`` registry in ``library_data.json``.

A hedId is permanent. When an element is removed from a released schema, or an id is assigned in
a prerelease and then withdrawn before release, the id goes into ``retired_ids`` for the owning
schema and must never be reassigned. These tests keep the registry honest against the real
schema files in the repository:

- every retired id is well formed and lies inside its owner's ``id_range``;
- no id is claimed by two owners, and no retired id is also live in a prerelease;
- a retired id is absent from every prerelease schema and from every released schema newer than
  its ``last_version``;
- ``last_version`` (when given) is a real released version of that schema.

Run from the repository root::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIBRARY_DATA = REPO_ROOT / "library_data.json"
SCHEMA_VERSIONS = REPO_ROOT / "schema_versions.json"

HED_ID_PATTERN = re.compile(r"^HED_(\d{7})$")
HED_ID_IN_TEXT = re.compile(r"hedId=(HED_\d{7})")
SECTIONS = {"tags", "unitClasses", "units", "unitModifiers", "valueClasses", "attributes", "properties"}
REQUIRED_FIELDS = {"label", "section", "last_version", "removed_in", "reason"}
OPTIONAL_FIELDS = {"replacement", "reference"}


def _schema_dir(library: str) -> Path:
    """Return the directory holding a schema's files ("" is the standard schema)."""
    return REPO_ROOT / "standard_schema" if library == "" else REPO_ROOT / "library_schemas" / library


def _version_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def _ids_in(path: Path) -> set[str]:
    return set(HED_ID_IN_TEXT.findall(path.read_text(encoding="utf-8")))


class TestRetiredIds(unittest.TestCase):
    """Validate ``retired_ids`` against the id ranges and the schema files on disk."""

    @classmethod
    def setUpClass(cls):
        cls.library_data = json.loads(LIBRARY_DATA.read_text(encoding="utf-8"))
        cls.versions = json.loads(SCHEMA_VERSIONS.read_text(encoding="utf-8"))["libraries"]
        cls.retired = {library: data.get("retired_ids", {}) for library, data in cls.library_data.items()}

    def test_registry_shape(self):
        """``retired_ids`` is an object keyed by hedId with the agreed fields."""
        for library, entries in self.retired.items():
            self.assertIsInstance(entries, dict, f"{library!r}: retired_ids must be an object keyed by hedId")
            for hed_id, entry in entries.items():
                with self.subTest(library=library, hed_id=hed_id):
                    self.assertRegex(hed_id, HED_ID_PATTERN)
                    self.assertIsInstance(entry, dict)
                    missing = REQUIRED_FIELDS - entry.keys()
                    unknown = entry.keys() - REQUIRED_FIELDS - OPTIONAL_FIELDS
                    self.assertFalse(missing, f"missing fields {sorted(missing)}")
                    self.assertFalse(unknown, f"unknown fields {sorted(unknown)}")
                    self.assertIn(entry["section"], SECTIONS)
                    self.assertTrue(entry["label"].strip())
                    self.assertTrue(entry["reason"].strip())
                    self.assertRegex(entry["removed_in"], r"^\d+\.\d+\.\d+$")
                    if entry["last_version"] is not None:
                        self.assertRegex(entry["last_version"], r"^\d+\.\d+\.\d+$")
                        self.assertLess(_version_tuple(entry["last_version"]), _version_tuple(entry["removed_in"]))
                    for text in (entry["label"], entry["reason"], entry.get("replacement") or ""):
                        self.assertTrue(text.isascii(), f"non-ASCII text in entry: {text!r}")

    def test_ids_within_owner_range(self):
        """Every retired id lies inside the id_range of the schema that lists it."""
        for library, entries in self.retired.items():
            low, high = self.library_data[library]["id_range"]
            for hed_id in entries:
                with self.subTest(library=library, hed_id=hed_id):
                    match = HED_ID_PATTERN.match(hed_id)
                    self.assertIsNotNone(match, f"{hed_id} is not a well-formed hedId (HED_ + 7 digits)")
                    number = int(match.group(1))
                    self.assertTrue(low <= number <= high, f"{hed_id} outside [{low}, {high}]")

    def test_ids_unique_across_registry(self):
        """No hedId is retired under two owners."""
        seen: dict[str, str] = {}
        for library, entries in self.retired.items():
            for hed_id in entries:
                self.assertNotIn(hed_id, seen, f"{hed_id} listed by both {seen.get(hed_id)!r} and {library!r}")
                seen[hed_id] = library

    def test_retired_ids_absent_from_prereleases(self):
        """A retired id must not be live in any prerelease schema of any library."""
        prerelease_files = list(REPO_ROOT.glob("standard_schema/prerelease/*.mediawiki")) + list(
            REPO_ROOT.glob("library_schemas/*/prerelease/*.mediawiki")
        )
        self.assertTrue(prerelease_files, "no prerelease .mediawiki files found")
        live = {path: _ids_in(path) for path in prerelease_files}
        for library, entries in self.retired.items():
            for hed_id in entries:
                for path, ids in live.items():
                    with self.subTest(library=library, hed_id=hed_id, file=path.name):
                        self.assertFalse(hed_id in ids, f"{hed_id} is retired but still present in {path}")

    def test_retired_ids_absent_from_newer_releases(self):
        """A retired id appears in no released schema newer than its last_version."""
        for library, entries in self.retired.items():
            released = self.versions.get(library, {}).get("released", [])
            for hed_id, entry in entries.items():
                last = entry["last_version"]
                for release in released:
                    if last is not None and _version_tuple(release["version"]) <= _version_tuple(last):
                        continue
                    wiki = _schema_dir(library) / "hedwiki" / Path(release["file"]).with_suffix(".mediawiki").name
                    if not wiki.exists():
                        continue
                    with self.subTest(library=library, hed_id=hed_id, version=release["version"]):
                        self.assertFalse(hed_id in _ids_in(wiki), f"{hed_id} present in {wiki.name}")

    def test_last_version_is_a_real_release(self):
        """A non-null last_version names a released version of the owning schema."""
        for library, entries in self.retired.items():
            released = {r["version"] for r in self.versions.get(library, {}).get("released", [])}
            for hed_id, entry in entries.items():
                last = entry["last_version"]
                if last is None:
                    continue
                with self.subTest(library=library, hed_id=hed_id):
                    self.assertIn(last, released, f"{last} is not a released version of {library or 'standard'}")
                    wiki = _schema_dir(library) / "hedwiki"
                    name = f"HED{last}.mediawiki" if library == "" else f"HED_{library}_{last}.mediawiki"
                    self.assertTrue(hed_id in _ids_in(wiki / name), f"{hed_id} not found in {name}")


if __name__ == "__main__":
    unittest.main()
