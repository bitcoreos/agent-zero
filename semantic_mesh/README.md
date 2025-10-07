# Semantic Mesh Overview

goal: lightweight, machine-readable knowledge lattice that lets agents/bioinformaticians fetch antibody-developability context with minimal tokens.

directories:
	concepts/: high-signal briefs, vocabularies, and modeling protocols
	schemas/: glossary + topic schemas backing controlled vocabulary
	library/: catalog + usage notes for targeted artefact retrieval
	mesh_bootstrap.md: declarative blueprint binding competition intel + modeling strategy into mesh nodes
	mesh_manifest.yaml: minimal node → artefact scaffold for quick lookups (now linked to ontology terms)
	../ontology_schema/: RDF/JSON-LD exports generated from the manifest for linked-data interoperability

usage:
	- agents load mesh nodes before executing plans outlined in `AGENTS.md`
	- humans reference mesh files for aligned terminology and pipeline context; consult `library/catalog.yaml` to pull only relevant artefacts
	- topic-aligned categories live in `schemas/mesh_topics.yaml`; combine with `concepts/competition_target_alignment.md` to reach property-specific guidance
	- node `summary` fields emphasise connection context, while complementary `definition` fields (mirrored in `ontology_schema/`) capture canonical meaning for each concept

stewardship (aligns with `init.md` backlog):
	- keep library catalog current as artefacts evolve
	- regenerate ontology exports via `ontology_schema/generate_ontology.py` whenever the manifest changes
	- maintain manifest hashes/owners and plan future validator coverage
	- review competition target alignment after every modeling milestone; update citations + manifests accordingly