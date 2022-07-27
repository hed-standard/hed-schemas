# SCORE schema library

The manual review and interpretation of the EEG is critical to the value of the EEG as a diagnostic tool but is highly sensitive to subjectivity. The consensus between experts interpreting the same EEG is higher when using the same structured standard. Still, EEG is very complex, making it difficult to describe it in structured fields adequately. Free-text fields might be more flexible but suffer from incompleteness, lack of consistency, and the limited ability to share reports. Therefore, the standardization of clinical terminology holds considerable potential for the field. 

The Standardized Computer-based Organized Reporting of EEG (SCORE)[^1]^,^[^2] is a standardized terminology for annotating EEG and ictal clinical events currently used in commercial software to create a standardized report. The SCORE standard goal is to give epileptologists a computerized tool and standard terminology that can be used in clinical practice and maximize interobserver agreement. The 1^st^ SCORE version received European consensus, endorsed by the European Chapter of the IFCN and the International League Against Epilepsy (ILAE) Commission on European Affairs. The 2^nd^ SCORE version is a revised terminology extended from the 1^st^ version with additional terms from multiple classifications, glossaries, and standard terminologies that have achieved international consensus.

The SCORE implementation in HED tackles these textual reports' lack of machine readability and makes SCORE available for and machine-readable by open-source software. Many researchers worldwide can use the SCORE library to reduce errors in clinical evaluations and perform advanced mega-analyses, ultimately advancing the understanding of the human brain.

![SFN poster](SFNposter_TPA.png)

## Development

The SCORE HED schema library maintains the hierarchy as in the SCORE EEG Educational Platform[^3] and presented in SCORE papers. The SCORE EEG Educational Platform is interactive web-based software that teaches how to use the SCORE standard. The educational platform guided the development process by permitting the interactive inspection of the main types of EEG graphoelements included in the SCORE report and the appropriate low-level nodes for each of them.

The top levels of the HED schema library for SCORE correspond to the main EEG graphoelements, including Modulators, Background activity, Sleep and drowsiness, Interictal findings, Episodes, Physiologic patterns, Uncertain significance patterns, EEG artifacts, and Polygraphic channels.

The SCORE HED schema library is intended to describe all normal and abnormal EEG features. Therefore, description of patient information, referral and recording condition information, administrative data, and continuous EEG monitoring in neonates is beyond this scope.

### Validation
The HED schema library for SCORE was converted and validated using the HED tools. See more [here](https://hedtools.ucsd.edu/hed).

## Brain imaging data structure (BIDS)
HED schema library for SCORE is compatible with the BIDS human and machine-readable events annotations .tsv files, see more [here](https://bids-specification.readthedocs.io/en/stable/99-appendices/03-hed.html#appendix-iii-hierarchical-event-descriptors).
A HED schema library for SCORE annotations implementation example is available [here](https://github.com/tpatpa/bids-examples/tree/master/xeeg_hed_score).

---
*Manuscript: Tal Pal Attia et al., (in prep). "Hierarchical Event Descriptor library schema for clinical EEG data annotation".*

[^1]: Beniczky, Sándor, et al. "Standardized computer‐based organized reporting of EEG: SCORE." Epilepsia 54.6 (2013): 1112-1124.

[^2]: Beniczky, Sándor, et al. "Standardized computer-based organized reporting of EEG: SCORE–second version." Clinical Neurophysiology 128.11 (2017): 2334-2346.

[^3]: https://www.holbergeeg.com/educational-platform