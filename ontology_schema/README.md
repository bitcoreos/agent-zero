# Ontology Schema for the Semantic Mesh

This directory contains the ontological representation of the antibody developability semantic mesh. The ontology mirrors every node, owner, artifact, and relation described in `semantic_mesh/mesh_manifest.yaml` and exposes them as linked-data resources.

## Artifacts

- `mesh_ontology.ttl` – Turtle serialization of the ontology, suitable for RDF tooling.
- `mesh_ontology.jsonld` – JSON-LD serialization of the same graph.
- `generate_ontology.py` – Utility script that parses the mesh manifest and regenerates both serializations.

## Regeneration Workflow

1. Make sure the semantic mesh manifest is current (`semantic_mesh/mesh_manifest.yaml`).
2. From the repository root, run:

```bash
python ontology_schema/generate_ontology.py
```

3. Commit the updated ontology serializations alongside any mesh changes so the systems remain synchronized.

## Design Notes

- Nodes, owners, artifacts, and relation predicates receive stable URNs under the `urn:mesh:` namespace.
- Relation types (for example `informs`, `optimizes`) become sub-properties of `urn:mesh:prop/relatedTo` so downstream agents can reason over both coarse and fine relation semantics.
- Artifact hashes from the manifest are embedded to preserve provenance at the ontology layer.
- Each semantic mesh node records a forward link (`ontology_term`) to its ontological term, and the ontology references the manifest path for round-trip traceability.
- Node definitions in the ontology mirror, but do not copy verbatim, the mesh definitions so that either surface is self-sufficient for understanding a concept.
