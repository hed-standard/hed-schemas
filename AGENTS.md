# hed-schemas

Purpose: the official HED (Hierarchical Event Descriptors) vocabulary schemas, published in four equivalent formats (MediaWiki, XML, JSON, TSV). Not in scope: validation tools and libraries - those live in the related repositories listed below.

## Commands

Test framework: unittest. Never convert the suite from one style to the other as a side effect of other work.

- Run tests: `python -m unittest discover -s tests -p "test_*.py" -v`
- Lint: `uvx ruff check .` and `uvx ruff format --check .`
- Spell check: `uvx typos`
- Markdown format check: `uvx --with mdformat-myst mdformat --check --wrap no --number docs/ *.md`
- Validate a schema: `hed_validate_schemas <path/to/schema.mediawiki>` (installed with `pip install git+https://github.com/hed-standard/hed-python.git@main`)
- Build docs: `sphinx-build -b html docs/ docs/_build/html` (requires `pip install ".[docs]"`)

CI runs the same checks: see `.github/workflows/` (schema validation, branch verification, ruff, typos, mdformat, docs build, link check).

## Layout

- `standard_schema/` - the base HED vocabulary, all formats plus prerelease.
- `library_schemas/` - domain vocabularies (score, lang, slam, mouse, testlib), same per-schema layout as the standard schema.
- `schemas_latest_json/` - generated copies of each latest released JSON schema; kept honest by `scripts/update_latest_json.py`.
- `schema_versions.json` - generated version manifest; written by `scripts/generate_schema_versions.py`.
- `docs/` - Sphinx documentation source.
- `scripts/` - manifest generation and branch verification.
- `tests/` - unittest suite for the scripts.
- `.status/` - working notes. Gitignored; local to each machine.

## Rules that are easy to get wrong

- ALL schema changes go in a `prerelease/` subdirectory. Never edit a released schema file.
- Edit only the `.mediawiki` file; CI generates the XML, JSON, and TSV formats. Never edit generated formats directly.
- Branch names gate what may change: `standard_*` for the standard schema, `score_*`/`lang_*`/`slam_*`/`mouse_*` for the matching library schema, `admin_*` for everything else. `scripts/verify_branch.py` enforces this on every PR.
- HedIds are permanent identifiers - never reuse one. Ranges per schema are assigned in `library_data.json`.
- Schema versions follow semantic versioning: major for breaking changes (removed or re-meant terms), minor for additions, patch for description fixes. Document changes in the schema's `prerelease/PRERELEASE_CHANGES.md`.
- Library schemas declare a compatible standard schema via `withStandard`.

## Conventions that differ from defaults

- **ASCII only** in prose, code, comments, and filenames: `-` not em or en dashes, `->` not arrows, `...` not an ellipsis character, straight quotes. Exception: genuine data (author names, dataset titles, recorded API responses) keeps whatever characters it actually contains.
- Markdown headings in sentence case: capitalize the first word, proper nouns, and acronyms only.
- HED tags are case-insensitive, but keep the schema's capitalization consistent.

## Related repositories

- `hed-python` - validation and conversion tools (`hedtools` package); the source of the `hed_*` commands above.
- `hed-specification` - the formal specification for HED annotation and schema structure.
- `hed-examples`, `hed-matlab`, `hed-javascript` - examples and tools in other languages.

## Where the thinking lives

`.status/` is gitignored, so it exists only on the machine that wrote it and never in a fresh clone or worktree.

- `.status/README.md` - the index. Read this first; it lists what is active.
- `.status/decisions.md` - why things are the way they are. Read before proposing structural changes. Append entries; never rewrite one.
- `.status/plans/*.md` - active plans. Check the `Status:` header and the `[ ]` / `[x]` markers before starting work.
- `.status/local-environment.md` - this machine's paths, interpreter, and quirks. Tool-agnostic. Never copy its contents into a committed file.
- IMPORTANT: do not read `.status/archive/` unless a file is named for you. Nothing new is created at the `.status/` root.

## Working agreements

- IMPORTANT: every file written to `.status/` opens with a `For humans:` summary - three or four sentences, at the very top: what the file is and what a person needs to take from it. The same applies to a long answer in a session: lead with the conclusion.
- IMPORTANT: temporary scripts, experiments, and one-off test files go in `.status/scratch/` - **never the repository root**. Delete them when the experiment ends; anything in `scratch/` may be deleted unread.
- IMPORTANT: never delete or rewrite a file under `.status/` without asking first. Appending is fine.
- For a change spanning more than three files, write a plan to `.status/plans/` and stop for review before editing.
- When you are guessing about an external API or data format, say so explicitly rather than assuming.
- Show evidence, not assertions: the command you ran and its actual output.
- Do not commit, push, or create branches unless asked.
