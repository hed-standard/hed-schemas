# HED schemas scripts

This directory contains utility scripts for the hed-schemas repository.

## Schema Validation Scripts

### verify_branch.py

Python script that verifies:

- Branch naming conventions (standard\_*, score\_*, lang\_\*, etc.)
- Changes are only in appropriate schema directories
- Changes are in prerelease/ subdirectories
- Schema files pass validation using hed-python tools

**Usage:**

```bash
# Basic usage
python scripts/verify_branch.py file1.xml file2.mediawiki

# Validate all schema extensions
python scripts/verify_branch.py file1.mediawiki --validate-all

# Override branch name
python scripts/verify_branch.py file1.xml --branch standard_new_feature
```

Used by the `verify_source_branch.yaml` workflow to ensure PRs follow repository conventions.

## Release script

### do_schema_release.py

Releases a schema, the standard schema or a library, following the [Schema release guide](../docs/release_guide.md). Maintainers only. It has two subcommands:

- **`prepare <standard|library> <version> --next <next>`** runs the release steps on an `admin_*` branch, before the pull request: preflight checks; for a library, regenerating the prerelease from its unmerged mediawiki against the released partner standard; validation; hedId assignment with `hed_add_ids` and a check that only hedIds were added; validation with `--require-ids` and the unit tests; regenerating `PRERELEASE_CHANGES.md` with the hedtools `SchemaComparer` and adding it to the schema's `CHANGELOG.md`; moving the four formats out of `prerelease/` and writing the copy in `schemas_xml_unmerged/`; starting the next prerelease with an empty change log; updating the Latest XML, the schema's rows in `docs/schemas_overview.md` and its row in the `README.md` schema table; and regenerating and checking `schema_versions.json` and `schemas_latest_json/`. It ends with everything staged, writes a commit message describing what the run did to a file in the system temporary directory, and prints the `git commit -F` command that uses it. It never commits.
- **`notes <standard|library> <version>`** runs after the pull request has merged: it checks that hed-standard `main` holds the release and that the tag does not exist yet, writes the version's CHANGELOG entry to a file, and prints the tag, target and title to enter when creating the release by hand in the GitHub web interface.

Every step prints what it does; the first failed command or check prints `FAILED:` with the reason and exits with status 1. The script never pushes, tags, or calls the GitHub API.

**Usage:**

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0
python scripts/do_schema_release.py prepare standard 8.6.0 --next 8.7.0
python scripts/do_schema_release.py notes score 2.2.0
python scripts/do_schema_release.py notes score 2.2.0 --out notes.md     # choose the notes file
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0 --repo /path/to/clone   # another checkout
```

Run it with the Python environment that has hedtools installed (`pip install -e .`); it finds the `hed_*` commands next to that interpreter. It needs a git remote pointing at `hed-standard/hed-schemas` (any name) and, for `prepare`, a clean working tree on an `admin_*` branch that contains hed-standard `main`. The pure logic is covered by `tests/test_do_schema_release.py`.

## Manifest and latest-JSON scripts

### generate_schema_versions.py

Generates `schema_versions.json` at the repository root: a single manifest listing every schema version (released / prerelease / deprecated) for the standard schema and each library, with each XML file's git blob SHA and last-commit date. It records version *listings* only, never schema content. Consumers (e.g. hedtools' `get_available_hed_versions()`) can fetch this one file from `raw.githubusercontent.com` instead of making dozens of GitHub REST API directory-listing calls.

**Usage:**

```bash
python scripts/generate_schema_versions.py            # write schema_versions.json
python scripts/generate_schema_versions.py --check     # exit 1 if the committed file is stale
```

### update_latest_json.py

Verifies (or fixes) that each `schemas_latest_json/*_Latest.json` is the merged JSON of the current latest *released* version of that schema. The standard schema's copy is taken byte for byte from `standard_schema/hedjson/`; a library's copy is generated from its merged `hedxml/` file with hedtools, because `hedjson/` is unmerged. Comparison is by git blob SHA. `testlib` is excluded and must never appear in `schemas_latest_json/`.

**Usage:**

```bash
python scripts/update_latest_json.py --check     # read-only; exit 1 if anything is out of sync
python scripts/update_latest_json.py --update     # write the latest released JSON into place
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
