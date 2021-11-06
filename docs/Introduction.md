Introduction to HED
This document contains the specification for third generation HED or HED-3G. 
It is meant for the implementers and users of HED tools. Other tutorials and tagging 
guides are available to researchers using HED to annotate their data. 
This document contains the specification for the first official release of HED-3G 
(HED versions 8.0.0-xxx and above.) **When the term HED is used in this document, 
it refers to third generation (HED-3G) unless explicitly stated otherwise.**

The aspects of HED that are described in this document are supported or will soon
be supported by validators and other tools and are available for immediate use by annotators. 
The schema vocabulary can be viewed using an expandable
[schema viewer](https://www.hedtags.org/display_hed.html).

All HED-related source and documentation repositories are housed on the HED-standard 
organization GitHub site, [https://github.com/hed-standard](https://github.com/hed-standard),
which is maintained by the HED Working Group. HED development is open-source and
community-based. Also see the official HED website [https://www.hedtags.org](https://www.hedtags.org)
for a list of additional resources.

The HED Working Group invites those interested in HED to contribute to the development process. 
Users are encouraged to use the *Issues* mechanism of the `hed-specification`
repository on the GitHub `hed-standard` working group website: 
[https://github.com/hed-standard/hed-specification/issues](https://github.com/hed-standard/hed-specification/issues)
to ask for help or make suggestions. The HED discussion forum 
[https://github.com/hed-standard/hed-specification/discussions](https://github.com/hed-standard/hed-specification/discussions) is maintained for in depth 
discussions of HED issues and evolution.

Several other aspects of HED annotation are being planned, but their specification has 
not been fully determined. These aspects are not contained in this specification document, 
but rather are contained in ancillary working documents which are open for discussion. 
These ancillary specifications include the HED working document on 
[spatial annotation](https://docs.google.com/document/u/0/d/1jpSASpWQwOKtan15iQeiYHVewvEeefcBUn1xipNH5-8/edit) 
and the HED working document on 
[task annotation](https://docs.google.com/document/u/0/d/1eGRI_gkYutmwmAl524ezwkX7VwikrLTQa9t8PocQMlU/edit).

## Scope of HED 

HED (an acronym for Hierarchical Event Descriptors) is an evolving framework that facilitates 
the description and formal annotation of events identified in time series data, 
together with tools for validation and for using HED annotations in data search, 
extraction, and analysis. HED allows researchers to annotate what happened during an 
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

To avoid uncontrolled expansion of the base HED vocabulary with specialized terminology, 
HED supports the creation of library schema, which are specialized vocabularies that can
be used in conjunction with the base schema and each other to annotate a variety of specialized
