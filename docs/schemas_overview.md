---
html_meta:
  "description": "Complete reference for HED schemas including how to view, use, and access HED schemas for data annotation"
  "keywords": "HED schemas, standard schema, library schemas, score, lang, slam, mouse, schema versions, HED annotation, schema browser"
---

```{index} schema reference; standard schema; library schemas; versions; formats; HED usage
```

# HED schemas overview

This guide provides an overview of the existing HED (Hierarchical Event Descriptors) schemas. You can also explore the available HED schemas using the [HED schema browser](https://www.hedtags.org/hed-schema-browser).

## What is a HED schema?

A **HED schema** is a hierarchically-structured specification of a vocabulary for annotating experimental data. HED allows researchers to describe what happened during an experiment including:

- Experimental stimuli and other sensory events
- Participant responses and actions
- Experimental design and task structure
- The role of events in the task
- The temporal structure of the experiment
- Participant metadata
- Environmental setup

The **standard schema** contains the basic vocabulary and organizational tags needed for annotation across all domains. Additional **library schemas** contain specialized field-specific vocabularies for domain-specific annotations.

HED schemas are structured as a set of trees, each corresponding to a major term category for the vocabulary. Each child tag in a HED schema is considered to be a special type of its ancestors, following an **is-a** relationship.

For example, the tag `Square` has a full schema path:

> `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

This means `Square` is-a type of `Rectangle`, which is-a type of `2D-shape`, etc. This strict hierarchy enables powerful search generalization: when downstream tools search for `2D-shape`, the search will return tag strings containing `Square`, `Rectangle`, and `2D-shape`.

## Available schemas

HED provides a standard schema and multiple specialized library schemas for specific research domains.

### Standard schema

The HED standard schema contains the basic vocabulary for annotating experiments across all domains. The standard schema DOI is [10.5281/zenodo.7876037](https://doi.org/10.5281/zenodo.7876037) and has HED IDs in the range HED_10000-HED_39999.

The standard schema is organized into the following top-level hierarchies:

- **Events**: Sensory presentations, experimental events, data features
- **Agents**: Humans, animals, avatars performing actions
- **Actions**: Movements, communications, cognitive processes
- **Items**: Objects, geometric entities, biological items, language items
- **Properties**: Characteristics describing agents, actions, and items
- **Relations**: Spatial and logical relationships

| Version | Status     | Release date | XML                                                                                                            | MEDIAWIKI                                                                                                            | JSON                                                                                                            | TSV                                                                                                  |
| ------- | ---------- | ------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 8.4.0   | Latest     | June 1, 2025 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.4.0.xml)     | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedwiki/HED8.4.0.mediawiki)    | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedjson/HED8.4.0.json)    | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedtsv/HED8.4.0)   |
| 8.5.0   | Prerelease |              | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.json) | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/prerelease/hedtsv) |

**Latest version (stable link):** [HEDLatest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

**References:**

> Makeig, S. and K. Robbins (2024).\\ Events in context—The HED framework for the study of brain, experience and behavior.\\ Front. Neuroinform. Vol. 18. [https://doi.org/10.3389/fninf.2024.1292667](https://doi.org/10.3389/fninf.2024.1292667)

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2021).\\ Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).\\ Neuroinformatics. [https://doi.org/10.1007/s12021-021-09537-4](https://doi.org/10.1007/s12021-021-09537-4)

______________________________________________________________________

### SCORE library schema

HED-SCORE implements the Standardized Computer-based Organized Reporting of EEG (SCORE) standard for clinical neurological annotation. The SCORE library schema DOI is [10.5281/zenodo.7897596](https://doi.org/10.5281/zenodo.7897596) and has HED IDs in the range HED_40000-HED_59999.

The SCORE library allows neurologists, neurophysiologists, and brain researchers to annotate electrophysiology recordings using terms from an internationally accepted set of defined terms compatible with the HED framework. The vocabulary covers:

- **Finding**: EEG phenomena and patterns observed in recordings
- **Sleep-related**: Sleep stages and sleep-specific phenomena
- **Modulators**: Factors affecting EEG patterns (eye state, vigilance, medication)
- **Background-activity**: Characteristics of ongoing EEG
- **Episode**: Specific event types (seizures, epileptic episodes)

| Version | Status     | Release date | Partnered with | XML                                                                                                                         | MEDIAWIKI                                                                                                                         | JSON                                                                                                                         | TSV                                                                                                             |
| ------- | ---------- | ------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 2.1.0   | Latest     | June 9, 2025 | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_2.1.0.xml)     | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedwiki/HED_score_2.1.0.mediawiki)    | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedjson/HED_score_2.1.0.json)    | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/hedtsv/HED_score_2.1.0) |
| 2.2.0   | Prerelease |              | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/prerelease/HED_score_2.2.0.json) | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/score/prerelease/hedtsv)      |

**Latest version (stable link):** [HED_score_Latest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/score/hedxml/HED_score_Latest.xml)

**References:**

> Hermes, D., Pal Attia, T., Beniczky, S. et al.\\ Hierarchical Event Descriptor library schema for EEG data annotation.\\ Sci Data 12, 1448 (2025). [https://doi.org/10.1038/s41597-025-05791-2](https://doi.org/10.1038/s41597-025-05791-2)

> Beniczky, S, et al. (2013). Standardized computer based organized reporting of EEG: SCORE.\\ Epilepsia 54.6 (2013).

> Beniczky, S., et al. (2017). Standardized computer based organized reporting of EEG: SCORE second version.\\ Clinical Neurophysiology 128.11 (2017).

______________________________________________________________________

### LANG library schema

The HED Language library schema (HED LANG) contains vocabulary for annotating language experiments in cognitive science. The LANG library schema DOI is [10.5281/zenodo.13987483](https://doi.org/10.5281/zenodo.13987483) and has HED IDs in the range HED_60000-HED_79999.

HED LANG allows for detailed annotation of language stimuli at multiple levels through orthogonal definition of:

- **Language-item**: Full sentences, words, morphemes, phonemes
- **Language-item-property**: Linguistic characteristics applicable across languages
  - Morphosyntactic properties (word class, case, tense, etc.)
  - Semantic properties (concreteness, animacy, etc.)
  - Orthographic properties (capitalization, script)
  - Phonological properties (stress, syllable structure)

The schema supports both carefully controlled experiments addressing specific psycholinguistic questions and complex naturalistic paradigms.

| Version | Status     | Release date  | Partnered with | XML                                                                                                                       | MEDIAWIKI                                                                                                                       | JSON                                                                                                                       | TSV                                                                                                           |
| ------- | ---------- | ------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 1.1.0   | Latest     | June 10, 2025 | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_1.1.0.xml)     | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedwiki/HED_lang_1.1.0.mediawiki)    | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedjson/HED_lang_1.1.0.json)    | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/hedtsv/HED_lang_1.1.0) |
| 1.2.0   | Prerelease |               | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.json) | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/prerelease/hedtsv)     |

**Latest version (stable link):** [HED_lang_Latest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_Latest.xml)

**Example datasets:** Annotated datasets using HED LANG are available at [ds001894](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds001894), [ds002155](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002155), [ds002382](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002382), and [ds003126](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds003126).

**References:**

> Denissen, M., Pöll, B., Robbins, K., Makeig, S. & Hutzler, F.\\ HED LANG – A Hierarchical Event Descriptors library extension for annotation of language cognition experiments.\\ Sci Data 11, 1428 (2024). [https://doi.org/10.1038/s41597-024-04282-0](https://doi.org/10.1038/s41597-024-04282-0)

______________________________________________________________________

### SLAM library schema

The HED SLAM library schema provides vocabulary for Sensor Location and Motion annotation. The SLAM library schema has HED IDs in the range HED_80000-HED_99999. The DOI has not yet been assigned. This library is currently in prerelease development and provides vocabulary for describing sensor locations and positioning, motion tracking and recording, spatial relationships, and movement characteristics.

| Version | Status     | Release date | Partnered with | XML                                                                                                                       | MEDIAWIKI                                                                                                                       | JSON                                                                                                                       |
| ------- | ---------- | ------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| 1.0.0   | Prerelease |              | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.json) |

______________________________________________________________________

### MOUSE library schema

The HED MOUSE library schema provides vocabulary for mouse/rodent experiment annotation. The MOUSE library schema has HED IDs in the range HED_100000-HED_119999. The DOI has not yet been assigned. This library is currently in prerelease development and provides vocabulary specific to mouse and rodent experiments, including rodent-specific behaviors, experimental paradigms for animal studies, sensory stimuli relevant to rodent research, and recording techniques specific to animal models.

| Version | Status     | Release date | Partnered with | XML                                                                                                                         | MEDIAWIKI                                                                                                                         | JSON                                                                                                                         |
| ------- | ---------- | ------------ | -------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 1.0.0   | Prerelease |              | Standard 8.3.0 | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.json) |

______________________________________________________________________

### TESTLIB library schema

The TESTLIB schema is a copy of the standard schema used for testing purposes only. This schema is for testing and development use only and should not be used for actual data annotation.

______________________________________________________________________

## Schema formats

Each schema is stored in **four equivalent formats**. All formats contain the same semantic information and conversion between formats is lossless.

| Format        | Extension    | Location   | Use Case                              | Editing                         |
| ------------- | ------------ | ---------- | ------------------------------------- | ------------------------------- |
| **XML**       | `.xml`       | `hedxml/`  | Tool validation and analysis          | ❌ Never edit directly          |
| **MEDIAWIKI** | `.mediawiki` | `hedwiki/` | Human-readable, schema development    | ✅ Primary editing format       |
| **JSON**      | `.json`      | `hedjson/` | AI tools, easy lookup                 | ❌ Generated from XML/MEDIAWIKI |
| **TSV**       | `.tsv`       | `hedtsv/`  | Spreadsheet editing, ontology mapping | ✅ Good for adding attributes   |

**MEDIAWIKI** is the primary editing format - a human-readable text format in a single file that makes it easy to visualize the hierarchical structure. **XML** is the format used by all HED tools for validation and analysis and is never edited directly. **JSON** provides a flat dictionary structure optimized for AI tools and programmatic access. **TSV** is a spreadsheet-compatible format with separate files for tags, units, etc., which is good for adding many attributes or ontology mappings.

______________________________________________________________________

## Using HED schemas

### Annotation basics

HED annotations consist of comma-separated lists of HED tags from the schema vocabulary. Tags can be grouped using parentheses to indicate associations:

```
Red, Triangle, Blue, Square              # Ambiguous - which color goes with which shape?
(Red, Triangle), (Blue, Square)          # Clear - red triangle and blue square
```

### Tag forms: Short vs. long

Although you can express a tag by any partial path in the hierarchy, when possible you should use just the tag node name (e.g., `Square`) rather than the full path or a partial path when annotating data:

- **Short form** (recommended): `Square`
- **Long form**: `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

There is no ambiguity, because tag names in a schema must be unique. HED-compliant tools can convert between this **"short-form"** and the complete path or **"long-form"** when needed for search, summarization, or other processing. Short form makes annotations simpler and is the recommended approach. In addition, a node sometimes changes position when a new schema version is released if additional intermediate nodes are added.

The hierarchy enables search generalization: when downstream tools search for `2D-shape`, the search will return tag strings containing `Square`, `Rectangle`, or any other descendant of `2D-shape`.

### Value tags and units

Some tags can take values and units:

```
Age/35                                    # Specific age value
(Duration/500 ms)                         # With units
Label/stimulus-image                      # Text label
```

Only tags that have a `#` placeholder child are permitted to have values and units. Tags with the `topLevelTagGroup` attribute (like `Duration`) must appear in unnested parentheses.

### Using placeholders in BIDS sidecars

In BIDS sidecars, you can use placeholders to indicate column values:

```json
{
  "response_time": {
    "HED": "(Label/Response-time, Time-value/# s)"
  }
}
```

The `#` will be replaced with the actual column value for each row during annotation assembly.

### Specifying schema versions in datasets

**BIDS datasets:** The `dataset_description.json` at the top level specifies the HED version.

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

**NWB files:** HED is supported in NWB (Neurodata Without Borders) via the `HedLabMetaData` element in a `NWBFile`. See [ndx-hed](https://www.hedtags.org/ndx-hed) for more information.

### Programmatic access

````{admonition} Python
---
class: tip
---
```python
from hed import load_schema_version
schema = load_schema_version('8.4.0')
```
````

````{admonition} MATLAB
---
class: tip
---
```matlab
hedTools = HedToolsPython('8.4.0');
```
````

This requires Python HEDTools installed in the MATLAB Python environment. Alternatively, use web service wrappers that require no installation. See [MATLAB HEDTools](https://www.hedtags.org/hed-matlab) for details.

````{admonition} JavaScript
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

### Schema versioning

HED schemas follow **semantic versioning** (major.minor.patch):

- **Major**: Breaking changes (removed terms, changed meaning)
- **Minor**: Backward-compatible additions (new terms, new attributes)
- **Patch**: Non-functional changes (description improvements, typos)

______________________________________________________________________

## Validation and troubleshooting

### Common validation errors

1. **Unknown tag**: Tag not found in schema - Check spelling and schema version
2. **Duplicate tag**: The same tag appears multiple times in an annotation - Remove duplicates
3. **Invalid unit**: Unit not compatible with tag's unit class - Use correct unit (e.g., `ms`, `s` for time)
4. **Missing required child**: Tag with `requireChild` attribute used without a value - Add a value
5. **Top-level tag group violation**: Tag with `topLevelTagGroup` not in unnested parentheses - Ensure proper nesting

______________________________________________________________________

## Tools and resources

### Online tools

- **[HED schema browser](https://www.hedtags.org/hed-schema-browser)**: Interactive schema exploration
- **[HED online tools](https://hedtools.org/hed)**: Web-based validation, conversion, and annotation tools
- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification

### Programming libraries

- **[Python HEDTools](https://github.com/hed-standard/hed-python)**: `hedtools` package for validation, analysis, and transformation
- **[MATLAB HEDTools](https://github.com/hed-standard/hed-matlab)**: MATLAB tools and web service wrappers
- **[JavaScript HEDTools](https://github.com/hed-standard/hed-javascript)**: JavaScript validation tools

### Documentation

- **[HED resources](https://www.hedtags.org/hed-resources)**: Comprehensive tutorials and documentation
- **[HED examples](https://github.com/hed-standard/hed-examples)**: Example annotated datasets
- **[README files](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/README.md)**: Schema-specific documentation in GitHub repository
- **[CHANGELOG files](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/CHANGELOG.md)**: Version history for each schema

### Contributing to schemas

To suggest new terms or changes:

1. Check if the term exists in the [HED schema browser](https://www.hedtags.org/hed-schema-browser)
2. Post an [issue](https://github.com/hed-standard/hed-schemas/issues) describing the term, why it's needed, where it fits, and usage examples
3. The HED Working Group will discuss and provide feedback
4. Approved changes will be added to the next schema version

To propose a new library schema, review the [Developer guide](developer_guide.md) and post an [issue](https://github.com/hed-standard/hed-schemas/issues) with details about the domain, scope, and vocabulary size.

______________________________________________________________________

## Getting help

- **Questions and issues**: [GitHub issues](https://github.com/hed-standard/hed-schemas/issues)
- **Technical support**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Schema development**: See the [Developer guide](developer_guide.md)
