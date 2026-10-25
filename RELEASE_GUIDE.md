# HED schema release guide (maintainers)

The release guide has moved to [`docs/release_guide.md`](docs/release_guide.md), published at [https://www.hedtags.org/hed-schemas/release_guide.html](https://www.hedtags.org/hed-schemas/release_guide.html).

In short, on an `admin_*` branch made from hed-standard `main`:

```bash
python scripts/do_schema_release.py prepare score 2.2.0 --next 2.3.0   # or: prepare standard 8.6.0 --next 8.7.0
```

Review the staged result, commit, push and open a pull request. After it merges:

```bash
python scripts/do_schema_release.py notes score 2.2.0
```

Then create the tag and the GitHub release by hand in the GitHub web interface, pasting the release notes it prints as the description.
