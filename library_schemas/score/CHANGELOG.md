# CHANGELOG for HED score library schema


## Minor release score 2.1.0 June 9, 2025.
This is a minor release of the HED score library schema. It includes changes to the schema and tags, as well as updates to the documentation. 
The changes are backward compatible with previous version of the schema.

- The annotations have been moved to a schema attribute to allow programmatic linking to other ontologies.
- The MEDIAWIKI and XML formats are now completely equivalent to the tsv version.
- The schema is partnered with HED schema version 8.4.0.

**Tags:**
 - Building-part (Minor): Item Building-part added
 - Door (Minor): Item Door added
 - Window (Minor): Item Window added
 - Attic (Minor): Tag Attic moved in schema from Item/Object/Man-made-object/Building/Attic to Item/Object/Man-made-object/Building-part/Attic
 - Basement (Minor): Tag Basement moved in schema from Item/Object/Man-made-object/Building/Basement to Item/Object/Man-made-object/Building-part/Basement
 - Entrance (Minor): Tag Entrance moved in schema from Item/Object/Man-made-object/Building/Entrance to Item/Object/Man-made-object/Building-part/Entrance
 - Roof (Minor): Tag Roof moved in schema from Item/Object/Man-made-object/Building/Roof to Item/Object/Man-made-object/Building-part/Roof
 - Room (Minor): Tag Room moved in schema from Item/Object/Man-made-object/Building/Room to Item/Object/Man-made-object/Building-part/Room
 - Screen-window (Minor): Tag Screen-window moved in schema from Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Computer-screen/Screen-window to Item/Object/Man-made-object/Device/IO-device/Output-device/Display-device/Screen-window
 - Sampling-rate (Minor): Value class numericClass added to Sampling-rate
 - Cue (Minor): Tag Cue moved in schema from Property/Task-property/Task-stimulus-role/Cue to Property/Task-property/Task-event-role/Cue
 - Feedback (Minor): Tag Feedback moved in schema from Property/Task-property/Task-stimulus-role/Feedback to Property/Task-property/Task-event-role/Feedback
 - Sleep-modulator (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 7 and Table 2
 - Sleep-modulator (Patch): Description of Sleep-modulator modified
 - Hyperventilation (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 2.
 - Hyperventilation (Patch): Description of Hyperventilation modified
 - Background-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 2.
 - Background-activity (Patch): Description of Background-activity modified
 - Posterior-dominant-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2,dc:source suggested tags from Beniczky ea 2017 Table 4.
 - Posterior-dominant-rhythm (Patch): Description of Posterior-dominant-rhythm modified
 - Mu-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2.
 - Mu-rhythm (Patch): Description of Mu-rhythm modified
 - Background-activity-special-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6
 - Background-activity-special-feature (Patch): Description of Background-activity-special-feature modified
 - Continuous-background-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6.
 - Continuous-background-activity (Patch): Description of Continuous-background-activity modified
 - Nearly-continuous-background-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6.
 - Nearly-continuous-background-activity (Patch): Description of Nearly-continuous-background-activity modified
 - Discontinuous-background-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6.
 - Discontinuous-background-activity (Patch): Description of Discontinuous-background-activity modified
 - Background-burst-suppression (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2,dc:source Beniczky ea 2017 Section 6.
 - Background-burst-suppression (Patch): Description of Background-burst-suppression modified
 - Background-burst-attenuation (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6.
 - Background-burst-attenuation (Patch): Description of Background-burst-attenuation modified
 - Background-activity-suppression (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2,dc:source Beniczky ea 2017 Section 6.
 - Background-activity-suppression (Patch): Description of Background-activity-suppression modified
 - Electrocerebral-inactivity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2,dc:source Beniczky ea 2017 Section 6.
 - Electrocerebral-inactivity (Patch): Description of Electrocerebral-inactivity modified
 - Critically-ill-patient-patterns (Patch): Attribute annotation modified from None to dc:source Hirsch ea 2013,dc:source Beniczky ea 2017 Section 9.
 - Critically-ill-patient-patterns (Patch): Description of Critically-ill-patient-patterns modified
 - Critically-ill-patient-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Hirsch ea 2013,dc:source Suggested tags from Beniczky ea 2017 Table 8.
 - Critically-ill-patient-periodic-discharges (Patch): Description of Critically-ill-patient-periodic-discharges modified
 - Rhythmic-delta-activity (Patch): Attribute annotation modified from None to dc:source Hirsch ea 2013,dc:source Suggested tags from Beniczky ea 2017 Table 8.
 - Rhythmic-delta-activity (Patch): Description of Rhythmic-delta-activity modified
 - Spike-or-sharp-and-wave (Patch): Attribute annotation modified from None to dc:source Hirsch ea 2013,dc:source Suggested tags from Beniczky ea 2017 Table 8.
 - Spike-or-sharp-and-wave (Patch): Description of Spike-or-sharp-and-wave modified
 - Episode (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S1.
 - Episode (Patch): Description of Episode modified
 - Epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9 Supplement 1,dc:source Selection-tree and list of seizure-types according to the current ILAE seizure classification Fisher ea 2017.
 - Epileptic-seizure (Patch): Description of Epileptic-seizure modified
 - Focal-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2 and Key Points,dc:source Suggested tags from Fisher ea 2017 Figure 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code I.
 - Focal-onset-epileptic-seizure (Patch): Description of Focal-onset-epileptic-seizure modified
 - Aware-focal-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2 and Key Points,dc:source Suggested tags from Fisher ea 2017 Figure 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code I.
 - Aware-focal-onset-epileptic-seizure (Patch): Description of Aware-focal-onset-epileptic-seizure modified
 - Impaired-awareness-focal-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code I.B.
 - Impaired-awareness-focal-onset-epileptic-seizure (Patch): Description of Impaired-awareness-focal-onset-epileptic-seizure modified
 - Awareness-unknown-focal-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code I.C.
 - Awareness-unknown-focal-onset-epileptic-seizure (Patch): Description of Awareness-unknown-focal-onset-epileptic-seizure modified
 - Focal-to-bilateral-tonic-clonic-focal-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code I.D.01.
 - Focal-to-bilateral-tonic-clonic-focal-onset-epileptic-seizure (Patch): Description of Focal-to-bilateral-tonic-clonic-focal-onset-epileptic-seizure modified
 - Generalized-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2 and Key Points,dc:source Suggested tags from Fisher ea 2017 Figure 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code II.
 - Generalized-onset-epileptic-seizure (Patch): Description of Generalized-onset-epileptic-seizure modified
 - Unknown-onset-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 page 532,dc:source Suggested tags from Fisher ea 2017 Figure 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code III.
 - Unknown-onset-epileptic-seizure (Patch): Description of Unknown-onset-epileptic-seizure modified
 - Unclassified-epileptic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Beniczky ea 2017 Supplement 1,dc:source ILAE seizure classification code III.C.01.
 - Unclassified-epileptic-seizure (Patch): Description of Unclassified-epileptic-seizure modified
 - Electroencephalographic-seizure (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S5,dc:source Beniczky ea 2017 Table 9.
 - Electroencephalographic-seizure (Patch): Description of Electroencephalographic-seizure modified
 - Seizure-PNES (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S5,dc:source Beniczky ea 2017 Table 9.
 - Seizure-PNES (Patch): Description of Seizure-PNES modified
 - Sleep-related-episode (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9.
 - Sleep-related-episode (Patch): Description of Sleep-related-episode modified
 - Sleep-related-arousal (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9.
 - Sleep-related-arousal (Patch): Description of Sleep-related-arousal modified
 - Benign-sleep-myoclonus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5.
 - Benign-sleep-myoclonus (Patch): Description of Benign-sleep-myoclonus modified
 - Confusional-arousal (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5.
 - Confusional-arousal (Patch): Description of Confusional-arousal modified
 - Cataplexy (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5.
 - Cataplexy (Patch): Description of Cataplexy modified
 - Sleep-periodic-limb-movement (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Sleep-periodic-limb-movement (Patch): Description of Sleep-periodic-limb-movement modified
 - REM-sleep-behavioral-disorder (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5.
 - REM-sleep-behavioral-disorder (Patch): Description of REM-sleep-behavioral-disorder modified
 - Sleep-walking (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Sleep-walking (Patch): Description of Sleep-walking modified
 - Pediatric-episode (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9.
 - Pediatric-episode (Patch): Description of Pediatric-episode modified
 - Hyperekplexia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Hyperekplexia (Patch): Description of Hyperekplexia modified
 - Jactatio-capitis-nocturna (Patch): Description of Jactatio-capitis-nocturna modified
 - Pavor-nocturnus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Pavor-nocturnus (Patch): Description of Pavor-nocturnus modified
 - Pediatric-stereotypical-behavior-episode (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Pediatric-stereotypical-behavior-episode (Patch): Description of Pediatric-stereotypical-behavior-episode modified
 - Paroxysmal-motor-event (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Paroxysmal-motor-event (Patch): Description of Paroxysmal-motor-event modified
 - Syncope (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 9,dc:source Beniczky ea 2013 Appendix S5
 - Syncope (Patch): Description of Syncope modified
 - Signal-morphology-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5 Table 8 Table 12
 - Signal-morphology-property (Patch): Description of Signal-morphology-property modified
 - Rhythmic-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5 Table 12 Table 14
 - Rhythmic-property (Patch): Description of Rhythmic-property modified
 - Gamma-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Beniczky ea 2013 Appendix S4
 - Temporal-intermittent-rhythmic-delta-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Beniczky ea 2013 Appendix S4
 - RPP-morphology (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-morphology (Patch): Description of RPP-morphology modified
 - RPP-with-superimposed-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-with-superimposed-activity (Patch): Description of RPP-with-superimposed-activity modified
 - RPP-sharpness (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-sharpness (Patch): Description of RPP-sharpness modified
 - RPP-spiky (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-spiky (Patch): Description of RPP-spiky modified
 - RPP-sharp (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-sharp (Patch): Description of RPP-sharp modified
 - RPP-sharply-contoured (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-sharply-contoured (Patch): Description of RPP-sharply-contoured modified
 - RPP-blunt (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-blunt (Patch): Description of RPP-blunt modified
 - Triphasic-morphology (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Triphasic-morphology (Patch): Description of Triphasic-morphology modified
 - RPP-relative-amplitude (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-relative-amplitude (Patch): Description of RPP-relative-amplitude modified
 - RPP-polarity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-polarity (Patch): Description of RPP-polarity modified
 - Location-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 8 and Section 10
 - Location-property (Patch): Description of Location-property modified
 - Modulators-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 10
 - Modulators-property (Patch): Description of Modulators-property modified
 - Facilitating-factor (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013
 - Facilitating-factor (Patch): Description of Facilitating-factor modified
 - Provocative-factor (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013
 - Provocative-factor (Patch): Description of Provocative-factor modified
 - Intermittent-photic-stimulation-effect (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017
 - Intermittent-photic-stimulation-effect (Patch): Description of Intermittent-photic-stimulation-effect modified
 - Posterior-stimulus-dependent-response (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Posterior-stimulus-dependent-response (Patch): Description of Posterior-stimulus-dependent-response modified
 - Posterior-stimulus-independent-response-limited (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Posterior-stimulus-independent-response-limited (Patch): Description of Posterior-stimulus-independent-response-limited modified
 - Posterior-stimulus-independent-response-self-sustained (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Posterior-stimulus-independent-response-self-sustained (Patch): Description of Posterior-stimulus-independent-response-self-sustained modified
 - Generalized-photoparoxysmal-response-limited (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Generalized-photoparoxysmal-response-limited (Patch): Description of Generalized-photoparoxysmal-response-limited modified
 - Generalized-photoparoxysmal-response-self-sustained (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Generalized-photoparoxysmal-response-self-sustained (Patch): Description of Generalized-photoparoxysmal-response-self-sustained modified
 - Activation-of-pre-existing-epileptogenic-area (Patch): Attribute annotation modified from None to dc:source Trenite ea 2001,dc:source Beniczky ea 2017 Table 7
 - Activation-of-pre-existing-epileptogenic-area (Patch): Description of Activation-of-pre-existing-epileptogenic-area modified
 - Time-related-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 Table 8
 - Time-related-property (Patch): Description of Time-related-property modified
 - Discharge-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6,dc:source Beniczky ea 2013 Appendix 4
 - Discharge-pattern (Patch): Description of Discharge-pattern modified
 - Single-discharge (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6,dc:source Beniczky ea 2013 Appendix 4
 - Single-discharge (Patch): Description of Single-discharge modified
 - Rhythmic-trains-or-bursts (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6,dc:source Beniczky ea 2013 Appendix 4
 - Rhythmic-trains-or-bursts (Patch): Description of Rhythmic-trains-or-bursts modified
 - Arrhythmic-trains-or-bursts (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6,dc:source Beniczky ea 2013 Appendix 4
 - Arrhythmic-trains-or-bursts (Patch): Description of Arrhythmic-trains-or-bursts modified
 - Fragmented-discharge (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Fragmented-discharge (Patch): Description of Fragmented-discharge modified
 - RPP-time-related-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-time-related-feature (Patch): Description of RPP-time-related-feature modified
 - RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-duration (Patch): Description of RPP-duration modified
 - Very-brief-RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Very-brief-RPP-duration (Patch): Description of Very-brief-RPP-duration modified
 - Brief-RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Brief-RPP-duration (Patch): Description of Brief-RPP-duration modified
 - Intermediate-RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Intermediate-RPP-duration (Patch): Description of Intermediate-RPP-duration modified
 - Long-RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Long-RPP-duration (Patch): Description of Long-RPP-duration modified
 - Very-long-RPP-duration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Very-long-RPP-duration (Patch): Description of Very-long-RPP-duration modified
 - RPP-onset (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-onset (Patch): Description of RPP-onset modified
 - Sudden-RPP-onset (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Sudden-RPP-onset (Patch): Description of Sudden-RPP-onset modified
 - Gradual-RPP-onset (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - Gradual-RPP-onset (Patch): Description of Gradual-RPP-onset modified
 - RPP-dynamics (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 8
 - RPP-dynamics (Patch): Description of RPP-dynamics modified
 - Static-RPP-dynamics (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 8 and Table 6
 - Feature-incidence (Patch): Description of Feature-incidence modified
 - One-time-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - One-time-incidence (Patch): Description of One-time-incidence modified
 - Rare-feature-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Rare-feature-incidence (Patch): Description of Rare-feature-incidence modified
 - Uncommon-feature-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Uncommon-feature-incidence (Patch): Description of Uncommon-feature-incidence modified
 - Occasional-feature-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Occasional-feature-incidence (Patch): Description of Occasional-feature-incidence modified
 - Frequent-feature-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Frequent-feature-incidence (Patch): Description of Frequent-feature-incidence modified
 - Abundant-feature-incidence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6
 - Feature-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 8 Table 6 Table 8
 - Feature-prevalence (Patch): Description of Feature-prevalence modified
 - Rare-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 and Table 8
 - Rare-prevalence (Patch): Description of Rare-prevalence modified
 - Occasional-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 and Table 8
 - Occasional-prevalence (Patch): Description of Occasional-prevalence modified
 - Frequent-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 and Table
 - Frequent-prevalence (Patch): Description of Frequent-prevalence modified
 - Abundant-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 and Table 8
 - Abundant-prevalence (Patch): Description of Abundant-prevalence modified
 - Continuous-prevalence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 6 and Table 8
 - Continuous-prevalence (Patch): Description of Continuous-prevalence modified
 - Posterior-dominant-rhythm-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 6 and Table 4
 - Posterior-dominant-rhythm-property (Patch): Description of Posterior-dominant-rhythm-property modified
 - Posterior-dominant-rhythm-amplitude-range (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-amplitude-range (Patch): Description of Posterior-dominant-rhythm-amplitude-range modified
 - Posterior-dominant-rhythm-eye-opening-reactivity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S2,dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-eye-opening-reactivity (Patch): Description of Posterior-dominant-rhythm-eye-opening-reactivity modified
 - Posterior-dominant-rhythm-organization (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-organization (Patch): Description of Posterior-dominant-rhythm-organization modified
 - Posterior-dominant-rhythm-organization-poorly-organized (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-organization-poorly-organized (Patch): Description of Posterior-dominant-rhythm-organization-poorly-organized modified
 - Posterior-dominant-rhythm-organization-disorganized (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-organization-disorganized (Patch): Description of Posterior-dominant-rhythm-organization-disorganized modified
 - Posterior-dominant-rhythm-organization-markedly-disorganized (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-organization-markedly-disorganized (Patch): Description of Posterior-dominant-rhythm-organization-markedly-disorganized modified
 - Posterior-dominant-rhythm-caveat (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Posterior-dominant-rhythm-caveat (Patch): Description of Posterior-dominant-rhythm-caveat modified
 - Absence-of-posterior-dominant-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Absence-of-posterior-dominant-rhythm (Patch): Description of Absence-of-posterior-dominant-rhythm modified
 - Absence-of-posterior-dominant-rhythm-extreme-low-voltage (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Absence-of-posterior-dominant-rhythm-extreme-low-voltage (Patch): Description of Absence-of-posterior-dominant-rhythm-extreme-low-voltage modified
 - Absence-of-posterior-dominant-rhythm-eye-closure-could-not-be-achieved (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Absence-of-posterior-dominant-rhythm-eye-closure-could-not-be-achieved (Patch): Description of Absence-of-posterior-dominant-rhythm-eye-closure-could-not-be-achieved modified
 - Absence-of-posterior-dominant-rhythm-lack-of-compliance (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 4
 - Absence-of-posterior-dominant-rhythm-lack-of-compliance (Patch): Description of Absence-of-posterior-dominant-rhythm-lack-of-compliance modified
 - Seizure-classification (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017,dc:source Beniczky ea 2017
 - Seizure-classification (Patch): Description of Seizure-classification modified
 - Myoclonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Duration tag from Beniczky ea Table 13
 - Myoclonic-seizure (Patch): Description of Myoclonic-seizure modified
 - Negative-myoclonic-seizure (Patch): Description of Negative-myoclonic-seizure modified
 - Motor-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Duration tag from Beniczky ea Table 13
 - Motor-seizure (Patch): Description of Motor-seizure modified
 - Clonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Clonic-seizure (Patch): Description of Clonic-seizure modified
 - Tonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Tonic-seizure (Patch): Description of Tonic-seizure modified
 - Atonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Atonic-seizure (Patch): Description of Atonic-seizure modified
 - Myoclonic-atonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Myoclonic-atonic-seizure (Patch): Description of Myoclonic-atonic-seizure modified
 - Myoclonic-tonic-clonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Myoclonic-tonic-clonic-seizure (Patch): Description of Myoclonic-tonic-clonic-seizure modified
 - Tonic-clonic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Tonic-clonic-seizure (Patch): Description of Tonic-clonic-seizure modified
 - Automatism-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Automatism-seizure (Patch): Description of Automatism-seizure modified
 - Hyperkinetic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Hyperkinetic-seizure (Patch): Description of Hyperkinetic-seizure modified
 - Epileptic-spasm (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Epileptic-spasm (Patch): Description of Epileptic-spasm modified
 - Nonmotor-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Duration tag from Beniczky ea Table 13
 - Nonmotor-seizure (Patch): Description of Nonmotor-seizure modified
 - Behavior-arrest-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017
 - Behavior-arrest-seizure (Patch): Description of Behavior-arrest-seizure modified
 - Sensory-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Sensory-seizure (Patch): Description of Sensory-seizure modified
 - Emotional-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Emotional-seizure (Patch): Description of Emotional-seizure modified
 - Cognitive-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Cognitive-seizure (Patch): Description of Cognitive-seizure modified
 - Autonomic-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Autonomic-seizure (Patch): Description of Autonomic-seizure modified
 - Absence-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2,dc:source Duration tag from Beniczky ea Table 13
 - Absence-seizure (Patch): Description of Absence-seizure modified
 - Typical-absence-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Typical-absence-seizure (Patch): Description of Typical-absence-seizure modified
 - Atypical-absence-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Atypical-absence-seizure (Patch): Description of Atypical-absence-seizure modified
 - Myoclonic-absence-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 page 536
 - Myoclonic-absence-seizure (Patch): Description of Myoclonic-absence-seizure modified
 - Eyelid-myoclonia-seizure (Patch): Attribute annotation modified from None to dc:source Fisher ea 2017 Table 2
 - Eyelid-myoclonia-seizure (Patch): Description of Eyelid-myoclonia-seizure modified
 - Seizure-semiology (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 10,dc:source Duration tag from Beniczky ea Table 13
 - Seizure-semiology (Patch): Description of Seizure-semiology modified
 - Semiology-motor-behavioral-arrest (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-motor-behavioral-arrest (Patch): Description of Semiology-motor-behavioral-arrest modified
 - Semiology-dyscognitive (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-dyscognitive (Patch): Description of Semiology-dyscognitive modified
 - Semiology-elementary-motor (Patch): Attribute annotation modified from None to dc:source Blume ea 2001 1.1,dc:source Beniczky ea 2017 Table 10
 - Semiology-elementary-motor (Patch): Description of Semiology-elementary-motor modified
 - Semiology-myoclonic-jerk (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-myoclonic-jerk (Patch): Description of Semiology-myoclonic-jerk modified
 - Semiology-negative-myoclonus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-negative-myoclonus (Patch): Description of Semiology-negative-myoclonus modified
 - Semiology-clonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-clonic (Patch): Description of Semiology-clonic modified
 - Semiology-jacksonian-march (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-jacksonian-march (Patch): Description of Semiology-jacksonian-march modified
 - Semiology-epileptic-spasm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-epileptic-spasm (Patch): Description of Semiology-epileptic-spasm modified
 - Semiology-tonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-tonic (Patch): Description of Semiology-tonic modified
 - Semiology-dystonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-dystonic (Patch): Description of Semiology-dystonic modified
 - Semiology-postural (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-postural (Patch): Description of Semiology-postural modified
 - Semiology-versive (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-versive (Patch): Description of Semiology-versive modified
 - Semiology-tonic-clonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-tonic-clonic (Patch): Description of Semiology-tonic-clonic modified
 - Semiology-tonic-clonic-without-figure-of-four (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-tonic-clonic-without-figure-of-four (Patch): Description of Semiology-tonic-clonic-without-figure-of-four modified
 - Semiology-tonic-clonic-with-figure-of-four-extension-left-elbow (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-tonic-clonic-with-figure-of-four-extension-left-elbow (Patch): Description of Semiology-tonic-clonic-with-figure-of-four-extension-left-elbow modified
 - Semiology-tonic-clonic-with-figure-of-four-extension-right-elbow (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-tonic-clonic-with-figure-of-four-extension-right-elbow (Patch): Description of Semiology-tonic-clonic-with-figure-of-four-extension-right-elbow modified
 - Semiology-astatic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-astatic (Patch): Description of Semiology-astatic modified
 - Semiology-atonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-atonic (Patch): Description of Semiology-atonic modified
 - Semiology-eye-blinking (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10.
 - Semiology-eye-blinking (Patch): Description of Semiology-eye-blinking modified
 - Semiology-automatisms (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Fisher ea 2017 Table 2
 - Semiology-automatisms (Patch): Description of Semiology-automatisms modified
 - Semiology-mimetic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-mimetic (Patch): Description of Semiology-mimetic modified
 - Semiology-oroalimentary (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-oroalimentary (Patch): Description of Semiology-oroalimentary modified
 - Semiology-dacrystic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-dacrystic (Patch): Description of Semiology-dacrystic modified
 - Semiology-manual (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source  Beniczky ea 2013 Appendix S5
 - Semiology-manual (Patch): Description of Semiology-manual modified
 - Semiology-gestural (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-gestural (Patch): Description of Semiology-gestural modified
 - Semiology-hypermotor (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-hypermotor (Patch): Description of Semiology-hypermotor modified
 - Semiology-hypokinetic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-hypokinetic (Patch): Description of Semiology-hypokinetic modified
 - Semiology-gelastic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-gelastic (Patch): Description of Semiology-gelastic modified
 - Semiology-sensory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Blume ea 2001 2.2
 - Semiology-sensory (Patch): Description of Semiology-sensory modified
 - Semiology-headache (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-headache (Patch): Description of Semiology-headache modified
 - Semiology-visual (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-visual (Patch): Description of Semiology-visual modified
 - Semiology-auditory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-auditory (Patch): Description of Semiology-auditory modified
 - Semiology-olfactory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10
 - Semiology-olfactory (Patch): Description of Semiology-olfactory modified
 - Semiology-gustatory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-gustatory (Patch): Description of Semiology-gustatory modified
 - Semiology-epigastric (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-epigastric (Patch): Description of Semiology-epigastric modified
 - Semiology-somatosensory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-somatosensory (Patch): Description of Semiology-somatosensory modified
 - Semiology-autonomic-sensation (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5,dc:source Blume ea 2001 2.2.1.8
 - Semiology-autonomic-sensation (Patch): Description of Semiology-autonomic-sensation modified
 - Semiology-experiential (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Blume ea 2001 2.2.2
 - Semiology-experiential (Patch): Description of Semiology-experiential modified
 - Semiology-affective-emotional (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-affective-emotional (Patch): Description of Semiology-affective-emotional modified
 - Semiology-hallucinatory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-hallucinatory (Patch): Description of Semiology-hallucinatory modified
 - Semiology-illusory (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-illusory (Patch): Description of Semiology-illusory modified
 - Semiology-mnemonic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-mnemonic (Patch): Description of Semiology-mnemonic modified
 - Semiology-language (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10
 - Semiology-language (Patch): Description of Semiology-language modified
 - Semiology-vocalization (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-vocalization (Patch): Description of Semiology-vocalization modified
 - Semiology-verbalization (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-verbalization (Patch): Description of Semiology-verbalization modified
 - Semiology-dysphasia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-dysphasia (Patch): Description of Semiology-dysphasia modified
 - Semiology-aphasia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-aphasia (Patch): Description of Semiology-aphasia modified
 - Semiology-autonomic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Blume ea 2001 3.2
 - Semiology-autonomic (Patch): Description of Semiology-autonomic modified
 - Semiology-pupillary (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-pupillary (Patch): Description of Semiology-pupillary modified
 - Semiology-hypersalivation (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-hypersalivation (Patch): Description of Semiology-hypersalivation modified
 - Semiology-respiratory-apnoeic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-respiratory-apnoeic (Patch): Description of Semiology-respiratory-apnoeic modified
 - Semiology-cardiovascular (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-cardiovascular (Patch): Description of Semiology-cardiovascular modified
 - Semiology-gastrointestinal (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-gastrointestinal (Patch): Description of Semiology-gastrointestinal modified
 - Semiology-urinary-incontinence (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-urinary-incontinence (Patch): Description of Semiology-urinary-incontinence modified
 - Semiology-genital (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-genital (Patch): Description of Semiology-genital modified
 - Semiology-vasomotor (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-vasomotor (Patch): Description of Semiology-vasomotor modified
 - Semiology-sudomotor (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 10,dc:source Beniczky ea 2013 Appendix S5
 - Semiology-sudomotor (Patch): Description of Semiology-sudomotor modified
 - Postictal-semiology (Patch): Attribute annotation modified from None to dc:source Blume ea 2001,dc:source Beniczky ea 2017 Table 11,dc:source Duration tag from Beniczky ea Table 13
 - Postictal-semiology (Patch): Description of Postictal-semiology modified
 - Postictal-unconscious (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-unconscious (Patch): Description of Postictal-unconscious modified
 - Postictal-quick-recovery-of-consciousness (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-quick-recovery-of-consciousness (Patch): Description of Postictal-quick-recovery-of-consciousness modified
 - Postictal-aphasia-or-dysphasia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-aphasia-or-dysphasia (Patch): Description of Postictal-aphasia-or-dysphasia modified
 - Postictal-behavioral-change (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-behavioral-change (Patch): Description of Postictal-behavioral-change modified
 - Postictal-hemianopia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-hemianopia (Patch): Description of Postictal-hemianopia modified
 - Postictal-impaired-cognition (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-impaired-cognition (Patch): Description of Postictal-impaired-cognition modified
 - Postictal-dysphoria (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-dysphoria (Patch): Description of Postictal-dysphoria modified
 - Postictal-headache (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-headache (Patch): Description of Postictal-headache modified
 - Postictal-nose-wiping (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-nose-wiping (Patch): Description of Postictal-nose-wiping modified
 - Postictal-anterograde-amnesia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-anterograde-amnesia (Patch): Description of Postictal-anterograde-amnesia modified
 - Postictal-retrograde-amnesia (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-retrograde-amnesia (Patch): Description of Postictal-retrograde-amnesia modified
 - Postictal-paresis (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-paresis (Patch): Description of Postictal-paresis modified
 - Postictal-sleep (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-sleep (Patch): Description of Postictal-sleep modified
 - Postictal-unilateral-myoclonic-jerks (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 11,dc:source Beniczky ea 2013 Appendix S5
 - Postictal-unilateral-myoclonic-jerks (Patch): Description of Postictal-unilateral-myoclonic-jerks modified
 - Episode-time-context-property (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 10
 - Episode-time-context-property (Patch): Description of Episode-time-context-property modified
 - Episode-consciousness-affected (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 13
 - Episode-consciousness-affected (Patch): Description of Episode-consciousness-affected modified
 - Episode-awareness (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 13
 - Episode-awareness (Patch): Description of Episode-awareness modified
 - Status-epilepticus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 13
 - Status-epilepticus (Patch): Description of Status-epilepticus modified
 - Episode-tongue-biting (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 13
 - Episode-tongue-biting (Patch): Description of Episode-tongue-biting modified
 - Artifact-significance-to-recording (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 12
 - Artifact-significance-to-recording (Patch): Description of Artifact-significance-to-recording modified
 - Interictal-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S1,dc:source Beniczky ea 2017 Table 5
 - Interictal-activity (Patch): Description of Interictal-activity modified
 - Epileptiform-interictal-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S4,dc:source Morphologies from Beniczky ea 2017 Table 5. annotation
 - Epileptiform-interictal-activity (Patch): Description of Epileptiform-interictal-activity modified
 - Abnormal-interictal-rhythmic-activity (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S4,dc:source Morphologies from Beniczky ea 2017 Table 5,dc:source Suggested tags from Beniczky ea 2017 Section 8
 - Abnormal-interictal-rhythmic-activity (Patch): Description of Abnormal-interictal-rhythmic-activity modified
 - Interictal-special-patterns (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5
 - Interictal-special-patterns (Patch): Description of Interictal-special-patterns modified
 - Interictal-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5
 - Interictal-periodic-discharges (Patch): Description of Interictal-periodic-discharges modified
 - Generalized-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Hirsch ea 2013
 - Generalized-periodic-discharges (Patch): Description of Generalized-periodic-discharges modified
 - Lateralized-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Hirsch ea 2013
 - Lateralized-periodic-discharges (Patch): Description of Lateralized-periodic-discharges modified
 - Bilateral-independent-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Hirsch ea 2013
 - Bilateral-independent-periodic-discharges (Patch): Description of Bilateral-independent-periodic-discharges modified
 - Multifocal-periodic-discharges (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5,dc:source Hirsch ea 2013
 - Multifocal-periodic-discharges (Patch): Description of Multifocal-periodic-discharges modified
 - Extreme-delta-brush (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 5
 - Extreme-delta-brush (Patch): Description of Extreme-delta-brush modified
 - Physiologic-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S1,dc:source Beniczky ea 2017 Table 14
 - Physiologic-pattern (Patch): Description of Physiologic-pattern modified
 - Rhythmic-activity-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 14
 - Rhythmic-activity-pattern (Patch): Description of Rhythmic-activity-pattern modified
 - Slow-alpha-variant-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Slow-alpha-variant-rhythm (Patch): Description of Slow-alpha-variant-rhythm modified
 - Fast-alpha-variant-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Fast-alpha-variant-rhythm (Patch): Description of Fast-alpha-variant-rhythm modified
 - Lambda-wave (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Lambda-wave (Patch): Description of Lambda-wave modified
 - Posterior-slow-waves-youth (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Posterior-slow-waves-youth (Patch): Description of Posterior-slow-waves-youth modified
 - Diffuse-slowing-hyperventilation (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Diffuse-slowing-hyperventilation (Patch): Description of Diffuse-slowing-hyperventilation modified
 - Photic-driving (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Photic-driving (Patch): Description of Photic-driving modified
 - Photomyogenic-response (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Photomyogenic-response (Patch): Description of Photomyogenic-response modified
 - Arousal-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Arousal-pattern (Patch): Description of Arousal-pattern modified
 - Frontal-arousal-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Frontal-arousal-rhythm (Patch): Description of Frontal-arousal-rhythm modified
 - Polygraphic-channel-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 13
 - Polygraphic-channel-feature (Patch): Description of Polygraphic-channel-feature modified
 - Respiration-channel-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 13 Table 16
 - Respiration-channel-feature (Patch): Description of Respiration-channel-feature modified
 - Periodic-respiration (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Periodic-respiration (Patch): Description of Periodic-respiration modified
 - ECG-channel-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 13 Table 16
 - ECG-channel-feature (Patch): Description of ECG-channel-feature modified
 - EMG-channel-feature (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 13 Table 16
 - EMG-channel-feature (Patch): Description of EMG-channel-feature modified
 - Myoclonus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Myoclonus (Patch): Description of Myoclonus modified
 - Negative-myoclonus (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Negative-myoclonus (Patch): Description of Negative-myoclonus modified
 - Myoclonus-arrhythmic (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Myoclonus-arrhythmic (Patch): Description of Myoclonus-arrhythmic modified
 - Myoclonus-synchronous (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Myoclonus-synchronous (Patch): Description of Myoclonus-synchronous modified
 - Myoclonus-asynchronous (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Myoclonus-asynchronous (Patch): Description of Myoclonus-asynchronous modified
 - PLMS (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - PLMS (Patch): Description of PLMS modified
 - Spasm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Spasm (Patch): Description of Spasm modified
 - Tonic-contraction (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 16
 - Tonic-contraction (Patch): Description of Tonic-contraction modified
 - Sleep-and-drowsiness (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S1
 - Sleep-and-drowsiness (Patch): Description of Sleep-and-drowsiness modified
 - Sleep-architecture (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3
 - Sleep-architecture (Patch): Description of Sleep-architecture modified
 - Normal-sleep-architecture (Patch): Attribute annotation modified from None to dc:source Benizcky ea 2013 Appendix S3
 - Normal-sleep-architecture (Patch): Description of Normal-sleep-architecture modified
 - Abnormal-sleep-architecture (Patch): Attribute annotation modified from None to dc:source Benizcky ea 2013 Appendix S3
 - Abnormal-sleep-architecture (Patch): Description of Abnormal-sleep-architecture modified
 - Sleep-stage-reached (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 7
 - Sleep-stage-reached (Patch): Description of Sleep-stage-reached modified
 - Sleep-stage-N1 (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Section 7
 - Sleep-spindles (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - Sleep-spindles (Patch): Description of Sleep-spindles modified
 - Vertex-wave (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - Vertex-wave (Patch): Description of Vertex-wave modified
 - K-complex (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - K-complex (Patch): Description of K-complex modified
 - Saw-tooth-waves (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - Saw-tooth-waves (Patch): Description of Saw-tooth-waves modified
 - POSTS (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - POSTS (Patch): Description of POSTS modified
 - Hypnagogic-hypersynchrony (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - Hypnagogic-hypersynchrony (Patch): Description of Hypnagogic-hypersynchrony modified
 - Non-reactive-sleep (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S3,dc:source Beniczky ea 2017 Section 7
 - Non-reactive-sleep (Patch): Description of Non-reactive-sleep modified
 - Uncertain-significant-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S1,dc:source Beniczky ea 2017 Table 14
 - Uncertain-significant-pattern (Patch): Description of Uncertain-significant-pattern modified
 - Sharp-transient-pattern (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 14
 - Sharp-transient-pattern (Patch): Description of Sharp-transient-pattern modified
 - Wicket-spikes (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Wicket-spikes (Patch): Description of Wicket-spikes modified
 - Small-sharp-spikes (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Small-sharp-spikes (Patch): Description of Small-sharp-spikes modified
 - Fourteen-six-Hz-positive-burst (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Fourteen-six-Hz-positive-burst (Patch): Description of Fourteen-six-Hz-positive-burst modified
 - Six-Hz-spike-slow-wave (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Six-Hz-spike-slow-wave (Patch): Description of Six-Hz-spike-slow-wave modified
 - Rudimentary-spike-wave-complex (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Rudimentary-spike-wave-complex (Patch): Description of Rudimentary-spike-wave-complex modified
 - Slow-fused-transient (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Slow-fused-transient (Patch): Description of Slow-fused-transient modified
 - Needle-like-occipital-spikes-blind (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Needle-like-occipital-spikes-blind (Patch): Description of Needle-like-occipital-spikes-blind modified
 - Subclinical-rhythmic-EEG-discharge-adults (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Subclinical-rhythmic-EEG-discharge-adults (Patch): Description of Subclinical-rhythmic-EEG-discharge-adults modified
 - Rhythmic-temporal-theta-burst-drowsiness (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Rhythmic-temporal-theta-burst-drowsiness (Patch): Description of Rhythmic-temporal-theta-burst-drowsiness modified
 - Ciganek-rhythm (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2017 Table 14
 - Ciganek-rhythm (Patch): Description of Ciganek-rhythm modified
 - Temporal-slowing-elderly (Patch): Attribute annotation modified from None to dc:source Beniczky ea 2013 Appendix S6,dc:source Beniczky ea 2017 Table 14
 - Temporal-slowing-elderly (Patch): Description of Temporal-slowing-elderly modified
 - Breach-rhythm (Patch): Description of Breach-rhythm modified
 - Event (Patch): Attribute annotation modified from None to ncit:C25499,rdfs:comment Should have this tag in every event process.
 - Building (Patch): Description of Building modified
 - Screen-window (Patch): Description of Screen-window modified
 - Age (Patch): Unit class timeUnits added to Age
 - Task-stimulus-role (Patch): Description of Task-stimulus-role modified
 - Cue (Patch): Description of Cue modified

**Units:**
 - degree Celsius (Patch): Description of degree Celsius modified

**Attributes:**
 - annotation (Minor): Item annotation added

**Misc Metadata:**
 - header_attributes (Patch): header_attributes changed from {'version': '2.0.0', 'library': 'score', 'withStandard': '8.3.0', 'unmerged': 'True'} to {'version': '2.1.0', 'library': 'score', 'withStandard': '8.4.0', 'unmerged': 'True'}
 - epilogue (Patch): epilogue changed

**Sources:**
 - Blume ea 2001 (Major): Row Blume ea 2001 missing in first schema
 - Beniczky ea 2013 (Major): Row Beniczky ea 2013 missing in first schema
 - Fisher ea 2017 (Major): Row Fisher ea 2017 missing in first schema
 - Wikipedia (Major): Row Wikipedia missing in first schema
 - Trenite ea 2001 (Major): Row Trenite ea 2001 missing in first schema
 - Beniczky ea 2017 (Major): Row Beniczky ea 2017 missing in first schema
 - Hirsch ea 2013 (Major): Row Hirsch ea 2013 missing in first schema

**Prefixes:**
 - dc: (Major): Row dc: missing in first schema
 - ncit: (Major): Row ncit: missing in first schema
 - rdfs: (Major): Row rdfs: missing in first schema
 - foaf: (Major): Row foaf: missing in first schema
 - rdf: (Major): Row rdf: missing in first schema
 - xml: (Major): Row xml: missing in first schema
 - obogo: (Major): Row obogo: missing in first schema
 - prov: (Major): Row prov: missing in first schema
 - skos: (Major): Row skos: missing in first schema
 - terms: (Major): Row terms: missing in first schema
 - owl: (Major): Row owl: missing in first schema
 - iao: (Major): Row iao: missing in first schema
 - xsd: (Major): Row xsd: missing in first schema

**AnnotationPropertyExternal:**
 - ('dc:', 'language') (Major): Row ('dc:', 'language') missing in first schema
 - ('dc:', 'type') (Major): Row ('dc:', 'type') missing in first schema
 - ('dc:', 'description') (Major): Row ('dc:', 'description') missing in first schema
 - ('dc:', 'publisher') (Major): Row ('dc:', 'publisher') missing in first schema
 - ('obogo:', 'has_dbxref') (Major): Row ('obogo:', 'has_dbxref') missing in first schema
 - ('dc:', 'creator') (Major): Row ('dc:', 'creator') missing in first schema
 - ('dc:', 'source') (Major): Row ('dc:', 'source') missing in first schema
 - ('dc:', 'identifier') (Major): Row ('dc:', 'identifier') missing in first schema
 - ('terms:', 'license') (Major): Row ('terms:', 'license') missing in first schema
 - ('dc:', 'contributor') (Major): Row ('dc:', 'contributor') missing in first schema
 - ('dc:', 'subject') (Major): Row ('dc:', 'subject') missing in first schema
 - ('dc:', 'date') (Major): Row ('dc:', 'date') missing in first schema
 - ('foaf:', 'homepage') (Major): Row ('foaf:', 'homepage') missing in first schema
 - ('dc:', 'relation') (Major): Row ('dc:', 'relation') missing in first schema
 - ('dc:', 'title') (Major): Row ('dc:', 'title') missing in first schema
 - ('dc:', 'format') (Major): Row ('dc:', 'format') missing in first schema


## Major release score 2.0.0 September 6, 2024.

Many tags were deleted, reorganized or renamed. Spreadsheets containing the work and mappings are available under
release notes for 2.0.0 on GitHub. The goals of this release were:
* Make sure that the tags exactly corresponded to the SCORE standard as delineated by Beniczky et al. 2013.
* Assign GUID's to every tag to better integrate into the linked data ecosystem.
* Update tag descriptions to give a description of every tag with source also cited.
* Move and expand the Artifact subtree from SCORE into the HED standard schema.
* Reorganize and clarify the Finding and Episode subtrees.
* Spreadsheets are available on Zenodo and in the release files showing how tags in 1.2.0 map into tags in 2.0.0.

## Changes for score 1.2.0 released July 16, 2024.

**Tags moved (Minor):**
 * Myoclonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Myoclonic-motor-seizure
 * Negative-myoclonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Negative-myoclonic-motor-seizure
 * Clonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Clonic-motor-seizure
 * Tonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Tonic-motor-seizure
 * Atonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Atonic-motor-seizure
 * Myoclonic-atonic-motor-seizure): from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Myoclonic-atonic-motor-seizure 
 * Myoclonic-tonic-clonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Myoclonic-tonic-clonic-motor-seizure
 * Tonic-clonic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Tonic-clonic-motor-seizure
 * Automatism-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Automatism-motor-seizure
 * Hyperkinetic-motor-seizure: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Hyperkinetic-motor-seizure
 * Epileptic-spasm-episode: from Finding-property/Episode-property/Seizure-classification/Motor-onset-seizure/Epileptic-spasm-episode

**Descriptions changed (Patch)
 * Motor-onset-seizure 
 * Myoclonic-motor-onset-seizure
 * Negative-myoclonic-motor-onset-seizure
 * Clonic-motor-onset-seizure
 * Tonic-motor-onset-seizure 
 * Atonic-motor-onset-seizure 
 * Myoclonic-atonic-motor-onset-seizure
 * Myoclonic-tonic-clonic-motor-onset-seizure
 * Tonic-clonic-motor-onset-seizure
 * Automatism-motor-onset-seizure
 * Hyperkinetic-motor-onset-seizure
 * Saw-tooth-waves
 * POSTS


## Changes for score 1.1.0 released July 12, 2023.
* Partnered with HED standard schema 8.2.0
* 'Epileptic-seizure': description update
* 'Focal-onset-epileptic-seizure': replaced '{suggestedTag=Seizure-classification}' with '{suggestedTag=Automatism-motor-seizure, suggestedTag=Atonic-motor-seizure, suggestedTag=Clonic-motor-seizure, suggestedTag=Epileptic-spasm-episode, suggestedTag=Hyperkinetic-motor-seizure, suggestedTag=Myoclonic-motor-seizure, suggestedTag=Tonic-motor-seizure, suggestedTag=Autonomic-nonmotor-seizure, suggestedTag=Behavior-arrest-nonmotor-seizure, suggestedTag=Cognitive-nonmotor-seizure, suggestedTag=Emotional-nonmotor-seizure, suggestedTag=Sensory-nonmotor-seizure}'
* 'Aware-focal-onset-epileptic-seizure': removed '{suggestedTag=Seizure-classification}'
* 'Impaired-awareness-focal-onset-epileptic-seizure': removed '{suggestedTag=Seizure-classification}'
* 'Awareness-unknown-focal-onset-epileptic-seizure': removed '{suggestedTag=Seizure-classification}'
* 'Generalized-onset-epileptic-seizure: replaced '{suggestedTag=Seizure-classification}' with '{suggestedTag=Tonic-clonic-motor-seizure, suggestedTag=Clonic-motor-seizure, suggestedTag=Tonic-motor-seizure, suggestedTag=Myoclonic-motor-seizure, suggestedTag=Myoclonic-tonic-clonic-motor-seizure, suggestedTag=Myoclonic-atonic-motor-seizure, suggestedTag=Atonic-motor-seizure, suggestedTag=Epileptic-spasm-episode, suggestedTag=Typical-absence-seizure, suggestedTag=Atypical-absence-seizure, suggestedTag=Myoclonic-absence-seizure, suggestedTag=Eyelid-myoclonia-absence-seizure,}'
* 'Unknown-onset-epileptic-seizure' : replaced '{suggestedTag=Seizure-classification}' with '{suggestedTag=Tonic-clonic-motor-seizure, suggestedTag=Epileptic-spasm-episode, suggestedTag=Behavior-arrest-nonmotor-seizure}'
* 'Focal-to-bilateral-tonic-clonic-focal-onset-epileptic-seizure': description update
* 'Generalized-onset-epileptic-seizure': description update
* 'Unknown-onset-epileptic-seizure': description update
* 'Unclassified-epileptic-seizure': description update
* 'Seizure-classification': description update   
* 'Motor-onset-seizure': deprecated
* 'Motor-seizure': added
* 'Myoclonic-motor-onset-seizure': deprecated
* 'Myoclonic-motor-seizure': added
* 'Negative-myoclonic-motor-onset-seizure': deprecated
* 'Negative-myoclonic-motor-seizure': added
* 'Clonic-motor-onset-seizure': deprecated
* 'Clonic-motor-seizure': added
* 'Tonic-motor-onset-seizure': deprecated
* 'Tonic-motor-seizure': added
* 'Atonic-motor-onset-seizure': deprecated
* 'Atonic-motor-seizure': added
* 'Myoclonic-atonic-motor-onset-seizure': deprecated
* 'Myoclonic-atonic-motor-seizure': added
* 'Myoclonic-tonic-clonic-motor-onset-seizure': deprecated
* 'Myoclonic-tonic-clonic-motor-seizure': added
* 'Tonic-clonic-motor-onset-seizure': deprecated
* 'Tonic-clonic-motor-seizure': added
* 'Automatism-motor-onset-seizure': deprecated
* 'Automatism-motor-seizure': added
* 'Hyperkinetic-motor-onset-seizure': deprecated
* 'Hyperkinetic-motor-seizure': added
* 'Epileptic-spasm-episode': description update
* 'Nonmotor-onset-seizure': deprecated
* 'Nonmotor-seizure': added
* 'Behavior-arrest-nonmotor-onset-seizure': deprecated
* 'Behavior-arrest-nonmotor-seizure': added
* 'Sensory-nonmotor-onset-seizure': deprecated
* 'Sensory-nonmotor-seizure': added
* 'Emotional-nonmotor-onset-seizure': deprecated
* 'Emotional-nonmotor-seizure': added
* 'Cognitive-nonmotor-onset-seizure': deprecated
* 'Cognitive-nonmotor-seizure': added
* 'Autonomic-nonmotor-onset-seizure': deprecated
* 'Autonomic-nonmotor-seizure': added
* 'Absence-seizure': description update
* 'Typical-absence-seizure': description update
* 'Atypical-absence-seizure': description update
* 'Myoclonic-absence-seizure': description update
* 'Eyelid-myoclonia-absence-seizure': description update
* 'Seizure-semiology-manifestation': description update

## Changes for HED score schema 1.0.0 released Jan 28, 2023.

* Initial release 

