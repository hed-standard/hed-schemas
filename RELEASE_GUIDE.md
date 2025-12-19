# HED Schema Release Guide (Maintainers)

This guide describes the process for releasing a new version of a HED schema. This process is performed by HED maintainers after all prerelease development and review is complete.

## Release process

When ready to release a new version:

1. **Update version number** in schema header:

   ```text
   !# Version="8.5.0"
   ```

2. **Update CHANGELOG.md** with comprehensive documentation:

   ```markdown
   ## Version 8.5.0 - 2024-12-16

   ### Added
   - New action tags for gestural communication

   ### Changed
   - Improved descriptions for clarity

   ### Fixed
   - Corrected typo in Description-of description
   ```

3. **Move files** from `prerelease/` to release directories:

   ```powershell
   # Move MediaWiki
   mv standard_schema/prerelease/HED8.5.0.mediawiki standard_schema/hedwiki/

   # Move other formats
   mv standard_schema/prerelease/HED8.5.0.xml standard_schema/hedxml/
   mv standard_schema/prerelease/HED8.5.0.json standard_schema/hedjson/
   # etc.
   ```

4. **Update Latest links**:

   ```powershell
   # Create/update symlink or copy
   cp standard_schema/hedxml/HED8.5.0.xml standard_schema/hedxml/HEDLatest.xml
   ```

5. **Create git tag**:

   ```powershell
   git tag -a v8.5.0 -m "Release HED standard schema 8.5.0"
   git push origin v8.5.0
   ```

6. **Create GitHub release** with release notes

7. **Update DOI** on Zenodo (automatic through GitHub integration)

## Semantic versioning rules

| Change type | Version increment | Examples                                                |
| ----------- | ----------------- | ------------------------------------------------------- |
| **Major**   | X.0.0             | Removed tags, changed meaning, breaking changes         |
| **Minor**   | X.Y.0             | New tags, new attributes, backward-compatible additions |
| **Patch**   | X.Y.Z             | Description improvements, typo fixes, clarifications    |
