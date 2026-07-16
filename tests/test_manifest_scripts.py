#!/usr/bin/env python3
"""Unit tests for the schema-manifest scripts in ``scripts/``.

Covers ``generate_schema_versions.py`` and ``update_latest_json.py``. Uses only the standard
library (``unittest``) and temporary directories - no network, no real schemas, no git repo
required (the scripts fall back gracefully when git history is unavailable).

Run from the repository root::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import contextlib
import io
import shutil
import sys
import tempfile
import types
import unittest
from hashlib import sha1
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


def _load(module_name: str):
    """Load a script module from source (scripts/ is not a package).

    Compiles the freshly-read source rather than using importlib's SourceFileLoader, which may
    reuse a stale ``__pycache__`` .pyc; this keeps the tests deterministic and immune to stale
    bytecode.
    """
    path = SCRIPTS_DIR / f"{module_name}.py"
    module = types.ModuleType(module_name)
    module.__file__ = str(path)
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), module.__dict__)
    return module


gsv = _load("generate_schema_versions")
ulj = _load("update_latest_json")


def _write(path: Path, text: str) -> None:
    """Write ``text`` to ``path`` (creating parents), always with LF newlines.

    Any CR/CRLF in ``text`` is normalized to LF so the on-disk bytes are deterministic across
    platforms - the hashing tests depend on exact byte content.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(normalized.encode("utf-8"))


def _run_main(module, argv: list[str]):
    """Call ``module.main()`` with a synthetic argv, capturing stdout/stderr.

    Returns (return_code, stdout, stderr).
    """
    saved = sys.argv
    sys.argv = ["prog", *argv]
    out, err = io.StringIO(), io.StringIO()
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = module.main()
        return rc, out.getvalue(), err.getvalue()
    finally:
        sys.argv = saved


def _manual_lf_blob_sha(text: str) -> str:
    data = text.encode("utf-8")
    hasher = sha1()
    hasher.update(f"blob {len(data)}\0".encode())
    hasher.update(data)
    return hasher.hexdigest()


