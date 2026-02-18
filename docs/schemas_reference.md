---
description: Complete reference for HED schemas including how to view, use, and 
  access HED schemas for data annotation
keywords: HED schemas, standard schema, library schemas, score, lang, slam, 
  mouse, schema versions, HED annotation, schema browser
---

```{index} schema reference; standard schema; library schemas; versions; formats; HED usage
```

# HED schemas reference

This guide provides comprehensive information about HED (Hierarchical Event Descriptors) schemas, including how to view, use, and access them for annotating your data. As you read this reference, it may be helpful to view the available HED schemas using the [HED schema browser](https://www.hed-tags.org/hed-schema-browser).

## What is a HED schema?

A **HED schema** is a hierarchically-structured specification of a vocabulary for annotating experimental data. HED allows researchers to describe what happened during an experiment including:

- Experimental stimuli and other sensory events
- Participant responses and actions
- Experimental design and task structure
- The role of events in the task
- The temporal structure of the experiment
- Participant metadata
- Environmental setup

The **standard schema** contains the basic vocabulary and organizational tags needed for annotation across all domains. Additional **library schemas** contain specialized field-specific vocabularies for domain-specific annotations. The HED schemas form the core of the HED ecosystem, which includes:

- **Controlled vocabularies** specified by HED schemas for annotating experimental data
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)
- **Tools** for validation and using HED annotations in data search, extraction, and analysis

## Understanding schema structure

### Hierarchical organization

HED schemas are structured as a set of trees, each corresponding to a major term category for the vocabulary. Each child tag in a HED schema is considered to be a special type of its ancestors, following an **is-a** relationship.

For example, the tag `Square` has a full schema path:

> `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

This means `Square` is-a type of `Rectangle`, which is-a type of `2D-shape`, etc. This strict hierarchy enables powerful search generalization: when downstream tools search for `2D-shape`, the search will return tag strings containing `Square`, `Rectangle`, and `2D-shape`.

### Tag forms: Short vs. long

Although you can express a tag by any partial path in the hierarchy, when possible you SHOULD ONLY USE JUST the tag node name (e.g., `Square`) rather than the full path or a partial path when annotating data:

- **Short form** (recommended): `Square`
- **Long form**: `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

There is no ambiguity, because tag names in a schema must be unique. HED-compliant tools can convert between this **"short-form"** and the complete path or **"long-form"** when needed for search, summarization, or other processing. Short form makes annotations simpler. In addition, a node sometimes changes position when a new schema version is released if additional intermediate nodes are added.

## Available schemas

HED provides a standard schema and multiple specialized library schemas for specific research domains.

### Standard schema

The HED standard schema contains the basic vocabulary for annotating experiments across all domains. The standard schema DOI is [10.5281/zenodo.7876037](https://doi.org/10.5281/zenodo.7876037) and has HED IDs in the range HED_10000-HED_39999.


| Version  | Status     | Release date | XML | MEDIAWIKI | JSON  | TSV |
| -------- | ---------- | ------------ | --- | --------- | ----- | --- | 
| 8.4.0    | Latest     | June 1, 2024 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.4.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedwiki/HED8.4.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedjson/HED8.4.0.json) | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedtsv/HED8.4.0) |
| 8.5.0    | Prerelease |    | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.json) | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/prerelease/hedtsv) | 

The standard schema is organized into th following top-level hierarchies:

- **Events**: Sensory presentations, experimental events, data features
- **Agents**: Humans, animals, avatars performing actions
- **Actions**: Movements, communications, cognitive processes
- **Items**: Objects, geometric entities, biological items, language items
- **Properties**: Characteristics describing agents, actions, and items
- **Relations**: Spatial and logical relationships

