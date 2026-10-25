# HED schema release guide (maintainers)

The release guide has moved to [`docs/release_guide.md`](docs/release_guide.md), published at [https://www.hedtags.org/hed-schemas/release_guide.html](https://www.hedtags.org/hed-schemas/release_guide.html).

In short, run `prepare` on an `admin_*` branch made from hed-standard `main`. The following examples assume that you are in the root of your local repository with its venv activated, and that you are releasing either the SCORE 2.2.0 prerelease (with 2.3.0 as the next prerelease) or the standard schema 8.6.0 prerelease (with 8.7.0 as the next prerelease).

**Prepare a library release.**

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0
```

**Prepare a standard schema release.**

```bash
python scripts/do_schema_release.py prepare standard 8.6.0 --next 8.7.0
```

Review the staged result, commit, push and open a pull request. After it merges, run `notes` with the same schema and version, for example:

```bash
python scripts/do_schema_release.py notes score 2.2.0
```

Then create the tag and the GitHub release by hand in the GitHub web interface, pasting the release notes it prints as the description and attaching the released files. Finally, a HED maintainer uploads the same files to the schema's Zenodo record by hand; Zenodo does not do this automatically.
