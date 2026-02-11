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

HED (Hierarchical Event Descriptors) allow researchers to annotate what happened during an experiment including:

- Experimental stimuli and other sensory events
- Participant responses and actions
- Experimental design
- The role of events in the task
- The temporal structure of the experiment
- Participant metadata
- Environmental setup

This guide provides information for users who want to view, use, or understand HED schemas for annotating their data.

## Table of contents

01. [What is a HED schema?](#what-is-a-hed-schema)
02. [Available schemas](#available-schemas)
03. [Schema formats](#schema-formats)
04. [Viewing HED schemas](#viewing-hed-schemas)
05. [Using HED schemas](#using-hed-schemas)
06. [Schema versions](#schema-versions)
07. [Using schemas in your data](#using-schemas-in-your-data)
08. [Related tools and resources](#related-tools-and-resources)
09. [Repository structure](#repository-structure)
10. [Contributing to schemas](#contributing-to-schemas)
11. [Getting help](#getting-help)

## What is a HED schema?

A **HED schema** is a hierarchically-structured specification of a vocabulary. The **standard schema** contains the basic vocabulary and organizational tags needed for annotation of experimental data. Additional **library schemas** contain specialized field-specific vocabularies for domain-specific annotations. The HED schemas form the core of the HED ecosystem, which includes:

- **Controlled vocabularies** specified by HED schemas for annotating experimental data
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)
- **Tools** for validation and using HED annotations in data search, extraction, and analysis

### Schema hierarchical structure

HED schemas are structured as a set of trees, each corresponding to a major term category for the vocabulary. Each child tag in a HED schema is considered to be a special type of its ancestors, following an **is-a** relationship.

For example, the tag `Square` has a full schema path:

> `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

This means `Square` is-a type of `Rectangle`, which is-a type of `2D-shape`, etc. This strict hierarchy enables powerful search generalization: when downstream tools search for `2D-shape`, the search will return tag strings containing `Square`, `Rectangle`, and `2D-shape`.

Although you can express a tag by any partial path in the hierarchy, when possible you SHOULD ONLY USE JUST the tag node name (e.g., `Square`) rather than the full path or a partial path when annotating data. There is no ambiguity, because tag names in a schema must be unique. HED-compliant tools can convert between this **"short-form"** and the complete path or **"long-form"** when needed for search, summarization, or other processing. Short form makes annotations simpler. In addition, a node sometimes changes position when a new version is released if additional intermediate nodes are added.

## Available schemas

### Standard schema

- **Current Version**: 8.4.0 (prerelease: 8.5.0)
- **HedId Range**: 10000-39999
- **DOI**: [10.5281/zenodo.7876037](https://doi.org/10.5281/zenodo.7876037)
- Contains fundamental terms for describing events, properties, agents, actions, and experimental structures

### Library schemas

1. **SCORE** (HedId: 40000-59999)

   - Clinical neurological annotation vocabulary
   - Based on SCORE standard for EEG/clinical event description
   - Current: 2.1.0, Prerelease: 2.2.0
   - DOI: [10.5281/zenodo.7897596](https://doi.org/10.5281/zenodo.7897596)

2. **LANG** (HedId: 60000-79999)

   - Linguistic stimuli annotation vocabulary
   - Current: 1.1.0, Prerelease: 1.2.0
   - DOI: [10.5281/zenodo.13987483](https://doi.org/10.5281/zenodo.13987483)

3. **SLAM** (HedId: 80000-99999)

   - Sensor Location and Motion vocabulary
   - Prerelease: 1.0.0

4. **MOUSE** (HedId: 100000-119999)

   - Mouse/rodent experiment vocabulary
   - Prerelease: 1.0.0

5. **TESTLIB** (HedId: auto-assigned)

   - Testing vocabulary (not stable)
   - For development/testing purposes only

## Schema formats

Each schema is stored in **four equivalent formats**:

1. **MEDIAWIKI** (`.mediawiki`) - in `hedwiki/` directory

   - Human-readable text format
   - Primary editing format for schema developers
   - Easy to review in GitHub and text editors

2. **XML** (`.xml`) - in `hedxml/` directory

   - Format used by all HED tools for validation and analysis
   - Includes XSD schema definition files
   - Never edited directly - generated from MEDIAWIKI or TSV

3. **JSON** (`.json`) - in `hedjson/` directory

   - Flat dictionary structure for easy lookups
   - Optimized for AI tools and programmatic access
   - Never edited directly - generated from other formats

4. **Tabular TSV** (`.tsv`) - in `hedtsv/` directory

   - Spreadsheet-compatible format - good for adding attributes
   - Each schema entity type (tags, units, etc.) in separate TSV files
   - May contain additional ontology mapping information

**CRITICAL**: All four formats contain the same semantic information. Conversion between formats is lossless.

## Viewing HED schemas

### HED schema browser

The easiest way to explore HED schemas is through the [HED schema browser](https://www.hedtags.org/hed-schema-browser):

1. Select a schema (standard or library) from the dropdown
2. Choose a version
3. Navigate the hierarchical tree structure
4. Click on any tag to see its description, attributes, and position in the hierarchy

The browser allows you to explore the hierarchical structure described in the [Schema hierarchical structure](#schema-hierarchical-structure) section above.

### GitHub repository

All schemas are available in the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository:

- **Standard schema**: `standard_schema/` directory
- **Library schemas**: `library_schemas/<name>/` directories

Each schema is available in the four formats described in the [Schema formats](#schema-formats) section above.

## Using HED schemas

### Annotation basics

HED annotations consist of comma-separated lists of HED tags from the schema vocabulary. Tags can be grouped using parentheses:

```
Red, Triangle, Blue, Square              # Ambiguous - which color goes with which shape?
(Red, Triangle), (Blue, Square)          # Clear - red triangle and blue square
```

### Tag forms

As described in the [Schema hierarchical structure](#schema-hierarchical-structure) section, you should use short form when annotating rather than a full path:

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

## Related tools and resources

### Online tools and documentation

- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED resources](https://www.hedtags.org/hed-resources)**: Comprehensive tutorials and documentation
- **[HED schema browser](https://www.hedtags.org/hed-schema-browser)**: Interactive schema exploration
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification defining HED annotation rules
- **[HED online tools](https://hedtools.org)**: Web-based schema validation, conversion, and annotation tools
- **[HED examples](https://github.com/hed-standard/hed-examples)**: Example datasets annotated with HED

### Programming libraries

- **[Python HEDTools](https://github.com/hed-standard/hed-python)**: Python tools for HED validation, analysis, and transformation (`hedtools` package)
- **[MATLAB HEDTools](https://github.com/hed-standard/hed-matlab)**: MATLAB tools for HED processing
- **[JavaScript HEDTools](https://github.com/hed-standard/hed-javascript)**: JavaScript validation tools (BIDS validator)

### Web-based tools

For users who prefer not to program, HED provides online tools and RESTful services:

- **[hedtools.org/hed](https://hedtools.org/hed)** - Production version
- **[hedtools.org/hed_dev](https://hedtools.org/hed_dev)** - Development version

These tools support:

- Schema validation and conversion
- Event file validation
- Sidecar validation
- HED string validation

### Programmatic access

Schemas can be accessed programmatically through:

- **Python**: [Python HEDTools](https://github.com/hed-standard/hed-python)
- **MATLAB**: [MATLAB HEDTools](https://github.com/hed-standard/hed-matlab)
- **JavaScript**: [JavaScript HEDTools](https://github.com/hed-standard/hed-javascript)

## Repository structure

This repository is organized as follows:

| Directory             | Description                                            |
| --------------------- | ------------------------------------------------------ |
| `standard_schema/`    | Base HED vocabulary for all domains                    |
| `library_schemas/`    | Specialized vocabularies for specific domains          |
| `schemas_latest_json` | Easy access for AIs                                    |
| `scripts/`            | Utility scripts for schema validation and verification |
| `docs/`               | Documentation source files                             |
| `.github/workflows/`  | CI/CD pipelines for validation and conversion          |

Each schema directory contains:

- `hedxml/` - XML format schemas
- `hedwiki/` - MediaWiki format schemas
- `hedjson/` - JSON format schemas
- `hedtsv/` - Tabular TSV format schemas
- `prerelease/` - Working versions under development
- `README.md` - Schema-specific documentation
- `CHANGELOG.md` - Version history
- `CONTRIBUTORS.md` - List of contributors

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

### Documentation resources

- **[User guide](user_guide.md)**: This guide for using and accessing schemas
- **[Developer guide](developer_guide.md)**: Guide for contributing to schemas
- **[Schemas reference](schemas_reference.md)**: Detailed schema information
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification
- **[HED resources](https://www.hedtags.org/hed-resources)**: Tutorials and guides

### Support

- **Issues**: Report bugs, ask questions, or request features on [GitHub issues](https://github.com/hed-standard/hed-schemas/issues)
- **Questions about annotation**: See [HED resources](https://www.hedtags.org/hed-resources) tutorials
- **Technical questions**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Schema development**: See the [Schema developer's guide](developer_guide.md)
