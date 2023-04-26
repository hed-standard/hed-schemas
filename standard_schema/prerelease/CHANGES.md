## Changes proposed for 8.2.0

* Added the `withStandard` attribute in library schema header to represent the partnered schema. This is first supported for versions >=8.2.0.
* Added the `rooted` schema attribute applied to a top-level node in the library schema with the same node name as a node in the standard partnered schema. The subtree under this library node is placed under its partnered standard schema node when the schemas are merged.
* Added `reserved` schema attribute as per issue #50. Added this attribute to `Definition`, `Def`, `Def-expand`, `Event-context`, `Delay`, `Duration`,`Inset`, `Onset`, and `Offset`.
* Added the `isInherited` schema property to the `Properties`. Added this to schema property to:
`extensionAllowed`, `suggestedTag` and `relatedTag` as per hed-specification issue #428.
* Added `meter` and claimed it as an `SIUnit`. The actual SI unit is `metre`.
* Deprecated `Gentalia` because of misspelling.
* Added `unit` attribute indicating that an element is a unit.
* Added an `elementProperty` indicating that an attribute applies to elements in
any section of the schema.
* Added a `nodeProperty` to indicate that a schema attribute applies to schema nodes. If an attribute has no section property, it is assumed to apply to schema nodes only. However, an attribute may apply to several types of nodes.
* Added a `deprecatedFrom` schema attribute that applies to all types of elements. The value of the attribute is the last version of the schema in which the tag was valid.
* Added `Property/Agent-property/Agent-trait/Race` and `Property/Agent-property/Agent-trait/Ethnicity`.
Did not specify any children or the `takesValue` child. Expect users are going to extend or use a `Label` until
BIDS or another standard specifies details.
* Added `Relation/Logical-relation`, `Relation/Logical-relation/And`, and `Relation/Logical-relation/Or`.
* Updated the descriptions of the major `Relation` subgroups to include idea of focus.
* Added `Relation/Spatial-relation/Left-center-of` and `Relation/Spatial-relation/Right-center-of`
and updated the `relatedTags` of other spatial relationship tags.
* Corrected missing open parenthesis in description for `Relation/Connective-relation/Performed-using`.
* Added an `inLibrary` schema attribute indicating that this term is from a partner library schema in a merged schema. The attribute takes the library name as a value.
* Added `Property/Data-property/Data-marker/Temporal-marker/Inset` as a special tag to mark intermediate points in an ongoing event.