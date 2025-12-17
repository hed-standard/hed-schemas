# Schema developer's guide

This guide describes how to develop your own library schema or contribute to existing HED vocabularies. For complete details, see the full [**HED Schema Developer's Guide**](https://www.hedtags.org/hed-resources/HedSchemaDevelopersGuide.html).

## Quick links

- 💬 [GitHub Issues](https://github.com/hed-standard/hed-schemas/issues) - Propose changes or ask questions
- 📧 [HED Maintainers](mailto:hed.maintainers@gmail.com) - Technical guidance
- 📖 [HED Specification](https://www.hedtags.org/hed-specification/) - Complete specification
- 🌐 [Schema Browser](https://www.hedtags.org/hed-schema-browser) - Explore existing schemas
- 🔧 [HED Online Tools](https://hedtools.org) - Validate and convert schemas

## Table of contents

1. [Getting started](#getting-started)
2. [Schema design principles](#schema-design-principles)
3. [Development workflow](#development-workflow)
4. [Branch naming conventions](#branch-naming-conventions)
5. [Making changes](#making-changes)
6. [Local validation and testing](#local-validation-and-testing)
7. [Release process](#release-process)
8. [Common pitfalls](#common-pitfalls)

## Getting started

Before developing a schema:

1. **Explore existing schemas** using the [HED Schema Browser](https://www.hedtags.org/hed-schema-browser)
2. **Post an issue** describing your proposed changes or new schema
3. **Discuss with the HED Working Group** to get guidance
4. **Choose a schema name** (short, informative, alphabetic string)
5. **Understand the structure** by reading this guide

## Schema design principles

All HED schemas must conform to these design principles:

### 1. Organized hierarchy

- Top-level nodes represent major categories
- Each subtree should have no more than 7 direct children (for human readability)
- The hierarchy should be intuitive and browsable

### 2. Is-a relationship

Every term must satisfy the **is-a** relationship with its ancestors. For example:

- `Clap-hands` is-a `Communicate-gesturally`
- `Communicate-gesturally` is-a `Communicate`
- `Communicate` is-a `Action`

This enables search generalization: searching for `Communicate` returns all descendant tags.

### 3. Orthogonal design

Independent concepts should be in different subtrees. For example:

- `Left-handed` is NOT a type of `Human`
- `Left-handed` IS a type of `Property`

Properties and categories must not be conflated.

### 4. Unique terms

- Each term must be unique within the schema
- Terms must be distinct from standard schema terms
- Avoid overlap with other library schemas when possible

### 5. Meaningful names

- Terms should be clear without context
- Use standard terminology when available
- Follow naming conventions (see below)

### Naming conventions

- First character capitalized (if letter)
- Remaining characters lowercase (except SI units)
- Multiple words hyphenated (e.g., `Clap-hands`)
- Only alphanumeric, hyphens, and underscores allowed
- No blanks

## Development workflow

### Branch naming conventions

Branch names determine which schema can be modified:

| Branch prefix | Allowed modifications            |
| ------------- | -------------------------------- |
| `standard_*`  | Only `standard_schema/`          |
| `score_*`     | Only `library_schemas/score/`    |
| `lang_*`      | Only `library_schemas/lang/`     |
| `slam_*`      | Only `library_schemas/slam/`     |
| `mouse_*`     | Only `library_schemas/mouse/`    |
| `admin_*`     | Any files (docs, scripts, CI/CD) |

CI/CD will reject pushes that violate these conventions.

### Development process

```{admonition} Critical workflow rules
---
class: warning
---
1. **ALL changes go to `prerelease/` subdirectory first**
2. **Edit ONLY the `.mediawiki` file**
3. **Let CI/CD convert to other formats**
4. **Never edit released schemas**
```

#### Step-by-step workflow

1. **Create a branch** with appropriate prefix:

   ```powershell
   git checkout -b standard_add_new_term
   ```

2. **Edit the prerelease MediaWiki file**:

   - For standard schema: `standard_schema/prerelease/HED8.5.0.mediawiki`
   - For library schema: `library_schemas/<name>/prerelease/HED_<name>_X.Y.Z.mediawiki`

3. **Document your changes** in `prerelease/PRERELEASE_CHANGES.md`:

   ```markdown
   ## Version 8.5.0

   ### Added
   - New tag `Action/Communicate/Wave-hand` for waving gestures

   ### Modified
   - Updated description of `Clap-hands` for clarity
   ```

4. **Commit and push**:

   ```powershell
   git add .
   git commit -m "Add Wave-hand action tag"
   git push origin standard_add_new_term
   ```

5. **CI/CD automatically**:

   - Converts `.mediawiki` → `.xml`, `.json`, `.tsv`
   - Validates all schema files
   - Assigns HedIds to new terms
   - Commits generated files back to your branch

6. **Create pull request** for review

7. **Merge** after approval

## Making changes

### Adding a new term

Edit the `.mediawiki` file in the appropriate location in the hierarchy:

```wiki
'''Action''' <nowiki>[Something that is done.]</nowiki>
* '''Communicate''' <nowiki>[Convey knowledge of or information about something.]</nowiki>
** '''Communicate-gesturally''' <nowiki>[Communication through body movements.]</nowiki>
*** '''Clap-hands''' <nowiki>[Strike the palms of the hands together.]</nowiki>
*** '''Wave-hand''' <nowiki>[Move the hand back and forth as a greeting.]</nowiki>
```

Key elements:

- `'''Term'''` - Bold for the tag name
- `<nowiki>[Description]</nowiki>` - Description in nowiki tags
- `*` for hierarchy level (more asterisks = deeper)
- Attributes in `{}` if needed: `{requireChild}`

### Modifying an existing term

Change the description, attributes, or position:

```wiki
*** '''Clap-hands''' <nowiki>[Strike the palms of one's hands together, typically repeatedly, especially to applaud.]</nowiki>
```

Document in `PRERELEASE_CHANGES.md` whether this is a minor or patch change.

### Adding attributes

Common attributes:

- `{requireChild}` - Must have a child tag
- `{required}` - Must appear in every event
- `{unique}` - Can only appear once
- `{rooted=ParentTag}` - Root this subtree under ParentTag in standard schema

Example:

```wiki
'''Task''' <nowiki>[Something that is to be done.] {required}</nowiki>
```

### Partnering with standard schema

In the schema header, specify the standard schema version:

```wiki
!# Version="1.2.0" withStandard="8.3.0" library="lang"
```

To root a library subtree under a standard schema node:

```wiki
'''Linguistic-item''' <nowiki>[Language-related entity.] {rooted=Item}</nowiki>
```

This places `Linguistic-item` under `Item` in the merged schema.

## Local validation and testing

### Install HED Python tools

```powershell
pip install git+https://github.com/hed-standard/hed-python.git@main
```

### Validate a schema

```powershell
hed_validate_schemas standard_schema/prerelease/HED8.5.0.mediawiki
```

### Convert between formats

```powershell
# Auto-generates .xml, .json, .tsv from .mediawiki
hed_update_schemas standard_schema/prerelease/HED8.5.0.mediawiki
```

### Clear cached schemas

```powershell
hed_cache_schemas --clear
```

## Release process

When ready to release a new version:

1. **Update version number** in schema header:

   ```wiki
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

### Semantic versioning rules

| Change type | Version increment | Examples                                                |
| ----------- | ----------------- | ------------------------------------------------------- |
| **Major**   | X.0.0             | Removed tags, changed meaning, breaking changes         |
| **Minor**   | X.Y.0             | New tags, new attributes, backward-compatible additions |
| **Patch**   | X.Y.Z             | Description improvements, typo fixes, clarifications    |

## Common pitfalls

### ❌ Don't do this

01. **Don't edit released schemas**

    - Only edit files in `prerelease/` directories

02. **Don't edit XML/JSON/TSV directly**

    - Always edit `.mediawiki` and let CI convert

03. **Don't use wrong branch prefix**

    - Branch name must match the schema you're modifying

04. **Don't reuse HedIds**

    - HedIds are permanent identifiers, never reuse

05. **Don't forget to document changes**

    - Update `PRERELEASE_CHANGES.md` for every change

06. **Don't use `&&` in PowerShell**

    - This is Windows/PowerShell: use `;` instead

07. **Don't violate is-a relationship**

    - Every child must be a type of its parent

08. **Don't mix properties with categories**

    - `Left-handed` is not a type of `Human`

09. **Don't create duplicate terms**

    - Check existing schemas before adding

10. **Don't skip version increment rules**

    - Understand major/minor/patch implications

### ✅ Do this instead

01. ✅ Edit in `prerelease/` subdirectories
02. ✅ Edit only `.mediawiki` files
03. ✅ Use correct branch prefix (`standard_*`, `score_*`, etc.)
04. ✅ Let CI auto-assign HedIds
05. ✅ Document all changes in `PRERELEASE_CHANGES.md`
06. ✅ Use `;` for command chaining in PowerShell
07. ✅ Maintain strict is-a hierarchy
08. ✅ Keep properties orthogonal to categories
09. ✅ Search existing schemas thoroughly
10. ✅ Follow semantic versioning strictly

## CI/CD pipeline

GitHub Actions automatically:

| Workflow                          | Purpose                                                |
| --------------------------------- | ------------------------------------------------------ |
| `validate_schemas.yaml`           | Validates all changed schema files                     |
| `update_and_convert_schemas.yaml` | Converts MediaWiki to other formats                    |
| `add_hed_ids.yaml`                | Assigns HedIds to new terms                            |
| `verify_source_branch.yaml`       | Ensures changes on correct branch and in `prerelease/` |
| `codespell.yaml`                  | Spell checking                                         |
| `mdformat.yaml`                   | Markdown formatting                                    |
| `links.yaml`                      | Check for broken links                                 |

## Getting help

- **Issues**: [github.com/hed-standard/hed-schemas/issues](https://github.com/hed-standard/hed-schemas/issues)
- **Working Group**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Documentation**: [hedtags.org](https://www.hedtags.org)
- **Resources**: [hedtags.org/hed-resources](https://www.hedtags.org/hed-resources)
- **Full Developer Guide**: [hedtags.org/hed-resources/HedSchemaDevelopersGuide.html](https://www.hedtags.org/hed-resources/HedSchemaDevelopersGuide.html)
