#!/usr/bin/env python3
"""Unit tests for the pure logic of ``scripts/do_schema_release.py``.

Covers the naming rules for the standard schema and a library, version checks, the check that
``hed_add_ids`` only added hedIds, CHANGELOG insertion and extraction, and the replacement of a
schema's rows in ``docs/schemas_overview.md``. Uses only the standard library (``unittest``); no git
repo, network or hedtools. The steps that run hedtools and git are exercised by a full ``prepare``
run on a throwaway clone (see docs/release_guide.md).

Run from the repository root::

    python -m unittest discover -s tests -v
"""

from __future__ import annotations

import contextlib
import datetime
import io
import tempfile
import types
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"


def _load(module_name: str):
    """Load a script module from source (scripts/ is not a package), bypassing any stale .pyc."""
    path = SCRIPTS_DIR / f"{module_name}.py"
    module = types.ModuleType(module_name)
    module.__file__ = str(path)
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), module.__dict__)
    return module


dr = _load("do_schema_release")

RAW = "https://raw.githubusercontent.com/hed-standard/hed-schemas/main"
TREE = "https://github.com/hed-standard/hed-schemas/tree/main"


class TestKind(unittest.TestCase):
    def test_standard_names(self):
        kind = dr.Kind("standard")
        self.assertEqual(kind.folder, "standard_schema")
        self.assertEqual(kind.library_key, "")
        self.assertEqual(kind.stem("8.6.0"), "HED8.6.0")
        self.assertEqual(kind.latest_xml(), "standard_schema/hedxml/HEDLatest.xml")
        self.assertEqual(kind.tag("8.6.0"), "v8.6.0")
        self.assertEqual(kind.title("8.6.0"), "HED v8.6.0")
        self.assertEqual(
            kind.changelog_heading("8.6.0", datetime.date(2026, 3, 5)), "## Changes for HED 8.6.0 Release 3/5/2026"
        )
        self.assertEqual(kind.commit_message("8.6.0"), "Release HED standard schema 8.6.0")
        self.assertEqual(kind.changelog_title(), "# CHANGELOG for HED standard schema")

    def test_library_names(self):
        kind = dr.Kind("score")
        self.assertEqual(kind.folder, "library_schemas/score")
        self.assertEqual(kind.library_key, "score")
        self.assertEqual(kind.stem("2.2.0"), "HED_score_2.2.0")
        self.assertEqual(kind.latest_xml(), "library_schemas/score/hedxml/HED_score_Latest.xml")
        self.assertEqual(kind.tag("2.2.0"), "score_v2.2.0")
        self.assertEqual(kind.title("2.2.0"), "HED SCORE v2.2.0")
        self.assertEqual(
            kind.changelog_heading("2.2.0", datetime.date(2026, 10, 16)),
            "## Changes for HED score 2.2.0 Release 10/16/2026",
        )
        self.assertEqual(kind.commit_message("2.2.0"), "Release HED score library 2.2.0")
        self.assertEqual(kind.changelog_title(), "# CHANGELOG for HED score library schema")

    def test_commit_messages_fit_subject_limit(self):
        # Commit subjects stay under 50 characters (.rules/git.md in the HED repositories).
        self.assertLess(len(dr.Kind("standard").commit_message("10.10.10")), 50)
        self.assertLess(len(dr.Kind("score").commit_message("10.10.10")), 50)


class TestReleasePaths(unittest.TestCase):
    def test_library_release_includes_tsv_and_unmerged_copy(self):
        self.assertEqual(
            dr.released_paths(dr.Kind("score"), "2.2.0"),
            [
                "library_schemas/score/hedwiki/HED_score_2.2.0.mediawiki",
                "library_schemas/score/hedxml/HED_score_2.2.0.xml",
                "library_schemas/score/hedjson/HED_score_2.2.0.json",
                "library_schemas/score/hedtsv/HED_score_2.2.0",
                "library_schemas/score/hedxml/HED_score_Latest.xml",
                "schemas_xml_unmerged/HED_score_2.2.0.xml",
            ],
        )

    def test_standard_release_includes_its_copy(self):
        paths = dr.released_paths(dr.Kind("standard"), "8.5.0")
        self.assertIn("standard_schema/hedtsv/HED8.5.0", paths)
        self.assertIn("standard_schema/hedxml/HEDLatest.xml", paths)
        self.assertIn("schemas_xml_unmerged/HED8.5.0.xml", paths)

    def test_prerelease_paths_cover_all_four_formats(self):
        self.assertEqual(
            dr.prerelease_paths(dr.Kind("standard"), "8.5.0"),
            [
                "standard_schema/prerelease/HED8.5.0.mediawiki",
                "standard_schema/prerelease/HED8.5.0.xml",
                "standard_schema/prerelease/HED8.5.0.json",
                "standard_schema/prerelease/hedtsv/HED8.5.0",
            ],
        )


