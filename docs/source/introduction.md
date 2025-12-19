# Introduction to HED schemas

## What is HED?

HED (Hierarchical Event Descriptors) is an evolving framework for the description and formal annotation of events and other types of data. The HED ecosystem includes:

- **Controlled vocabulary** specified by HED schemas for annotating experimental data
- **Standardized infrastructure** enabling automated analysis and interpretation
- **Integration** with major neuroimaging standards (BIDS and NWB)
- **Tools** for validation and using HED annotations in data search, extraction, and analysis

For more information, visit the [HED project homepage](https://www.hedtags.org).

## What is a HED schema?

A **HED schema** is a hierarchically-structured specification of a vocabulary. The HED ecosystem includes:

- **Standard schema**: Contains the basic vocabulary needed for annotation of experimental data
- **Library schemas**: Specialized field-specific vocabularies for domain-specific annotations

## Scope of HED

HED allows researchers to annotate what happened during an experiment, including:

- Experimental stimuli and other sensory events
- Participant responses and actions
- Experimental design
- The role of events in the task
- The temporal structure of the experiment

The resulting annotation is **machine-actionable**, meaning it can be used as input to algorithms without manual intervention. HED facilitates detailed comparisons of data across studies.

While HED can be used to annotate any type of data, the current HED community focuses on annotation of events in human neuroimaging, behavioral, and physiological data such as:

- EEG, MEG, iEEG
- fMRI
- Eye-tracking
- Motion-capture
- EKG
- Audiovisual recording

HED is also useful for participant metadata annotation as well as for media (images and video) and environmental annotation, since this information is important for understanding brain interaction with the outside world.

## Schema hierarchal structure

HED schemas are structured as a set of trees, each corresponding to a major term category for the vocabulary. Each child tag in a HED schema is considered to be a special type of its ancestors, following an **is-a** relationship.

For example, the tag `Square` has a full schema path:

> `Item/Object/Geometric-object/2D-shape/Rectangle/Square`

This means `Square` is-a type of `Rectangle`, which is-a type of `2D-shape`, etc. This strict hierarchy enables powerful search generalization: when downstream tools search for `2D-shape`, the search will return tag strings containing `Square`, `Rectangle`, and `2D-shape`.

Although you can express a tag by any partial path in the hierarchy, when posible you SHOULD ONLY USE JUST the tag node name (e.g., `Square`) rather than the full path or a partial path itself when annotating data. There is no ambiguity, because tag names in a schema must be unique. HED-compliant tools can convert between this **"short-form"** and the complete path or **"long-form"** when needed for search, summarization, or other processing. Short form makes annotations simpler. In addition, a node sometimes changes position when a new version is release if additional intermediate nodes are added.

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

Each schema is stored in **four equivalent formats**. Each format holds

1. **MediaWiki** (`.mediawiki`) - in `hedwiki/` directory

   - Human-readable text format
   - Primary editing format for schema developers
   - Easy to review in GitHub and text editors

2. **XML** (`.xml`) - in `hedxml/` directory

   - Format used by all HED tools for validation and analysis
   - Includes XSD schema definition files
   - Never edited directly - generated from MediaWiki or TSV

3. **JSON** (`.json`) - in `hedjson/` directory

   - Flat dictionary structure for easy lookups
   - Optimized for AI tools and programmatic access
   - Generated from XML/MediaWiki

4. **Tabular TSV** (`.tsv`) - in `hedtsv/` directory

   - Spreadsheet-compatible format
   - Each schema entity type (tags, units, etc.) in separate TSV file
   - May contain additional ontology mapping information

**CRITICAL**: All four formats contain the same semantic information. Conversion between formats is lossless.

## Related tools and resources

- **[HED homepage](https://www.hedtags.org)**: Overview and links for HED
- **[HED Schema Browser](https://www.hedtags.org/hed-schema-browser)**: Interactive schema exploration
- **[HED Specification](https://www.hedtags.org/hed-specification/)**: Formal specification defining HED annotation rules
- **[HED Online Tools](https://hedtools.org)**: Web-based schema validation, conversion, and annotation tools
- **[HED Python Tools](https://github.com/hed-standard/hed-python)**: Python tools for HED validation, analysis, and transformation
- **[HED MATLAB Tools](https://github.com/hed-standard/hed-matlab)**: MATLAB tools for HED processing
- **[HED JavaScript Tools](https://github.com/hed-standard/hed-javascript)**: JavaScript validation tools
- **[HED Examples](https://github.com/hed-standard/hed-examples)**: Example datasets annotated with HED
- **[HED Resources](https://www.hedtags.org/hed-resources)**: Comprehensive tutorials and documentation

## Repository structure

This repository is organized as follows:

| Directory            | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `standard_schema/`   | Base HED vocabulary for all domains                    |
| `library_schemas/`   | Specialized vocabularies for specific domains          |
| `scripts/`           | Utility scripts for schema validation and verification |
| `docs/`              | Documentation source files                             |
| `.github/workflows/` | CI/CD pipelines for validation and conversion          |

Each schema directory contains:

- `hedxml/` - XML format schemas
- `hedwiki/` - MediaWiki format schemas
- `hedjson/` - JSON format schemas
- `hedtsv/` - Tabular TSV format schemas
- `prerelease/` - Working versions under development
- `README.md` - Schema-specific documentation
- `CHANGELOG.md` - Version history
- `CONTRIBUTORS.md` - List of contributors

## Using HED schemas

HED schemas can be accessed and used through various tools and interfaces.

### Web-based tools

For users who prefer not to program, HED provides web-based tools at:

- **[hedtools.org](https://hedtools.org)** - Production version
- **[hedtools.org/hed_dev](https://hedtools.org/hed_dev)** - Development version

These tools support:

- Schema validation and conversion
- Event file validation
- Sidecar validation
- HED string validation

### Programmatic access

Schemas can be accessed programmatically through:

- **Python**: [HED Python Tools](https://github.com/hed-standard/hed-python)
- **MATLAB**: [HED MATLAB Tools](https://github.com/hed-standard/hed-matlab)
- **JavaScript**: [HED JavaScript Tools](https://github.com/hed-standard/hed-javascript)

## Getting help

### Documentation resources

- **[User guide](user_guide.md)**: Guide for using and accessing schemas
- **[Developer guide](developer_guide.md)**: Guide for contributing to schemas
- **[Schemas reference](schemas_reference.md)**: Detailed schema information
- **[Repository structure](api2.rst)**: Repository organization
- **[HED specification](https://www.hedtags.org/hed-specification/)**: Formal specification
- **[HED resources](https://www.hedtags.org/hed-resources)**: Tutorials and guides

### Support

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/hed-standard/hed-schemas/issues)
- **Questions**: Ask on the [HED forum](https://github.com/hed-standard/hed-specification/discussions)
- **Email**: Contact [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
