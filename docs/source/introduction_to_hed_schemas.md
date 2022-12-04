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

## Role of library schemas

**To avoid** uncontrolled expansion of the base HED vocabulary with specialized terminology, 
HED supports the creation of library schema, which are specialized vocabularies that can
be used in conjunction with the base schema to analyze specific aspects of interest.

To use a programming analogy, when programmers write a Python module, the resulting code 
does not become part of the Python language or core library. Instead, the module becomes 
part of a library used in conjunction with core modules of the programming language. 
HED annotations may contain any combination of tags from the standard vocabulary and/or
HED library vocabularies.

Several library schemas are currently under development including the SCORE library
for describing data features of clinical interest (e.g., seizure, sleep stage IV) as
well as schemas for describing features in language structure and video.

Each library schema has its own directory under in the 
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

## The HED community and resources

All HED-related source and documentation repositories are housed on the HED-standard 
organization GitHub site, [https://github.com/hed-standard](https://github.com/hed-standard),
which is maintained by the HED Working Group. HED development is open-source and
community-based. The official HED website [https://www.hedtags.org](https://www.hedtags.org)
for a list of additional resources. 

The HED Working Group invites those interested in HED to contribute to the HED ecosystem and development process.

HED schemas are community-driven. Users can contribute to existing schema or
propose the development of new schema by posting an
[**issue**](https://github.com/hed-standard/hed-schemas/issues) to the 
[**hed-schemas**](https://github.com/hed-standard/hed-schemas) GitHub repository.

The HED discussion forum is:
[https://github.com/hed-standard/hed-schemas/discussions](https://github.com/hed-standard/hed-schemas/discussions) 


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


`````{admonition} **Example:** Proposed specification of library schema in BIDS.

```json
{
    "Name": "A wonderful experiment",
    "BIDSVersion": "1.8.0",
    "HEDVersion": ["8.1.0", "la:testa_1.0.2"]
}
```
`````

The `"la"` library schema is the `./hedxml/HED_libraryA_1.0.2.xml` file found in the
[`hed-schemas`](https://github.com/hed-standard/hed-schemas) GitHub repository.
The specification indicates that annotations using HED tags from this library 
have the `la:` prefix (e.g., `la:XXX`). 