**Latest version (stable link) for tools:** [HEDLatest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

#### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/CHANGELOG.md)

#### References

> Makeig, S. and K. Robbins (2024).\
> Events in context—The HED framework for the study of brain, experience and behavior.\
> Front. Neuroinform. Vol. 18. [https://doi.org/10.3389/fninf.2024.1292667](https://doi.org/10.3389/fninf.2024.1292667)

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2021).\
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).\
> Neuroinformatics. [https://doi.org/10.1007/s12021-021-09537-4](https://doi.org/10.1007/s12021-021-09537-4)

______________________________________________________________________

### SCORE library schema

HED-SCORE implements the Standardized Computer-based Organized Reporting of EEG (SCORE) standard for clinical neurological annotation.

#### Overview

| Property               | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| **Current Version**    | 2.1.0                                                            |
| **Prerelease Version** | 2.2.0                                                            |
| **HedId Range**        | 40000-59999                                                      |
| **DOI**                | [10.5281/zenodo.7897596](https://doi.org/10.5281/zenodo.7897596) |
| **Partnered With**     | Standard 8.3.0                                                   |

#### Description

The SCORE library allows neurologists, neurophysiologists, and brain researchers to annotate electrophysiology recordings using terms from an internationally accepted set of defined terms compatible with the HED framework. The vocabulary covers:

- **Finding**: EEG phenomena and patterns observed in recordings
- **Sleep-related**: Sleep stages and sleep-specific phenomena
- **Modulators**: Factors affecting EEG patterns (eye state, vigilance, medication)
- **Background-activity**: Characteristics of ongoing EEG
- **Episode**: Specific event types (seizures, epileptic episodes)

### Access Links

| Format        | Current Release (2.1.0)                                                                                                                                                                                                                                 | Prerelease (2.2.0)                                                                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_2.1.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/hedxml/HED_score_2.1.0.xml)               | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/prerelease/HED_score_2.2.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedwiki/HED_score_2.1.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/hedwiki/HED_score_2.1.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/prerelease/HED_score_2.2.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedjson/HED_score_2.1.0.json)                                                                                                                               | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.json)                                                                                                                                  |
| **TSV**       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/hedtsv/HED_score_2.1.0)                                                                                                                                         | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/prerelease/hedtsv)                                                                                                                                                    |

**Latest version (stable link):** [HED_score_Latest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_Latest.xml)

#### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/CHANGELOG.md)
- [View in Schema Browser](https://www.hedtags.org/hed-schema-browser)
- [SCORE Documentation](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/README.md)

#### References

> Hermes, D., Pal Attia, T., Beniczky, S. et al.\
> Hierarchical Event Descriptor library schema for EEG data annotation.\
> Sci Data 12, 1448 (2025). [https://doi.org/10.1038/s41597-025-05791-2](https://doi.org/10.1038/s41597-025-05791-2)

> Beniczky, S, et al. (2013). Standardized computer based organized reporting of EEG: SCORE.\
> Epilepsia 54.6 (2013).

> Beniczky, S., et al. (2017). Standardized computer based organized reporting of EEG: SCORE second version.\
> Clinical Neurophysiology 128.11 (2017).

______________________________________________________________________

### LANG library schema

The HED Language library schema (HED LANG) contains vocabulary for annotating language experiments in cognitive science.

#### Overview

| Property               | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| **Current Version**    | 1.1.0                                                              |
| **Prerelease Version** | 1.2.0                                                              |
| **HedId Range**        | 60000-79999                                                        |
| **DOI**                | [10.5281/zenodo.13987483](https://doi.org/10.5281/zenodo.13987483) |
| **Partnered With**     | Standard 8.3.0                                                     |

#### Description

HED LANG allows for detailed annotation of language stimuli at multiple levels through orthogonal definition of:

- **Language-item**: Full sentences, words, morphemes, phonemes
- **Language-item-property**: Linguistic characteristics applicable across languages
  - Morphosyntactic properties (word class, case, tense, etc.)
  - Semantic properties (concreteness, animacy, etc.)
  - Orthographic properties (capitalization, script)
  - Phonological properties (stress, syllable structure)

The schema supports both carefully controlled experiments addressing specific psycholinguistic questions and complex naturalistic paradigms.

#### Access links

| Format        | Current Release (1.1.0)                                                                                                                                                                                                                             | Prerelease (1.2.0)                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_1.1.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/hedxml/HED_lang_1.1.0.xml)               | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/prerelease/HED_lang_1.2.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedwiki/HED_lang_1.1.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/hedwiki/HED_lang_1.1.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/prerelease/HED_lang_1.2.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedjson/HED_lang_1.1.0.json)                                                                                                                             | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.json)                                                                                                                                |
| **TSV**       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/hedtsv/HED_lang_1.1.0)                                                                                                                                       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/prerelease/hedtsv)                                                                                                                                                 |