class GitBlobShaTests(unittest.TestCase):
    """git_blob_sha must normalize CRLF -> LF so SHAs match git's committed blobs."""

    def test_crlf_and_lf_hash_identically(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            crlf = root / "crlf.xml"
            lf = root / "lf.xml"
            crlf.write_bytes(b"<HED>\r\n  <tag/>\r\n</HED>\r\n")
            lf.write_bytes(b"<HED>\n  <tag/>\n</HED>\n")
            self.assertEqual(gsv.git_blob_sha(crlf), gsv.git_blob_sha(lf))

    def test_matches_manual_lf_blob_sha(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "f.xml"
            f.write_bytes(b"hello\r\nworld\r\n")
            self.assertEqual(gsv.git_blob_sha(f), _manual_lf_blob_sha("hello\nworld\n"))

    def test_generate_and_update_agree(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "f.xml"
            f.write_bytes(b"content\r\n")
            self.assertEqual(gsv.git_blob_sha(f), ulj.git_blob_sha(f))


class VersionSortTests(unittest.TestCase):
    """Version ordering, including SemVer build-metadata handling."""

    def test_release_is_newest_and_ordering(self):
        versions = ["8.0.0", "8.4.0-rc.1", "8.4.0", "8.5.0", "8.4.1"]
        ordered = sorted(versions, key=gsv._version_sort_key)
        self.assertEqual(ordered, ["8.0.0", "8.4.0-rc.1", "8.4.0", "8.4.1", "8.5.0"])

    def test_prerelease_sorts_before_its_release(self):
        self.assertLess(gsv._version_sort_key("8.4.0-rc.1"), gsv._version_sort_key("8.4.0"))
        self.assertLess(ulj._version_key("8.4.0-rc.1"), ulj._version_key("8.4.0"))

    def test_build_metadata_ignored(self):
        # A version with SemVer build metadata must have the same precedence as the plain release,
        # not fall into the unparsable (-1, ...) bucket.
        self.assertEqual(gsv._version_sort_key("8.4.0+abc"), gsv._version_sort_key("8.4.0"))
        self.assertEqual(ulj._version_key("8.4.0+abc"), ulj._version_key("8.4.0"))
        self.assertNotEqual(gsv._version_sort_key("8.4.0+abc")[0], -1)

    def test_unparsable_sorts_last(self):
        self.assertEqual(gsv._version_sort_key("not-a-version")[0], -1)


class BuildManifestTests(unittest.TestCase):
    """build_manifest structure, categorization, filtering, and sorting."""

    def _make_repo(self, root: Path) -> None:
        _write(root / "standard_schema/hedxml/HED8.0.0.xml", "std800")
        _write(root / "standard_schema/hedxml/HED8.4.0.xml", "std840")
        _write(root / "standard_schema/hedxml/HEDLatest.xml", "pointer")  # no version -> ignored
        _write(root / "standard_schema/hedxml/HED8.4.0.xsd", "xsd")  # not .xml -> ignored
        _write(root / "standard_schema/hedxml/deprecated/HED7.2.0.xml", "dep720")
        _write(root / "standard_schema/prerelease/HED8.5.0.xml", "pre850")
        _write(root / "library_schemas/score/hedxml/HED_score_2.0.0.xml", "sc200")
        _write(root / "library_schemas/score/hedxml/HED_score_2.1.0.xml", "sc210")
        _write(root / "library_schemas/score/prerelease/HED_score_2.2.0.xml", "sc220")
        _write(root / "library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml", "mo100")  # prerelease only

    def test_structure_and_sorting(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            libs = gsv.build_manifest(root)["libraries"]

            # Standard schema uses the "" key and is newest-first, ignoring pointer/.xsd files.
            self.assertIn("", libs)
            self.assertEqual([e["version"] for e in libs[""]["released"]], ["8.4.0", "8.0.0"])
            self.assertEqual([e["version"] for e in libs[""]["prerelease"]], ["8.5.0"])
            self.assertEqual([e["version"] for e in libs[""]["deprecated"]], ["7.2.0"])

            # score: released newest-first + prerelease.
            self.assertEqual([e["version"] for e in libs["score"]["released"]], ["2.1.0", "2.0.0"])
            self.assertEqual([e["version"] for e in libs["score"]["prerelease"]], ["2.2.0"])

            # mouse: prerelease only -> present but with no released entries.
            self.assertEqual(libs["mouse"]["released"], [])
            self.assertEqual([e["version"] for e in libs["mouse"]["prerelease"]], ["1.0.0"])

    def test_entry_fields_and_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            entry = gsv.build_manifest(root)["libraries"][""]["released"][0]
            self.assertEqual(set(entry), {"version", "file", "sha", "date"})
            self.assertEqual(entry["file"], "standard_schema/hedxml/HED8.4.0.xml")  # posix, repo-relative
            self.assertEqual(entry["sha"], _manual_lf_blob_sha("std840"))


class DiffManifestTests(unittest.TestCase):
    """_diff_manifests: stable across volatile metadata, precise on real content changes."""

    def _make_repo(self, root: Path) -> None:
        _write(root / "standard_schema/hedxml/HED8.4.0.xml", "std840")
        _write(root / "library_schemas/score/hedxml/HED_score_2.1.0.xml", "sc210")

    def test_metadata_only_drift_is_no_diff(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            a = gsv.build_manifest(root)
            b = gsv.build_manifest(root)
            b["generated"] = "2000-01-01T00:00:00+00:00"
            b["repo_commit"] = "deadbeef"
            b["libraries"][""]["released"][0]["date"] = "1999-01-01T00:00:00+00:00"
            self.assertEqual(gsv._diff_manifests(a, b), [])

    def test_changed_added_removed(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            a = gsv.build_manifest(root)
            b = gsv.build_manifest(root)
            b["libraries"][""]["released"][0]["sha"] = "0" * 40  # changed
            b["libraries"]["score"]["released"].pop()  # removed score 2.1.0
            b["libraries"]["score"]["prerelease"].append(  # added
                {"version": "9.9.9", "file": "x", "sha": "abc", "date": "d"}
            )
            diffs = gsv._diff_manifests(a, b)
            joined = "\n".join(diffs)
            self.assertIn("changed: standard / released / 8.4.0", joined)
            self.assertIn("removed: score / released / 2.1.0", joined)
            self.assertIn("added:   score / prerelease / 9.9.9", joined)

    def test_format_version_change_detected(self):
        self.assertTrue(
            gsv._diff_manifests(
                {"manifest_format_version": 1, "libraries": {}},
                {"manifest_format_version": 2, "libraries": {}},
            )
        )


class GenerateMainTests(unittest.TestCase):
    """End-to-end write/check behavior of generate_schema_versions.main()."""

    def _make_repo(self, root: Path) -> None:
        _write(root / "standard_schema/hedxml/HED8.4.0.xml", "std840")
        _write(root / "library_schemas/score/hedxml/HED_score_2.1.0.xml", "sc210")

    def test_write_then_check_passes_then_fails_on_change(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            out = root / "schema_versions.json"

            rc, _, _ = _run_main(gsv, ["--repo-root", str(root), "-o", str(out)])
            self.assertEqual(rc, 0)
            self.assertTrue(out.exists())

            rc, _, _ = _run_main(gsv, ["--repo-root", str(root), "-o", str(out), "--check"])
            self.assertEqual(rc, 0)

            # Change a schema file -> check must fail and name the changed entry + remind to commit.
            _write(root / "library_schemas/score/hedxml/HED_score_2.1.0.xml", "CHANGED")
            rc, _, err = _run_main(gsv, ["--repo-root", str(root), "-o", str(out), "--check"])
            self.assertEqual(rc, 1)
            self.assertIn("changed: score / released / 2.1.0", err)
            self.assertIn("commit schema_versions.json", err)

    def test_check_missing_file_fails(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            rc, _, err = _run_main(gsv, ["--repo-root", str(root), "-o", str(root / "nope.json"), "--check"])
            self.assertEqual(rc, 1)
            self.assertIn("does not exist", err)


class LatestJsonHelperTests(unittest.TestCase):
    """Pure helpers in update_latest_json."""

    def test_name_builders(self):
        self.assertEqual(ulj.released_json_name("", "8.4.0"), "HED8.4.0.json")
        self.assertEqual(ulj.released_json_name("score", "2.1.0"), "HED_score_2.1.0.json")
        self.assertEqual(ulj.latest_json_name(""), "HEDLatest.json")
        self.assertEqual(ulj.latest_json_name("score"), "HED_score_Latest.json")

    def test_latest_released_version(self):
        with tempfile.TemporaryDirectory() as d:
            hedxml = Path(d) / "hedxml"
            _write(hedxml / "HED8.0.0.xml", "a")
            _write(hedxml / "HED8.4.0.xml", "b")
            _write(hedxml / "HEDLatest.xml", "pointer")  # ignored
            self.assertEqual(ulj.latest_released_version(hedxml), "8.4.0")
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(ulj.latest_released_version(Path(d) / "missing"))

    def test_discover_libraries_excludes_testlib(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            for lib in ("score", "lang", "mouse", "testlib"):
                (root / "library_schemas" / lib).mkdir(parents=True)
            libs = ulj.discover_libraries(root)
            self.assertIn("", libs)
            self.assertIn("score", libs)
            self.assertIn("mouse", libs)
            self.assertNotIn("testlib", libs)


class CheckAndUpdateTests(unittest.TestCase):
    """check_and_update: in-sync, drift, missing source, and stray-file detection."""

    def _make_repo(self, root: Path) -> None:
        _write(root / "standard_schema/hedxml/HED8.4.0.xml", "std")
        _write(root / "standard_schema/hedjson/HED8.4.0.json", "stdjson")
        _write(root / "library_schemas/score/hedxml/HED_score_2.1.0.xml", "sc")
        _write(root / "library_schemas/score/hedjson/HED_score_2.1.0.json", "scjson")
        _write(root / "library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml", "mo")  # prerelease only
        _write(root / "library_schemas/testlib/hedxml/HED_testlib_3.0.0.xml", "tl")
        _write(root / "library_schemas/testlib/hedjson/HED_testlib_3.0.0.json", "tljson")

    def _make_correct_latest(self, root: Path) -> None:
        ld = root / "schemas_latest_json"
        ld.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / "standard_schema/hedjson/HED8.4.0.json", ld / "HEDLatest.json")
        shutil.copyfile(root / "library_schemas/score/hedjson/HED_score_2.1.0.json", ld / "HED_score_Latest.json")

    def test_in_sync(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            self._make_correct_latest(root)
            _, in_sync, problems = ulj.check_and_update(root, do_update=False)
            self.assertEqual(problems, [])
            self.assertEqual(len(in_sync), 2)

    def test_drift_then_update_fixes(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            self._make_correct_latest(root)
            (root / "schemas_latest_json/HED_score_Latest.json").write_text("STALE")

            _, _, problems = ulj.check_and_update(root, do_update=False)
            self.assertTrue(any("score" in p and "out of date" in p for p in problems))

            updated, _, _ = ulj.check_and_update(root, do_update=True)
            self.assertTrue(any("score" in u for u in updated))

            _, _, problems = ulj.check_and_update(root, do_update=False)
            self.assertEqual(problems, [])

    def test_missing_source_json(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            self._make_correct_latest(root)
            (root / "library_schemas/score/hedjson/HED_score_2.1.0.json").unlink()
            _, _, problems = ulj.check_and_update(root, do_update=False)
            self.assertTrue(any("score" in p and "missing" in p for p in problems))

    def test_stray_prerelease_only_and_excluded_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            self._make_correct_latest(root)
            (root / "schemas_latest_json/HED_mouse_Latest.json").write_text("stray")  # no released version
            (root / "schemas_latest_json/HED_testlib_Latest.json").write_text("stray")  # excluded
            _, _, problems = ulj.check_and_update(root, do_update=False)
            self.assertTrue(any("HED_mouse_Latest.json" in p for p in problems))
            self.assertTrue(any("HED_testlib_Latest.json" in p for p in problems))

    def test_main_check_message_mentions_correct_invocation(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            self._make_repo(root)
            self._make_correct_latest(root)
            (root / "schemas_latest_json/HED_score_Latest.json").write_text("STALE")
            rc, _, err = _run_main(ulj, ["--repo-root", str(root), "--check"])
            self.assertEqual(rc, 1)
            self.assertIn("python scripts/update_latest_json.py --update", err)


if __name__ == "__main__":
    unittest.main()
