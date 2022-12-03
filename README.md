# HED schemas

The **HED schemas** are hierarchically-structured vocabularies for annotating data.
The HED ecosystem includes a **standard schema** containing the basic vocabulary
needed for annotation of experimental data as well as specialized **library schemas** for
the additional field-specific terms needed to complete an annotation.


| Schema | Current version | Viewers | Description |
| ------ | --------------- | ------- | ------------------------- |  
| [standard](standard_schema) | 8.1.0 | [**Latest**](http://www.hedtags.org/display_hed.html) <br/> [**Prelease**](https://www.hedtags.org/display_hed_prelease.html)  | Basic vocabulary for annotating data. |
| [score](library_schemas/score) | 0.0.1   | [**Latest**](https://www.hedtags.org/display_hed_score.html) <br/> [**Prerelease**](https://www.hedtags.org/display_hed_score_prerelease.html)  |  SCORE standard vocabulary for clinical neurological annotation (See [Score docs](https://hed-schema-library.readthedocs.io/en/latest/SCORE_library.html).) |
|  [testlib](library_schemas/testlib) | 1.0.1 | [**Latest**](https://www.hedtags.org/display_hed_testlib.html) <br/>  [**Prerelease**](https://www.hedtags.org/display_hed_testlib_prerelease.html) | A copy of the HED standard vocabulary for testing. <br/> (May not be stable.) |


## About HED
HED (Hierarchical Event Descriptors) is an evolving framework for the description and formal annotation of events 
identified in time series data. The HED ecosystem includes a structured vocabulary (HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. While HED can be used to annotate any type of event, 
the current HED community focuses on annotation of events in human 
electrophysiological and behavioral data such as EEG, MEG, iEEG, eye-tracking, 
motion-capture, EKG, and audiovisual recording.

## Using HED vocabularies

Access to the HED vocabularies hosted in this repository
happens automatically through tools in the HED ecosystem.

## Developing a new HED vocabulary

To begin to develop your own library post an issue in this repository.


## HED semantic versioning

HED schema use the following rules for
changing the  *major.minor.patch* semantic version.
These rules are based on the assumption that the HED short form
(**Needs link**) will not require data annotators to retag their data for patch-level or minor-version changes of the schema.
That is, a dataset tagged using schema version *X.Y.Z* will also validate for *X.Y+.Z+*. 
However, the reverse is not necessarily true.
In addition, validation errors might occur
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