**Latest version (stable link):** [HED_lang_Latest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_Latest.xml)

#### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/CHANGELOG.md)
- [View in Schema Browser](https://www.hedtags.org/hed-schema-browser)

#### Example datasets

Annotated datasets using HED LANG are available:

- [ds001894](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds001894)
- [ds002155](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002155)
- [ds002382](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002382)
- [ds003126](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds003126)

#### References

> Denissen, M., Pöll, B., Robbins, K., Makeig, S. & Hutzler, F.\
> HED LANG – A Hierarchical Event Descriptors library extension for annotation of language cognition experiments.\
> Sci Data 11, 1428 (2024). [https://doi.org/10.1038/s41597-024-04282-0](https://doi.org/10.1038/s41597-024-04282-0)

______________________________________________________________________

### SLAM library schema

The HED SLAM library schema provides vocabulary for Sensor Location and Motion annotation.

#### Overview

| Property               | Value               |
| ---------------------- | ------------------- |
| **Current Version**    | - (prerelease only) |
| **Prerelease Version** | 1.0.0               |
| **HedId Range**        | 80000-99999         |
| **DOI**                | Not yet assigned    |
| **Partnered With**     | Standard 8.3.0      |

#### Description

HED SLAM is currently in prerelease development. This library will provide vocabulary for describing:

- Sensor locations and positioning
- Motion tracking and recording
- Spatial relationships
- Movement characteristics

#### Access links

| Format        | Prerelease (1.0.0)                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/prerelease/HED_slam_1.0.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/prerelease/HED_slam_1.0.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.json)                                                                                                                                |

#### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/README.md)

______________________________________________________________________

### MOUSE library schema

The HED MOUSE library schema provides vocabulary for mouse/rodent experiment annotation.

#### Overview

| Property               | Value               |
| ---------------------- | ------------------- |
| **Current Version**    | - (prerelease only) |
| **Prerelease Version** | 1.0.0               |
| **HedId Range**        | 100000-119999       |
| **DOI**                | Not yet assigned    |
| **Partnered With**     | Standard 8.3.0      |

#### Description

HED MOUSE is currently in prerelease development. This library will provide vocabulary specific to mouse and rodent experiments, including:

- Rodent-specific behaviors
- Experimental paradigms for animal studies
- Sensory stimuli relevant to rodent research
- Recording techniques specific to animal models

#### Access links

| Format        | Prerelease (1.0.0)                                                                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.json)                                                                                                                                  |

#### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/README.md)

______________________________________________________________________

### TESTLIB library schema

The TESTLIB schema is a copy of the standard schema used for testing purposes only.

#### Overview

| Property     | Value                   |
| ------------ | ----------------------- |
| **Purpose**  | Testing and development |
| **Status**   | May not be stable       |
| **Use Case** | Internal testing only   |

⚠️ **Warning**: This schema is for testing purposes only and should not be used for actual data annotation.

______________________________________________________________________

## Schema formats

Each schema is stored in **four equivalent formats**. All formats contain the same semantic information and conversion between formats is lossless.

### Format comparison

| Format        | Extension    | Location   | Use Case                              | Editing                         |
| ------------- | ------------ | ---------- | ------------------------------------- | ------------------------------- |
| **XML**       | `.xml`       | `hedxml/`  | Tool validation and analysis          | ❌ Never edit directly          |
| **MEDIAWIKI** | `.mediawiki` | `hedwiki/` | Human-readable, schema development    | ✅ Primary editing format       |
| **JSON**      | `.json`      | `hedjson/` | AI tools, easy lookup                 | ❌ Generated from XML/MEDIAWIKI |
| **TSV**       | `.tsv`       | `hedtsv/`  | Spreadsheet editing, ontology mapping | ✅ Good for adding attributes   |

