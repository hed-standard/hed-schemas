# Schema developer's guide

This guide describes how to develop your own library schema or contribute to existing HED vocabularies. For complete details, see the full [**HED Schema Developer's Guide**](https://www.hedtags.org/hed-resources/HedSchemaDevelopersGuide.html).

## Quick links

- 💬 [GitHub issues](https://github.com/hed-standard/hed-schemas/issues) - Propose changes or ask questions
- 📧 [HED maintainers](mailto:hed.maintainers@gmail.com) - Technical guidance
- 📖 [HED specification](https://www.hedtags.org/hed-specification/) - Complete specification
- 🌐 [Schema browser](https://www.hedtags.org/hed-schema-browser) - Explore existing schemas
- 🔧 [HED online tools](https://hedtools.org/hed) - Validate and convert schemas

## Table of contents

1. [Getting started](#getting-started)
2. [Schema design principles](#schema-design-principles)
3. [Development workflow](#development-workflow)
4. [Branch naming conventions](#branch-naming-conventions)
5. [Developing a schema](#developing-a-schema)
6. [Local validation and testing](#local-validation-and-testing)
7. [Release process](#release-process)
8. [Common pitfalls](#common-pitfalls)

## Getting started

Before developing a schema:

1. **Explore existing schemas** using the [HED schema browser](https://www.hedtags.org/hed-schema-browser)
2. **Post an issue** describing your proposed changes or new schema
3. **Discuss with the HED Working Group** at [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
4. **Choose a schema name** (short, informative, alphabetic string)
5. **Understand the structure** by reading this guide

## Schema design principles

All HED schemas must conform to these design principles:

### 1. Organized hierarchy

- Top-level tags represent major categories
- Ideally each subtree should have no more than 7 direct children (for human readability)
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

- Each tag must be unique within the schema
- Tags MUST be distinct from standard schema tags
- Avoid overlap with other library schemas when possible

### 5. Meaningful names

- Tags should be clear without context
- Use standard terminology when available
- Follow naming conventions (see below)

### 6. Standard schema partnership

All library schemas should be partnered with the standard schema.

- Specify the `withStandard` version in the library schema header
- Use `{rooted=ParentTag}` attribute to integrate library terms under standard schema nodes
- Add top-level tags (corresponding to separate subtrees) only when required

### 7. Development format

All four HED schema formats (`.xml`, `.mediawiki`, `.tsv`, `.json`) are equivalent and any one format can be generated from another other format. However, schema developers should ONLY develop either in `.mediawiki` or `.tsv` format:

- **MediaWiki format** (`.mediawiki`) - Human-readable text format in a single file -- easiest format for visualizing the hierarchical structure
- **TSV format** (`.tsv`) - Spreadsheet-compatible format with separate files for tags, units, etc. Users usually only edit the `_Tag.tsv` file -- easiest format for including lots of attributes and links to other resources
- **XML/JSON formats** - Generated automatically by CI/CD, never edit directly

**When to use MediaWiki format**:

- Creating new schemas with simple hierarchy
- Visualizing and understanding tag relationships
- Making structural changes to the hierarchy
- When most tags have few attributes

**When to use TSV format**:

- Adding many attributes to existing tags
- Including extensive ontology mappings
- Working with spreadsheet tools for batch updates
- When collaborating with non-technical domain experts who prefer spreadsheets

### Naming conventions

- First character capitalized (if letter)
- Remaining characters lowercase (except SI units)
- Multiple words hyphenated (e.g., `Clap-hands`)
- Only alphanumeric, hyphens, and underscores allowed
- No blanks

For examples of these conventions in practice, see [MediaWiki schema structure](#mediawiki-schema-structure) and [TSV schema structure](#tsv-schema-structure). Note: All of the formats are available on GitHub.

## Proposing a new library schema

To propose a new library schema:

1. **Post an issue** on the [hed-schemas repository](https://github.com/hed-standard/hed-schemas/issues):

   - Describe the domain your schema will cover
   - Explain the need for this specialized vocabulary
   - Provide examples of terms or concepts you plan to include

2. **Discuss with the HED Working Group**:

   - Contact maintainers at [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
   - Present your use case and requirements
   - Get feedback on scope and approach

3. **Choose a schema name**:

   - Short, informative, alphabetic string (e.g., `lang`, `score`, `slam`)
   - Name should clearly indicate the domain

4. **Write schema documentation**:

   - **Prolog**: Brief description of the schema's purpose and scope (appears in schema header)
   - **Epilog**: Additional information -- often acknowledgements (appears in the schema footer)

5. **Maintainers create the schema structure**:

   - Create directory `library_schemas/<name>/`
   - Set up `prerelease/` directory with empty templates
   - Fill in schema headers with metadata:
     - Version number (start at 1.0.0)
     - Library name
     - HedId range (assigned in `library_data.json`)
     - Compatible standard schema version (`withStandard`)
     - Prologue and epilogue text
   - Create initial documentation files (`README.md`, `LICENSE`, `CONTRIBUTORS.md`)

6. **Begin development**:

   - Fork the repository and follow the development workflow below
   - Add your schema terms to the prerelease templates

## Development workflow

### Branch naming conventions

Branch names determine which schema can be modified:

| Branch prefix | Allowed modifications                               |
| ------------- | --------------------------------------------------- |
| `standard_*`  | Only `standard_schema/`: (docs, `/prerelease`)      |
| `score_*`     | Only `library_schemas/score/`: (docs, `prerelease`) |
| `lang_*`      | Only `library_schemas/lang/`: (docs, `prerelease`)  |
| `slam_*`      | Only `library_schemas/slam/`: (docs, `prerelease`)  |
| `mouse_*`     | Only `library_schemas/mouse/`: (docs, `prerelease`) |
| `admin_*`     | Any files: (docs, scripts, CI/CD)                   |

CI/CD will reject pushes that violate these conventions. These rules are in place to allow schemas to be housed in a single repository, while keeping development efforts for individual schemas separate. ONLY MAINTAINERS can do releases and move schemas from `prerelease` to the other directories.

### Development process

```{admonition} Critical workflow rules
---
class: warning
---
1. **ALL changes go to `prerelease/` subdirectory**
2. **Edit ONLY the `.mediawiki` file** OR ONLY the `.tsv` files during one PR (GitHub pull request)
3. **Let CI/CD pipeline convert to other formats**
4. **Never edit released schemas**
5. **NEVER assign or change `hedId` values. These are assigned system-wide programmatically.**
```

The actual official release of a new version of a HED schema is a multistage process.

#### Development workflow overview

```text
┌──────────────────────────────────────────────────────────┐
│  SETUP (done once)                                       │
│  1. Fork repository                                      │
│  2. Clone to local                                       │
│  3. Create branch with correct prefix                    │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│  DEVELOP PROCESS (iterate until approved)                │
│                                                          │
│  ┌────────────────────────────────────────────────────┐  │
│  │  EDIT CYCLE (repeat until valid)                   │  │
│  │  • Edit prerelease file (.mediawiki/.tsv)          │  │
│  │  • Document changes (PRERELEASE_CHANGES)           │  │
│  │  • Validate locally (HED online tools)             │  │
│  └────────────────────────┬───────────────────────────┘  │
│                           ▼                              │
│  ┌────────────────────────────────────────────────────┐  │
│  │  REVIEW CYCLE                                      │  │
│  │  • Push to fork & create pull request              │  │
│  │  • CI/CD validates automatically                   │  │
│  │  • Community review & feedback                     │  │
│  │  • Working Group feedback                          │  │
│  │                                                    │  │
│  │  If changes needed → return to EDIT CYCLE          │  │
│  └────────────────────────┬───────────────────────────┘  │
│                           ▼                              │
│  ┌────────────────────────────────────────────────────┐  │
│  │  UPDATE PRERELEASE                                 │  │
│  │  • Maintainer merges PR                            │  │
│  │  • Changes only affect prerelease/ dir             │  │
│  └────────────────────────────────────────────────────┘  │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│  RELEASE (Working Group approval required)               │
│  • Working Group approves release                        │
│  • Maintainer moves files from prerelease                │
│  • Maintainer tags version in git                        │
│  • Maintainer publishes DOI via Zen                      │
└──────────────────────────────────────────────────────────┘
```

#### Step-by-step workflow

01. **Fork the repository** on GitHub:

    - Go to [github.com/hed-standard/hed-schemas](https://github.com/hed-standard/hed-schemas)
    - Click the "Fork" button to create your own copy

02. **Clone your fork** locally:

    ```powershell
    git clone https://github.com/YOUR-USERNAME/hed-schemas.git
    cd hed-schemas
    ```

03. **Create a branch** with appropriate prefix:

    ```powershell
    git checkout -b xxx_add_new_term
    ```

    where `xxx` is `standard` or the library name depending on which schema you want to change. The `xxx` value `admin` is reserved mainly for maintainers and should not be used by individual schema developers.

04. **Edit the prerelease MediaWiki file** (alternatively the `xxx_Tag.tsv` file):

    - For standard schema: `standard_schema/prerelease/HEDX.Y.Z.mediawiki`
    - For library schema: `library_schemas/<name>/prerelease/HED_<name>_X.Y.Z.mediawiki`

05. **Document your changes** in `prerelease/PRERELEASE_CHANGES.md`:

    ```markdown
    ## Version 8.5.0

    ### Added
    - New tag `Action/Communicate/Wave-hand` for waving gestures

    ### Modified
    - Updated description of `Clap-hands` for clarity
    ```

06. **Validate and test conversion** using [HED online tools](https://hedtools.org/hed):

    - Go to [hedtools.org/hed/schemas](https://hedtools.org/hed/schemas)
    - Use the **Validate** tool to check your modified schema file for errors
    - Use the **Convert** tool to ensure your schema can be converted to other formats without errors
    - If validation or conversion errors occur, fix them in your schema file and repeat until successful
    - This step helps catch issues before creating a pull request

07. **Commit and push to your fork**:

    ```powershell
    git add .
    git commit -m "Add Wave-hand action tag"
    git push origin standard_add_new_term
    ```

08. **Create pull request** to the main repository:

    - Go to your fork on GitHub
    - Click "Pull Request" to create a PR targeting the `main` branch
    - Provide a clear description of your changes

09. **CI/CD pipeline automatically runs** on your PR:

    - Converts the format you have changed to other formats (e.g., `.mediawiki` → `.xml`, `.json`, `.tsv`)
    - Validates all schema files
    - Commits generated files back to your PR branch
    - **Note**: HED IDs are NOT assigned during prerelease development -- they are only assigned when the schema is officially released (handled by maintainers during the release process)

    **If CI/CD pipeline validation fails**:

    - Review the error messages in the GitHub Actions log
    - Common errors:
      - Schema syntax errors (missing brackets, mismatched tags)
      - Invalid attribute values
      - Undefined parent tags in TSV `omn:SubClassOf`
      - Duplicate term names
    - Fix errors in your prerelease file and push again
    - CI/CD will re-run automatically on each push

10. **Review and merge**:

- Maintainers review your changes
- Address any feedback or requested changes
- Once approved, maintainers will merge your PR (contributors cannot merge their own PRs)

11. **Check your release**:

- View your schema in the [HED schema browser](https://www.hedtags.org/hed-schema-browser) using the *View prelease schema* button on the viewer
- Check both with and without showing the partnered schema by toggling the \**Show/hide merged library* button the viewer
- If any problems, correct and repeat from Step 4

## Developing a schema

Detailed information about the various HED schema formats is available [Appendix A: Schema format details](https://www.hedtags.org/hed-specification/Appendix_A.html) of the HED specification.

### MEDIAWIKI schema structure

The MEDIAWIKI format is a single file that contains many sections needed to completely reconstruct the schema. However, schema developeres will mainly be concerned with the specification of the HED tags, whic is the portion of the file between `!# start schema` and `!# end schema`. Each tag specification must be on a single line.

````{admonition} An excerpt from HED8.4.0.mediawiki
---
class: tip
---

```text
'''Action''' <nowiki>{extensionAllowed, hedId=HED_0012016} [Do something.]</nowiki>
* Communicate <nowiki>{hedId=HED_0012017} [Action conveying knowledge of or about something.]</nowiki>
** Communicate-gesturally <nowiki>{relatedTag=Move-face, relatedTag=Move-upper-extremity, hedId=HED_0012018} [Communicate non-verbally using visible bodily actions, either in place of speech or together and in parallel with spoken words. Gestures include movement of the hands, face, or other parts of the body.]</nowiki>
*** Clap-hands <nowiki>{hedId=HED_0012019} [Strike the palms of against one another resoundingly, and usually repeatedly, especially to express approval.]</nowiki>
```
````

Key elements:

- `'''Action'''` - The triple single quotes indicate a root tag (no ancestors)
- The asterisks (`*`) indicate hierarchy level (more asterisks = deeper in the hierarchy)
- Hierarchy is determined by the number of asterisks:
  - Tags with `***` (3 asterisks) are children of the nearest preceding tag with `**` (2 asterisks)
  - Tags with `**` are children of the nearest preceding tag with `*` (1 asterisk)
  - Tags with `*` are children of the nearest preceding root tag (`'''TagName'''`)
- The `<nowiki>...</nowiki>` is MediaWiki markup that preserves the content literally -- this markup should enclose everything after the tag name
- The description appears in square brackets: `[...description...]`
- Attributes appear in `{}` if needed: `{relatedTag=Move-face}`

Modifying an entry usually involves changing the attributes or the description. Moving the line or changing the number of asterisks (`*`) changes the structure of the hierarchy and should be done with care unless this library schema has never been released.

```{admonition} Important: Tag deletion is not allowed
---
class: warning
---
**Once a schema has had its initial release, tags cannot be deleted**. Use the `deprecatedFrom` schema attribute to designate that the tag should not be used in future annotations. In this case the notes in the description should include advice about what should be used instead.
```

Adding a tag to a MEDIAWIKI file involves added an additional line in the file.

````{admonition} Adding the Beckon term to MEDIAWIKI
---
class: tip
---

```text
'''Action''' <nowiki>{extensionAllowed, hedId=HED_0012016} [Do something.]</nowiki>
* Communicate <nowiki>{hedId=HED_0012017} [Action conveying knowledge of or about something.]</nowiki>
** Communicate-gesturally <nowiki>{relatedTag=Move-face, relatedTag=Move-upper-extremity, hedId=HED_0012018} [Communicate non-verbally using visible bodily actions, either in place of speech or together and in parallel with spoken words. Gestures include movement of the hands, face, or other parts of the body.]</nowiki>
*** Beckon <nowiki>[Signal or summon someone with a gesture, typically by moving the hand or head.]</nowiki>
*** Clap-hands <nowiki>{hedId=HED_0012019} [Strike the palms of against one another resoundingly, and usually repeatedly, especially to express approval.]</nowiki>
```
````

In this example:

- `Beckon` is added at the same level as `Clap-hands` (both have leading `***`)
- `Beckon` becomes a child of `Communicate-gesturally` (the nearest previous line with fewer asterisks)
- The description is enclosed in square brackets within `<nowiki> </nowiki>` tags
- Note that `Beckon` does not have a `hedId` yet since it's in prerelease - `hedId` values are assigned only at release time
- By convention, we keep the sibling tags of a parent tag in alphabetical order, so we put `Beckon` before `Clap-hands`, although it makes no difference in the internal representation.

### TSV schema structure

Each version of a schema in TSV format is stored in its own directory, and information about the schema is stored in multiple files. The schema developer will mainly be concerned with the file ending in `_Tag.tsv`. All of the files are tabular (tab-separated-value) files, which can be easily imported into Excel and other tools.

```{admonition} An excerpt from HED8.4.0_Tag.tsv
---
class: tip
---

| hedId | Level | rdfs:label | omn:SubClassOf | Attributes | dc:description |
|-------|-------|------------|----------------|------------|----------------|
| HED_0012016 | 0 | Action | HedTag | extensionAllowed | Do something. |
| HED_0012017 | 1 | Communicate | Action | | Action conveying knowledge of or about something. |
| HED_0012018 | 2 | Communicate-gesturally | Communicate | relatedTag=Move-face, relatedTag=Move-upper-extremity | Communicate non-verbally using visible bodily actions, either in place of speech or together and in parallel with spoken words. Gestures include movement of the hands, face, or other parts of the body. |
| HED_0012019 | 3 | Clap-hands | Communicate-gesturally | | Strike the palms of against one another resoundingly, and usually repeatedly, especially to express approval. |
```

Key elements:

- **hedId**: Unique identifier for each term (empty for prerelease terms)
- **Level**: Hierarchy depth (0 = root, 1 = child of root, etc.)
- **rdfs:label**: The tag name
- **omn:SubClassOf**: The parent tag name, or `HedTag` for root-level tags (tags with no parent)
- **Attributes**: Comma-separated list of schema attributes
- **dc:description**: The tag description

Adding a tag to the TSV format involves adding a line to the `_Tag.tsv` spreadsheet.

`````{admonition} Adding the tag
---
class: tip
---

| hedId | Level | rdfs:label | omn:SubClassOf | Attributes | dc:description |
|-------|-------|------------|----------------|------------|----------------|
| HED_0012016 | 0 | Action | HedTag | extensionAllowed | Do something. |
| HED_0012017 | 1 | Communicate | Action | | Action conveying knowledge of or about something. |
| HED_0012018 | 2 | Communicate-gesturally | Communicate | relatedTag=Move-face, relatedTag=Move-upper-extremity | Communicate non-verbally using visible bodily actions, either in place of speech or together and in parallel with spoken words. Gestures include movement of the hands, face, or other parts of the body. |
| HED_0012019 | 3 | Clap-hands | Communicate-gesturally | | Strike the palms of against one another resoundingly, and usually repeatedly, especially to express approval. |
| | 3 | **Beckon** | Communicate-gesturally | | Signal or summon someone with a gesture, typically by moving the hand or head. |

In this example:
- `Beckon` is added with `Level=3` (same as `Clap-hands`)
- `omn:SubClassOf=Communicate-gesturally` specifies the parent
- `hedId` is empty (left blank) for prerelease terms - HedIds are assigned only at release time
- The row is at the end of the file (for convenience) -- the hierarchy is determined by `omn:SubClassOf
- Attributes column is empty (or contains comma-separated attributes if needed)

The TSV format is easier than MediaWiki format for adding large numbers of attributes and checking descriptions, but it is more difficult to check the hierarchy (you must trace parent-child relationships through the `omn:SubClassOf` column instead of visually seeing indentation levels).  

### Adding attributes

HED schema attributes modify tag behavior and provide additional metadata (see [Schema design principles](#schema-design-principles) for design guidance). Attributes can be:
- **Boolean**: Set by name only to indicate presence or absence (e.g., `requireChild`, `topLevelTagGroup`)
- **Value attributes**: Require a string or numeric value (e.g., `suggestedTag=Task-property`, `hedId=HED_0012808`). When multiple values of the same attribute are needed, repeat the attribute name with each value as comma-separated name-value pairs (e.g., `suggestedTag=Tag1,suggestedTag=Tag2`).



````{admonition} The Definition tag has both boolean and value attributes
---
class: tip
---

**MediaWiki format**:
```text
** Definition <nowiki>{requireChild, reserved, topLevelTagGroup, hedId=HED_0012808} [A HED-specific utility tag whose child value is the name of the concept and the tag group associated with the tag is an English language explanation of a concept.]</nowiki>
```

**TSV format**:

| hedId | Level | rdfs:label | omn:SubClassOf | Attributes | dc:description |
|-------|-------|------------|----------------|------------|----------------|
| HED_0012808 | 2 | Definition | Organizational-property | requireChild, reserved, topLevelTagGroup | A HED-specific utility tag whose child value is the name of the concept and the tag group associated with the tag is an English language explanation of a concept. |
`````

The `Definition` tag has the boolean attributes `requireChild`, `reserved`, `topLevelTagGroup` and the value attribute `hedId`

**Important notes about hedId**:

- In **MediaWiki format**: `hedId` appears in the attributes list within `{}`
- In **TSV format**: `hedId` has its own dedicated column and does NOT appear in the Attributes column
- During prerelease development, leave `hedId` empty for new tags - it is assigned automatically during official release
- Once assigned, `hedId` values become permanent identifiers and must never be changed or reused

Some attributes have special requirements. For example the `suggestedTag` and the `relatedTag` are schema value attributes whose values must be tags that are also in the schema.

````{admonition} Using multiple suggestedTag attributes
---
class: tip
---

**MediaWiki format**:
```text
'''Posterior-dominant-rhythm''' <nowiki>{suggestedTag=Feature-frequency,suggestedTag=Occipital-lobe} [Rhythmic activity occurring during wakefulness.]</nowiki>
```

**TSV format**:

| hedId | Level | rdfs:label | omn:SubClassOf | Attributes | dc:description |
|-------|-------|------------|----------------|------------|----------------|
| HED_0042046 | 1 | Posterior-dominant-rhythm | Background-activity | suggestedTag=Feature-frequency,suggestedTag=Occipital-lobe | Rhythmic activity occurring during wakefulness. |
````

Note, the `Posterior-dominant-rhythm` is a tag from the SCORE library schema as is `Feature-frequency`. The `Occipital-lobe` is a tag from the HED standard schema that this version of the SCORE library is partnered with.

All schema attributes must be defined in the `Schema attributes` section (for `.mediawiki`) or split among the `_AnnotationProperty.tsv`, `_DataProperty.tsv`, and `_ObjectProperty.tsv` files (for `.tsv`). For library schema developers, these files should usually only have headers, since these are defined in the standard schema that this schema is partnered with. The attributes are in separate `.tsv` files for easier mapping with ontologies using the OWL format. See the [HED ontology](https://www.hedtags.org/hed-specification/08_HED_ontology.html) chapter of the HED specification for more information on HED's equivalence to a formal ontology.

### External links

External annotations link schema terms to external resources like ontologies, publications, or databases using namespace prefixes. All external annotations and links are included using the `annotation` schema attribute. The information about the links is defined in three places:

1. **Sources** - Define bibliographic references that can be cited
2. **Prefixes** - Map short prefixes (e.g., `dc:`) to full namespace URIs
3. **External annotations** - Define which external properties can be used (e.g., `dc:source`)

The most common use case for external links is to cite a reference. This is done with `annotation=dc:source` followed by the citation as illustrated in the following example.

````{admonition} Including citations in schemas
---
class: tip
---

**MediaWiki format**:

```text
'''Mu-rhythm''' <nowiki>{annotation=dc:source Beniczky ea 2013 Appendix S2} [EEG rhythm at 7-11 Hz composed of arch-shaped waves.]</nowiki>
```

**TSV format**:

| hedId | Level | rdfs:label | omn:SubClassOf | Attributes | dc:description |
|-------|-------|------------|----------------|------------|----------------|
| HED_0042047 | 1 | Mu-rhythm | Background-activity | annotation=dc:source Beniczky ea 2013 Appendix S2 | EEG rhythm at 7-11 Hz composed of arch-shaped waves. |
````

The annotation `dc:source Beniczky ea 2013 Appendix S2` uses:

- `dc:` prefix (defined in `Prefixes` for MEDIAWIKI) pointing to Dublin Core
- `source` property from Dublin Core elements (defined in `External annotations` for MEDIAWIKI)
- `Beniczky ea 2013` source reference (defined in `Sources` MEDIAWIKI)
- `Appendix S2` specific location within that source

To use other external ontology terms as annotations, you must define an appropriate prefix (abbreviation of the resource) as well as an external annotation giving the IRI of the item within that resource. This allows inclusion of links to most ontology terms and external resources.

#### Sources

Sources define bibliographic references that can be cited in schema tags. Each source has a short name, URL/DOI link, and description. The short source name (e.g., `Beniczky ea 2017`) is used when citing the reference in tag annotations.

````{admonition} Defining bibliographic sources
---
class: tip
---

**MediaWiki format** (in `Sources` section):
```text
'''Sources'''
* <nowiki>source=Beniczky ea 2017,link=https://doi.org/10.1016/j.clinph.2017.07.418,description=Standardized computer based organized reporting of EEG: SCORE second version.</nowiki>
* <nowiki>source=Wikipedia,link=https://en.wikipedia.org,description=General definitions of concepts.</nowiki>
```

**TSV format** (in `_Sources.tsv` file):

| source | link | description |
|--------|------|-------------|
| Beniczky ea 2017 | https://doi.org/10.1016/j.clinph.2017.07.418 | Standardized computer based organized reporting of EEG: SCORE second version. |
| Wikipedia | https://en.wikipedia.org | General definitions of concepts. |
````

#### Prefixes

Prefixes map short abbreviations to full namespace URIs for external ontologies and vocabularies. All prefixes used in External annotations must be defined here. Common prefixes include `dc:` (Dublin Core), `ncit:` (NCI Thesaurus), `rdfs:` (RDF Schema), and `skos:` (SKOS vocabulary).

````{admonition} Defining namespace prefixes
---
class: tip
---

**MediaWiki format** (in `Prefixes` section):
```text
'''Prefixes'''
* <nowiki>prefix=dc:,namespace=http://purl.org/dc/elements/1.1/#,description=The Dublin Core elements</nowiki>
* <nowiki>prefix=ncit:,namespace=http://purl.obolibrary.org/obo/ncit.owl,description=NCI Thesaurus OBO Edition</nowiki>
```

**TSV format** (in `_Prefixes.tsv` file):

| prefix | namespace | description |
|--------|-----------|-------------|
| dc: | http://purl.org/dc/elements/1.1/# | The Dublin Core elements |
| ncit: | http://purl.obolibrary.org/obo/ncit.owl | NCI Thesaurus OBO Edition |
````

#### External annotations

External annotation properties define which ontology terms can be used as annotation keys in your schema. The most commonly used is `dc:source` for citations. The `dc:source` entry enables you to use `annotation=dc:source` in your schema tags to cite references.

````{admonition} Defining external annotation properties
---
class: tip
---

**MediaWiki format** (in `External annotations` section):
```text
'''External annotations'''
* <nowiki>prefix=dc:,id=source,iri=http://purl.org/dc/elements/1.1/source,description=A related resource from which the described resource is derived.</nowiki>
* <nowiki>prefix=dc:,id=creator,iri=http://purl.org/dc/elements/1.1/creator,description=An entity primarily responsible for making the resource.</nowiki>
```

**TSV format** (in `_AnnotationPropertyExternal.tsv` file):

| prefix | id | iri | description |
|--------|-------|-----|-------------|
| dc: | source | http://purl.org/dc/elements/1.1/source | A related resource from which the described resource is derived. |
| dc: | creator | http://purl.org/dc/elements/1.1/creator | An entity primarily responsible for making the resource. |
````

### Partnering with standard schema

Library schemas are usually partnered with a standard schema. When you specify a library schema (e.g. `score_2.2.0`), the information from that schema is automatically merged with its standard schema partner to form a single schema.A given version of a library schema is partnered with a specific version of the schema, as specified in the schema header.

#### Specifying the partner

````{admonition} The header for partnered library schema lang_1.1.0
---
class: tip
---

**MEDIAWIKI format**:
```text
!# Version="1.1.0" withStandard="8.4.0" library="lang"
```
````

**Note**: The header information for TSV is contained in the `_Structure.tsv` file and is generally setup by the HED maintainers when the directory for that library schema is created in [hed-schemas](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas).

#### Rooting a term

To root a library subtree under a standard schema node, use the `rooted` attribute:

````{admonition} Rooting Linguistic-item of lang_1.1.0 under Item
---
class: tip
---

```text
'''Linguistic-item''' <nowiki>[Language-related entity.] {rooted=Item}</nowiki>
```
````

This places the entire `Linguistic-item` subtree under the standard schema's `Item` tag in the merged schema. The `rooted` attribute is useful when your library schema tags logically belong under an existing standard schema category. Without `rooted`, library schema root tags appear at the top level of the merged schema.

**When to use `rooted`**:

- Your library terms are specializations of standard schema concepts
- You want library terms integrated into the standard hierarchy
- Users should see library terms as extensions of standard categories

**When NOT to use `rooted`**:

- Your library defines completely new top-level categories
- Your domain is orthogonal to standard schema organization

## Local validation and testing

### Install HED Python tools

```powershell
pip install hedtools
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

## Common pitfalls

### ❌ Don't do this

1. **Don't edit released schemas**

   - Only edit files in `prerelease/` directories

2. **Don't edit XML/JSON directly**

   - Always edit EITHER MEDIAWIKI OR TSV and let CI convert

3. **Don't use wrong branch prefix**

   - Branch name must match the schema you're modifying

4. **Don't reuse HedIds**

   - HedIds are permanent identifiers, never reuse or assign yourself

5. **Don't forget to document changes**

   - Update `PRERELEASE_CHANGES.md` for every change

6. **Don't violate is-a relationship**

   - Every child must be a type of its parent

7. **Don't mix properties with categories**

   - `Left-handed` is not a type of `Human`

8. **Don't create duplicate terms**

   - Check existing schemas before adding

9. **Don't skip version increment rules**

   - Understand major/minor/patch implications

### ✅ Do this instead

1. ✅ Edit in `prerelease/` subdirectories
2. ✅ Edit only `.mediawiki` files or `.tsv` files
3. ✅ Use correct branch prefix (`standard_*`, `score_*`, etc.)
4. ✅ Let CI auto-assign HedIds
5. ✅ Document all changes in `PRERELEASE_CHANGES.md`
6. ✅ Maintain strict is-a hierarchy
7. ✅ Keep properties orthogonal to categories
8. ✅ Search existing schemas thoroughly
9. ✅ Follow semantic versioning strictly

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

## Quick reference

### MediaWiki syntax

| Element          | Syntax                 | Example                                |
| ---------------- | ---------------------- | -------------------------------------- |
| Root tag         | `'''TagName'''`        | `'''Action'''`                         |
| Child tag        | `*` (1 level)          | `* Communicate`                        |
| Grandchild       | `**` (2 levels)        | `** Communicate-gesturally`            |
| Great-grandchild | `***` (3 levels)       | `*** Clap-hands`                       |
| Literal content  | `<nowiki>...</nowiki>` | `<nowiki>{hedId=HED_0012001}</nowiki>` |
| Description      | `[text]`               | `[Do something.]`                      |
| Attributes       | `{attr1, attr2=value}` | `{requireChild, hedId=HED_0012808}`    |

### TSV required columns

| Column           | Description                              | Example                 |
| ---------------- | ---------------------------------------- | ----------------------- |
| `hedId`          | Unique identifier (empty for prerelease) | `HED_0012016`           |
| `Level`          | Hierarchy depth (0=root)                 | `0`, `1`, `2`, `3`      |
| `rdfs:label`     | Tag name                                 | `Action`, `Communicate` |
| `omn:SubClassOf` | Parent tag name                          | `HedTag`, `Action`      |
| `Attributes`     | Comma-separated attributes               | `extensionAllowed`      |
| `dc:description` | Tag description                          | `Do something.`         |

### Common attributes

| Attribute          | Type    | Description                  | Example                                 |
| ------------------ | ------- | ---------------------------- | --------------------------------------- |
| `hedId`            | Value   | Permanent unique identifier  | `hedId=HED_0012016`                     |
| `suggestedTag`     | Value   | Recommended accompanying tag | `suggestedTag=Task-property`            |
| `relatedTag`       | Value   | Related tag reference        | `relatedTag=Move-face`                  |
| `annotation`       | Value   | External resource link       | `annotation=dc:source Beniczky ea 2017` |
| `rooted`           | Value   | Parent in partnered schema   | `rooted=Item`                           |
| `requireChild`     | Boolean | Must have child value        | `requireChild`                          |
| `topLevelTagGroup` | Boolean | Must be at top level         | `topLevelTagGroup`                      |
| `extensionAllowed` | Boolean | User extensions allowed      | `extensionAllowed`                      |
| `reserved`         | Boolean | Reserved for HED use         | `reserved`                              |
| `deprecatedFrom`   | Value   | Deprecated version           | `deprecatedFrom=8.3.0`                  |

### Key file locations

| Schema Component     | MediaWiki Location                   | TSV Location                                                          |
| -------------------- | ------------------------------------ | --------------------------------------------------------------------- |
| Tags                 | In main `.mediawiki` file            | `_Tag.tsv`                                                            |
| Prefixes             | `'''Prefixes'''` section             | `_Prefixes.tsv`                                                       |
| External annotations | `'''External annotations'''` section | `_AnnotationPropertyExternal.tsv`                                     |
| Sources              | `'''Sources'''` section              | `_Sources.tsv`                                                        |
| Schema attributes    | `'''Schema attributes'''` section    | `_AnnotationProperty.tsv`, `_DataProperty.tsv`, `_ObjectProperty.tsv` |

## Getting help

- **Issues**: [github.com/hed-standard/hed-schemas/issues](https://github.com/hed-standard/hed-schemas/issues)
- **Working Group**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Homepage**\*: [hedtags.org](https://www.hedtags.org)
- **Resources**: [hedtags.org/hed-resources](https://www.hedtags.org/hed-resources)
