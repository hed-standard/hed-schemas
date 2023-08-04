[![Documentation Status](https://readthedocs.org/projects/hed-schemas/badge/?version=latest)](https://hed-schemas.readthedocs.io/en/latest/?badge=latest)
Standard:[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7876037.svg)](https://doi.org/10.5281/zenodo.7876037) 
SCORE:[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7897596.svg)](https://doi.org/10.5281/zenodo.7897596)
[![@HEDstandard](http://img.shields.io/twitter/follow/hedstandard.svg?style=social)](https://twitter.com/HEDstandard)

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

| Schema | Latest<br/>version| Description | Prerelease<br/>version  | DOI  |
| ------ | --------------- | ------- | ------------------------- | ---- |
| [**standard**](./standard_schema) | 8.2.0 | Basic vocabulary for annotating data. | 8.3.0 | 10.5281/zenodo.7876037 |
| [**score**](library_schemas/score) | 1.1.0  | SCORE standard vocabulary for <br/>clinical neurological annotation<br/>(See [**Score docs**](https://hed-schemas.readthedocs.io/en/latest/hed_score_library.html).) |1.1.1 | 10.5281/zenodo.7897596  |
|  [**language**](library_schemas/language) |  | Language stimuli annotation vocabulary. | 0.0.1 |  |
|  [**testlib**](library_schemas/testlib) | 2.0.0 | A copy of the HED standard vocabulary<br/> for testing. <br/> (May not be stable.) | 2.0.1 |  |


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

For a more complete view of the process see the [**HED schema development guide**](https://www.hed-resources.org/en/latest/HedSchemaDevelopmentGuide.html).


## Tools to help with HED annotations

The GUI tool [**CTagger**](https://github.com/hed-standard/CTagger) is available to help users with the annotation process. 
CTagger can be used as a standalone application or can be called from EEGLAB via the
[**hedtools plug-in**](https://github.com/hed-standard/hed-matlab) to annotate an EEGLAB dataset/STUDY directly. 
Please refer to the linked repositories for more documentation on how to start HED-tagging using CTagger.


## Web-based HED tools

The current online HED tools include an online validator of spreadsheets (Excel or tsv)
containing HED tags. 
Schema tools are available for validating and converting HED schema specifications between `.mediawiki` and `.xml` formats. 

The released version of the web-based HED tools is located at [**https://hedtools.ucsd.edu/hed**](https://hedtools.ucsd.edu/hed).
The development version of the tools, used to test features before release,
is located at [**https://hedtools.ucsd.edu/hed_dev**](https://hedtools.ucsd.edu/hed_dev).


## HED semantic versioning

HED schema use the following rules for
changing the  *major.minor.patch* semantic version.
These rules are based on the assumption that the [**HED tag**](https://hed-specification.readthedocs.io/en/latest/02_Terminology.html#hed-tag) 
short form will not require data annotators to retag their data for patch-level or minor-version changes of the schema.
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

**Note:** It is an official policy that once in a schema, a node will not be removed.
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


### Mapping HED tags to defined terms in existing ontologies

The following working document describes the origin of the descriptions associated with individual nodes in the HED hierarchy. Many terms appear in the NCIT ontology (National Cancer Institute Thesaurus OBO edition).

> [**Google doc with mapping of HED-3G term descriptions to existing ontology terms**](https://drive.google.com/file/d/13y17OwwNBlHdhB7hguSmOBdxn0Uk4hsI/view?usp=sharing) 
