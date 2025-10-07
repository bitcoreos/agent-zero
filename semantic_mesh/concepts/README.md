# Semantic Layer

goal: expose lightweight, machine-readable context modules covering assays, competition structure, modeling intent, and vocabulary.

key artefacts:
	- `assay_definitions.md`: concise descriptions of competition-target assays with relevance notes
	- `competition_structure.md`: snapshot of tracks, timelines, and submission logistics
	- `evaluation_metrics.md`: authoritative summary of leaderboard metrics and validation checks
	- `model_requirements.md`: high-signal modeling expectations distilled from the execution plan
	- `protocols.md`: workflow checklist aligning data prep, feature builds, and training loops
	- `semantic_mesh_concepts.md`: detailed concept mesh spanning sequence, modeling, calibration, and QA themes
	- `context_terms.yaml` + `core_concepts.yaml`: machine-friendly vocabularies for targeted retrieval
	- `competition_target_alignment.md`: maps GDPa1 assays to mesh nodes, features, and citations
	- `sequence_structural_features.md`, `feature_engineering_methods.md`: reusable ledgers for feature derivation
	- `topic_categories.md`: human-readable index paired with `schemas/mesh_topics.yaml`
	- `bioinformatics_pipeline.md`: intake, QC, and structure-linkage guardrails for GDPa1
	- `biophysics_interpretation.md`: assay-level biophysical rationale and production context
	- `isotype_systematics.md`: subclass-aware modeling directives and diagnostics
	- `ai_finetuning_pipeline.md`: embedding + fine-tuning workflow with reproducibility hooks
	- `submission_automation.md`: automation checklist for CV and test submissions
	- `dataset_access_controls.md`: license, read-only, and audit requirements for GDPa1

usage:
	- agents load only the artefacts referenced in `semantic_mesh/library/catalog.yaml` for their task scope
	- humans verify terminology and pipeline context without trawling the full plan
	- ontological IDs for every node live in `ontology_schema/` and are mirrored in `mesh_manifest.yaml`
	- per-node `summary` text in the manifest foregrounds mesh connections; paired `definition` text supplies the ontological wording

stewardship guidelines:
	- keep prose lean; retire or trim any section that drifts from competition docs or the live plan
	- refresh citations via `semantic_mesh/REFERENCES.md` when adding new external evidence