---
html_meta:
  description: Maintainer guide for releasing a HED standard or library schema from hed-schemas
  keywords: HED release, schema release, hedId, do_schema_release, maintainers
---

```{index} release guide; schema release; hedId; do_schema_release
```

# Schema release guide

This guide is for HED maintainers. It describes how a new version of a schema, the standard schema or a library schema, goes from a reviewed prerelease to a published release. Contributors never do any of this: their work ends when a prerelease change is merged (see the [Schema developer guide](developer_guide.md)).

A release is done in three parts:

1. **`prepare`** - on an `admin_*` branch, `scripts/do_schema_release.py prepare` runs every file-level release step, checks each one, and leaves the result staged for review.
2. **Pull request** - you review, commit and push, open a pull request against hed-standard `main`, and merge it when CI is green.
3. **`notes` and the GitHub release** - after the merge, `scripts/do_schema_release.py notes` checks `main` and writes the CHANGELOG entry to a file; you create the tag and the GitHub release by hand in the GitHub web interface.

The script never commits, pushes, tags, or calls the GitHub API. The final look over everything, and the release itself, stay with a person.

## What a release changes

| Item                                                                   | Before the release                                   | After the release                                                                 |
| ---------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| Prerelease files `prerelease/<stem>.*` and `prerelease/hedtsv/<stem>/` | the candidate, possibly without some hedIds          | moved to `hedwiki/`, `hedxml/`, `hedjson/`, `hedtsv/`, every element with a hedId |
| `prerelease/` contents                                                 | the version being released                           | the next version, seeded from the release, with an empty change log               |
| `CHANGELOG.md` of the schema                                           | -                                                    | a new entry at the top, generated with the hedtools `SchemaComparer`              |
| `hedxml/HEDLatest.xml` or `hedxml/HED_<lib>_Latest.xml`                | the previous release                                 | a copy of the new release                                                         |
| `schemas_xml_unmerged/<stem>.xml`                                      | -                                                    | the unmerged XML of the new release                                               |
| `docs/schemas_overview.md`                                             | old Latest row, Prerelease row for this version      | new Latest row (with release date) and Prerelease row for the next version        |
| `README.md` schema table                                               | Latest = previous release, Prerelease = this version | Latest = this version, Prerelease = the next version                              |
| `schema_versions.json`, `schemas_latest_json/`                         | list the old release and this prerelease             | regenerated                                                                       |