class TestVersionKey(unittest.TestCase):
    def test_orders_numerically(self):
        self.assertLess(dr.version_key("2.9.0"), dr.version_key("2.10.0"))
        self.assertEqual(dr.version_key("8.5.0"), (8, 5, 0))

    def test_rejects_non_semver(self):
        for bad in ("8.5", "8.5.0-beta", "v8.5.0", ""):
            with self.subTest(bad=bad), self.assertRaises(dr.ReleaseError):
                dr.version_key(bad)


class TestCheckIdsOnly(unittest.TestCase):
    RANGE = [40000, 59999]
    BEFORE = (
        "'''Tag-a''' <nowiki>[First tag.]</nowiki>\n"
        "* Tag-b <nowiki>{suggestedTag=Tag-a} [Second tag.]</nowiki>\n"
        "* Tag-c <nowiki>{suggestedTag=Tag-a, hedId=HED_0040001} [Has an id.]</nowiki>\n"
    )

    def test_accepts_added_ids_in_both_forms(self):
        after = (
            "'''Tag-a''' <nowiki>{hedId=HED_0040002} [First tag.]</nowiki>\n"
            "* Tag-b <nowiki>{suggestedTag=Tag-a, hedId=HED_0040003} [Second tag.]</nowiki>\n"
            "* Tag-c <nowiki>{suggestedTag=Tag-a, hedId=HED_0040001} [Has an id.]</nowiki>\n"
        )
        self.assertEqual(dr.check_ids_only("x.mediawiki", self.BEFORE, after, self.RANGE), 2)

    def test_accepts_id_only_wrapper_on_bare_element(self):
        # An element with no attributes and no description gains a whole <nowiki> wrapper.
        before = (
            "'''Tag-a''' <nowiki>[First tag.]</nowiki>\n* Medication-modulator\n** Child <nowiki>[A child.]</nowiki>\n"
        )
        after = before.replace(
            "* Medication-modulator\n", "* Medication-modulator <nowiki>{hedId=HED_0042013}</nowiki>\n"
        )
        self.assertEqual(dr.check_ids_only("x.mediawiki", before, after, self.RANGE), 1)

    def test_rejects_wrapper_hiding_other_text(self):
        before = "* Medication-modulator\n"
        after = "* Medication-modulator <nowiki>{hedId=HED_0042013} [Added text.]</nowiki>\n"
        with self.assertRaises(dr.ReleaseError):
            dr.check_ids_only("x.mediawiki", before, after, self.RANGE)

    def test_no_change_is_zero_ids(self):
        self.assertEqual(dr.check_ids_only("x.mediawiki", self.BEFORE, self.BEFORE, self.RANGE), 0)

    def test_rejects_other_edits(self):
        after = self.BEFORE.replace("[First tag.]", "{hedId=HED_0040002} [First tag, edited.]")
        with self.assertRaises(dr.ReleaseError):
            dr.check_ids_only("x.mediawiki", self.BEFORE, after, self.RANGE)

    def test_rejects_id_outside_range(self):
        after = self.BEFORE.replace("[First tag.]", "{hedId=HED_0012001} [First tag.]")
        with self.assertRaises(dr.ReleaseError):
            dr.check_ids_only("x.mediawiki", self.BEFORE, after, self.RANGE)

    def test_rejects_duplicate_id(self):
        after = self.BEFORE.replace("[First tag.]", "{hedId=HED_0040005} [First tag.]").replace(
            "{suggestedTag=Tag-a} [Second", "{suggestedTag=Tag-a, hedId=HED_0040005} [Second"
        )
        with self.assertRaises(dr.ReleaseError):
            dr.check_ids_only("x.mediawiki", self.BEFORE, after, self.RANGE)

    def test_rejects_removed_line(self):
        after = "\n".join(self.BEFORE.splitlines()[1:]) + "\n"
        with self.assertRaises(dr.ReleaseError):
            dr.check_ids_only("x.mediawiki", self.BEFORE, after, self.RANGE)


