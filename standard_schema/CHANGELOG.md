
# CHANGELOG for HED schema

## Changes for HED 8.2.0 Released 4/28/2023

* Added the `withStandard` attribute in library schema header to represent the partnered schema. This is first supported for versions >=8.2.0.
* Added the `rooted` schema attribute applied to a top-level node in the library schema with the same node name as a node in the standard partnered schema. The subtree under this library node is placed under its partnered standard schema node when the schemas are merged.
* Added `reserved` schema attribute as per issue #50. Added this attribute to `Definition`, `Def`, `Def-expand`, `Event-context`, `Delay`, `Duration`,`Inset`, `Onset`, and `Offset`.
* Added the `isInheritedProperty` schema property to the `Properties`. Added this to schema property to:
`extensionAllowed`, `suggestedTag` and `relatedTag` as per hed-specification issue #428.
* Added `meter` and claimed it as an `SIUnit`. The actual SI unit is `metre`.
* Deprecated `Gentalia` because of misspelling.
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

## Changes for HED 8.1.0 Released 5/23/2022

* `{suggestedTag=Attribute/Sensory}` changed to `{suggestedTag=Sensory-presentation}` (correction).
* `{suggestedTag=Attribute/Sensory}` changed to `{suggestedTag=Sensory-presentation}` (correction).
* `Fraction`: betwee spelling error corrected in description (correction). 
* `Parameter-label`: the `valueClass` changed from `labelClass` to `nameClass` (correction).
* `Timbre`: the `valueClass` changed from `labelClass` to `nameClass` (correction).
* `HSV-value`: the AAttribute spelling error corrected in description (correction).
* Changed `#<nowiki>` to `<nowiki>#` in all places (correction).
* `Opacity`: Fixed `</nowiki>` closing tag (correction).
* `Read`: Changed `</nowki>` closing tag to `</nowiki>` (correction).
* `Plant`: Fixed `</nowiki>` closing tag (correction).
* `{relatedTag=Incorrect}` changed to `{relatedTag=Wrong}` (correction).
* `Incidental`: Clarified the description (clarification).
* Moved `unitClass` designation for `Angle` tag to `#` (correction).
* Added `extensionAllowed` to the `Relation` tag (correction).
* Added `valueClass=numericClass` to `#` tags of `Screen-resolution`, `Sensory-resolution`, `Spatial-resolution`, `Spectral-resolution`, `Temporal-resolution` (improvement).
* Corrected many descriptions of many tags in the `Relation` subtree (correction).
* Added tag `Relation/Connective-relation/Includes` in order to allow symmetric treatment with
 `Contained-in` (tag addition).
* Added `Relation/Connective-relation/Performed-using` (tag addition).
* Added `Relation/Connective-relation/Unrelated-to` (tag addition).
* Added `Property/Data-property/Data-value/Quantitative-value/Item-index/#` to allow identification of position of steps within groups (tag addition).
* Added `Property/Task-property/Task-action-type/Done-indication` and `Property/Task-property/Task-action-type/Ready-indication` used to characterize transition actions (tag addition).
* Added "A tag group can have at most one tag with this attribute." to the description of the `TopLevelTagGroup` schema attribute (clarification).
* Added `Property/Data-property/Data-marker/Data-break-marker` to indicate a break in the data (tag addition).
* Added `Item/Anatomical-item/Body` to allow relationships to be better specified (tag addition).
* Added `Property/Agent-property/Agent-cognitive-state/Distracted` (tag addition).
* Added `Item/Object/Man-made-object/Document/Questionnaire` to cover surveys (tag addition).
* Added `conversionFactor` schema attribute and added the conversion factors to the units and the unit modifiers (enhancement).
* Added `Item/Object/Man-made-object/Geometric-object/2D-shape/Arrow` (tag addition).
* Added `Property/Data-property/Data-value/Physical-value/Temperature` and added the unit class `temperatureUnits` (tag addition).
* Added `Property/Sensory-property/Sensory-attribute/Auditory-attribute/Sound-volume` (tag addition).
* Added `Property/Data-property/Data-value/Categorical-value/Categorical-level-value/Large`
and `Property/Data-property/Data-value/Categorical-value/Categorical-level-value/Small`.
* Corrected some descriptions for items under `Categorical-level-value`.
* Added `electricPotentialUnits` and `magneticFieldUnits` for EEG and MEG signals respectively.
* Small punctuation corrections.