Here `<stem>` is `HED8.5.0` for the standard schema and `HED_score_2.2.0` for a library; see [Naming](#naming).

## Before you start

### Working Group approval

The HED Working Group must have approved the prerelease for release. Nothing in the tooling checks this.

### Release the standard schema first

Release the standard schema before any library that partners with it. A library's merged XML embeds the standard schema it partners with (its `withStandard`), and hedtools loads that standard from its local cache, not from this checkout. A library regenerated against a prerelease of the standard bakes stale standard content, without hedIds, into its released XML.

For a library release, `prepare` therefore stops unless:

- the library's `withStandard` is the **latest released** standard schema (repartnering a library is a content change for its own `<lib>_*` branch, not part of a release), and
- the local hedtools cache has no stale prerelease copy of that standard (`~/.hedtools/hed_cache/prerelease/HED<version>.xml`). Delete such a copy if `prepare` reports one; hedtools then downloads the released file on demand.

### Tools

hedtools is a dependency of this repository (`pyproject.toml`), installed from PyPI. From the repository root:

```bash
pip install -e .
```

pip does not upgrade an installed hedtools that already satisfies the requirement, so before every release update it to the latest release:

```bash
pip install --upgrade hedtools
```

`prepare` checks that the installed hedtools has `hed_validate_schemas --require-ids` and stops if it is too old. Run the script with the Python of that environment (for example `.venv\Scripts\python.exe` on Windows); it finds the `hed_*` commands next to that interpreter.

### Git remote

The script needs a git remote that points at `hed-standard/hed-schemas`. The remote's name does not matter (it is often `upstream` in a fork checkout and `origin` in a direct clone); the script finds it by URL and fetches it.

### Branch

A release must be done on an **`admin_*` branch** that starts from hed-standard `main`. The following example assumes that you are on the `main` branch in your local repository and that you are going to release the SCORE HED library schema version 2.2.0:

```bash
git fetch upstream
git switch -c admin_score_2.2.0 upstream/main
```

(Use the name of your remote for hed-standard in place of `upstream`.) The reason is the branch check in CI, `scripts/verify_branch.py`: a schema-area branch (`standard_*`, `score_*`, `lang_*`, ...) may change only its own `prerelease/` folder, and may not touch the released folders `hedxml/`, `hedwiki/`, `hedtsv/` and `hedjson/`, `docs/` or the generated files. Only `admin_*` branches may change anything. `prepare` refuses to run on any other branch, so a release never gets as far as a pull request that CI would reject.

The working tree must be clean when `prepare` starts, and the branch must contain hed-standard `main`.

## Releasing with do_schema_release.py

The script takes `standard` or a library name, exactly as `hed_add_ids` does. A release uses one `prepare` command and, after the merge, one `notes` command. The following examples assume that you are in the root of your local repository with its venv activated, on the `admin_*` branch made in [Branch](#branch).

**Prepare a library release.** This example releases the SCORE 2.2.0 prerelease and starts 2.3.0 as the next SCORE prerelease:

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0
```

**Prepare a standard schema release.** This example releases the standard schema 8.6.0 prerelease and starts 8.7.0 as the next standard prerelease:

```bash
python scripts/do_schema_release.py prepare standard 8.6.0 --next 8.7.0
```

`--next` is required: it is the version of the prerelease that `prepare` starts after the release. It is normally the next minor version, but the choice is yours. `--repo PATH` runs the script against another checkout (the default is the current directory); this is how the script is tried out on a throwaway clone.

**Write the release notes after the merge.** This example assumes that the pull request that released SCORE 2.2.0 has been merged:

```bash
python scripts/do_schema_release.py notes score 2.2.0
```

Every step prints a `== Step N` header, then each command before it runs and an `ok:` line with its result. The first command that exits with an error, or the first check that fails, prints `FAILED:` with the reason (and the last lines of the command's output) and stops the script with exit status 1. Nothing after that point runs.

### The prepare steps

| Step                           | What it does                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | It stops if                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. Preflight                   | Checks the setup; changes nothing.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | not a hed-schemas checkout; not on an `admin_*` branch; uncommitted changes; the branch does not contain hed-standard `main`; hedtools too old; the schema is not in `library_data.json`; a prerelease file is missing; the version is already released; `--next` is not greater, or already exists; for a library, the partner is not the latest released standard, or a stale copy of it is in the cache; the `README.md` schema table or the `docs/schemas_overview.md` sections lack the schema or are not in order (standard first, then libraries alphabetically) |
| 1. Regenerate and validate     | For a library, rebuilds the prerelease from its unmerged mediawiki with `hed_update_schemas`, against the released partner, and prints what changed. Then validates all four formats with `hed_validate_schemas --add-all-extensions`.                                                                                                                                                                                                                                                    | the formats do not agree                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2. Assign hedIds               | Runs `hed_add_ids . <schema> <version>`, which gives each element without an id the lowest free id in the schema's range, and rewrites the four formats. Then compares the mediawiki before and after.                                                                                                                                                                                                                                                                                    | any line changed by more than an added hedId; an id is outside the schema's range in `library_data.json`; an id was assigned twice                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 3. Verify                      | Validates again with `--require-ids` and runs the repository unit tests (`python -m unittest discover -s tests`), which include the retired-id registry checks.                                                                                                                                                                                                                                                                                                                           | an element has no hedId; a test fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 4. CHANGELOG                   | Regenerates the comparison from the last released version to the candidate with the hedtools `SchemaComparer` and writes it to `prerelease/PRERELEASE_CHANGES.md` if it changed. Inserts it at the top of the schema's `CHANGELOG.md` under `## Changes for HED <version> Release M/D/YYYY` (standard) or `## Changes for HED <lib> <version> Release M/D/YYYY` (library), in the layout described in [CHANGELOG entries](#changelog-entries).                                            | the comparison fails; the CHANGELOG already has an entry for this version                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 5. Move                        | `git mv` of the four formats from `prerelease/` to `hedwiki/`, `hedxml/`, `hedjson/` and `hedtsv/`. Also writes `schemas_xml_unmerged/<stem>.xml`: for a library, the unmerged XML generated from the released merged XML; for the standard schema, a copy of the released XML.                                                                                                                                                                                                           | a move fails; the unmerged XML cannot be written                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 6. Next prerelease             | Copies the released mediawiki to `prerelease/<next stem>.mediawiki`, changes the version on its first line, lets `hed_update_schemas` write the XML, JSON and TSV, validates them with `--require-ids`, and replaces `PRERELEASE_CHANGES.md` with just its heading. `PROPOSED.md` is left as it is.                                                                                                                                                                                       | the new prerelease does not validate                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 7. Latest, overview and README | Copies the released XML over the Latest file. In `docs/schemas_overview.md`, replaces the schema's Latest and Prerelease rows: the new release becomes Latest with today's date and links to the released folders, the next version becomes Prerelease with links into `prerelease/`, and for a library the "Partnered with" column comes from the `withStandard` header. In the schema table of `README.md`, sets the schema's Latest and Prerelease cells. Runs mdformat on both files. | the schema's table does not have exactly one Prerelease row and at most one Latest row; a column is not recognized; the overview still links to the moved prerelease files; `README.md` does not have exactly one row for the schema                                                                                                                                                                                                                                                                                                                                    |
| 8. Generated files             | Runs `scripts/generate_schema_versions.py` and `scripts/update_latest_json.py --update`, then both with `--check`, then the unit tests again.                                                                                                                                                                                                                                                                                                                                             | a check fails                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Done                           | Stages the changes with `git add` and prints `git status --short`. Prints a summary of what this run did, for the pull request description: whether regeneration changed anything, how many hedIds were assigned, how the CHANGELOG entry was made, what a first release had to create. Then prints the commit command, `git commit -m "Release HED score library 2.2.0"`. Nothing is written outside the repository.                                                                     | anything is left unstaged or untracked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Example: score 2.2.0

This is a trial run of the SCORE 2.2.0 release on a throwaway clone of the repository. The following example assumes that the clone is on a branch named `admin_score_test` made from hed-standard `main`, that its remote for hed-standard is named `upstream`, and that the script was run with `--repo` pointing at the clone. At the time, SCORE 2.1.0 (partnered with standard 8.4.0) was the last SCORE release, the SCORE 2.2.0 prerelease was partnered with standard 8.5.0, and 8.5.0 was the latest released standard schema. The output is shortened; repeated lines are removed:

```text
== Step 0: Preflight checks
   ok: on branch admin_score_test
   ok: working tree is clean
   $ git fetch upstream
   ok: exit 0
   ok: HEAD contains upstream/main
   ok: hedtools has --require-ids
   ok: 'score' registered in library_data.json, id range 40000-59999
   ok: prerelease HED_score_2.2.0 has all four formats and PRERELEASE_CHANGES.md
   ok: last released version: 2.1.0
   ok: partner standard 8.5.0 is the latest released standard and not stale in the cache

== Step 1: Regenerate the prerelease from the unmerged mediawiki against standard 8.5.0, then validate
   $ hed_update_schemas library_schemas/score/prerelease/HED_score_2.2.0.mediawiki
   ok: regeneration changed:
 .../score/prerelease/HED_score_2.2.0.xml           | 223 ++++++++++++++++++++-
   $ hed_validate_schemas library_schemas/score/prerelease/HED_score_2.2.0.mediawiki --add-all-extensions
   ok: exit 0

== Step 2: Assign hedIds
   $ hed_add_ids . score 2.2.0
   ok: 0 hedIds added to HED_score_2.2.0.mediawiki; no other line changed; all inside the range

== Step 4: Update CHANGELOG.md
   ok: PRERELEASE_CHANGES.md regenerated (214 -> 228 lines); the CHANGELOG entry uses the new report
   ok: inserted '## Changes for HED score 2.2.0 Release 10/16/2026' into library_schemas/score/CHANGELOG.md

== Step 7: Update the Latest file, the overview table and the README table
   ok: library_schemas/score/hedxml/HED_score_Latest.xml is a copy of HED_score_2.2.0.xml
   ok: overview rows: 2.2.0 Latest (October 16, 2026), 2.3.0 Prerelease
   ok: README.md: score Latest 2.2.0, Prerelease 2.3.0

== Done: staging the release (nothing is committed)
R  library_schemas/score/prerelease/HED_score_2.2.0.xml -> library_schemas/score/hedxml/HED_score_2.2.0.xml
A  library_schemas/score/prerelease/HED_score_2.3.0.mediawiki
M  schema_versions.json
A  schemas_xml_unmerged/HED_score_2.2.0.xml

Summary of this run, for the pull request description:

   Prepared with scripts/do_schema_release.py on 10/16/2026.

   - Regenerated the prerelease against released standard 8.5.0
     (HED_score_2.2.0.xml).
   - Assigned 0 new hedIds; validated with --require-ids.
   - Added the CHANGELOG entry from the SchemaComparer report against 2.1.0
     (226 lines; PRERELEASE_CHANGES.md regenerated).
   - Moved the four formats to hedwiki/, hedxml/, hedjson/ and hedtsv/ and
     wrote schemas_xml_unmerged/HED_score_2.2.0.xml.
   - Started the 2.3.0 prerelease with an empty PRERELEASE_CHANGES.md.
   - Updated HED_score_Latest.xml, the docs/schemas_overview.md rows and
     the README.md row.
   - Regenerated schema_versions.json and schemas_latest_json/.

Review the staged changes, then commit and push:
   git commit -m "Release HED score library 2.2.0"
```

Two things in this run are typical of a library release:

- **Step 1 changed the merged XML.** The score prerelease had last been regenerated against an early prerelease of standard 8.5.0, so its merged XML lacked six standard tags and the hedIds of 152 standard elements, while score's own entries were unchanged. Regenerating from the unmerged mediawiki against the released 8.5.0 fixes this. Without the regeneration, the validation fails with a report that lists these differences under "From the partner standard schema".
- **Step 4 regenerated `PRERELEASE_CHANGES.md`.** The comparison is between merged schemas, so a new partner changes it. The CHANGELOG entry is always built from the regenerated report.

### Reviewing and committing

`prepare` leaves everything staged. Before committing, look at least at:

- `git diff --cached --stat` - the moves should show as renames (`R`), and the only new files should be the next prerelease and the `schemas_xml_unmerged/` copy;
- the new entry at the top of the schema's `CHANGELOG.md`, and add a `## Key overall changes:` summary under its heading if the release needs one (see [CHANGELOG entries](#changelog-entries));
- the schema's two rows in `docs/schemas_overview.md`, and its row in the `README.md` schema table;
- `prerelease/PRERELEASE_CHANGES.md`, which should hold only its heading.

Then commit with the printed `git commit -m` command, push the branch, and open a pull request against hed-standard `main`, pasting the printed summary into its description. CI runs the schema validation on the changed schema files, the branch check, the manifest and Latest-JSON checks, the unit tests, and the documentation checks. Merge when it is green.

### If prepare fails

A failure leaves the steps before it done and the rest undone. Nothing is committed, so the branch can always be put back. The following example assumes that you are in the root of your local repository, on the `admin_*` branch where `prepare` failed, and that the branch had no uncommitted changes of your own before `prepare` started (these commands discard every uncommitted change):

```bash
git restore --staged --worktree .
git clean -n        # lists the new files prepare created; check the list, then
git clean -f        # removes them
```

Fix the cause the `FAILED:` line names, and run `prepare` again from a clean tree.

### After the merge: notes and the GitHub release

When the pull request is merged, run `notes`. The following example assumes that you are in the root of your local repository with its venv activated, and that the pull request that released SCORE 2.2.0 has been merged into hed-standard `main` (any local branch will do, since `notes` reads hed-standard `main` directly):

```bash
python scripts/do_schema_release.py notes score 2.2.0
```

`notes` fetches hed-standard `main` and checks that it holds the released files and the Latest file, that it no longer holds the prerelease of that version, and that the tag does not exist yet. It then extracts the version's entry from the schema's `CHANGELOG.md` on `main`, prints what to enter, and prints the entry between `----- release notes -----` and `----- end of release notes -----` markers. With `--out FILE` it also writes the entry to that file.

The following example is the end of the actual output of `notes mouse 1.0.0`, run on 10/25/2026 after the pull request that released MOUSE 1.0.0 (the first MOUSE release) was merged. The two marker lines are not part of the notes: paste only the lines between them into the release description.

```text
== Step 2: Extract the CHANGELOG entry
   ok: 3 lines, printed between the markers below

Create the release in the GitHub web interface:
   https://github.com/hed-standard/hed-schemas/releases/new
   Tag:    mouse_v1.0.0   (create it on publish)
   Target: main
   Title:  HED MOUSE v1.0.0
   Notes:  paste the text between the markers

----- release notes -----
## Changes for HED mouse 1.0.0 Release 10/25/2026

This is the initial release of the HED MOUSE library schema, partnered with HED standard schema 8.5.0.
----- end of release notes -----
```

Create the release in the GitHub web interface. The following steps use SCORE 2.2.0 as the example; `notes` prints the tag and title for your release, and [Naming](#naming) shows the pattern:

1. Open [https://github.com/hed-standard/hed-schemas/releases/new](https://github.com/hed-standard/hed-schemas/releases/new).
2. In the tag field, type the new tag (for example `score_v2.2.0`) and choose to create it when the release is published. Set the target branch to `main`.
3. Enter the title (for example `HED SCORE v2.2.0`).
4. Paste the release notes (the text between the markers, or the `--out` file) into the description.
5. Attach the released files (drag them onto the box below the description). Take them from hed-standard `main` as merged, not from whatever branch you ran `notes` on: `notes` reads `main` remotely and does not change your working tree. With a clean working tree, check out the merged `main` first (switch back to your branch afterwards):
   ```bash
   git fetch upstream
   git switch --detach upstream/main
   ```
   For SCORE 2.2.0 the files are, from `library_schemas/score/`:
   - `hedxml/HED_score_2.2.0.xml` (for a library, this is the merged file that includes the standard schema)
   - `hedjson/HED_score_2.2.0.json`
   - `hedwiki/HED_score_2.2.0.mediawiki`
   - `hedtsv.zip`, a zip of the `hedtsv/HED_score_2.2.0/` folder. The following example assumes that you are in the root of your local repository with its venv activated; it writes the zip next to the repository, not inside it, and works the same in bash, PowerShell and cmd:
     ```bash
     python -m zipfile -c ../hedtsv.zip library_schemas/score/hedtsv/HED_score_2.2.0
     ```
   For the standard schema the files are in `standard_schema/` and named `HED8.6.0.xml`, `HED8.6.0.json`, `HED8.6.0.mediawiki` and `hedtsv/HED8.6.0/`. The same files are uploaded to Zenodo (see [After the release](#after-the-release)).
6. Look everything over one last time and publish the release.

GitHub creates the tag on `main` when the release is published; no tag is made locally.

## Releasing the standard schema

The same commands apply, with `standard` in place of a library name. The following example assumes that you are in the root of your local repository with its venv activated, on an `admin_*` branch made from hed-standard `main` (for example `admin_8.6.0`), that 8.5.0 is the latest released standard schema, and that you are going to release the standard schema prerelease 8.6.0 and start 8.7.0 as the next prerelease.

**Prepare the release** (before the pull request):

```bash
python scripts/do_schema_release.py prepare standard 8.6.0 --next 8.7.0
```

**Write the release notes** (after the pull request is merged):

```bash
python scripts/do_schema_release.py notes standard 8.6.0
```

The differences from a library release are handled by the script:

- there is no partner, so step 0 has no partner checks and step 1 only validates;
- the standard schema has no merged or unmerged distinction, so its `schemas_xml_unmerged/` copy in step 5 is a plain copy of the released XML;
- the Latest file is `standard_schema/hedxml/HEDLatest.xml`, and the overview table has no "Partnered with" column;
- the tag is `v8.6.0` and the title `HED v8.6.0`.

After a standard release, the libraries that will partner with it are repartnered on their own `<lib>_*` branches before their next release.

## Naming

The following table assumes a release of standard schema 8.6.0 and of SCORE library schema 2.2.0; substitute your own schema name and version:

| Item              | Standard schema                             | Library schema (score)                            |
| ----------------- | ------------------------------------------- | ------------------------------------------------- |
| Folder            | `standard_schema/`                          | `library_schemas/score/`                          |
| File stem         | `HED8.6.0`                                  | `HED_score_2.2.0`                                 |
| Latest file       | `hedxml/HEDLatest.xml`                      | `hedxml/HED_score_Latest.xml`                     |
| CHANGELOG heading | `## Changes for HED 8.6.0 Release M/D/YYYY` | `## Changes for HED score 2.2.0 Release M/D/YYYY` |
| Git tag           | `v8.6.0`                                    | `score_v2.2.0`                                    |
| Release title     | `HED v8.6.0`                                | `HED SCORE v2.2.0`                                |
| Commit message    | `Release HED standard schema 8.6.0`         | `Release HED score library 2.2.0`                 |

## The steps by hand

The script follows these steps; use them to understand a failure, or when the script cannot be used. The following steps assume that you are in the root of your local repository with its venv activated, on the `admin_*` branch made in [Branch](#branch), and that you are going to release the SCORE 2.2.0 prerelease (partnered with standard 8.5.0, the latest released standard schema), that SCORE 2.1.0 is the last SCORE release, and that 2.3.0 will be the next SCORE prerelease. For the standard schema, use `standard_schema/` and `HED8.6.0` in place of `library_schemas/score/` and `HED_score_2.2.0`, and skip the library-only parts. The `cp` commands work in bash and PowerShell; in cmd use `copy`.

1. **Regenerate (library) and validate the prerelease.**

   ```bash
   hed_update_schemas library_schemas/score/prerelease/HED_score_2.2.0.mediawiki
   hed_validate_schemas library_schemas/score/prerelease/HED_score_2.2.0.mediawiki --add-all-extensions
   ```

2. **Assign the hedIds.** Each element without an id gets the lowest free id in the schema's range from `library_data.json` (retired ids are never reused), and all four prerelease formats are rewritten. The schema must be registered in `library_data.json`; a new library gets its `id_range` there, merged to `main`, before its first release. Review the diff: only `hedId` additions, all inside the schema's range.

   ```bash
   hed_add_ids . score 2.2.0
   ```

   `hed_update_schemas <prerelease .mediawiki> --set-ids` does the same from the mediawiki.

3. **Verify the candidate**: all four formats agree and every element has an id.

   ```bash
   hed_validate_schemas library_schemas/score/prerelease/HED_score_2.2.0.mediawiki --add-all-extensions --require-ids
   python -m unittest discover -s tests
   ```

   For a library, `--require-ids` also reports standard elements without an id in the merged form: that means the library was regenerated against a prerelease of the standard.

4. **Update CHANGELOG.md** from the `SchemaComparer` report of the last release against the candidate (do not hand-edit it):

   ```python
   from hed.schema import load_schema
   from hed.schema.schema_comparer import SchemaComparer

   old = load_schema("library_schemas/score/hedxml/HED_score_2.1.0.xml")
   new = load_schema("library_schemas/score/prerelease/HED_score_2.2.0.mediawiki")
   print(SchemaComparer(old, new).compare_differences(title="Differences between HED_score_2.1.0 and HED_score_2.2.0"))
   ```

   Write the report to `prerelease/PRERELEASE_CHANGES.md`, and put it at the top of `CHANGELOG.md` under the heading from [Naming](#naming) in place of the report's own heading, in the layout described in [CHANGELOG entries](#changelog-entries).

5. **Move all four formats** to the release folders:

   ```bash
   git mv library_schemas/score/prerelease/HED_score_2.2.0.mediawiki library_schemas/score/hedwiki/
   git mv library_schemas/score/prerelease/HED_score_2.2.0.xml library_schemas/score/hedxml/
   git mv library_schemas/score/prerelease/HED_score_2.2.0.json library_schemas/score/hedjson/
   git mv library_schemas/score/prerelease/hedtsv/HED_score_2.2.0 library_schemas/score/hedtsv/
   ```

   Then write the copy in `schemas_xml_unmerged/`. For the standard schema it is a plain copy (`cp standard_schema/hedxml/HED8.6.0.xml schemas_xml_unmerged/`); for a library, save the unmerged form:

   ```python
   from hed.schema import load_schema

   load_schema("library_schemas/score/hedxml/HED_score_2.2.0.xml").save_as_xml(
       "schemas_xml_unmerged/HED_score_2.2.0.xml", save_merged=False
   )
   ```

6. **Start the next prerelease** with the released content and an empty change log:

   ```bash
   cp library_schemas/score/hedwiki/HED_score_2.2.0.mediawiki library_schemas/score/prerelease/HED_score_2.3.0.mediawiki
   # edit line 1: version="2.2.0" -> version="2.3.0" (keep library= and withStandard=)
   hed_update_schemas library_schemas/score/prerelease/HED_score_2.3.0.mediawiki
   ```

   Then replace `prerelease/PRERELEASE_CHANGES.md` with just its heading, `## Differences between HED_score_2.2.0 and HED_score_2.3.0`. `PROPOSED.md` stays as it is.

7. **Update the Latest file and the overview table**:

   ```bash
   cp library_schemas/score/hedxml/HED_score_2.2.0.xml library_schemas/score/hedxml/HED_score_Latest.xml
   ```

   In `docs/schemas_overview.md`, make the release the Latest row (with its release date and links to `hedxml/`, `hedwiki/`, `hedjson/` and `hedtsv/`) and the next version the Prerelease row (links into `prerelease/`). The moves in step 5 break the old prerelease links, so this is not optional. In the schema table of `README.md`, set the schema's Latest cell to the release and its Prerelease cell to the next version. Run `python -m mdformat --wrap no --number docs/schemas_overview.md README.md` afterwards.

8. **Regenerate the generated files** and check them:

   ```bash
   python scripts/generate_schema_versions.py
   python scripts/update_latest_json.py --update
   python scripts/generate_schema_versions.py --check
   python scripts/update_latest_json.py --check
   ```

   `schemas_latest_json/` holds the merged JSON of the latest released version of each schema; the script generates a library's copy from its merged `hedxml/` file with hedtools. CI rejects a pull request whose manifest or Latest copies are stale.

9. **Commit, push and open the pull request**, then after the merge create the release in the GitHub web interface as described in [After the merge](#after-the-merge-notes-and-the-github-release).

## After the release

- **Zenodo**: a HED maintainer creates the Zenodo upload by hand; nothing happens automatically when the GitHub release is published. Each schema has its own Zenodo record (the DOIs in the `README.md` schema table), so a release of an existing schema is uploaded as a new version of that schema's record, and the first release of a new library creates a new record. Upload the same files that are attached to the GitHub release (step 5 in [After the merge](#after-the-merge-notes-and-the-github-release)). In the upload form, set **Copyright** to the line in the schema's `LICENSE` file (for example `Copyright (c) 2021, HED Contributors.`) and **License** to Creative Commons Attribution 4.0 International, which is the license in that file. When a new record's DOI is minted, add it in a small `admin_*` pull request: to the badges on the first line of `README.md`, the schema's row in the `README.md` schema table, its section in `docs/schemas_overview.md`, and as a badge on the first line of the schema's own `README.md` (for example `library_schemas/mouse/README.md`). A new version of an existing record keeps the same DOI, so nothing changes.
- **Downstream**: hed-python bundles the released standard XML in `hed/schema/schema_data/` (and the released library XML it ships), hed-tests refreshes its schema snapshots, and the JavaScript validator picks up the new version.
- **Partnered libraries**: after a standard release, a library that should use the new standard is repartnered and regenerated on its own branch, then released with this guide.

## Troubleshooting

**`FAILED: on branch '...': a release must run on an admin_* branch`** - create an `admin_*` branch from hed-standard `main` (see [Branch](#branch)). The pull request from a schema-area branch would be rejected by `verify_source_branch.yaml`.

**Step 1 validation lists differences "From the partner standard schema", or "Attribute hedId modified from None"** - the library's merged XML embeds an old prerelease of its partner. For a library, step 1 regenerates the prerelease before validating, which fixes this; if it still fails, check for a stale copy of the partner in `~/.hedtools/hed_cache/prerelease/` (step 0 reports one) and refresh hedtools.

**`partner standard X is not the latest released standard`** - the library must be repartnered with the latest standard on its own branch, and that change merged, before it is released.

**`hedtools is too old (no --require-ids)`** - update hedtools with `pip install --upgrade hedtools` (see [Tools](#tools)).

**Step 2 reports a line changed by more than a hedId** - the prerelease formats were not in step with each other; validate and regenerate the prerelease on its schema branch first.

**`PRERELEASE_CHANGES.md regenerated (N -> M lines)`** - not an error. The committed report was made against older content (often an older partner); the regenerated one is what the release uses.

**The library CHANGELOG lists changes to standard tags** - expected: `SchemaComparer` compares the merged schemas, so changes to the partnered standard between the two releases appear in the library's report, under `## Changes to the partner standard schema`.

**`notes` writes only part of an entry** - a `##` section heading inside the entry contains the word "release", so `notes` took it for the next release's heading. Reword the section heading (see [CHANGELOG entries](#changelog-entries)).

**CI: Validate schemas fails on a non-schema file** - `validate_schemas.yaml` validates only files under the schema folders; a JSON file elsewhere (such as `schema_versions.json`) is not a schema and is not passed to the validator.

**CI: the manifest or Latest JSON check fails** - rerun step 8 and commit the result.

## Reference

### File forms

Each folder holds exactly one form of a schema:

| Folder                            | Form                                                     |
| --------------------------------- | -------------------------------------------------------- |
| `hedwiki/`, `hedtsv/`, `hedjson/` | unmerged (library content only)                          |
| `hedxml/`                         | merged (standard content included for a library)         |
| `schemas_xml_unmerged/`           | unmerged XML, one per released version of each schema    |
| `schemas_latest_json/`            | merged JSON, only the latest released version per schema |

The test-only library `testlib` is excluded from both generated folders. `hed_update_schemas` and `hed_add_ids` write the four prerelease files in these forms. The standard schema has no merged or unmerged distinction.

### CHANGELOG entries

Each schema's `CHANGELOG.md` starts with its title and lists the releases newest first. An entry starts with a release heading and runs to the next release heading. For a library with an earlier release, `prepare` writes an entry like the following. The following example assumes the LANG 1.2.0 release of 10/17/2026, whose previous release, LANG 1.1.0, was partnered with standard 8.4.0, while LANG 1.2.0 is partnered with standard 8.5.0:

```markdown
## Changes for HED lang 1.2.0 Release 10/17/2026

## Changes to LANG

**Tags:**

- ...

## Changes to the partner standard schema (8.4.0 -> 8.5.0)

**Tags:**

- ...
```

Before committing, a summary can be added directly under the release heading. The following example is the summary written for that LANG 1.2.0 release:

```markdown
## Key overall changes:

- Fixed all of the internal annotations to have correct sources.
- Updated partner to the newly released standard schema 8.5.0.
```

An entry for the standard schema, or for a library's first release, is the release heading followed by the report (or, for a first release, the text of `PRERELEASE_CHANGES.md`).

`##` sections inside an entry are fine, but their headings must not contain the word "release": the script recognizes a release heading as a `##` heading containing "release" (or "Released"), which matches every release heading in the repository, old and new. The entry, summary included, is what `notes` writes for the GitHub release.

### hedId rules

- A hedId is permanent: never reuse one and never change one. `tests/test_retired_ids.py` enforces the registry.
- Each schema's id range is assigned in `library_data.json`; the tools take the range from the copy on hed-schemas `main`.
- An id removed from a released schema, or assigned in a prerelease and withdrawn before release, is recorded under `retired_ids` in `library_data.json` with the version it last appeared in.
- `hed_validate_schemas` checks every id of a candidate against the previous release, so a changed id fails validation.

### Semantic versioning

| Change type | Version increment | Examples                                                |
| ----------- | ----------------- | ------------------------------------------------------- |
| **Major**   | X.0.0             | Removed tags, changed meaning, breaking changes         |
| **Minor**   | X.Y.0             | New tags, new attributes, backward-compatible additions |
| **Patch**   | X.Y.Z             | Description improvements, typo fixes, clarifications    |

The `SchemaComparer` report labels each change Major, Minor or Patch; use those labels when choosing the version of the next prerelease.