class TestChangelog(unittest.TestCase):
    TEXT = "# CHANGELOG for HED score library schema\n\n\n## Minor release score 2.1.0 June 9, 2025.\nOld entry.\n"
    ENTRY = "## Changes for HED score 2.2.0 Release 10/16/2026\n\n**Tags:**\n\n- New (Minor): Item New added\n\n"

    def test_inserts_before_first_entry(self):
        result = dr.insert_changelog_entry(self.TEXT, dr.Kind("score"), "2.2.0", self.ENTRY)
        self.assertTrue(
            result.startswith("# CHANGELOG for HED score library schema\n\n\n## Changes for HED score 2.2.0")
        )
        self.assertLess(result.index("2.2.0 Release"), result.index("2.1.0 June"))
        self.assertIn("Old entry.", result)

    def test_inserts_at_end_when_no_entries(self):
        result = dr.insert_changelog_entry("# CHANGELOG\n\n", dr.Kind("score"), "2.2.0", self.ENTRY)
        self.assertEqual(result, "# CHANGELOG\n\n" + self.ENTRY)

    def test_refuses_duplicate_entry(self):
        once = dr.insert_changelog_entry(self.TEXT, dr.Kind("score"), "2.2.0", self.ENTRY)
        with self.assertRaises(dr.ReleaseError):
            dr.insert_changelog_entry(once, dr.Kind("score"), "2.2.0", self.ENTRY)

    def test_extract_round_trip(self):
        text = dr.insert_changelog_entry(self.TEXT, dr.Kind("score"), "2.2.0", self.ENTRY)
        self.assertEqual(dr.extract_changelog_entry(text, dr.Kind("score"), "2.2.0"), self.ENTRY.strip() + "\n")

    def test_extract_handles_crlf_and_last_entry(self):
        text = "# CHANGELOG\r\n\r\n" + self.ENTRY.replace("\n", "\r\n")
        self.assertEqual(dr.extract_changelog_entry(text, dr.Kind("score"), "2.2.0"), self.ENTRY.strip() + "\n")

    def test_first_release_creates_changelog(self):
        # A library awaiting its first release (no earlier version, no CHANGELOG.md yet).
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp)
            pre = repo / "library_schemas" / "slam" / "prerelease"
            pre.mkdir(parents=True)
            (pre / "PRERELEASE_CHANGES.md").write_text(
                "## Differences between HED_slam_0.0.0 and HED_slam_1.0.0\n\n**Tags:**\n\n- Item (Minor): added\n",
                encoding="utf-8",
            )
            with contextlib.redirect_stdout(io.StringIO()):
                dr.update_changelog(repo, dr.Kind("slam"), None, "1.0.0", datetime.date(2026, 10, 16))
            text = (repo / "library_schemas" / "slam" / "CHANGELOG.md").read_text(encoding="utf-8")
        self.assertTrue(text.startswith("# CHANGELOG for HED slam library schema\n\n## Changes for HED slam 1.0.0"))
        self.assertIn("- Item (Minor): added", text)

    def test_release_headings_in_the_repository(self):
        # Every release heading form found in the CHANGELOGs, and the section headings used inside entries.
        for heading in (
            "## Changes for HED 8.5.0 Release 10/15/2026",
            "## Changes for HED 8.3.0 Released 6/10/2024",
            "## Changes for HED lang 1.2.0 Release 10/17/2026",
            "## Release 1.1.0 - June 10, 2025",
            "##  Initial release October 28, 2024",
            "## Minor release score 2.1.0 June 9, 2025.",
            "## Changes for score 1.2.0 released July 16, 2024.",
        ):
            self.assertTrue(dr.is_release_heading(heading), heading)
        for heading in (
            "## Key overall changes:",
            "## Changes to LANG",
            "## Changes to the partner standard schema (8.4.0 -> 8.5.0)",
            "### Release notes",
            "**Tags:**",
        ):
            self.assertFalse(dr.is_release_heading(heading), heading)

    def test_library_entry_layout(self):
        body = "**Tags:**\n\n- A (Minor): added\n\n### From the partner standard schema (8.4.0 -> 8.5.0)\n\n**Tags:**\n\n- B (Minor): added"
        entry = dr.format_changelog_entry(
            dr.Kind("lang"), "1.2.0", datetime.date(2026, 10, 17), body, first_release=False
        )
        self.assertEqual(
            entry,
            "## Changes for HED lang 1.2.0 Release 10/17/2026\n\n## Changes to LANG\n\n**Tags:**\n\n- A (Minor): added\n\n"
            "## Changes to the partner standard schema (8.4.0 -> 8.5.0)\n\n**Tags:**\n\n- B (Minor): added\n\n",
        )

    def test_standard_and_first_release_entries_keep_the_body(self):
        body = "**Tags:**\n\n- A (Minor): added"
        standard = dr.format_changelog_entry(dr.Kind("standard"), "8.6.0", datetime.date(2027, 3, 5), body, False)
        self.assertEqual(standard, "## Changes for HED 8.6.0 Release 3/5/2027\n\n" + body + "\n\n")
        first = dr.format_changelog_entry(dr.Kind("slam"), "1.0.0", datetime.date(2026, 10, 17), "Initial.", True)
        self.assertEqual(first, "## Changes for HED slam 1.0.0 Release 10/17/2026\n\nInitial.\n\n")

    def test_entry_with_sections_is_extracted_whole(self):
        text = (
            "# CHANGELOG for HED lang library schema\n\n\n"
            "## Changes for HED lang 1.2.0 Release 10/17/2026\n\n"
            "## Key overall changes:\n\n- Summary.\n\n"
            "## Changes to LANG\n\n**Tags:**\n\n- A (Minor): added\n\n"
            "## Changes to the partner standard schema (8.4.0 -> 8.5.0)\n\n- B (Minor): added\n\n"
            "## Release 1.1.0 - June 10, 2025\n\nOlder.\n"
        )
        entry = dr.extract_changelog_entry(text, dr.Kind("lang"), "1.2.0")
        self.assertTrue(entry.startswith("## Changes for HED lang 1.2.0 Release"))
        self.assertIn("- Summary.", entry)
        self.assertTrue(entry.endswith("- B (Minor): added\n"))
        self.assertNotIn("Older.", entry)

    def test_insert_goes_before_the_latest_release_not_its_sections(self):
        text = (
            "# CHANGELOG\n\n## Changes for HED lang 1.2.0 Release 10/17/2026\n\n## Key overall changes:\n\n- Summary.\n"
        )
        result = dr.insert_changelog_entry(
            text, dr.Kind("lang"), "1.3.0", "## Changes for HED lang 1.3.0 Release 1/2/2027\n\nNew.\n\n"
        )
        self.assertTrue(result.startswith("# CHANGELOG\n\n## Changes for HED lang 1.3.0 Release"))
        self.assertLess(result.index("1.3.0 Release"), result.index("1.2.0 Release"))

    def test_extract_requires_the_entry(self):
        with self.assertRaises(dr.ReleaseError):
            dr.extract_changelog_entry(self.TEXT, dr.Kind("score"), "2.2.0")


