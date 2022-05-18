# Hierarchical Event Descriptors (HED) Schema Library

**The HED library schema are currently under review and subject to change
their official release.**


### HED Library Schema

The individual library schema are located in their own directories under the
`library_schemas` directory. The following table gives links to the `READMEs`
for the individual library schemas, which contain viewers and other information
specific to each schema.

| Library name | Version | Description |
| ------------ | ------- | --------------------------- |
|  [score](library_schemas/score) | 0.0.1   | Library schema based on the SCORE standard for clinical neurological annotation (See [Score docs](https://hed-schema-library.readthedocs.io/en/latest/SCORE_library.html) for additional information.) |
|  [testlib](library_schemas/testlib) | 1.0.1   | A prerelease copy of same schema as HED 8.0.1 for testing. |

**Note:** The website contains both `.mediawiki` and `.xml` versions of the schema.
The schemas are located in the `hedwiki` and `hedxml` subdirectories, respectively,
of the library schema directory.

## HED semantic versioning

HED library schema use the following rules for
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

As modifications to the HED library schema are proposed, they are entered into the
`PROPOSED.md` document for discussion.
Approved changes and corrections are first made in a working version of the
schema that is located in the `prerelease` subdirectory. 
Upon final review, the new HED schema is released and moved to the respective
`hedxml` directory of the respective library schema.
