## Differences between HED8.4.0 and HED8.5.0

**Tags:**

- Consume (Minor): Item Consume added
- Electrical-artifact (Minor): Item Electrical-artifact added
- Localized-channel-artifact (Minor): Item Localized-channel-artifact added
- Cued (Minor): Item Cued added
- Uncued (Minor): Item Uncued added
- Omitted-presentation (Minor): Item Omitted-presentation added
- Electrode-pops-artifact (Minor): Tag Electrode-pops-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Electrode-pops-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Localized-channel-artifact/Electrode-pops-artifact
- Induction-artifact (Minor): Tag Induction-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Induction-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Electrical-artifact/Induction-artifact
- Line-noise-artifact (Minor): Tag Line-noise-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Line-noise-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Electrical-artifact/Line-noise-artifact
- Salt-bridge-artifact (Minor): Tag Salt-bridge-artifact moved in schema from Property/Data-property/Data-artifact/Nonbiological-artifact/Salt-bridge-artifact to Property/Data-property/Data-artifact/Nonbiological-artifact/Localized-channel-artifact/Salt-bridge-artifact
- Event (Patch): Attribute annotation modified from ncit:C25499,rdfs:comment Should have this tag in every event process. to None
- Electrode-pops-artifact (Patch): Suggested tag changed on Electrode-pops-artifact from empty to ID
- Salt-bridge-artifact (Patch): Suggested tag changed on Salt-bridge-artifact from empty to ID

**Units:**

- coulomb (Minor): Item coulomb added
- C (Minor): Item C added
- molar (Minor): Item molar added
- mol-per-L (Minor): Item mol-per-L added
- ampere (Minor): Item ampere added
- A (Minor): Item A added
- joule (Minor): Item joule added
- J (Minor): Item J added
- calorie (Minor): Item calorie added
- newton (Minor): Item newton added
- N (Minor): Item N added
- watt (Minor): Item watt added
- W (Minor): Item W added
- pascal (Minor): Item pascal added
- Pa (Minor): Item Pa added
- mmHg (Minor): Item mmHg added
- ohm (Minor): Item ohm added
- Ohm (Minor): Item Ohm added
- week (Minor): Item week added
- liter (Minor): Item liter added
- litre (Minor): Item litre added
- L (Minor): Item L added
- $ (Patch): Attribute deprecatedFrom modified from None to 8.4.0
- $ (Patch): Description of $ modified
- V (Patch): Attribute conversionFactor modified from 0.000001 to 1000000
- volt (Patch): Attribute conversionFactor modified from 0.000001 to 1000000
- m-per-s^3 (Patch): Attribute SIUnit added
- tesla (Patch): Attribute conversionFactor modified from 10e-15 to 1.0
- T (Patch): Attribute conversionFactor modified from 10e-15 to 1.0
- uV (Unknown): Tag uV deleted from Units

**Unit Classes:**

- electricPotentialUnits (Major): Unit uV removed from electricPotentialUnits
- chargeUnits (Minor): Item chargeUnits added
- concentrationUnits (Minor): Item concentrationUnits added
- currentUnits (Minor): Item currentUnits added
- energyUnits (Minor): Item energyUnits added
- forceUnits (Minor): Item forceUnits added
- powerUnits (Minor): Item powerUnits added
- pressureUnits (Minor): Item pressureUnits added
- resistanceUnits (Minor): Item resistanceUnits added
- accelerationUnits (Patch): Description of accelerationUnits modified
- angleUnits (Patch): Description of angleUnits modified
- areaUnits (Patch): Description of areaUnits modified
- currencyUnits (Patch): Attribute defaultUnits modified from $ to dollar
- electricPotentialUnits (Patch): Description of electricPotentialUnits modified
- frequencyUnits (Patch): Description of frequencyUnits modified
- intensityUnits (Patch): Description of intensityUnits modified
- jerkUnits (Patch): Description of jerkUnits modified
- magneticFieldUnits (Patch): Description of magneticFieldUnits modified
- memorySizeUnits (Patch): Description of memorySizeUnits modified
- physicalLengthUnits (Patch): Description of physicalLengthUnits modified
- speedUnits (Patch): Description of speedUnits modified
- temperatureUnits (Patch): Description of temperatureUnits modified
- timeUnits (Patch): Unit week added to timeUnits
- timeUnits (Patch): Description of timeUnits modified
- volumeUnits (Patch): Unit liter added to volumeUnits
- volumeUnits (Patch): Unit litre added to volumeUnits
- volumeUnits (Patch): Unit L added to volumeUnits
- volumeUnits (Patch): Description of volumeUnits modified
- weightUnits (Patch): Description of weightUnits modified

**Unit Modifiers:**

