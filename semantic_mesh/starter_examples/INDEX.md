
// this file needs to be refactored into one that actually uses our paths to correct files 

# Semantic Mesh Index (seed)

Purpose
- Canonical manifest and manifest-driven seed for the agent-zero semantic mesh.
- Machine+human facing list that enables CI validation and programmatic discovery.

Components (seed)
- path-to-file: description. (template placeholder)

Quick validation checklist
- [ ] No `§§include(...)` placeholder tokens remain anywhere.
- [ ] All TTL/JSON-LD parse cleanly.
- [ ] JSON Schema validates examples.
- [ ] REFERENCES.bib parses with bibtexparser.
- [ ] CI runs validation on PRs touching semantic_mesh/ or ontological/.