### Format details

1. **MEDIAWIKI** (`.mediawiki`) - in `hedwiki/` directory

   - Human-readable text format in a single file
   - Primary editing format for schema developers
   - Easy to review in GitHub and text editors
   - Easiest format for visualizing the hierarchical structure

2. **XML** (`.xml`) - in `hedxml/` directory

   - Format used by all HED tools for validation and analysis
   - Includes XSD schema definition files
   - Never edited directly - generated from MEDIAWIKI or TSV

3. **JSON** (`.json`) - in `hedjson/` directory

   - Flat dictionary structure for easy lookups
   - Optimized for AI tools and programmatic access
   - Never edited directly - generated from other formats

4. **Tabular TSV** (`.tsv`) - in `hedtsv/` directory

   - Spreadsheet-compatible format with separate files for tags, units, etc.
   - Good for adding many attributes or ontology mappings
   - May contain additional ontology mapping information

### Converting between formats

Use the [HED online tools](https://www.hedtools.org/hed) or command-line tools:

```bash
# Install HED Python tools 
pip install hedtools

# Convert schema
hed_convert_schema path/to/schema.mediawiki
```

______________________________________________________________________

## Viewing HED schemas

### HED schema browser

The easiest way to explore HED schemas is through the [HED schema browser](https://www.hedtags.org/hed-schema-browser):

1. Select a schema (standard or library) from the dropdown
2. Choose a version
3. Navigate the hierarchical tree structure
4. Click on any tag to see its description, attributes, and position in the hierarchy

The browser allows you to explore the hierarchical structure and is-a relationships described in the [Understanding schema structure](#understanding-schema-structure) section above.

### GitHub repository

All schemas are available in the [hed-schemas](https://github.com/hed-standard/hed-schemas) GitHub repository:

- **Standard schema**: `standard_schema/` directory
- **Library schemas**: `library_schemas/<name>/` directories

Each schema is available in the four formats described in the [Schema formats](#schema-formats) section above.

### Repository structure

This repository is organized as follows:

| Directory              | Description                                            |
| ---------------------- | ------------------------------------------------------ |
| `standard_schema/`     | Base HED vocabulary for all domains                    |
| `library_schemas/`     | Specialized vocabularies for specific domains          |
| `schemas_latest_json/` | Easy access to latest versions for AIs                 |
| `scripts/`             | Utility scripts for schema validation and verification |
| `docs/`                | Documentation source files                             |
| `.github/workflows/`   | CI/CD pipelines for validation and conversion          |

Each schema directory contains:

- `hedxml/` - XML format schemas
- `hedwiki/` - MediaWiki format schemas
- `hedjson/` - JSON format schemas
- `hedtsv/` - Tabular TSV format schemas
- `prerelease/` - Working versions under development
- `README.md` - Schema-specific documentation
- `CHANGELOG.md` - Version history
- `CONTRIBUTORS.md` - List of contributors

______________________________________________________________________

## Using HED schemas

### Annotation basics

HED annotations consist of comma-separated lists of HED tags from the schema vocabulary. Tags can be grouped using parentheses to indicate associations:

```
Red, Triangle, Blue, Square              # Ambiguous - which color goes with which shape?
(Red, Triangle), (Blue, Square)          # Clear - red triangle and blue square
```

### Using short vs. long form

As described in the [Understanding schema structure](#understanding-schema-structure) section, you should use short form when annotating:

- **Short form** (recommended): `Square`
- **Long form**: `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

HED tools can convert between forms as needed. The hierarchy enables search generalization: searching for `2D-shape` will find annotations containing `Square`, `Rectangle`, or any other descendant of `2D-shape`.

### Value tags and placeholders

Some tags can take values and units:

```
Age/35                                    # Specific age value
(Duration/500 ms)                         # With units
Label/stimulus-image                      # Text label
```

Only tags that have a `#` placeholder child are permitted to have values and units. Note the parentheses around the `Duration` tag. The `Duration` tag has the `topLevelTagGroup` attribute, meaning that it must appear in unnested parentheses in any annotation. The `Duration` tag is expected to be grouped with other tags that describe what it is the duration of.

### Using placeholders in BIDS sidecars

In BIDS sidecars, you can use placeholders to indicate column values:

```json
{
  "response_time": {
    "HED": "(Label/Response-time, Time-value/# s)"
  }
}
```

This format designates that the `response_time` column will be described by a single HED annotation. The `#` will be replaced with the actual column value for each row during annotation assembly.

### Schema versioning

HED schemas follow **semantic versioning** (major.minor.patch):

- **Major**: Breaking changes (removed terms, changed meaning)
- **Minor**: Backward-compatible additions (new terms, new attributes)
- **Patch**: Non-functional changes (description improvements, typos)

______________________________________________________________________

## Integrating schemas in your data

HED requires that you specify a HED version for most operations.

### BIDS datasets

In BIDS, the `dataset_description.json` located at the top level of the directory containing a dataset specifies the HED version.

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

````{admonition} BIDS dataset using multiple library schemas
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

### NWB files

HED is supported in NWB (Neurodata Without Borders) in a similar fashion. The HED version must be specified in `HedLabMetaData` element in a `NWBFile` before usage. See [ndx-hed](https://www.hedtags.org/ndx-hed) for more information.

### Programmatic access

Schemas can be accessed programmatically through the HED tools libraries:

````{admonition} Python - Loading a schema
---
class: tip
---
```python
from hed import load_schema_version
schema = load_schema_version('8.4.0')
```
````

The HED schemas are cached in Python HEDTools. Pass the `schema` object as needed to validation and analysis functions.

````{admonition} MATLAB - Direct Python calls
---
class: tip
---
```matlab
hedTools = HedToolsPython('8.4.0');
```
````

The `hedTools` object provides wrappers to the main Python HEDTools operations and loads the schema internally. This usage requires that the Python HEDTools be installed in the MATLAB Python environment. See [MATLAB HEDTools](https://www.hedtags.org/hed-matlab) for more information.

The MATLAB HEDTools also provide web service wrappers that require no installation. See the [MATLAB HEDTools documentation](https://www.hedtags.org/hed-matlab) for details.

````{admonition} JavaScript - Building a schema
---
class: tip
---
```javascript
import { buildSchema, SchemaSpec, SchemaSpecs } from '@hed-standard/hed-validator';
const spec1 = new SchemaSpec('', '8.4.0', '', '')
const specs = new SchemaSpecs().addSchemaSpec(spec1)
const hedSchemas = await buildSchemas(specs)
```
````

See [JavaScript HEDTools](https://www.hedtags.org/hed-javascript) for more information.

______________________________________________________________________

## Validation and troubleshooting

### Using validation tools

For most validation work, use the [HED online tools](https://hedtools.org/hed). These tools require no installation and provide quick feedback on:

- Schema validation and conversion
- Event file validation
- Sidecar validation
- HED string validation

If you want to do validation programmatically, consult the individual tool guides:

- [Python HEDTools](https://www.hedtags.org/hed-python)
- [MATLAB HEDTools](https://www.hedtags.org/hed-matlab)
- [JavaScript HEDTools](https://www.hedtags.org/hed-javascript)

### Common validation errors

1. **Unknown tag**: Tag not found in schema

   - Solution: Check spelling, check schema version

2. **Duplicate tag**: The same tag or tag group appears multiple times in an annotation

   - Solution: Remove duplicates. This can be tricky to spot in complex annotations, particularly in event files in which multiple rows have the same `onset` value and the duplication is not evident until the rows are combined

3. **Invalid unit**: Unit not compatible with tag's unit class

   - Solution: Use correct unit (e.g., `ms`, `s` for time). For tags that don't have `#` children, you can't use units at all

4. **Missing required child**: Tag with `requireChild` attribute used without a value

   - Solution: Add a value (e.g., `Label/my-label` instead of just `Label`)

5. **Top-level tag group violation**: Tag with `topLevelTagGroup` not in unnested parentheses

   - Solution: Ensure tags like `Definition` and `Duration` appear as `(Definition/...)`, not nested inside other groups

______________________________________________________________________

## Tools and resources

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
- Sidecar validation and assembly
- HED string validation
- Schema comparison

### Contributing to schemas

If you want to contribute to HED schema development:

#### Suggesting new terms or changes

1. Check if the term already exists in the [HED schema browser](https://www.hedtags.org/hed-schema-browser)
2. Post an [issue](https://github.com/hed-standard/hed-schemas/issues) describing:
   - The term you want to add/modify
   - Why it's needed
   - Where it should fit in the hierarchy
   - Examples of how it would be used
3. The HED Working Group will discuss and provide feedback
4. Approved changes will be added to the next schema version

#### Proposing a new library schema

If you have a specialized domain that needs extensive vocabulary:

1. Review the [Schema developer's guide](developer_guide.md)
2. Post an [issue](https://github.com/hed-standard/hed-schemas/issues) proposing the new library
3. Describe the domain, scope, and approximate vocabulary size
4. The HED Working Group will provide guidance on:
   - HedId range assignment
   - Schema structure and design
   - Development process
   - Partnership with standard schema

______________________________________________________________________

## Getting help

### Documentation resources

- **[HED schemas reference](schemas_reference.md)**: This guide for viewing and using schemas
- **[Developer guide](developer_guide.md)**: Guide for contributing to schemas
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification
- **[HED resources](https://www.hedtags.org/hed-resources)**: Tutorials and guides

### Support

- **Issues**: Report bugs, ask questions, or request features on [GitHub issues](https://github.com/hed-standard/hed-schemas/issues)
- **Questions about annotation**: See [HED resources](https://www.hedtags.org/hed-resources) tutorials
- **Technical questions**: Email [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Schema development**: See the [Schema developer's guide](developer_guide.md)

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

### Programmatic access

````{admonition} Accessing the schema in Python
---
class: tip
---
```python
from hed import load_schema_version
schema = load_schema_version('8.4.0')

```
````

The HED schemas are cached in the Python HEDTools. Pass the `schema` object as needed.

The MATLAB HEDTools provide two ways of analyzing HED, both of which rely on an underlying Python HEDTools for their implementation: calls to web services and direct installation. Both approaches use MATLAB wrappers, so no knowledge of Python is required. The web services method requires no installation except for adding the tools to the MAtLAB path. The services are hosted at [HED online tools](https://www.hedtags.org/hed). The other method involves direct calls to the Python HEDTools within MATLAB.

````{admonition} Direct calls to Python in MATLAB
---
class: tip
---
**MATLAB:** Direct Python calls in MATLAB

```matlab
hedTools = HedToolsPython('8.4.0');
```
````

The `hedTools` object, which provides wrappers to the main Python HEDTools operations, loads the schema internally. This usage requires that the Python HEDTools be installed in the MATLAB Python environment, which is probablematic for older versions of MATLAB. See [MATLAB HEDTools](https://www.hedtags.org/hed-matlab) for more information.

````{admonition} Direct calls to Python in MATLAB
---
class: tip
---
```javascript
import { buildSchema, SchemaSpec, SchemaSpecs } from '@hed-standard/hed-validator';
const spec1 = new SchemaSpec('', '8.4.0', '', '')
const specs = new SchemasSpec().addSchemaSpec(spec1)
const hedSchemas = await buildSchemas(specs)
```
````
______________________________________________________________________

## Getting help

- **Schema questions**: [GitHub issues](https://github.com/hed-standard/hed-schemas/issues)
- **Technical support**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Documentation**: [hedtags.org](https://www.hedtags.org)
- **Community**: [HED Working Group](https://www.hedtags.org)
````
