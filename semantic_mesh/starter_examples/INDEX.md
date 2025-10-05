
# Semantic Mesh Index

purpose:
	description: canonical manifest for semantic+ontological knowledge nodes powering agent-zero
	usage:
		- machine discovery (CI validation, automated loaders)
		- human orientation (bioinformaticians, engineers, PI)

components:
	competition_overview:
		path: competition_public/2025 AbDev Competition Overview.md
		summary: narrative brief of competition scope, timelines, participation requirements
		tags: [competition, overview]
	leaderboard_overview:
		path: competition_public/AbDev Leaderboard Overview.md
		summary: explains Hugging Face leaderboard surfaces, submission logic, scoring cadence
		tags: [competition, leaderboard]
	dataset_overview:
		path: competition_public/GDPa1 Dataset Overview.md
		summary: GDPa1 schema, assay definitions, gated-access notes, PROPHET-Ab digest
		tags: [dataset, assays, schema]
	tutorial_reference:
		path: competition_public/How to Train an Antibody Developability Model.md
		summary: condensed tutorial describing embedding workflows, ridge baseline, CV usage
		tags: [tutorial, modeling]
	dataset_public_csv:
		path: competition_public/dataset/GDPa1_v1.2_sequences.csv
		summary: public GDPa1 sequences + assays (CSV)
		tags: [dataset, csv, public]
	dataset_heldout_csv:
		path: competition_public/dataset/heldout-set-sequences.csv
		summary: private heldout sequences for final exam predictions (no assay labels)
		tags: [dataset, csv, heldout]
	initial_plan:
		path: research_plans/initial_plan/plan.md
		summary: step-by-step modeling roadmap, feature architecture, ensemble strategy
		tags: [plan, modeling, pipeline]
	gaps_log:
		path: research_plans/initial_plan/gaps.md
		summary: prioritized gap list with pattern-based tests and Markov curriculum notes
		tags: [risks, features]
	gaps_risks_log:
		path: research_plans/initial_plan/gaps_risks.md
		summary: licensing, data leakage, compute risk register
		tags: [risks, governance]
	flow_diagram:
		path: research_plans/initial_plan/flow.md
		summary: mermaid workflow graph from data ingest to submission
		tags: [pipeline, visualization]
	antibody_glossary:
		path: semantic_mesh/ontological/glossary.md
		summary: terminological grounding for assays, antibody properties, modeling vocabulary
		tags: [ontology, glossary]
	semantic_concepts:
		path: semantic_mesh/semantic/semantic_mesh_concepts.md
		summary: curated concept mesh linking sequence features, modeling techniques, calibration logic
		tags: [semantic, concepts]
		semantic_context_terms:
			path: semantic_mesh/semantic/context_terms.yaml
			summary: compact vocabulary map (antibody terms, assays, modeling constructs) with sources + tags
			tags: [semantic, vocabulary]
		semantic_core_concepts:
			path: semantic_mesh/semantic/core_concepts.yaml
			summary: distilled lattice of high-priority concepts linking plans and competition briefs
			tags: [semantic, concepts, lattice]
		mesh_bootstrap:
			path: semantic_mesh/mesh_bootstrap.md
			summary: declarative blueprint for semantic mesh nodes, JSON-LD frame, pre-execution tasks
			tags: [semantic, architecture, bootstrap]
			mesh_references:
				path: semantic_mesh/REFERENCES.md
				summary: redundant citation ledger covering competition, planning, and mesh artefacts
				tags: [references]
			mesh_manifest:
				path: semantic_mesh/mesh_manifest.yaml
				summary: lightweight node+relation scaffold linking core concepts to artefacts
				tags: [semantic, manifest]

validation_checklist:
	- ensure no `§§include(...)` placeholders remain in referenced artefacts
	- TTL/JSON-LD artefacts parse cleanly once generated
	- JSON Schema + ontology validators succeed (pending script implementation)
	- REFERENCES.bib (when added) parses with bibtexparser
	- mesh validator script to enforce manifest completeness (TODO)
