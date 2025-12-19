# HED schemas reference

This page provides detailed information about each available HED schema, including links to different formats, versions, and documentation.

## Standard schema

The HED standard schema contains the basic vocabulary for annotating experiments across all domains.

### Overview

| Property               | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| **Current Version**    | 8.4.0                                                            |
| **Prerelease Version** | 8.5.0                                                            |
| **HedId Range**        | 10000-39999                                                      |
| **DOI**                | [10.5281/zenodo.7876037](https://doi.org/10.5281/zenodo.7876037) |
| **Release Date**       | June 1, 2024                                                     |

### Description

The HED standard schema provides fundamental terms for describing:

- **Events**: Sensory presentations, experimental events, data features
- **Agents**: Humans, animals, avatars performing actions
- **Actions**: Movements, communications, cognitive processes
- **Items**: Objects, geometric entities, biological items, language items
- **Properties**: Characteristics describing agents, actions, and items
- **Relations**: Spatial and logical relationships

### Access Links

| Format        | Current Release (8.4.0)                                                                                                                                                                                                       | Prerelease (8.5.0)                                                                                                                                                                                                                  |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HED8.4.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/hedxml/HED8.4.0.xml)               | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/prerelease/HED8.5.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedwiki/HED8.4.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/hedwiki/HED8.4.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/prerelease/HED8.5.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedjson/HED8.4.0.json)                                                                                                                  | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/prerelease/HED8.5.0.json)                                                                                                                     |
| **TSV**       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedtsv/HED8.4.0)                                                                                                                            | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/prerelease/hedtsv)                                                                                                                                |

**Latest version (stable link):** [HEDLatest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml)

### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/standard_schema/CHANGELOG.md)
- [View in Schema Browser](https://www.hedtags.org/hed-schema-browser)

### References

> Makeig, S. and K. Robbins (2024).\
> Events in context—The HED framework for the study of brain, experience and behavior.\
> Front. Neuroinform. Vol. 18. [https://doi.org/10.3389/fninf.2024.1292667](https://doi.org/10.3389/fninf.2024.1292667)

> Robbins, K., Truong, D., Jones, A., Callanan, I., & Makeig, S. (2021).\
> Building FAIR functionality: Annotating event-related imaging data using Hierarchical Event Descriptors (HED).\
> Neuroinformatics. [https://doi.org/10.1007/s12021-021-09537-4](https://doi.org/10.1007/s12021-021-09537-4)

______________________________________________________________________

## SCORE library schema

HED-SCORE implements the Standardized Computer-based Organized Reporting of EEG (SCORE) standard for clinical neurological annotation.

### Overview

| Property               | Value                                                            |
| ---------------------- | ---------------------------------------------------------------- |
| **Current Version**    | 2.1.0                                                            |
| **Prerelease Version** | 2.2.0                                                            |
| **HedId Range**        | 40000-59999                                                      |
| **DOI**                | [10.5281/zenodo.7897596](https://doi.org/10.5281/zenodo.7897596) |
| **Partnered With**     | Standard 8.3.0                                                   |

### Description

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

### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/score/CHANGELOG.md)
- [View in Schema Browser](https://www.hedtags.org/hed-schema-browser)
- [SCORE Documentation](https://www.hedtags.org/hed-schemas/hed_score_schema.html)

### References

> Hermes, D., Pal Attia, T., Beniczky, S. et al.\
> Hierarchical Event Descriptor library schema for EEG data annotation.\
> Sci Data 12, 1448 (2025). [https://doi.org/10.1038/s41597-025-05791-2](https://doi.org/10.1038/s41597-025-05791-2)

> Beniczky, S, et al. (2013). Standardized computer based organized reporting of EEG: SCORE.\
> Epilepsia 54.6 (2013).

> Beniczky, S., et al. (2017). Standardized computer based organized reporting of EEG: SCORE second version.\
> Clinical Neurophysiology 128.11 (2017).

______________________________________________________________________

## LANG library schema

The HED Language library schema (HED LANG) contains vocabulary for annotating language experiments in cognitive science.

### Overview

| Property               | Value                                                              |
| ---------------------- | ------------------------------------------------------------------ |
| **Current Version**    | 1.1.0                                                              |
| **Prerelease Version** | 1.2.0                                                              |
| **HedId Range**        | 60000-79999                                                        |
| **DOI**                | [10.5281/zenodo.13987483](https://doi.org/10.5281/zenodo.13987483) |
| **Partnered With**     | Standard 8.3.0                                                     |

### Description

HED LANG allows for detailed annotation of language stimuli at multiple levels through orthogonal definition of:

- **Language-item**: Full sentences, words, morphemes, phonemes
- **Language-item-property**: Linguistic characteristics applicable across languages
  - Morphosyntactic properties (word class, case, tense, etc.)
  - Semantic properties (concreteness, animacy, etc.)
  - Orthographic properties (capitalization, script)
  - Phonological properties (stress, syllable structure)

The schema supports both carefully controlled experiments addressing specific psycholinguistic questions and complex naturalistic paradigms.

### Access Links

| Format        | Current Release (1.1.0)                                                                                                                                                                                                                             | Prerelease (1.2.0)                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_1.1.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/hedxml/HED_lang_1.1.0.xml)               | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/prerelease/HED_lang_1.2.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedwiki/HED_lang_1.1.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/hedwiki/HED_lang_1.1.0.mediawiki) | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/prerelease/HED_lang_1.2.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedjson/HED_lang_1.1.0.json)                                                                                                                             | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/prerelease/HED_lang_1.2.0.json)                                                                                                                                |
| **TSV**       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/hedtsv/HED_lang_1.1.0)                                                                                                                                       | [Directory](https://github.com/hed-standard/hed-schemas/tree/main/library_schemas/lang/prerelease/hedtsv)                                                                                                                                                 |

**Latest version (stable link):** [HED_lang_Latest.xml](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/lang/hedxml/HED_lang_Latest.xml)

### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/README.md)
- [CHANGELOG](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/lang/CHANGELOG.md)
- [View in Schema Browser](https://www.hedtags.org/hed-schema-browser)

### Example datasets

Annotated datasets using HED LANG are available:

- [ds001894](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds001894)
- [ds002155](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002155)
- [ds002382](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds002382)
- [ds003126](https://data.anc.plus.ac.at/bids-datasets/openneuro/ds003126)

### References

> Denissen, M., Pöll, B., Robbins, K., Makeig, S. & Hutzler, F.\
> HED LANG – A Hierarchical Event Descriptors library extension for annotation of language cognition experiments.\
> Sci Data 11, 1428 (2024). [https://doi.org/10.1038/s41597-024-04282-0](https://doi.org/10.1038/s41597-024-04282-0)

______________________________________________________________________

## SLAM library schema

The HED SLAM library schema provides vocabulary for Sensor Location and Motion annotation.

### Overview

| Property               | Value               |
| ---------------------- | ------------------- |
| **Current Version**    | - (prerelease only) |
| **Prerelease Version** | 1.0.0               |
| **HedId Range**        | 80000-99999         |
| **DOI**                | Not yet assigned    |
| **Partnered With**     | Standard 8.3.0      |

### Description

HED SLAM is currently in prerelease development. This library will provide vocabulary for describing:

- Sensor locations and positioning
- Motion tracking and recording
- Spatial relationships
- Movement characteristics

### Access Links

| Format        | Prerelease (1.0.0)                                                                                                                                                                                                                                        |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/prerelease/HED_slam_1.0.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/prerelease/HED_slam_1.0.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/slam/prerelease/HED_slam_1.0.0.json)                                                                                                                                |

### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/slam/README.md)

______________________________________________________________________

## MOUSE library schema

The HED MOUSE library schema provides vocabulary for mouse/rodent experiment annotation.

### Overview

| Property               | Value               |
| ---------------------- | ------------------- |
| **Current Version**    | - (prerelease only) |
| **Prerelease Version** | 1.0.0               |
| **HedId Range**        | 100000-119999       |
| **DOI**                | Not yet assigned    |
| **Partnered With**     | Standard 8.3.0      |

### Description

HED MOUSE is currently in prerelease development. This library will provide vocabulary specific to mouse and rodent experiments, including:

- Rodent-specific behaviors
- Experimental paradigms for animal studies
- Sensory stimuli relevant to rodent research
- Recording techniques specific to animal models

### Access Links

| Format        | Prerelease (1.0.0)                                                                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **XML**       | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.xml)             |
| **MEDIAWIKI** | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.mediawiki) \| [View](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.mediawiki) |
| **JSON**      | [Raw](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/library_schemas/mouse/prerelease/HED_mouse_1.0.0.json)                                                                                                                                  |

### Documentation

- [README](https://github.com/hed-standard/hed-schemas/blob/main/library_schemas/mouse/README.md)

______________________________________________________________________

## TESTLIB library schema

The TESTLIB schema is a copy of the standard schema used for testing purposes only.

### Overview

| Property     | Value                   |
| ------------ | ----------------------- |
| **Purpose**  | Testing and development |
| **Status**   | May not be stable       |
| **Use Case** | Internal testing only   |

⚠️ **Warning**: This schema is for testing purposes only and should not be used for actual data annotation.

______________________________________________________________________

## Schema format comparison

All schemas are available in four equivalent formats:

| Format        | Extension    | Use Case                              | Editing                         |
| ------------- | ------------ | ------------------------------------- | ------------------------------- |
| **XML**       | `.xml`       | Tool validation and analysis          | ❌ Never edit directly          |
| **MEDIAWIKI** | `.mediawiki` | Human-readable, schema development    | ✅ Primary editing format       |
| **JSON**      | `.json`      | AI tools, easy lookup                 | ❌ Generated from XML/MEDIAWIKI |
| **TSV**       | `.tsv`       | Spreadsheet editing, ontology mapping | ⚠️ Advanced use only            |

### Conversion between formats

Use the [HED Online Tools](https://hedtools.org) or command-line tools:

```powershell
# Install HED Python tools
pip install git+https://github.com/hed-standard/hed-python.git@main

# Convert schema
hed_update_schemas path/to/schema.mediawiki
```

______________________________________________________________________

## Using schemas in your data

### BIDS datasets

In your `dataset_description.json`:

```json
{
  "Name": "My Dataset",
  "BIDSVersion": "1.9.0",
  "HEDVersion": "8.4.0"
}
```

For library schemas:

```json
{
  "HEDVersion": ["8.3.0", "sc:score_2.1.0"]
}
```

### Programmatic access

**Python:**

```python
from hed import schema as hedschema
schema = hedschema.load_schema('8.4.0')
score_schema = hedschema.load_schema('score_2.1.0')
```

**MATLAB:**

```matlab
hedTools = getHedTools();
schema = hedTools.getSchema('8.4.0');
```

**JavaScript:**

```javascript
import { buildSchema } from '@hed-standard/hed-validator';
const schema = await buildSchema({ schemas: [['8.4.0', '']] });
```

______________________________________________________________________

## Getting help

- **Schema questions**: [GitHub Issues](https://github.com/hed-standard/hed-schemas/issues)
- **Technical support**: [hed.maintainers@gmail.com](mailto:hed.maintainers@gmail.com)
- **Documentation**: [hedtags.org](https://www.hedtags.org)
- **Community**: [HED Working Group](https://www.hedtags.org)
