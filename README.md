[![Documentation Status](https://readthedocs.org/projects/hed-schemas/badge/?version=latest)](https://hed-schemas.readthedocs.io/en/latest/?badge=latest)
Standard:[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7876037.svg)](https://doi.org/10.5281/zenodo.7876037) 
SCORE:[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7897596.svg)](https://doi.org/10.5281/zenodo.7897596) 
LANG:[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13987483.svg)](https://doi.org/10.5281/zenodo.13987483)

## About HED
HED (Hierarchical Event Descriptors) is an evolving framework for the description and
formal annotation of events and other information in data.
The HED ecosystem includes a structured vocabulary (specified by a HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. 

While HED can be used to annotate any type of data, 
the current HED community focuses on annotation of events in human 
neuroimaging and behavioral data such as EEG, MEG, iEEG, fMRI, eye-tracking, 
motion-capture, EKG, and audiovisual recording. 

See the [**HED project homepage**](https://www.hedtags.org) and
[**HED resources**](https://www.hed-resources.org),
particularly the [**How do you use HED?**](https://www.hed-resources.org/en/latest/HowCanYouUseHed.html)
for information about how to get started or how to get involved in the HED community.

## Viewing HED schemas
The **HED schemas** are hierarchically-structured vocabularies for annotating data.
The HED ecosystem includes a **standard schema** containing the basic vocabulary
needed for annotation of experimental data as well as specialized **library schemas** for
the additional field-specific terms needed to complete an annotation.

All released and prereleased versions of the HED schemas can be viewed the [**HED Schema Browser**](https://www.hedtags.org/display_hed.html).

The following table summarizes the current versions of the HED schemas.

| Schema                                 | Latest<br/>version | Description       | Prerelease<br/>version | DOI  |
|----------------------------------------|--------------------|------|------------------------| ---- |
| [**standard**](./standard_schema)      | 8.3.0              | Basic vocabulary for annotating data.       | 8.4.0                  | 10.5281/zenodo.7876037 |
| [**score**](library_schemas/score)     | 1.2.0              | SCORE standard vocabulary for <br/>clinical neurological annotation<br/>(See [**Score docs**](https://hed-schemas.readthedocs.io/en/latest/hed_score_schema.html).) | 2.0.0                  | 10.5281/zenodo.7897596  |
| [**lang**](library_schemas/lang)       | 1.0.0              | LANG linguistic stimuli annotation vocabulary.                                               | 1.0.1                  | 10.5281/zenodo.13987483 |
| [**slam**](library_schemas/slam) |                    | SLAM (Sensor Location and Motion) | 1.0.0                  | |  
| [**testlib**](library_schemas/testlib) | 3.0.0              | A copy of the HED standard vocabulary<br/> for testing. <br/> (May not be stable.)    | 4.0.0                  |  |

## HED formats
HED schemas are stored in three different formats:
MediaWiki (`.mediawiki`), XML (`.xml`), and tabular (`.tsv`).
An online schema conversion tool is available at as part of the
[**HED online tools**](https://hedtools.org/hed/schemas).

### MediaWiki format
The `.mediawiki` Markdown format is used by schema developers to create and
maintain HED schemas. For each schema, the `.mediawiki` versions are
stored in the respective `hedwiki` directory for the schema.

### XML format
The XML (`.xml`) format used with all HED analysis and validation tools.
It is never created directly by schema developers, but rather created from either the
MediaWiki or the tabular versions of the schema.
For each schema, the XML versions are
stored in the respective `hedxml` directory for the schema.
The XML and MediaWiki contain equivalent information.

### Tabular format
The `.tsv` format is a tabular  (tab-separated) text format.
Each type of entity in the HED schema (e.g., tags, unit classes, etc.) has its own tsv file.
For each schema the tabular versions are stored in the respective `hedtsv` directory for the schema.
The tabular version may contain additional information such as provenance and links to other ontologies.


## HED revision process
If you want to suggest a new feature or a change to the standard HED schema or one
of the HED library schemas, just post an [**issue**](https://github.com/hed-standard/hed-schemas/issues)
to this repository, and it will find its way to the right place.

As modifications to a HED schema are proposed, they are entered into the
`PROPOSED.md` document in the schema's respective directory for discussion.
Approved changes and corrections are first made in a working version of the
schema that is located in the `prerelease` subdirectory. 
Upon final review, the new HED schema is released and moved to the
`hedxml` directory of the respective library schema.

For a more complete view of the process see the [**HED schema developer's guide**](https://www.hed-resources.org/en/latest/HedSchemaDevelopersGuide.html).

## Tools to help with HED annotations
The GUI tool [**CTagger**](https://www.hed-resources.org/en/latest/CTaggerGuiTaggingTool.html) is available to help users with the annotation process. 
CTagger can be used as a standalone application or can be called from EEGLAB via the
[**hedtools plug-in**](https://www.hed-resources.org/en/latest/HedMatlabTools.html) to annotate an EEGLAB dataset/STUDY directly. 
Please refer to the linked repositories for more documentation on how to start HED-tagging using CTagger.

## Web-based HED tools
The current online HED tools include an online validator of spreadsheets (Excel or tsv)
containing HED tags. 
Schema tools are available for validating and converting HED schema specifications between `.mediawiki` and `.xml` formats. 

The released version of the web-based HED tools is located at [**https://hedtools.org**](https://hedtools.org).
The development version of the tools, used to test features before release,
is located at [**https://hedtools.org/hed_dev**](https://hedtools.org/hed_dev).

## HED semantic versioning
HED schemas use the following rules for
changing the  *major.minor.patch* semantic version.
These rules are based on the assumption that annotators using the [**HED tag**](https://hed-specification.readthedocs.io/en/latest/02_Terminology.html#hed-tag) 
short form will not have to retag their data for patch-level or minor-version changes of the schema.
That is, a dataset tagged using schema version *X.Y.Z* will also validate for *X.Y+.Z+*.
In addition, validation errors might occur
during for patch-level or minor-version changes for changes or
corrections in tag values or units. 

Here is a summary of the types of changes that correspond to different
levels of changes in the semantic version:

| Change                                          | Semantic-level |
|-------------------------------------------------|----------------|
| Major addition to HED functionality             | Major          |
| Tag deleted from schema.                        | Major          |
| Unit or unit class removed from node.           | Major          |
| Node attribute value changed                    | Minor          |
| Inherited attribute change                      | Minor          |
| New property added to or removed from schema    | Minor          |
| New value class added to schema                 | Minor          |
| New unit modifier added to schema               | Minor          |
| New tag added to the schema.                    | Minor          |
| New attribute added to schema.                  | Minor          |
| New unit class or unit added to schema.         | Minor          |
| New unit class added to node.                   | Minor          |
| New value class added to node.                  | Minor          |
| Node moved in schema without change in meaning. | Minor          |
| Revision of description field in schema.        | Patch          |
| Correction of suggestedTag or relatedTag.       | Patch          |


**Note:** It is an official policy that once in a schema, a node will not be removed without
a major schema version change.
If a node becomes out-of-date, a `deprecated` attribute will be added to the tag in the schema.
Suggested replacement tags should be included in the node description.
A suggested replacement should be added to the tag patch table.

## HED generations and schema versions 
The HED system has gone through two major restructurings since the original system
(HED-1G) was introduced. The following table shows the correspondence between 
HED schema version number and the design generation.

| schema version | release date | HED generation |
| --- | --- | --- |
| 1.0 | 2011-01-01 | HED-1G |
| 4.0.0 | 2016-02-25 | HED-2G |
| 8.0.0 | 2021-08-07 | HED-3G |


HED-1G introduced the basic ideas of annotation using path strings and is
still in use in the [HEADIT archive](https://headit.ucsd.edu). 

A major redesign of HED, HED-2G released in 2016 (4.0.0 <= schema version < 8.0.0), 
orthogonalized the vocabulary terms and introduced parentheses for grouping modifiers
with the terms they modify, resulting in much improved annotation. 

The second majoring restructuring, HED-3G (7.x.x < schema version), 
has resulted in a dramatic improvement in capabilities, including the 
introduction of annotations of condition variables and experimental 
design within the data as well as the ability to handle event context 
and events with temporal extent.

## Stable links for HED validation

> [**Stable directory link for software requiring a HED standard schema for validation**](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml).

> [**Stable link for the latest version of the HED standard schema**](https://raw.githubusercontent.com/hed-standard/hed-schemas/main/standard_schema/hedxml/HEDLatest.xml).

The full HED specification is available at the
[**HED specification**](https://hed-specification.readthedocs.io/en/latest/index.html) website. 

### HED ontologies
Efforts are underway to map HED to a formal ontology in order to leverage links to 
other terminologies and vocabularies. The development effort is housed on the
[**hed-ontology**](https://github.com/hed-standard/hed-ontology) GitHub repository.