- deca (Patch): Description of deca modified
- da (Patch): Description of da modified
- hecto (Patch): Description of hecto modified
- h (Patch): Description of h modified
- kilo (Patch): Description of kilo modified
- k (Patch): Description of k modified
- mega (Patch): Attribute conversionFactor modified from 10e6 to 1e6
- mega (Patch): Description of mega modified
- M (Patch): Attribute conversionFactor modified from 10e6 to 1e6
- M (Patch): Description of M modified
- giga (Patch): Attribute conversionFactor modified from 10e9 to 1e9
- giga (Patch): Description of giga modified
- G (Patch): Attribute conversionFactor modified from 10e9 to 1e9
- G (Patch): Description of G modified
- tera (Patch): Attribute conversionFactor modified from 10e12 to 1e12
- tera (Patch): Description of tera modified
- T (Patch): Attribute conversionFactor modified from 10e12 to 1e12
- T (Patch): Description of T modified
- peta (Patch): Attribute conversionFactor modified from 10e15 to 1e15
- peta (Patch): Description of peta modified
- P (Patch): Attribute conversionFactor modified from 10e15 to 1e15
- P (Patch): Description of P modified
- exa (Patch): Attribute conversionFactor modified from 10e18 to 1e18
- exa (Patch): Description of exa modified
- E (Patch): Attribute conversionFactor modified from 10e18 to 1e18
- E (Patch): Description of E modified
- zetta (Patch): Attribute conversionFactor modified from 10e21 to 1e21
- zetta (Patch): Description of zetta modified
- Z (Patch): Attribute conversionFactor modified from 10e21 to 1e21
- Z (Patch): Description of Z modified
- yotta (Patch): Attribute conversionFactor modified from 10e24 to 1e24
- yotta (Patch): Description of yotta modified
- Y (Patch): Attribute conversionFactor modified from 10e24 to 1e24
- Y (Patch): Description of Y modified
- deci (Patch): Description of deci modified
- d (Patch): Description of d modified
- centi (Patch): Description of centi modified
- c (Patch): Description of c modified
- milli (Patch): Description of milli modified
- m (Patch): Description of m modified
- micro (Patch): Attribute conversionFactor modified from 10e-6 to 1e-6
- micro (Patch): Description of micro modified
- u (Patch): Attribute conversionFactor modified from 10e-6 to 1e-6
- u (Patch): Description of u modified
- nano (Patch): Attribute conversionFactor modified from 10e-9 to 1e-9
- nano (Patch): Description of nano modified
- n (Patch): Attribute conversionFactor modified from 10e-9 to 1e-9
- n (Patch): Description of n modified
- pico (Patch): Attribute conversionFactor modified from 10e-12 to 1e-12
- pico (Patch): Description of pico modified
- p (Patch): Attribute conversionFactor modified from 10e-12 to 1e-12
- p (Patch): Description of p modified
- femto (Patch): Attribute conversionFactor modified from 10e-15 to 1e-15
- femto (Patch): Description of femto modified
- f (Patch): Attribute conversionFactor modified from 10e-15 to 1e-15
- f (Patch): Description of f modified
- atto (Patch): Attribute conversionFactor modified from 10e-18 to 1e-18
- atto (Patch): Description of atto modified
- a (Patch): Attribute conversionFactor modified from 10e-18 to 1e-18
- a (Patch): Description of a modified
- zepto (Patch): Attribute conversionFactor modified from 10e-21 to 1e-21
- zepto (Patch): Description of zepto modified
- z (Patch): Attribute conversionFactor modified from 10e-21 to 1e-21
- z (Patch): Description of z modified
- yocto (Patch): Attribute conversionFactor modified from 10e-24 to 1e-24
- yocto (Patch): Description of yocto modified
- y (Patch): Attribute conversionFactor modified from 10e-24 to 1e-24
- y (Patch): Description of y modified

**Attributes:**

- unitPrefix (Patch): Attribute deprecatedFrom modified from None to 8.4.0
- unitPrefix (Patch): Description of unitPrefix modified

**Misc Metadata:**

- header_attributes (Patch): header_attributes changed from {'version': '8.4.0', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'xsi:noNamespaceSchemaLocation': 'https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd', 'unmerged': 'True'} to {'version': '8.5.0', 'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance', 'xsi:noNamespaceSchemaLocation': 'https://raw.githubusercontent.com/hed-standard/hed-schemas/refs/heads/main/standard_schema/hedxml/HED8.4.0.xsd', 'unmerged': 'True'}
- prologue (Patch): prologue changed

**Prefixes:**

- xml: (Patch): Row xml: columns differ: description

**AnnotationPropertyExternal:**

- ('rdfs:', 'comment') (Minor): Row ('rdfs:', 'comment') missing in first schema