def _row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


class TestOverviewRows(unittest.TestCase):
    LIB_HEADER = _row(["Version", "Status", "Release date", "Partnered with", "XML", "MEDIAWIKI", "JSON", "TSV"])
    SEP = "| --- | --- | --- | --- | --- | --- | --- | --- |"

    def score_lines(self, with_latest: bool = True) -> list[str]:
        base = f"{RAW}/library_schemas/score"
        rows = ["### SCORE library schema", "", self.LIB_HEADER, self.SEP]
        if with_latest:
            rows.append(
                _row(["2.1.0", "Latest", "June 9, 2025", "Standard 8.3.0", f"[Raw]({base}/hedxml/HED_score_2.1.0.xml)"])
            )
        rows.append(
            _row(["2.2.0", "Prerelease", "", "Standard 8.3.0", f"[Raw]({base}/prerelease/HED_score_2.2.0.xml)"])
        )
        rows += ["", "### LANG library schema", "", self.LIB_HEADER, self.SEP]
        rows.append(_row(["1.2.0", "Prerelease", "", "Standard 8.4.0", f"[Raw]({RAW}/library_schemas/lang/x.xml)"]))
        return rows

    def test_library_rows_replaced(self):
        lines = dr.replace_overview_rows(
            self.score_lines(), dr.Kind("score"), "2.2.0", "2.3.0", "October 16, 2026", "8.5.0"
        )
        base = f"{RAW}/library_schemas/score"
        latest = _row(
            [
                "2.2.0",
                "Latest",
                "October 16, 2026",
                "Standard 8.5.0",
                f"[Raw]({base}/hedxml/HED_score_2.2.0.xml)",
                f"[Raw]({base}/hedwiki/HED_score_2.2.0.mediawiki)",
                f"[Raw]({base}/hedjson/HED_score_2.2.0.json)",
                f"[Directory]({TREE}/library_schemas/score/hedtsv/HED_score_2.2.0)",
            ]
        )
        prerelease = _row(
            [
                "2.3.0",
                "Prerelease",
                "",
                "Standard 8.5.0",
                f"[Raw]({base}/prerelease/HED_score_2.3.0.xml)",
                f"[Raw]({base}/prerelease/HED_score_2.3.0.mediawiki)",
                f"[Raw]({base}/prerelease/HED_score_2.3.0.json)",
                f"[Directory]({TREE}/library_schemas/score/prerelease/hedtsv/HED_score_2.3.0)",
            ]
        )
        self.assertEqual(lines[4:6], [latest, prerelease])
        self.assertEqual(len(lines), len(self.score_lines()))
        # The next library's table is untouched.
        self.assertEqual(lines[-1], self.score_lines()[-1])

    def test_first_release_inserts_latest_row(self):
        lines = dr.replace_overview_rows(
            self.score_lines(with_latest=False), dr.Kind("score"), "2.2.0", "2.3.0", "October 16, 2026", "8.5.0"
        )
        self.assertEqual(len(lines), len(self.score_lines(with_latest=False)) + 1)
        self.assertIn("| 2.2.0 | Latest |", lines[4])
        self.assertIn("| 2.3.0 | Prerelease |", lines[5])

    def test_standard_table_without_partner_column(self):
        header = _row(["Version", "Status", "Release date", "XML", "MEDIAWIKI", "JSON", "TSV"])
        base = f"{RAW}/standard_schema"
        lines = [
            header,
            "| --- | --- | --- | --- | --- | --- | --- |",
            _row(["8.5.0", "Latest", "October 15, 2026", f"[Raw]({base}/hedxml/HED8.5.0.xml)"]),
            _row(["8.6.0", "Prerelease", "", f"[Raw]({base}/prerelease/HED8.6.0.xml)"]),
        ]
        result = dr.replace_overview_rows(lines, dr.Kind("standard"), "8.6.0", "8.7.0", "March 5, 2027", None)
        self.assertTrue(result[2].startswith("| 8.6.0 | Latest | March 5, 2027 | [Raw]("))
        self.assertIn(f"{base}/hedxml/HED8.6.0.xml", result[2])
        self.assertIn(f"{base}/prerelease/HED8.7.0.json", result[3])
        self.assertEqual(result[3].count("|"), 8)

    def test_requires_one_prerelease_row(self):
        lines = [line for line in self.score_lines() if "Prerelease" not in line or "/lang/" in line]
        with self.assertRaises(dr.ReleaseError):
            dr.replace_overview_rows(lines, dr.Kind("score"), "2.2.0", "2.3.0", "October 16, 2026", "8.5.0")

    def test_rejects_unknown_column(self):
        lines = self.score_lines()
        lines[2] = lines[2].replace("Partnered with", "Notes")
        with self.assertRaises(dr.ReleaseError):
            dr.replace_overview_rows(lines, dr.Kind("score"), "2.2.0", "2.3.0", "October 16, 2026", "8.5.0")


