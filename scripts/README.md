# HED schemas scripts

This directory contains utility scripts for the hed-schemas repository.

## Schema Validation Scripts

### verify_branch.py

Python script that verifies:

- Branch naming conventions (standard\_*, score\_*, lang\_\*, etc.)
- Changes are only in appropriate schema directories
- Changes are in prerelease/ subdirectories
- Schema files pass validation using hed-python tools

**Usage:** the following examples assume that you are in the root of your local repository with its venv activated, and that `file1.xml` and `file2.mediawiki` are the changed files to check.

**Check the changed files.**

```bash
python scripts/verify_branch.py file1.xml file2.mediawiki
```

**Also validate all schema extensions.**

```bash
python scripts/verify_branch.py file1.mediawiki --validate-all
```

**Check against a different branch name** than the current one.

```bash
python scripts/verify_branch.py file1.xml --branch standard_new_feature
```

Used by the `verify_source_branch.yaml` workflow to ensure PRs follow repository conventions.

## Release script

### do_schema_release.py

Releases a schema, the standard schema or a library, following the [Schema release guide](../docs/release_guide.md). Maintainers only. It has two subcommands:

- **`prepare <standard|library> <version> --next <next>`** runs the release steps on an `admin_*` branch, before the pull request: preflight checks; for a library, regenerating the prerelease from its unmerged mediawiki against the released partner standard; validation; hedId assignment with `hed_add_ids` and a check that only hedIds were added; validation with `--require-ids` and the unit tests; regenerating `PRERELEASE_CHANGES.md` with the hedtools `SchemaComparer` and adding it to the schema's `CHANGELOG.md`; moving the four formats out of `prerelease/` and writing the copy in `schemas_xml_unmerged/`; starting the next prerelease with an empty change log; updating the Latest XML, the schema's rows in `docs/schemas_overview.md` and its row in the `README.md` schema table; and regenerating and checking `schema_versions.json` and `schemas_latest_json/`. It ends with everything staged, prints a summary of what the run did for the pull request description, and prints the `git commit -m` command for the release. It never commits.
- **`notes <standard|library> <version>`** runs after the pull request has merged: it checks that hed-standard `main` holds the release and that the tag does not exist yet, prints the tag, target and title to enter when creating the release by hand in the GitHub web interface, and prints the version's CHANGELOG entry between `----- release notes -----` and `----- end of release notes -----` markers (with `--out FILE` it also writes the entry to that file).

Every step prints what it does; the first failed command or check prints `FAILED:` with the reason and exits with status 1. The script never pushes, tags, or calls the GitHub API.

**Usage:** the following examples assume that you are in the root of your local repository with its venv activated, on an `admin_*` branch made from hed-standard `main`, and that you are releasing either the SCORE 2.2.0 prerelease (with 2.3.0 as the next prerelease) or the standard schema 8.6.0 prerelease (with 8.7.0 as the next prerelease).

**Prepare a library release.**

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0
```

**Prepare a standard schema release.**

```bash
python scripts/do_schema_release.py prepare standard 8.6.0 --next 8.7.0
```

**Prepare a release in another checkout** than the current directory (here `/path/to/clone`).

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0 --repo /path/to/clone
```

**Print the release notes after the merge.**

```bash
python scripts/do_schema_release.py notes score 2.2.0
```

**Print the release notes and also write them to a file** (here `notes.md`).

```bash
python scripts/do_schema_release.py notes score 2.2.0 --out notes.md
```

Run it with the Python environment that has hedtools installed (`pip install -e .`); it finds the `hed_*` commands next to that interpreter. It needs a git remote pointing at `hed-standard/hed-schemas` (any name) and, for `prepare`, a clean working tree on an `admin_*` branch that contains hed-standard `main`. The pure logic is covered by `tests/test_do_schema_release.py`.

## Manifest and latest-JSON scripts

### generate_schema_versions.py

Generates `schema_versions.json` at the repository root: a single manifest listing every schema version (released / prerelease / deprecated) for the standard schema and each library, with each XML file's git blob SHA and last-commit date. It records version *listings* only, never schema content. Consumers (e.g. hedtools' `get_available_hed_versions()`) can fetch this one file from `raw.githubusercontent.com` instead of making dozens of GitHub REST API directory-listing calls.

**Usage:**

**Write `schema_versions.json`.**

```bash
python scripts/generate_schema_versions.py
```

**Check the committed file** (read-only; exits 1 if it is stale).

```bash
python scripts/generate_schema_versions.py --check
```

### update_latest_json.py

Verifies (or fixes) that each `schemas_latest_json/*_Latest.json` is the merged JSON of the current latest *released* version of that schema. The standard schema's copy is taken byte for byte from `standard_schema/hedjson/`; a library's copy is generated from its merged `hedxml/` file with hedtools, because `hedjson/` is unmerged. Comparison is by git blob SHA. `testlib` is excluded and must never appear in `schemas_latest_json/`.

**Usage:**

**Check the Latest copies** (read-only; exits 1 if anything is out of sync).

```bash
python scripts/update_latest_json.py --check
```

**Write the latest released JSON into place.**

```bash
python scripts/update_latest_json.py --update
```

Generating a library's JSON needs hedtools (`pip install -e .` from the repository root installs it). The output depends on the hedtools version: after hedtools changes its JSON writer, `--check` can report a library out of date, and `--update` rewrites the copy.

Both scripts are run by the `update_manifests.yaml` workflow: `--check` on pull requests, and regenerate-and-commit on push to `main`.

## Documentation Build

### Building Documentation Locally

Navigate to the repository root and use `sphinx-build`:

**Windows:**

```powershell
sphinx-build -b html docs/ docs/_build/html
```

**Unix/Mac:**

```bash
sphinx-build -b html docs/ docs/_build/html
```

This will build the Sphinx documentation to `docs/_build/html/`.

### Serving Documentation Locally

After building, you can serve the documentation with Python's built-in HTTP server:

**Windows:**

```powershell
cd docs\_build\html
python -m http.server 8000
```

**Unix/Mac:**

```bash
cd docs/_build/html
python -m http.server 8000
```

Then open your browser to [http://localhost:8000](http://localhost:8000).

Press Ctrl+C to stop the server.

**Alternative**: You can also open `docs/_build/html/index.html` directly in your web browser.

### Options for HTTP server

```bash
# Use a different port
python -m http.server 8080
```

## Quick Start

To set up your development environment:

```bash
# Install all development dependencies
pip install ".[dev]"

# Build documentation
sphinx-build -b html docs/ docs/_build/html

# Serve documentation
cd docs/_build/html
python -m http.server 8000
```
