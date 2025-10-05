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

usage:
	- agents load only the artefacts referenced in `semantic_mesh/library/catalog.yaml` for their task scope
	- humans verify terminology and pipeline context without trawling the full plan

next actions:
	- map semantic documents to ontological IDs once the validator is implemented
	- keep prose lean; retire or trim any section that drifts from competition docs or the live plan