class TestCommitMessage(unittest.TestCase):
    DATE = datetime.date(2026, 10, 17)

    def test_library_release_describes_the_run(self):
        run = {
            "partner": "8.5.0",
            "regenerated": ["HED_lang_1.2.0.xml"],
            "ids": 0,
            "last": "1.1.0",
            "report_lines": 274,
            "report_regenerated": True,
            "created": [],
        }
        message = dr.release_commit_message(dr.Kind("lang"), "1.2.0", "1.3.0", run, self.DATE)
        flat = " ".join(message.split())  # bullets are wrapped at 72 columns
        lines = message.splitlines()
        self.assertEqual(lines[0], "Release HED lang library 1.2.0")
        self.assertEqual(lines[1], "")
        self.assertEqual(lines[2], "Prepared with scripts/do_schema_release.py on 10/17/2026.")
        self.assertIn("released standard 8.5.0 (HED_lang_1.2.0.xml)", flat)
        self.assertIn("Assigned 0 new hedIds", flat)
        self.assertIn("against 1.1.0 (274 lines; PRERELEASE_CHANGES.md regenerated)", flat)
        self.assertIn("schemas_xml_unmerged/HED_lang_1.2.0.xml", flat)
        self.assertIn("Started the 1.3.0 prerelease", flat)
        self.assertIn("HED_lang_Latest.xml", flat)
        self.assertNotIn("Created", flat)
        self.assertTrue(all(len(line) <= 72 for line in lines), [line for line in lines if len(line) > 72])

    def test_first_library_release_lists_created_items(self):
        run = {
            "partner": "8.5.0",
            "regenerated": [],
            "ids": 37,
            "last": None,
            "report_lines": 1,
            "report_regenerated": False,
            "created": ["library_schemas/slam/CHANGELOG.md", "library_schemas/slam/hedwiki/"],
        }
        message = dr.release_commit_message(dr.Kind("slam"), "1.0.0", "1.1.0", run, self.DATE)
        flat = " ".join(message.split())
        self.assertIn("(nothing changed)", flat)
        self.assertIn("Assigned 37 new hedIds", flat)
        self.assertIn("from PRERELEASE_CHANGES.md (first release)", flat)
        self.assertIn("library_schemas/slam/CHANGELOG.md", flat)

    def test_standard_release_has_no_partner(self):
        run = {
            "partner": None,
            "regenerated": [],
            "ids": 1,
            "last": "8.5.0",
            "report_lines": 50,
            "report_regenerated": False,
            "created": [],
        }
        message = dr.release_commit_message(dr.Kind("standard"), "8.6.0", "8.7.0", run, self.DATE)
        flat = " ".join(message.split())
        self.assertTrue(message.startswith("Release HED standard schema 8.6.0\n\n"))
        self.assertIn("Assigned 1 new hedId;", flat)
        self.assertNotIn("Regenerated the prerelease", flat)
        self.assertIn("schemas_xml_unmerged/HED8.6.0.xml", flat)
        self.assertIn("HEDLatest.xml", flat)


