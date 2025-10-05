# Competency and Query Framework

updated_utc: 2025-10-05T13:20:00Z  
sources: `semantic_mesh/concepts/context_terms.yaml`, `semantic_mesh/schemas/glossary.md`, `semantic_mesh/concepts/competition_target_alignment.md`

## Competency Questions
- **CQ-01**: Which mesh nodes inform hydrophobicity predictions for a given antibody?
- **CQ-02**: What features drive polyreactivity risk in GDPa1 sequences?
- **CQ-03**: How can we detect drift between cross-validation and heldout submissions?
- **CQ-04**: Which citations justify the thermostability feature stack?

## Query Templates
```json
{
  "intent": "assay_alignment",
  "property": "HIC",
  "requires": ["sequence_structural_features", "statistical_information_features"],
  "format": "table",
  "include": ["features", "citations"]
}
```

## Ontology Bindings
- Vocabulary terms reside in `semantic_mesh/concepts/context_terms.yaml` (YAML) and `semantic_mesh/schemas/glossary.md` (Markdown).
- Maintain OWL/JSON-LD identifiers once ontology export pipeline is ready (see `mesh_bootstrap.md`).

## Maintenance
- Append new competency questions when modeling scope expands.
- Keep query templates synchronized with mesh validator API design.
- Ensure every competency question maps to at least one citeable artifact in `semantic_mesh/REFERENCES.md`.
