# Semantic Mesh Query Guide

This guide maps common questions to mesh resources. Treat all files as read-only; use hashes in `mesh_manifest.yaml` to verify provenance before consumption.

## Competition & Governance
- **"What are the competition rules and deadlines?"** → `competition_public/2025 AbDev Competition Overview.md`, `semantic_mesh/concepts/competition_structure.md`
- **"How do we submit predictions safely?"** → `semantic_mesh/concepts/submission_automation.md`, `semantic_mesh/concepts/submission_schema_standards.md`
- **"Who owns governance directives?"** → `AGENTS.md`, `semantic_mesh/mesh_manifest.yaml` (owner fields).

## Dataset & Bioinformatics
- **"How do I authenticate and retrieve GDPa1?"** → `semantic_mesh/concepts/dataset_access_controls.md`
- **"What sanity checks do we run on sequences?"** → `semantic_mesh/concepts/bioinformatics_pipeline.md`
- **"Where can I inspect fold metadata?"** → `competition_public/GDPa1 Dataset Overview.md`, `semantic_mesh/concepts/cross_validation_integrity.md`

## Modeling & Features
- **"Which features feed HIC predictions?"** → `semantic_mesh/concepts/feature_engineering_methods.md`, `semantic_mesh/concepts/sequence_structural_features.md`
- **"How do we fine-tune p-IgGen embeddings?"** → `semantic_mesh/concepts/ai_finetuning_pipeline.md`
- **"What ensembles are supported?"** → `semantic_mesh/concepts/ensembling_postprocessing.md`

## Assays & Biophysics
- **"What does AC-SINS measure?"** → `semantic_mesh/concepts/assay_definitions.md`, `semantic_mesh/concepts/biophysics_interpretation.md`
- **"How do isotypes affect Tm2?"** → `semantic_mesh/concepts/isotype_systematics.md`

## Validation & QA
- **"How do we mirror leaderboard metrics locally?"** → `semantic_mesh/concepts/validation_evaluation_logic.md`, `semantic_mesh/concepts/evaluation_metrics.md`
- **"What drift checks exist before submission?"** → `semantic_mesh/concepts/drift_detection_quality_assurance.md`

## Ontology & Vocabulary
- **"Which IDs represent assays vs. features?"** → `semantic_mesh/schemas/mesh_topics.yaml`, `semantic_mesh/concepts/context_terms.yaml`
- **"Where are ontology exports stored?"** → `ontology_schema/mesh_ontology.jsonld`, `ontology_schema/mesh_ontology.ttl`

## Usage Pattern
1. Identify your question category above.
2. Load the referenced resource(s) through `catalog.yaml` to minimize tokens.
3. Verify hashes/owners in `mesh_manifest.yaml` before citing outputs or wiring agents.
