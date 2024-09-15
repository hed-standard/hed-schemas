# CHANGELOG for HED score library schema

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

