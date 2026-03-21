## Differences between HED8.4.0 and HED8.5.0

**Tags:**

- Electrical-artifact (Minor): Item Electrical-artifact added
- Localized-channel-artifact (Minor): Item Localized-channel-artifact added
- Omitted-presentation (Minor): Item Omitted-presentation added
- Electrode-pops-artifact (Minor): Tag Electrode-pops-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Electrode-pops-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Localized-channel-artifact/Electrode-pops-artifact
- Induction-artifact (Minor): Tag Induction-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Induction-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Electrical-artifact/Induction-artifact
- Line-noise-artifact (Minor): Tag Line-noise-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Line-noise-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Electrical-artifact/Line-noise-artifact
- Salt-bridge-artifact (Minor): Tag Salt-bridge-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Salt-bridge-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Localized-channel-artifact/Salt-bridge-artifact
- Event (Patch): Attribute annotation modified from ncit:C25499,rdfs:comment Should have this tag in every event process. to None
- Electrode-pops-artifact (Patch): Suggested tag changed on Electrode-pops-artifact from empty to ID
- Salt-bridge-artifact (Patch): Suggested tag changed on Salt-bridge-artifact from empty to ID

**Misc Metadata:**

- header_attributes (Patch): header_attributes changed from {'version': '8.4.0', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'xsi:noNamespaceSchemaLocation': 'https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd', 'unmerged': 'True'} to {'version': '8.5.0', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'xsi:noNamespaceSchemaLocation': 'https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd', 'unmerged': 'True'}

**AnnotationPropertyExternal:**

- ('rdfs:', 'comment') (Minor): Row ('rdfs:', 'comment') missing in first schema
