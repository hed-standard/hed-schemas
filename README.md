# Hierarchical Event Descriptors (HED) Schemas

HED is an evolving framework for the description and formal annotation of events 
identified in time series data. The HED ecosystem includes a structured vocabulary (HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. While HED can be used to annotate any type of event, 
the current HED community focuses on annotation of events in human 
electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, 
motion-capture, EKG, and audiovisual recording.

The **HED schemas** are hierarchically-structured vocabularies for annotation.
The HED ecosystem includes a **standard schema** for basic the basic vocabulary
needed for annotation as well as specialized **library schemas** for
the additional field-specific terms needed to complete an annotation.


| Schema | Latest<br/>version | Viewers | Description |
| ------ | ------- | ------ | ---------------| ------------------------- |
| [standard](standard_schema) | 8.1.0 | [**Latest**](http://www.hedtags.org/display_hed.html) <br/>[**Prelease**](https://www.hedtags.org/display_hed_prelease.html)  |
| [score](library_schemas/score) | 0.0.1   | [**Latest**](https://www.hedtags.org/display_hed_score.html) <br/>[**Prerelease**](https://www.hedtags.org/display_hed_score_prerelease.html)  |  SCORE standard vocabulary for clinical neurological annotation (See [Score docs](https://hed-schema-library.readthedocs.io/en/latest/SCORE_library.html).) |
|  [testlib](library_schemas/testlib) | 1.0.1 |   | A prerelease copy of same schema as HED 8.0.1 for testing. |

**Note:** The website contains both `.mediawiki` and `.xml` versions of the schema.
The schemas are located in the `hedwiki` and `hedxml` subdirectories, respectively,
of the respective schema directory.

## HED semantic versioning

HED schema use the following rules for
changing the semantic version *major.minor.patch*. These rules are
based on the assumption that the short form will not require retagging
for patch-level or minor-version changes. A validation error might occur
during for patch-level or minor-version changes for changes or
corrections in tag values or units. 

Here is a summary of the types of changes that correspond to different
levels of changes in the semantic version:

| Change                          | Semantic-level | 
| ---------------------------------- | -------------- |
| Major addition to HED functionality     | Major  |
| Tag deleted from schema.                | Major  |
| Unit or unit class removed from node.   | Major  |
| New tag added to the schema.            | Minor  |
| New attribute added to schema.          | Minor  |
| New unit class or unit added to schema. | Minor  |
| New unit class added to node.           | Minor  |
| Node moved in schema without change in meaning. | Minor |
| Revision of description field in schema.        | Patch   |
| Correction of suggestedTag or relatedTag.       | Patch  |
| Correction of wiki syntax such as closing tags. | Patch |

## HED revision process

As modifications to the HED schema are proposed, they are entered into the
`PROPOSED.md` document in their respective directory for discussion.
Approved changes and corrections are first made in a working version of the
schema that is located in the `prerelease` subdirectory. 
Upon final review, the new HED schema is released and moved to the
`hedxml` directory of the respective library schema.
