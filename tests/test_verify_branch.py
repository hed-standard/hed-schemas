#!/usr/bin/env python3
"""Unit tests for ``scripts/verify_branch.py``.

Covers the branch-scoping rules (which files each branch prefix may modify) and the exemption
for generated manifest files (``schema_versions.json``). Uses only the standard library
(``unittest``); no git repo or network required. Schema-file *validation* (which shells out to
``hed_validate_schemas``) is not exercised here - tests use non-schema file extensions or
out-of-place schema paths, which are rejected before validation runs.

Run from the repository root::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import types
import unittest
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


vb = _load("verify_branch")


class TestBranchPrefix(unittest.TestCase):
    def test_prefix_extraction(self):
        self.assertEqual(vb.get_branch_prefix("mouse_update"), "mouse")
        self.assertEqual(vb.get_branch_prefix("standard_fix_typo"), "standard")
        self.assertEqual(vb.get_branch_prefix("admin_fix_actions"), "admin")
        self.assertEqual(vb.get_branch_prefix("noprefix"), "noprefix")

    def test_base_pattern(self):
        self.assertEqual(vb.get_base_pattern("standard"), "standard_schema/")
        self.assertEqual(vb.get_base_pattern("mouse"), "library_schemas/mouse/")


class TestVerifyFiles(unittest.TestCase):
    def test_admin_branch_allows_anything(self):
        files = ["docs/index.md", "scripts/foo.py", "schema_versions.json"]
        self.assertEqual(vb.verify_files(files, "admin_fix_actions"), [])

    def test_library_branch_allows_in_scope_files(self):
        files = ["library_schemas/mouse/prerelease/PRERELEASE_CHANGES.md"]
        self.assertEqual(vb.verify_files(files, "mouse_update"), [])

    def test_library_branch_rejects_other_library(self):
        files = ["library_schemas/score/prerelease/PRERELEASE_CHANGES.md"]
        errors = vb.verify_files(files, "mouse_update")
        self.assertEqual(len(errors), 1)
        self.assertIn("library_schemas/mouse/", errors[0])

    def test_library_branch_rejects_root_files(self):
        errors = vb.verify_files(["docs/index.md"], "mouse_update")
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/index.md", errors[0])

    def test_library_branch_rejects_released_directories(self):
        # Non-schema extension so the banned-directory check fires (schema extensions are
        # rejected earlier by the prerelease-placement rule).
        errors = vb.verify_files(["library_schemas/mouse/hedxml/notes.txt"], "mouse_update")
        self.assertEqual(len(errors), 1)
        self.assertIn("restricted directory", errors[0])

    def test_schema_file_outside_prerelease_rejected(self):
        errors = vb.verify_files(["library_schemas/mouse/hedwiki/HED_mouse_1.1.0.mediawiki"], "mouse_update")
        self.assertEqual(len(errors), 1)
        self.assertIn("must be in", errors[0])

    def test_dependabot_branch_limited_to_github_directory(self):
        branch = "dependabot/github_actions/actions/checkout-5"
        self.assertEqual(vb.verify_files([".github/workflows/ci.yaml"], branch), [])
        errors = vb.verify_files(["scripts/foo.py"], branch)
        self.assertEqual(len(errors), 1)
        self.assertIn("dependabot", errors[0])


class TestManifestExemption(unittest.TestCase):
    """schema_versions.json is generated from the schema files and stale after any schema
    change, so every branch may commit a regenerated copy. Correctness is enforced by the
    update_manifests.yaml --check job, not by branch scoping."""

    def test_manifest_allowed_on_library_branch(self):
        self.assertEqual(vb.verify_files(["schema_versions.json"], "mouse_update"), [])

    def test_manifest_allowed_on_standard_branch(self):
        self.assertEqual(vb.verify_files(["schema_versions.json"], "standard_fix_typo"), [])

    def test_manifest_allowed_alongside_schema_change(self):
        files = [
            "library_schemas/mouse/prerelease/PRERELEASE_CHANGES.md",
            "schema_versions.json",
        ]
        self.assertEqual(vb.verify_files(files, "mouse_update"), [])

    def test_exemption_does_not_excuse_other_files(self):
        files = ["schema_versions.json", "docs/index.md"]
        errors = vb.verify_files(files, "mouse_update")
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/index.md", errors[0])

    def test_exemption_is_exact_filename_only(self):
        # schemas_latest_json/ and lookalike paths are NOT exempt.
        errors = vb.verify_files(["schemas_latest_json/HED_mouse.json"], "mouse_update")
        self.assertEqual(len(errors), 1)
        errors = vb.verify_files(["docs/schema_versions.json"], "mouse_update")
        self.assertEqual(len(errors), 1)

    def test_manifest_allowed_on_dependabot_branch(self):
        branch = "dependabot/github_actions/actions/checkout-5"
        self.assertEqual(vb.verify_files(["schema_versions.json"], branch), [])


if __name__ == "__main__":
    unittest.main()