class TestReadmeRow(unittest.TestCase):
    HEADER = "| Schema | Latest | Description | Prerelease | DOI |"
    LINES = [
        "## Viewing HED schemas",
        "",
        HEADER,
        "| --- | --- | --- | --- | --- |",
        "| [**standard**](./standard_schema) | 8.4.0 | Basic vocabulary.<br/> HED_0010000 - HED_0039999 | 8.5.0 | 10.5281/zenodo.7876037 |",
        "| [**score**](library_schemas/score) | 2.1.0 | SCORE vocabulary | 2.2.0 | 10.5281/zenodo.7897596 |",
        "| [**slam**](library_schemas/slam) |  | SLAM (Sensor Location and Motion). | 1.0.0 |  |",
    ]

    def test_standard_row(self):
        lines = dr.replace_readme_row(self.LINES, dr.Kind("standard"), "8.5.0", "8.6.0")
        self.assertEqual(
            lines[4],
            "| [**standard**](./standard_schema) | 8.5.0 | Basic vocabulary.<br/> HED_0010000 - HED_0039999 | 8.6.0 | 10.5281/zenodo.7876037 |",
        )
        self.assertEqual(lines[5:], self.LINES[5:])

    def test_library_row(self):
        lines = dr.replace_readme_row(self.LINES, dr.Kind("score"), "2.2.0", "2.3.0")
        self.assertEqual(
            lines[5],
            "| [**score**](library_schemas/score) | 2.2.0 | SCORE vocabulary | 2.3.0 | 10.5281/zenodo.7897596 |",
        )
        self.assertEqual(lines[4], self.LINES[4])

    def test_first_release_fills_empty_latest(self):
        lines = dr.replace_readme_row(self.LINES, dr.Kind("slam"), "1.0.0", "1.1.0")
        self.assertEqual(
            lines[6], "| [**slam**](library_schemas/slam) | 1.0.0 | SLAM (Sensor Location and Motion). | 1.1.0 |  |"
        )

    def test_requires_the_row(self):
        with self.assertRaises(dr.ReleaseError):
            dr.replace_readme_row(self.LINES, dr.Kind("mouse"), "1.0.0", "1.1.0")

    def test_requires_latest_and_prerelease_columns(self):
        lines = list(self.LINES)
        lines[2] = "| Schema | Current | Description | Next | DOI |"
        with self.assertRaises(dr.ReleaseError):
            dr.replace_readme_row(lines, dr.Kind("score"), "2.2.0", "2.3.0")


if __name__ == "__main__":
    unittest.main()
