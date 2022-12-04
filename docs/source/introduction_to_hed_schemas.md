# Introduction to HED schemas

HED (Hierarchical Event Descriptors) is an evolving framework for the description and
formal annotation of events and other information in data.
The HED ecosystem includes a structured vocabulary (specified by a HED schema)
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. 

A **HED schema** is a hierarchically-structured specification of a vocabulary.
The HED ecosystem includes a **standard schema** containing the basic vocabulary
needed for annotation of experimental data as well as specialized **library schemas** for
the additional field-specific terms needed to complete an annotation.

## Scope of HED 

HED allows researchers to annotate what happened during an 
experiment, including experimental stimuli and other sensory events, participant responses 
and actions, experimental design, the role of events in the task, and the temporal structure 
of the experiment. The resulting annotation is machine-actionable, meaning that it can be 
used as input to algorithms without manual intervention. HED facilitates detailed comparisons
of data across studies.

As the name HED implies, much of the HED framework focuses on
associating metadata with the experimental timeline to make datasets analysis-ready and
machine-actionable. However, HED annotations and framework can be used to incorporate 
other types of metadata into analysis by providing a common API (Application Programming 
Interface) for building inter-operable tools. 

## The HED community and resources

All HED-related source and documentation repositories are housed on the HED-standard 
organization GitHub site, [https://github.com/hed-standard](https://github.com/hed-standard),
which is maintained by the HED Working Group. HED development is open-source and
community-based. The official HED website [https://www.hedtags.org](https://www.hedtags.org)
for a list of additional resources. Tg

The HED Working Group invites those interested in HED to contribute to the development process. 
Users are encouraged to use the *Issues* mechanism of the `hed-specification`
repository on the GitHub `hed-standard` working group website: 
[https://github.com/hed-standard/hed-specification/issues](https://github.com/hed-standard/hed-specification/issues)
to ask for help or make suggestions. The HED discussion forum 
[https://github.com/hed-standard/hed-specification/discussions](https://github.com/hed-standard/hed-specification/discussions) is maintained for in depth 
discussions of HED issues and evolution.


## Adding to the vocabulary

The HED vocabulary is organized hierarchically (in a schema) to make it easier for users to 
annotate and search for terms.
Although the users are allowed to extend the schema in most places by adding more specific
tags, expansion should be avoided unless absolutely necessary because only the
terms in the official schema will be shared among users.

The way to add a tag 
Users who wish to add a HED

## Role of library schemas

**To avoid** uncontrolled expansion of the base HED vocabulary with specialized terminology, 
HED supports the creation of library schema, which are specialized vocabularies that can
be used in conjunction with the base schema to analyze specific aspects of interest. 
Experiments in any given subfield can contribute to pressure to add 
overly-specific terms and jargon to the schema hierarchy—for example, adding musical 
terms to tag events in music-based experiments, video markup terms for experiments 
involving movie viewing, traffic terms for experiments involving
virtual driving, and so forth. 

Clinical fields using neuroimaging also have their own specific
vocabularies for describing data features of clinical interest (e.g., seizure, sleep stage IV).
Including these discipline-specific terms quickly makes the base HED schema unwieldy and less
usable by the broader user community.

## HED schemas in BIDS

[BIDS](https://bids.neuroimaging.io/), which stands for Brain Imaging Data Structure,
is a widely-used standard that specifies how neuroimaging data should be organized.
HED is well-integrated into the BIDS standard.

The most common use case (for 99.9% of the HED users) is to use the standard 
HED schema available on GitHub in the `hedxml` directory of the `hed-specification` repository 
([https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml](https://github.com/hed-standard/hed-schemas/tree/main/standard_schema/hedxml)).

Starting with BIDS version 1.8.0, BIDS allows the value associated with the
`"HEDVersion"` key in the `dataset_description.json` file to be a list rather 
than a string expressing the HED version. 

The following example specifies that the annotations in this dataset use HED standard schema
version 8.1.0, along with library schema `testlib` version 1.0.2.
Tags from the `testlib` schema library are to be prefixed with `la:`.


````{admonition} **Example:** Proposed specification of library schema in BIDS.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.8.0",
    "HEDVersion": ["8.1.0", la:testa_1.0.2]
}
```
````

The `"la"` library schema is the `./hedxml/HED_libraryA_1.0.2.xml` file found in the
[`hed-schemas`](https://github.com/hed-standard/hed-schemas) GitHub repository.
The specification indicates that annotations using HED tags from this library 
have the `la:` prefix (e.g., `la:XXX`). 

