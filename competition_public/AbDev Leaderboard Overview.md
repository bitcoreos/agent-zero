# Ginkgo Antibody Developability Benchmark — Leaderboard Overview

**Source:** [Hugging Face Space — ginkgo-datapoints/abdev-leaderboard](https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard)  
**Hosted by:** Ginkgo Datapoints in collaboration with Hugging Face  
**Submission deadline:** 1 November 2025  
**Early scoring run:** 13 October 2025

## Challenge Snapshot
Participants benchmark antibody developability models by uploading CSV predictions to the Hugging Face competition space. Submissions can cover any subset of five developability properties, and leaderboards can be filtered by property. Test-set scoring happens automatically on announced dates.

## Developability Properties
- 💧 Hydrophobicity (HIC)  
- 🎯 Polyreactivity (CHO)  
- 🧲 Self-association (AC-SINS at pH 7.4)  
- 🌡️ Thermostability (Tm2)  
- 🧪 Titer

## Prize Structure
- Five property-specific prizes for the top-performing models on the private test set.  
- One **open-source prize** for the best reproducible model trained solely on GDPa1 (requires sharing training code and data; judged by overall Spearman correlation across properties and community impact).  
- Winners choose between **$10,000 in Ginkgo Datapoints data-generation credits** or **$2,000 cash** per prize.

## Participation Checklist
1. Create a Hugging Face account (required for dataset access and submission tracking).  
2. Register on the Ginkgo competition site to receive the secret submission code.  
3. Train and validate models on the GDPa1 dataset, using `hierarchical_cluster_IgG_isotype_stratified_fold` for cross-validation splits and outputting fold-level predictions.  
4. Generate predictions for the 80-antibody private test set (downloadable from the "✉️ Submit" tab).  
5. Upload both cross-validation predictions and private test set predictions through the submission tab.  
6. Monitor the leaderboard and adjust models ahead of the final deadline.

The space includes links to introductory tutorials (e.g., how to train an antibody developability model with cross-validation) to assist new participants.

## Timeline
- **13 October 2025:** Interim scoring of all test set submissions received to date.  
- **1 November 2025:** Final submission deadline.  
- Winners announced in November 2025.

## Acknowledgements
Tamarind Bio contributed benchmark runs for several reference models currently on the leaderboard:
- TAP (Therapeutic Antibody Profiler)  
- SaProt  
- DeepViscosity  
- Aggrescan3D  
- AntiFold

Organizers are working to add more public models (e.g., absolute folding stability predictors, PROPERMAB, AbMelt) to expand available features for participants.

## Community and Support
- Join the Slack community co-hosted by Bits in Bio to form teams and discuss approaches.  
- Contact: [antibodycompetition@ginkgobioworks.com](mailto:antibodycompetition@ginkgobioworks.com).  
- Registration, terms, and updates hosted on the Ginkgo competition portal.

## Downloads and Resources
- GDPa1 dataset and private test sequences available for direct download via the competition space (authentication required).  
- Submission interface located under the "✉️ Submit" tab.  
- Additional documentation provided in the "📖 About / Rules" and "❓ FAQs" tabs.
