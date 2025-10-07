# Semantic Mesh Index

Use this index to navigate the read-only antibody developability mesh. All artefacts are immutable; reference them directly without modification.

## Quick Access
- **Competition Rules & Timeline**: `competition_public/2025 AbDev Competition Overview.md`
- **Leaderboard Workflow**: `competition_public/AbDev Leaderboard Overview.md`
- **Dataset Schema & Assays**: `competition_public/GDPa1 Dataset Overview.md`
- **Heldout Sequences (Read-Only)**: `competition_public/dataset/heldout-set-sequences.csv`
- **Modeling Strategy**: `research_plans/initial_plan/plan.md`
- **Semantic Mesh Manifest**: `semantic_mesh/mesh_manifest.yaml`

## Semantic Categories
- **Biology & Assays**: `semantic_mesh/concepts/assay_definitions.md`, `semantic_mesh/concepts/biophysics_interpretation.md`, `semantic_mesh/concepts/sequence_structural_features.md`
- **Competition & Governance**: `semantic_mesh/concepts/competition_structure.md`, `semantic_mesh/concepts/governance` (see `AGENTS.md`), `semantic_mesh/concepts/submission_schema_standards.md`, `semantic_mesh/concepts/submission_automation.md`
- **Data & Bioinformatics**: `semantic_mesh/concepts/bioinformatics_pipeline.md`, `semantic_mesh/concepts/dataset_access_controls.md`, `semantic_mesh/concepts/cross_validation_integrity.md`
- **Modeling & Features**: `semantic_mesh/concepts/feature_engineering_methods.md`, `semantic_mesh/concepts/model_architectures_training.md`, `semantic_mesh/concepts/ai_finetuning_pipeline.md`, `semantic_mesh/concepts/ensembling_postprocessing.md`
- **Validation & QA**: `semantic_mesh/concepts/validation_evaluation_logic.md`, `semantic_mesh/concepts/drift_detection_quality_assurance.md`
- **Ontology & Vocabulary**: `semantic_mesh/schemas/glossary.md`, `semantic_mesh/concepts/context_terms.yaml`, `ontology_schema/mesh_ontology.ttl`

## Retrieval Tips
- Consult `semantic_mesh/library/catalog.yaml` for machine-friendly lookup (resource IDs, tags, related artefacts, query hints). Ontological URNs resolve under `urn:mesh:node/` and are materialized in `ontology_schema/`.
- See `semantic_mesh/QUERY_GUIDE.md` for example questions mapped to nodes.
- Use `mesh_topics.yaml` for topic-driven traversal when building agent plans.

## Provenance & Hashes
Content hashes and owner assignments live in `semantic_mesh/mesh_manifest.yaml`. Always verify hashes before citing artefacts.
