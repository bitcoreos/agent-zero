# Ontological Layer

goal: capture durable identifiers, schemas, and grounded definitions for concepts used across the semantic mesh.

key artefacts:
	- `glossary.md`: vetted term definitions aligned with GDPa1 documentation and the modeling plan
	- `antibody_ontology.json`: current JSON schema stub describing core resource classes; to be pruned/converted into JSON-LD & Turtle exports
	- `.gitkeep`: placeholder until ontology exports land

reference policy:
	- authoritative citation list now lives in `semantic_mesh/REFERENCES.md`; retire duplicated ledgers here
	- glossary entries should cite that ledger using anchors rather than duplicating metadata

roadmap:
	- refactor `antibody_ontology.json` into a minimal namespace-aware JSON-LD context plus Turtle serialisation
	- link glossary terms and semantic vocab (`context_terms.yaml`, `core_concepts.yaml`) via shared IDs
	- add validator hooks ensuring every ontology class/property is referenced by at least one mesh artefact