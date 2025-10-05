# Competition Target Alignment Playbook

updated_utc: 2025-10-05T13:00:00Z  
sources: `competition_public/GDPa1 Dataset Overview.md`, `semantic_mesh/concepts/assay_definitions.md`, `research_plans/initial_plan/plan.md`, `semantic_mesh/concepts/semantic_mesh_concepts.md`

## Property-to-Mesh Mapping

This table maps each leaderboard property to the mesh nodes that own or supply the relevant knowledge. Node identifiers follow `semantic_mesh/mesh_manifest.yaml`.

| Property (Leaderboard label) | Measurement intent | Primary nodes | Supporting nodes | Feature focus | Key references |
| --- | --- | --- | --- | --- | --- |
| Hydrophobicity (`HIC`) | Salt-mediated retention time tracks exposed hydrophobic patches | `assay_metric_definitions`, `sequence_structural_features` | `feature_engineering_methods`, `statistical_information_features`, `ensembling_post_processing` | Kyte–Doolittle hydropathy⁽¹⁾, aromatic/Leu patch counts, solvent-accessible surface estimates, LM embeddings for hydropathy motifs | [GDPa1 Overview (HIC)](#references), [Kyte & Doolittle 1982](#references) |
| Polyreactivity (`PR_CHO`) | PSP bead binding to CHO membrane proteins flags nonspecific interactions | `assay_metric_definitions`, `statistical_information_features` | `sequence_structural_features`, `feature_engineering_methods`, `drift_detection_quality` | Net positive charge, isoelectric point, CDR basic residue run-length, VH/VL imbalance, entropy-triggered gating | [GDPa1 Overview (PR_CHO)](#references), [Jain et al. 2017](#references) |
| Self-association (`AC-SINS_pH7.4`) | Gold nanoparticle shift at pH 7.4 indicates colloidal self-interaction | `assay_metric_definitions`, `sequence_structural_features` | `feature_engineering_methods`, `model_arch_training`, `statistical_information_features` | Charge at pH 7.4, exposed aromatic surface, PBT red-flag motifs, Markov surprisal tiers | [GDPa1 Overview (AC-SINS)](#references), [Jain et al. 2017](#references) |
| Thermostability (`Tm2`) | nanoDSF Fab melting transition (higher is better) | `assay_metric_definitions`, `model_arch_training` | `sequence_structural_features`, `feature_engineering_methods`, `validation_evaluation_logic` | IgFold loop RMSD, hydrogen bond counts, β-sheet propensity, LM secondary-structure logits | [GDPa1 Overview (Tm2)](#references), [Chennamsetty et al. 2009](#references) |
| Titer (`Titer`) | HEK293F expression yield proxy | `assay_metric_definitions`, `model_arch_training` | `feature_engineering_methods`, `cross_validation_integrity`, `submission_schema_standards` | Secretory signal motif flags, glycosylation motif coverage, surface charge balance, surprisal outlier detection | [GDPa1 Overview (Titer)](#references), [How to Train AbDev Baseline](#references) |

## Feature Extraction Blueprint

1. **Sequence normalization** — Parse VH/VL chains from `GDPa1_v1.2_sequences.csv`; enforce ANARCI numbering (`feature_engineering_methods`).
2. **Region-aware descriptors** — Derive FR/CDR hydropathy, net charge, aromatic density, glycosylation motifs (`sequence_structural_features`).
3. **Statistical models** — Train fold-specific n-gram Markov models (`statistical_information_features`) and emit log-probability, surprisal, and entropy tiers per region.
4. **Language-model embeddings** — Extract ESM-2 / AntiBERTa / AbLang representations, average within regions, and surface task-specific heads (`feature_engineering_methods`).
5. **Structure-lite proxies** — Generate IgFold loop summaries (where licensing cleared) and structural heuristics (contact counts, hydrogen bonds) with provenance hashes (`model_arch_training`).
6. **Quality gates** — Run QA checks (alphabet validation, surprisal drift, polyreactivity charge thresholds) and annotate failures in the mesh (`drift_detection_quality`).
7. **Submission-ready aggregation** — Combine calibrated predictions, track ensemble members, and document transformations (`ensembling_post_processing`).

## Data Source Inventory

| Asset | Purpose | Update cadence | Storage node |
| --- | --- | --- | --- |
| `competition_public/dataset/GDPa1_v1.2_sequences.csv` | Canonical sequences, assay labels, folds | Weekly checksum verification | `dataset_assets` |
| `competition_public/dataset/heldout-set-sequences.csv` | Held-out sequences for final scoring | Static (verify SHA256 once) | `dataset_assets` |
| IgFold summaries (planned) | Loop RMSD, contacts for thermostability features | Pending licensing sign-off | `model_arch_training` |
| `semantic_mesh/concepts/context_terms.yaml` | Vocabulary alignment for features and QA flags | On edit | `competency_query_framework` |
| `semantic_mesh/concepts/markov_notes.md` | Markov configuration, surprisal buckets | On new model iteration | `statistical_information_features` |

## Edge Guidance

- Create `aligns_with` edges from `assay_metric_definitions` to each modeling node that produces predictions (see `mesh_manifest.yaml`).
- Record feature lineage via `derived_from` edges (e.g., `feature_engineering_methods -> sequence_structural_features`).
- When new assays or score transforms appear, extend this playbook **and** `mesh_topics.yaml` within 24h.

## Maintenance Checklist

- [ ] Confirm manifest node coverage after each modeling sprint retro.
- [ ] Sync prominent citations with `semantic_mesh/REFERENCES.md`.
- [ ] Mirror any schema changes into `semantic_mesh/schemas/mesh_topics.yaml` for machine-readable access.
- [ ] Update QA gates when leaderboard validation introduces new failure cases.

## References

1. Ginkgo Datapoints. *GDPa1 Dataset Overview*. competition_public/GDPa1 Dataset Overview.md.
2. Kyte, J., & Doolittle, R. F. (1982). A simple method for displaying the hydropathic character of a protein. *Journal of Molecular Biology*, 157(1), 105–132.
3. Jain, T., et al. (2017). Biophysical properties of the clinical-stage antibody landscape. *mAbs*, 9(3), 424–434.
4. Chennamsetty, N., et al. (2009). Prediction of aggregation-prone regions of therapeutic proteins. *Journal of Physical Chemistry B*, 113(19), 6629–6635.
5. Ginkgo Datapoints. *How to Train an Antibody Developability Model*. competition_public/How to Train an Antibody Developability Model.md.
