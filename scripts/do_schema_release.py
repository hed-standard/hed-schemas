#!/usr/bin/env python3
"""Release a HED schema (standard or library) from hed-schemas; see docs/release_guide.md.

Two subcommands, run from the repository root:

    python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0   # steps 0-8, before the PR
    python scripts/do_schema_release.py notes score 2.2.0                  # after the PR has merged

``prepare`` runs every release step on an ``admin_*`` branch and ends with all changes staged
(never committed). ``notes`` checks that the release is on hed-standard main and writes the
CHANGELOG entry to a file for pasting into the GitHub release, which is always created by hand in
the GitHub web interface. The script never pushes, tags, or calls the GitHub API.

Every step prints what it does; the first failed command or check prints the reason and exits 1.
Run it with the Python environment that has hedtools installed (``pip install -e .``).
"""

from __future__ import annotations

import argparse
import datetime
import difflib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

RAW = "https://raw.githubusercontent.com/hed-standard/hed-schemas/main"
TREE = "https://github.com/hed-standard/hed-schemas/tree/main"
UPSTREAM = "hed-standard/hed-schemas"
TOOLS = ("hed_validate_schemas", "hed_add_ids", "hed_update_schemas")


class ReleaseError(Exception):
    """A step failed; the message says why."""


# ---------------------------------------------------------------------------------------------
# Per-kind differences between the standard schema and a library schema
# ---------------------------------------------------------------------------------------------


class Kind:
    """Names and paths for one schema (``standard`` or a library name)."""

    def __init__(self, name: str):
        self.name = name
        self.is_standard = name == "standard"
        self.folder = "standard_schema" if self.is_standard else f"library_schemas/{name}"
        self.library_key = "" if self.is_standard else name

    def stem(self, version: str) -> str:
        return f"HED{version}" if self.is_standard else f"HED_{self.name}_{version}"

    def latest_xml(self) -> str:
        return f"{self.folder}/hedxml/" + ("HEDLatest.xml" if self.is_standard else f"HED_{self.name}_Latest.xml")

    def tag(self, version: str) -> str:
        return f"v{version}" if self.is_standard else f"{self.name}_v{version}"

    def title(self, version: str) -> str:
        return f"HED v{version}" if self.is_standard else f"HED {self.name.upper()} v{version}"

    def changelog_heading(self, version: str, date: datetime.date) -> str:
        label = "HED" if self.is_standard else f"HED {self.name}"
        return f"## Changes for {label} {version} Release {date.month}/{date.day}/{date.year}"

    def changelog_heading_prefix(self, version: str) -> str:
        label = "HED" if self.is_standard else f"HED {self.name}"
        return f"## Changes for {label} {version} Release "

    def commit_message(self, version: str) -> str:
        return (
            f"Release HED standard schema {version}"
            if self.is_standard
            else f"Release HED {self.name} library {version}"
        )


# ---------------------------------------------------------------------------------------------
# Printing and running
# ---------------------------------------------------------------------------------------------


def step(number: int, name: str) -> None:
    print(f"\n== Step {number}: {name}", flush=True)


def ok(message: str) -> None:
    print(f"   ok: {message}", flush=True)


def require(condition: bool, message: str) -> None:
    """Stop the release with ``message`` unless ``condition`` holds."""
    if not condition:
        raise ReleaseError(message)


def run(cmd: list[str], repo: Path, show: str | None = None) -> str:
    """Run ``cmd`` in ``repo``, print it and its result, and stop on a non-zero exit.

    Returns the combined stdout and stderr.
    """
    print(f"   $ {show or ' '.join(cmd)}", flush=True)
    result = subprocess.run(cmd, cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace")
    output = (result.stdout or "") + (result.stderr or "")
    if result.returncode != 0:
        tail = "\n".join("     | " + line for line in output.strip().splitlines()[-30:])
        raise ReleaseError(f"command failed with exit {result.returncode}: {show or ' '.join(cmd)}\n{tail}")
    last = next((line.strip() for line in reversed(output.splitlines()) if line.strip()), "")
    ok(f"exit 0{' - ' + last if last else ''}")
    return output


def git(repo: Path, *args: str) -> str:
    return run(["git", *args], repo)


def git_quiet(repo: Path, *args: str) -> subprocess.CompletedProcess:
    """Run git without printing; the caller checks the result."""
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, encoding="utf-8", errors="replace")


