# Topic-Aligned Category Guide

updated_utc: 2025-10-05T13:22:00Z  
sources: `semantic_mesh/schemas/mesh_topics.yaml`, `semantic_mesh/mesh_manifest.yaml`

Each category corresponds to a mesh node family and is indexed in `schemas/mesh_topics.yaml` for machine access. Use this guide for human-readable summaries.

| Category | Mesh node ID | Description | Key artifacts |
| --- | --- | --- | --- |
| Assay and Metric Definitions | `assay_metric_definitions` | Connects GDPa1 assays to metrics, features, and citations. | `concepts/competition_target_alignment.md`, `concepts/assay_definitions.md`, `concepts/evaluation_metrics.md` |
| Sequence and Structural Features | `sequence_structural_features` | Region-aware hydropathy, charge, and structure-lite descriptors. | `concepts/sequence_structural_features.md`, `concepts/context_terms.yaml` |
| Feature Engineering Methods | `feature_engineering_methods` | Recipes for statistical, physicochemical, and LM feature derivation. | `concepts/feature_engineering_methods.md`, `concepts/markov_notes.md` |
| Model Architectures and Training Protocols | `model_arch_training` | Curriculum-aware training plans and deployment hooks. | `concepts/model_architectures_training.md`, `concepts/protocols.md` |
| Validation and Evaluation Logic | `validation_evaluation_logic` | Leaderboard parity checks and QA gating. | `concepts/validation_evaluation_logic.md`, `concepts/evaluation_metrics.md` |
| Cross-Validation and Data Integrity Rules | `cross_validation_integrity` | Fold stewardship, leakage prevention, provenance requirements. | `concepts/cross_validation_integrity.md`, `competition_public/dataset/README.md` |
| Submission Schema and File Standards | `submission_schema_standards` | CSV schema, manifest conventions, change control. | `concepts/submission_schema_standards.md`, `competition_public/AbDev Leaderboard Overview.md` |
| Ensembling and Post-Processing Strategies | `ensembling_post_processing` | Ensemble composition, calibration, packaging. | `concepts/ensembling_postprocessing.md`, `concepts/semantic_mesh_concepts.md` |
| Statistical and Information-Theory Features | `statistical_information_features` | Markov, surprisal, entropy, and smoothing records. | `concepts/statistical_information_features.md`, `concepts/markov_notes.md` |
| Drift Detection and Quality Assurance | `drift_detection_quality` | Monitoring metrics, QA gates, alert workflow. | `concepts/drift_detection_quality_assurance.md`, `concepts/protocols.md` |
| Competency and Query Framework | `competency_query_framework` | Competency questions, ontology bindings, query templates. | `concepts/competency_query_framework.md`, `schemas/glossary.md` |
| References and Provenance Sources | `references_provenance_sources` | Citation ledger and provenance governance. | `concepts/references_provenance.md`, `REFERENCES.md`, `library/catalog.yaml` |

## Maintenance Checklist
- Validate that every category links to live artifacts after each sprint.
- Sync any changes in this table with `mesh_topics.yaml` and `mesh_manifest.yaml`.
- Add new categories here (and in the schema) before introducing new nodes.
