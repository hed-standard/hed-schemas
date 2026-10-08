# HED schema release guide (maintainers)

This guide describes how a HED maintainer releases a new version of a schema, standard or library, after prerelease development and Working Group review are complete. Contributors never do any of this; their work ends when a prerelease change is merged (see the developer guide).

## Before you start

- **Install the current tools** in a Python environment: `pip install git+https://github.com/hed-standard/hed-python.git@main`. Everything below uses the `hed_*` commands it provides.
- **Work on an `admin_*` branch** off `upstream/main` (for example `admin_release_8.5.0`). The schema-area branches (`standard_*`, `score_*`, ...) may not touch the released folders `hedxml/`, `hedwiki/`, `hedtsv/` and `hedjson/`, so a release pull request from one of them is rejected by CI.
- **Release the standard schema before any library that partners with it.** A library's merged XML embeds the standard schema that hedtools loads from its local cache, not the file in this checkout. Regenerating a library against a prerelease of the standard bakes stale standard content, without hedIds, into the library's released XML. For a library release: the partner standard version must be released and present in `schema_versions.json` on `main`, and your local cache must hold it. Delete any stale copy under `~/.hedtools/hed_cache/prerelease/` for that version first; hedtools then downloads the released file on demand.

## Release process

01. **Confirm the Working Group approval** and that the prerelease validates:

    ```bash
    hed_validate_schemas standard_schema/prerelease/HED8.5.0.mediawiki --add-all-extensions -v
    ```

02. **Assign the hedIds.** New elements in a prerelease carry no id; this step gives each one the lowest free id in the schema's range from `library_data.json` (retired ids are never reused) and rewrites all four prerelease formats:

    ```bash
    hed_add_ids . standard 8.5.0          # standard schema
    hed_add_ids . score 2.2.0             # a library
    ```

    `hed_update_schemas <prerelease .mediawiki> --set-ids` does the same from the mediawiki. The schema must be registered in `library_data.json` (a new library gets its `id_range` there, merged to `main`, before its first release). Review the diff: only `hedId` additions, all inside the schema's range.

03. **Verify the release candidate**: all four formats agree and every element has an id.

    ```bash
    hed_validate_schemas standard_schema/prerelease/HED8.5.0.mediawiki --add-all-extensions --require-ids -v
    python -m unittest discover -s tests          # retired-id registry consistency
    ```

    For a library, `--require-ids` also reports standard elements without an id in the merged form: that means the library was regenerated against a prerelease of the standard (see above).

04. **Update CHANGELOG.md** of the schema from `prerelease/PRERELEASE_CHANGES.md` (regenerate it with the hedtools `SchemaComparer` against the last release; do not hand-edit it):

    ```markdown
    ## Version 8.5.0 - 2026-10-07

    ### Added
    - New action tags for gestural communication

    ### Changed
    - Improved descriptions for clarity

    ### Fixed
    - Corrected typo in Description-of description
    ```

05. **Move all four formats** from `prerelease/` to the release directories. For the standard schema:

    ```bash
    git mv standard_schema/prerelease/HED8.5.0.mediawiki standard_schema/hedwiki/
    git mv standard_schema/prerelease/HED8.5.0.xml standard_schema/hedxml/
    git mv standard_schema/prerelease/HED8.5.0.json standard_schema/hedjson/
    git mv standard_schema/prerelease/hedtsv/HED8.5.0 standard_schema/hedtsv/
    ```

    For a library (`score` 2.2.0 here), the same four moves under `library_schemas/score/`, plus the unmerged XML copy for tools that cache compactly:

    ```python
    from hed.schema import load_schema

    load_schema("library_schemas/score/hedxml/HED_score_2.2.0.xml").save_as_xml(
        "schemas_xml_unmerged/HED_score_2.2.0.xml", save_merged=False
    )
    ```

06. **Update the Latest files**:

    ```bash
    cp standard_schema/hedxml/HED8.5.0.xml standard_schema/hedxml/HEDLatest.xml
    cp library_schemas/score/hedxml/HED_score_2.2.0.xml library_schemas/score/hedxml/HED_score_Latest.xml
    ```

07. **Regenerate the generated version files** and check them:

    ```bash
    python scripts/generate_schema_versions.py
    python scripts/update_latest_json.py --update
    python scripts/generate_schema_versions.py --check
    python scripts/update_latest_json.py --check
    ```

    `schemas_latest_json/` holds the merged JSON of the latest released version of each schema; the script generates a library's copy from its merged `hedxml/` file with hedtools. CI rejects a pull request whose manifest or Latest copies are stale.

08. **Commit, push and open the pull request** against `main`; merge when CI is green.

09. **Create the git tag** and the GitHub release with the CHANGELOG entry as its notes:

    ```bash
    git tag -a v8.5.0 -m "Release HED standard schema 8.5.0"
    git push origin v8.5.0
    ```

10. **Zenodo DOI** is minted automatically through the GitHub integration.

11. **Downstream**: hed-python bundles the released standard XML in `hed/schema/schema_data/` (and the released library XML it ships), hed-tests refreshes its schema snapshots, and the JavaScript validator picks up the new version.

## File forms

Each folder holds exactly one form of a schema. Check the moved files against this table before tagging:

| Folder                            | Form                                                     |
| --------------------------------- | -------------------------------------------------------- |
| `hedwiki/`, `hedtsv/`, `hedjson/` | unmerged (library content only)                          |
| `hedxml/`                         | merged (standard content included for a library)         |
| `schemas_xml_unmerged/`           | unmerged XML, one per released library version           |
| `schemas_latest_json/`            | merged JSON, only the latest released version per schema |

`hed_update_schemas` and `hed_add_ids` write the four prerelease files in these forms. The standard schema has no merged or unmerged distinction.

## hedId rules

- A hedId is permanent: never reuse one and never change one. `tests/test_retired_ids.py` enforces the registry.
- Each schema's id range is assigned in `library_data.json`; the tools take the range from the copy on hed-schemas `main`.
- An id removed from a released schema, or assigned in a prerelease and withdrawn before release, is recorded under `retired_ids` in `library_data.json` with the version it last appeared in.
- `hed_validate_schemas` checks every id of a candidate against the previous release, so a changed id fails validation.

## Semantic versioning rules

| Change type | Version increment | Examples                                                |
| ----------- | ----------------- | ------------------------------------------------------- |
| **Major**   | X.0.0             | Removed tags, changed meaning, breaking changes         |
| **Minor**   | X.Y.0             | New tags, new attributes, backward-compatible additions |
| **Patch**   | X.Y.Z             | Description improvements, typo fixes, clarifications    |