def tool(name: str) -> str:
    """Path of a hedtools command, preferring the running interpreter's environment."""
    folder = Path(sys.executable).parent
    for candidate in (folder / name, folder / f"{name}.exe", folder / "Scripts" / f"{name}.exe"):
        if candidate.is_file():
            return str(candidate)
    found = shutil.which(name)
    require(found is not None, f"hedtools command '{name}' not found; run with the environment that has hedtools")
    return found


# ---------------------------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------------------------


def version_key(version: str) -> tuple[int, ...]:
    require(re.fullmatch(r"\d+\.\d+\.\d+", version) is not None, f"'{version}' is not a version of the form X.Y.Z")
    return tuple(int(part) for part in version.split("."))


def released_versions(repo: Path, kind: Kind) -> list[str]:
    pattern = re.compile(re.escape(kind.stem("")) + r"(\d+\.\d+\.\d+)\.xml$")
    found = [m.group(1) for f in (repo / kind.folder / "hedxml").glob("*.xml") if (m := pattern.match(f.name))]
    return sorted(found, key=version_key)


def header_line(path: Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.readline()


def header_attribute(path: Path, name: str) -> str | None:
    match = re.search(rf'\b{name}="([^"]*)"', header_line(path))
    return match.group(1) if match else None


def upstream_remote(repo: Path) -> str:
    """Name of the remote that points at hed-standard/hed-schemas (names vary by checkout)."""
    for line in git_quiet(repo, "remote", "-v").stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and UPSTREAM in parts[1].replace(".git", ""):
            return parts[0]
    raise ReleaseError(f"no git remote points at {UPSTREAM}")


def read(path: Path) -> str:
    return path.read_bytes().decode("utf-8")


def write(path: Path, text: str) -> None:
    path.write_bytes(text.encode("utf-8"))


# ---------------------------------------------------------------------------------------------
# prepare
# ---------------------------------------------------------------------------------------------


def preflight(repo: Path, kind: Kind, version: str, next_version: str) -> dict:
    step(0, "Preflight checks")
    require(
        (repo / "library_data.json").is_file() and (repo / "scripts" / "generate_schema_versions.py").is_file(),
        f"{repo} is not a hed-schemas checkout",
    )
    ok(f"hed-schemas checkout at {repo}")

    branch = git_quiet(repo, "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    require(
        branch.startswith("admin_"),
        f"on branch '{branch}': a release must run on an admin_* branch (CI rejects release changes from others)",
    )
    ok(f"on branch {branch}")

    dirty = git_quiet(repo, "status", "--porcelain").stdout.strip()
    require(not dirty, "working tree is not clean:\n" + dirty)
    ok("working tree is clean")

    remote = upstream_remote(repo)
    git(repo, "fetch", remote)
    require(
        git_quiet(repo, "merge-base", "--is-ancestor", f"{remote}/main", "HEAD").returncode == 0,
        f"HEAD does not contain {remote}/main; rebase the branch on it first",
    )
    ok(f"HEAD contains {remote}/main")

    tools = {name: tool(name) for name in TOOLS}
    help_text = run([tools["hed_validate_schemas"], "--help"], repo, "hed_validate_schemas --help")
    require(
        "--require-ids" in help_text, "hedtools is too old (no --require-ids); refresh it with pip --force-reinstall"
    )
    ok("hedtools has --require-ids")

    library_data = json.loads(read(repo / "library_data.json"))
    require(kind.library_key in library_data, f"'{kind.name}' is not registered in library_data.json")
    id_range = library_data[kind.library_key]["id_range"]
    ok(f"'{kind.name}' registered in library_data.json, id range {id_range[0]}-{id_range[1]}")

    version_key(version)
    require(version_key(next_version) > version_key(version), f"--next {next_version} is not greater than {version}")
    pre = repo / kind.folder / "prerelease"
    stem = kind.stem(version)
    for path in (
        pre / f"{stem}.mediawiki",
        pre / f"{stem}.xml",
        pre / f"{stem}.json",
        pre / "hedtsv" / stem,
        pre / "PRERELEASE_CHANGES.md",
    ):
        require(path.exists(), f"missing prerelease file {path.relative_to(repo).as_posix()}")
    ok(f"prerelease {stem} has all four formats and PRERELEASE_CHANGES.md")
    require(
        header_attribute(pre / f"{stem}.mediawiki", "version") == version,
        f'{stem}.mediawiki header does not say version="{version}"',
    )
    require(not (repo / kind.folder / "hedxml" / f"{stem}.xml").exists(), f"{stem} is already released")
    require(
        not (pre / f"{kind.stem(next_version)}.mediawiki").exists(),
        f"prerelease {kind.stem(next_version)} already exists",
    )

    released = released_versions(repo, kind)
    last = released[-1] if released else None
    if last:
        require(version_key(last) < version_key(version), f"last released {last} is not older than {version}")
    ok(f"last released version: {last or 'none (first release)'}")

    partner = None
    if not kind.is_standard:
        partner = header_attribute(pre / f"{stem}.mediawiki", "withStandard")
        require(partner is not None, f"{stem}.mediawiki has no withStandard attribute")
        require(
            (repo / "standard_schema" / "hedxml" / f"HED{partner}.xml").is_file(),
            f"partner standard {partner} is not released (no standard_schema/hedxml/HED{partner}.xml)",
        )
        standards = released_versions(repo, Kind("standard"))
        require(
            bool(standards) and partner == standards[-1],
            f"partner standard {partner} is not the latest released standard "
            f"({standards[-1] if standards else 'none'}); repartner the library on its own branch first",
        )
        stale = Path.home() / ".hedtools" / "hed_cache" / "prerelease" / f"HED{partner}.xml"
        require(
            not stale.exists(),
            f"stale prerelease copy of the partner standard in the schema cache: {stale}\n"
            "     Delete it so hedtools loads the released file, then rerun.",
        )
        ok(f"partner standard {partner} is the latest released standard and not stale in the cache")

    return {"tools": tools, "id_range": id_range, "last": last, "partner": partner}


def check_ids_only(rel: str, before: str, after: str, id_range: list[int]) -> int:
    """Check that ``after`` differs from ``before`` only by added hedIds inside the range. Returns the count."""
    diff = list(difflib.unified_diff(before.splitlines(), after.splitlines(), lineterm="", n=0))
    removed = [line[1:] for line in diff if line.startswith("-") and not line.startswith("---")]
    added = [line[1:] for line in diff if line.startswith("+") and not line.startswith("+++")]
    require(len(removed) == len(added), f"{rel}: {len(removed)} lines removed but {len(added)} added")
    ids = []
    for old, new in zip(removed, added, strict=True):
        ids += [int(n) for n in re.findall(r"hedId=HED_(\d+)", new)]
        stripped = re.sub(r"\{hedId=HED_\d+\} ", "", new)
        stripped = re.sub(r", *hedId=HED_\d+", "", stripped)
        stripped = re.sub(r"hedId=HED_\d+, *", "", stripped)
        require(stripped == old, f"{rel}: a line changed by more than a hedId:\n     - {old}\n     + {new}")
    require(len(ids) == len(added), f"{rel}: {len(added)} changed lines but {len(ids)} hedIds")
    outside = [n for n in ids if not id_range[0] <= n <= id_range[1]]
    require(not outside, f"hedIds outside {id_range}: {outside}")
    require(len(set(ids)) == len(ids), "the same hedId was assigned twice")
    return len(ids)


def comparison_report(repo: Path, kind: Kind, last: str | None, version: str) -> str:
    """SchemaComparer report from the last release to the candidate, as in PRERELEASE_CHANGES.md."""
    from hed.schema import load_schema
    from hed.schema.schema_comparer import SchemaComparer

    new = load_schema(str(repo / kind.folder / "prerelease" / f"{kind.stem(version)}.mediawiki"))
    old = load_schema(str(repo / kind.folder / "hedxml" / f"{kind.stem(last)}.xml"))
    title = f"Differences between {kind.stem(last)} and {kind.stem(version)}"
    return SchemaComparer(old, new).compare_differences(title=title)


def insert_changelog_entry(text: str, kind: Kind, version: str, entry: str) -> str:
    """Return CHANGELOG ``text`` with ``entry`` placed before the first ``## `` heading (newest first)."""
    require(kind.changelog_heading_prefix(version) not in text, f"CHANGELOG.md already has an entry for {version}")
    match = re.search(r"^## ", text, flags=re.MULTILINE)
    position = match.start() if match else len(text)
    return text[:position] + entry + text[position:]


def extract_changelog_entry(text: str, kind: Kind, version: str) -> str:
    """Return the CHANGELOG entry for ``version``: its heading up to the next ``## `` heading."""
    lines = text.replace("\r\n", "\n").split("\n")
    prefix = kind.changelog_heading_prefix(version)
    starts = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    require(len(starts) == 1, f"expected one CHANGELOG heading starting '{prefix}', found {len(starts)}")
    end = next((i for i in range(starts[0] + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    return "\n".join(lines[starts[0] : end]).strip() + "\n"


def update_changelog(repo: Path, kind: Kind, last: str | None, version: str, today: datetime.date) -> None:
    changes = repo / kind.folder / "prerelease" / "PRERELEASE_CHANGES.md"
    committed = read(changes).replace("\r\n", "\n")
    if last:
        print(f"   comparing released {kind.stem(last)} with the candidate {kind.stem(version)} (SchemaComparer)")
        try:
            report = comparison_report(repo, kind, last, version)
        except Exception as e:  # noqa: BLE001 - any load or compare failure stops the release
            raise ReleaseError(f"SchemaComparer failed: {e}") from e
        require(report.strip().startswith("## "), "SchemaComparer returned no report")
        if report.strip() == committed.strip():
            ok("regenerated comparison equals the committed PRERELEASE_CHANGES.md")
        else:
            write(changes, report.strip() + "\n")
            old_n, new_n = len(committed.strip().splitlines()), len(report.strip().splitlines())
            ok(f"PRERELEASE_CHANGES.md regenerated ({old_n} -> {new_n} lines); the CHANGELOG entry uses the new report")
        committed = report
    else:
        ok("first release: no earlier version to compare; using the committed PRERELEASE_CHANGES.md")
    lines = committed.strip().split("\n")
    require(lines[0].startswith("## "), "PRERELEASE_CHANGES.md does not start with a ## heading")
    body = "\n".join(lines[1:]).strip()
    entry = kind.changelog_heading(version, today) + "\n\n" + body + "\n\n"

    path = repo / kind.folder / "CHANGELOG.md"
    write(path, insert_changelog_entry(read(path), kind, version, entry))
    ok(
        f"inserted '{kind.changelog_heading(version, today)}' into {kind.folder}/CHANGELOG.md ({len(body.splitlines())} lines)"
    )


def move_formats(repo: Path, kind: Kind, version: str) -> None:
    stem = kind.stem(version)
    pre = f"{kind.folder}/prerelease"
    git(repo, "mv", f"{pre}/{stem}.mediawiki", f"{kind.folder}/hedwiki/")
    git(repo, "mv", f"{pre}/{stem}.xml", f"{kind.folder}/hedxml/")
    git(repo, "mv", f"{pre}/{stem}.json", f"{kind.folder}/hedjson/")
    git(repo, "mv", f"{pre}/hedtsv/{stem}", f"{kind.folder}/hedtsv/")
    if not kind.is_standard:
        target = repo / "schemas_xml_unmerged" / f"{stem}.xml"
        print(f"   writing the unmerged XML copy schemas_xml_unmerged/{stem}.xml")
        try:
            from hed.schema import load_schema

            load_schema(str(repo / kind.folder / "hedxml" / f"{stem}.xml")).save_as_xml(str(target), save_merged=False)
        except Exception as e:  # noqa: BLE001
            raise ReleaseError(f"could not write the unmerged XML: {e}") from e
        require(target.is_file(), f"schemas_xml_unmerged/{stem}.xml was not written")
        ok(f"schemas_xml_unmerged/{stem}.xml written")


def start_next_prerelease(repo: Path, kind: Kind, version: str, next_version: str, tools: dict) -> None:
    stem, next_stem = kind.stem(version), kind.stem(next_version)
    source = repo / kind.folder / "hedwiki" / f"{stem}.mediawiki"
    target = repo / kind.folder / "prerelease" / f"{next_stem}.mediawiki"
    text = read(source)
    first, rest = text.split("\n", 1)
    require(first.count(f'version="{version}"') == 1, f'{stem}.mediawiki line 1 does not hold version="{version}" once')
    write(target, first.replace(f'version="{version}"', f'version="{next_version}"') + "\n" + rest)
    ok(f"copied {stem}.mediawiki to prerelease/{next_stem}.mediawiki with version {next_version}")
    rel = target.relative_to(repo).as_posix()
    run([tools["hed_update_schemas"], rel], repo, f"hed_update_schemas {rel}")
    run(
        [tools["hed_validate_schemas"], rel, "--add-all-extensions", "--require-ids"],
        repo,
        f"hed_validate_schemas {rel} --add-all-extensions --require-ids",
    )
    write(
        repo / kind.folder / "prerelease" / "PRERELEASE_CHANGES.md", f"## Differences between {stem} and {next_stem}\n"
    )
    ok("PRERELEASE_CHANGES.md reset to its heading only")


def overview_row(
    header: list[str], kind: Kind, version: str, status: str, date: str, partner: str | None, released: bool
) -> str:
    stem = kind.stem(version)
    base = kind.folder if released else f"{kind.folder}/prerelease"
    links = {
        "XML": f"[Raw]({RAW}/{base}/{'hedxml/' if released else ''}{stem}.xml)",
        "MEDIAWIKI": f"[Raw]({RAW}/{base}/{'hedwiki/' if released else ''}{stem}.mediawiki)",
        "JSON": f"[Raw]({RAW}/{base}/{'hedjson/' if released else ''}{stem}.json)",
        "TSV": f"[Directory]({TREE}/{base}/hedtsv/{stem})",
    }
    values = {
        "Version": version,
        "Status": status,
        "Release date": date,
        "Partnered with": f"Standard {partner}" if partner else "",
    }
    cells = []
    for name in header:
        require(name in values or name in links, f"unknown column '{name}' in the overview table")
        cells.append(values.get(name, links.get(name)))
    return "| " + " | ".join(cells) + " |"


def replace_overview_rows(
    lines: list[str], kind: Kind, version: str, next_version: str, date: str, partner: str | None
) -> list[str]:
    """Return ``lines`` of schemas_overview.md with the schema's Latest and Prerelease rows replaced.

    The schema's rows are those linking into its folder. There must be exactly one Prerelease row and
    at most one Latest row (a first release has none); the new Latest and Prerelease rows take their
    place, with cells built from the table's own header.
    """
    lines = list(lines)
    marker = f"/main/{kind.folder}/"

    def cells(line: str) -> list[str]:
        return [c.strip() for c in line.strip().strip("|").split("|")]

    def rows(status: str) -> list[int]:
        return [
            i for i, line in enumerate(lines) if line.startswith("|") and marker in line and cells(line)[1] == status
        ]

    prerelease_rows, latest_rows = rows("Prerelease"), rows("Latest")
    require(
        len(prerelease_rows) == 1,
        f"expected one Prerelease row for {kind.folder} in docs/schemas_overview.md, found {len(prerelease_rows)}",
    )
    require(len(latest_rows) <= 1, f"more than one Latest row for {kind.folder} in docs/schemas_overview.md")
    start = min(prerelease_rows + latest_rows)
    header_index = next((i for i in range(start, -1, -1) if lines[i].startswith("| Version")), None)
    require(header_index is not None, "no '| Version' header above the schema's rows")
    header = cells(lines[header_index])
    new_rows = [
        overview_row(header, kind, version, "Latest", date, partner, released=True),
        overview_row(header, kind, next_version, "Prerelease", "", partner, released=False),
    ]
    for index in sorted(prerelease_rows + latest_rows, reverse=True):
        del lines[index]
    lines[start:start] = new_rows
    return lines


def update_overview(repo: Path, kind: Kind, version: str, next_version: str, today: datetime.date) -> None:
    path = repo / "docs" / "schemas_overview.md"
    pre = repo / kind.folder / "prerelease" / f"{kind.stem(next_version)}.mediawiki"
    partner = None if kind.is_standard else header_attribute(pre, "withStandard")
    date = f"{today:%B} {today.day}, {today.year}"
    write(path, "\n".join(replace_overview_rows(read(path).split("\n"), kind, version, next_version, date, partner)))
    ok(f"overview rows: {version} Latest ({date}), {next_version} Prerelease")
    run(
        [sys.executable, "-m", "mdformat", "--wrap", "no", "--number", "docs/schemas_overview.md"],
        repo,
        "python -m mdformat --wrap no --number docs/schemas_overview.md",
    )
    text = read(path)
    require(
        f"{kind.folder}/prerelease/{kind.stem(version)}." not in text,
        "docs/schemas_overview.md still links to the moved prerelease files",
    )


def prepare(repo: Path, kind: Kind, version: str, next_version: str) -> None:
    today = datetime.date.today()
    print(f"Releasing {kind.name} {version} (next prerelease {next_version}) in {repo}")
    facts = preflight(repo, kind, version, next_version)
    tools, stem = facts["tools"], kind.stem(version)
    rel = f"{kind.folder}/prerelease/{stem}.mediawiki"

    if kind.is_standard:
        step(1, "Validate the prerelease")
    else:
        step(
            1,
            f"Regenerate the prerelease from the unmerged mediawiki against standard {facts['partner']}, then validate",
        )
        run([tools["hed_update_schemas"], rel], repo, f"hed_update_schemas {rel}")
        changed = git_quiet(repo, "diff", "--stat", "--", f"{kind.folder}/prerelease").stdout.rstrip()
        ok("regeneration changed nothing" if not changed else "regeneration changed:\n" + changed)
    run(
        [tools["hed_validate_schemas"], rel, "--add-all-extensions"],
        repo,
        f"hed_validate_schemas {rel} --add-all-extensions",
    )

    step(2, "Assign hedIds")
    before = read(repo / rel)
    run([tools["hed_add_ids"], ".", kind.name, version], repo, f"hed_add_ids . {kind.name} {version}")
    count = check_ids_only(rel, before, read(repo / rel), facts["id_range"])
    ok(f"{count} hedIds added to {stem}.mediawiki; no other line changed; all inside the range")

    step(3, "Verify the release candidate")
    run(
        [tools["hed_validate_schemas"], rel, "--add-all-extensions", "--require-ids"],
        repo,
        f"hed_validate_schemas {rel} --add-all-extensions --require-ids",
    )
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], repo, "python -m unittest discover -s tests")

    step(4, "Update CHANGELOG.md")
    update_changelog(repo, kind, facts["last"], version, today)

    step(5, "Move the four formats to the release folders")
    move_formats(repo, kind, version)

    step(6, f"Start the {next_version} prerelease")
    start_next_prerelease(repo, kind, version, next_version, tools)

    step(7, "Update the Latest file and the overview table")
    latest = repo / kind.latest_xml()
    shutil.copyfile(repo / kind.folder / "hedxml" / f"{stem}.xml", latest)
    require(latest.read_bytes() == (repo / kind.folder / "hedxml" / f"{stem}.xml").read_bytes(), "Latest copy differs")
    ok(f"{kind.latest_xml()} is a copy of {stem}.xml")
    update_overview(repo, kind, version, next_version, today)

    step(8, "Regenerate the generated files and check them")
    run([sys.executable, "scripts/generate_schema_versions.py"], repo, "python scripts/generate_schema_versions.py")
    run(
        [sys.executable, "scripts/update_latest_json.py", "--update"],
        repo,
        "python scripts/update_latest_json.py --update",
    )
    run(
        [sys.executable, "scripts/generate_schema_versions.py", "--check"],
        repo,
        "python scripts/generate_schema_versions.py --check",
    )
    run(
        [sys.executable, "scripts/update_latest_json.py", "--check"],
        repo,
        "python scripts/update_latest_json.py --check",
    )
    run([sys.executable, "-m", "unittest", "discover", "-s", "tests"], repo, "python -m unittest discover -s tests")

    print("\n== Done: staging the release (nothing is committed)")
    paths = [kind.folder, "docs/schemas_overview.md", "schema_versions.json", "schemas_latest_json"]
    if not kind.is_standard:
        paths.append("schemas_xml_unmerged")
    git(repo, "add", "-A", "--", *paths)
    leftover = git_quiet(repo, "status", "--porcelain").stdout
    # porcelain "XY path": X is the staged state, Y the unstaged one; only "X " lines are fully staged
    require(
        not [line for line in leftover.splitlines() if line[0] == "?" or line[1] != " "],
        "unstaged or untracked changes remain after staging:\n" + leftover,
    )
    print(git_quiet(repo, "status", "--short").stdout.rstrip())
    print("\nReview the staged changes, then commit and push:")
    print(f'   git commit -m "{kind.commit_message(version)}"')


# ---------------------------------------------------------------------------------------------
# notes
# ---------------------------------------------------------------------------------------------


def notes(repo: Path, kind: Kind, version: str, out: Path | None) -> None:
    stem = kind.stem(version)
    print(f"Release notes for {kind.name} {version} from hed-standard main")
    step(1, "Check the release is on hed-standard main")
    remote = upstream_remote(repo)
    git(repo, "fetch", remote)
    ref = f"{remote}/main"
    for rel in (
        f"{kind.folder}/hedxml/{stem}.xml",
        f"{kind.folder}/hedwiki/{stem}.mediawiki",
        f"{kind.folder}/hedjson/{stem}.json",
        kind.latest_xml(),
    ):
        require(
            git_quiet(repo, "cat-file", "-e", f"{ref}:{rel}").returncode == 0, f"{ref} has no {rel}; is the PR merged?"
        )
    ok(f"{ref} has the released {stem} files")
    require(
        git_quiet(repo, "cat-file", "-e", f"{ref}:{kind.folder}/prerelease/{stem}.mediawiki").returncode != 0,
        f"{ref} still has prerelease/{stem}.mediawiki",
    )
    ok(f"{ref} no longer has the {stem} prerelease")
    tags = git_quiet(repo, "ls-remote", "--tags", remote, kind.tag(version)).stdout.strip()
    require(not tags, f"tag {kind.tag(version)} already exists on {remote}")
    ok(f"tag {kind.tag(version)} does not exist yet")

    step(2, "Extract the CHANGELOG entry")
    changelog = git_quiet(repo, "show", f"{ref}:{kind.folder}/CHANGELOG.md")
    require(changelog.returncode == 0, f"cannot read {kind.folder}/CHANGELOG.md on {ref}")
    entry = extract_changelog_entry(changelog.stdout, kind, version)
    out = out or Path(tempfile.gettempdir()) / f"release_notes_{kind.tag(version)}.md"
    write(out, entry)
    ok(f"wrote {len(entry.splitlines())} lines to {out}")

    print("\nCreate the release in the GitHub web interface:")
    print("   https://github.com/hed-standard/hed-schemas/releases/new")
    print(f"   Tag:    {kind.tag(version)}   (create it on publish)")
    print("   Target: main")
    print(f"   Title:  {kind.title(version)}")
    print(f"   Notes:  paste the contents of {out}")


# ---------------------------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("prepare", help="run release steps 0-8 and stage the result")
    p.add_argument("schema", help='"standard" or a library name such as "score"')
    p.add_argument("version", help="the prerelease version to release, e.g. 2.2.0")
    p.add_argument("--next", required=True, dest="next_version", help="the next prerelease version, e.g. 2.3.0")
    p.add_argument("--repo", default=".", help="hed-schemas checkout (default: current directory)")
    n = sub.add_parser("notes", help="after the merge: check main and write the release notes")
    n.add_argument("schema")
    n.add_argument("version")
    n.add_argument("--repo", default=".")
    n.add_argument("--out", help="file for the CHANGELOG entry (default: temp directory)")
    args = parser.parse_args(argv)

    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)
    repo = Path(args.repo).resolve()
    kind = Kind(args.schema)
    try:
        if args.command == "prepare":
            prepare(repo, kind, args.version, args.next_version)
        else:
            notes(repo, kind, args.version, Path(args.out) if args.out else None)
    except ReleaseError as e:
        print(f"\nFAILED: {e}", file=sys.stderr, flush=True)
        print("Stopped; nothing after this step ran.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
