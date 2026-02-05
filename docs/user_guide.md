```{index} user guide; HED usage; schema viewing; annotation
```

```{meta}
---
description: User guide for viewing, using, and understanding HED schemas for 
  data annotation
keywords: HED user guide, schema browser, annotation, HED tools, data tagging
---
```

# User guide

This guide provides information for users who want to view, use, or understand HED schemas for annotating their data.

## Table of contents

1. [Viewing HED schemas](#viewing-hed-schemas)
2. [Using HED schemas](#using-hed-schemas)
3. [Schema versions](#schema-versions)
4. [Using schemas in your data](#using-schemas-in-your-data)
5. [Contributing to schemas](#contributing-to-schemas)
6. [Getting help](#getting-help)

## Viewing HED schemas

### HED schema browser

The easiest way to explore HED schemas is through the [HED schema browser](https://www.hedtags.org/hed-schema-browser):

1. Select a schema (standard or library) from the dropdown
2. Choose a version
3. Navigate the hierarchical tree structure
4. Click on any tag to see its description, attributes, and position in the hierarchy

### GitHub repository

All schemas are available in the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository:

- **Standard schema**: `standard_schema/` directory
- **Library schemas**: `library_schemas/<name>/` directories

Each schema is available in four formats within each directory:

- `hedwiki/` - MEDIAWIKI format (human-readable)
- `hedxml/` - XML format (used by tools)
- `hedjson/` - JSON format (for AI and lookups)
- `hedtsv/` - TSV format (spreadsheet-compatible)

## Using HED schemas

### Annotation basics

HED annotations consist of comma-separated lists of HED tags from the schema vocabulary. Tags can be grouped using parentheses:

```
Red, Triangle, Blue, Square              # Ambiguous - which color goes with which shape?
(Red, Triangle), (Blue, Square)          # Clear - red triangle and blue square
```

### Tag forms

Use short form when annotation rather than a full path:

- **Short form**: `Square`
- **Long form**: `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

HED tools can convert between forms as needed. The hierarchy enables search generalization: searching for `2D-shape` will find annotations containing `Square`, `Rectangle`, or any other descendant.

### Value tags and placeholders

Some tags can take values and units:

```
Age/35                                    # Specific age value
(Duration/500 ms)                          # With units
Label/stimulus-image                      # Text label
```

Only tags that have a `#` placeholder child are permitted to have values and units. Note the parentheses around the `Duration` tag. The `Duration` tag has the `topLevelTagGroup` attribute, meaning that it must appear in unnested parentheses in any annotation. The `Duration` tag is expected to be grouped with other tags that describe what it is the duration of.

In BIDS sidecars, you can use placeholders:

```json
{
  "response_time": {
    "HED": "(Label/Response-time, Time-value/# s)"
  }
}
```

This format designates that the `response_time` column will be described by a single HED annotation.The `#` will be replaced with the actual column value for each row during annotation assembly.

## Schema versions

### Semantic versioning

HED schemas follow semantic versioning (major.minor.patch):

- **Major**: Breaking changes (removed terms, changed meaning)
- **Minor**: Backward-compatible additions (new terms, new attributes)
- **Patch**: Non-functional changes (description improvements, typos)

### Current versions

| Schema   | Latest Release | Prerelease | DOI                                                                |
| -------- | -------------- | ---------- | ------------------------------------------------------------------ |
| Standard | 8.4.0          | 8.5.0      | [10.5281/zenodo.7876037](https://doi.org/10.5281/zenodo.7876037)   |
| SCORE    | 2.1.0          | 2.2.0      | [10.5281/zenodo.7897596](https://doi.org/10.5281/zenodo.7897596)   |
| LANG     | 1.1.0          | 1.2.0      | [10.5281/zenodo.13987483](https://doi.org/10.5281/zenodo.13987483) |
| SLAM     | -              | 1.0.0      | -                                                                  |
| MOUSE    | -              | 1.0.0      | -                                                                  |

______________________________________________________________________

## Using schemas in your data

HED requires that you specify a HED version for most operations.

### BIDS datasets

In BIDS, the `dataset_description.json` located at the top level of the directory containing a dataset has the version.

````{admonition} BIDS dataset using the standard schema
---
class: tip
---
```json
{
  "Name": "My Dataset",
  "BIDSVersion": "1.9.0",
  "HEDVersion": "8.4.0"
}
```
````

````{admonition} BIDS dataset using two non-conflicting library schemas
---
class: tip
---
```json
{
  "Name": "My Dataset",
  "BIDSVersion": "1.9.0",
  "HEDVersion": ["score_2.1.0", "lang_1.1.0"]
}
```
````

In this example the specified SCORE and LANG versions do not conflict and partner with the same HED standard schema (8.4.0), so they can be used together without namespace prefixes.

### HED in NWB

HED is supported in NWB in a similar fashion. The HED version must be specified in `HedLabMetaData` element in a `NWBFile` before usage. See [ndx-hed](https://www.hedtags.org/ndx-hed) for more information.

### Validating your annotations

For most schema development work, you should use the [HED online tools](https://hedtools.org/hed). These tools require no installation and provide quick feedback. If you want to do validation programmatically, consult the individual tool guides:

- [Python HEDTools](https://www.hedtags.org/hed-python)
- [MATLAB HEDTools](https://www.hedtags.org/hed-matlab)
- [JavaScript HEDTools](https://www.hedtags.org/hed-javascript)

### Common validation errors

1. **Unknown tag**: Tag not found in schema

   - Solution: Check spelling, check schema version

2. **Duplicate tag**: The same tag or tag group appears multiple times in an annotation.

   - Solution: Remove duplicates. This can be tricky to spot in complex annotations, particular in event files in which multiple rows have the same time `onset` value and the duplication is not evident until the rows are combined.

3. **Invalid unit**: Unit not compatible with tag's unit class

   - Solution: Use correct unit (e.g., `ms`, `s` for time). For tags that don't have `#` children, you can't use units at all.

## Contributing to schemas

### Suggesting new terms or changes

1. Check if the term already exists in the [HED schema browser](https://www.hedtags.org/hed-schema-browser)
2. Post an [issue](https://github.com/hed-standard/hed-schemas/issues) describing:
   - The term you want to add/modify
   - Why it's needed
   - Where it should fit in the hierarchy
   - Examples of how it would be used
3. The HED Working Group will discuss and provide feedback
4. Approved changes will be added to the next schema version

### Proposing a new library schema

If you have a specialized domain that needs extensive vocabulary:

1. Review the [Schema developer's guide](./developer_guide.md)
2. Post an issue proposing the new library
3. Describe the domain, scope, and approximate vocabulary size
4. The HED Working Group will provide guidance on:
   - HedId range assignment
   - Schema structure and design
   - Development process
   - Partnership with standard schema

## Getting help

- **Questions about using schemas**: Post on [GitHub issues](https://github.com/hed-standard/hed-schemas/issues)
- **Questions about annotation**: See [HED resources](https://www.hedtags.org/hed-resources) tutorials
- **Technical questions**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Schema development**: See the [Schema developer's guide](developer_guide.md)
