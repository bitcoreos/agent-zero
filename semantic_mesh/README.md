# Semantic Mesh Overview

goal: lightweight, machine-readable knowledge lattice that lets agents/bioinformaticians fetch antibody-developability context with minimal tokens.

directories:
	concepts/: high-signal briefs, vocabularies, and modeling protocols
	schemas/: glossary + ontology stubs pending JSON-LD/Turtle exports
	library/: catalog + usage notes for targeted artefact retrieval
	mesh_bootstrap.md: declarative blueprint binding competition intel + modeling strategy into mesh nodes
	mesh_manifest.yaml: minimal node → artefact scaffold for quick lookups

usage:
	- agents load mesh nodes before executing plans outlined in `AGENTS.md`
	- humans reference mesh files for aligned terminology and pipeline context; consult `library/catalog.yaml` to pull only relevant artefacts

next steps (mesh_build backlog ref `init.md`):
	- keep library catalog current as artefacts evolve
	- materialize ontology exports (TTL/JSON-LD)
	- deliver mesh validator + manifest hashes