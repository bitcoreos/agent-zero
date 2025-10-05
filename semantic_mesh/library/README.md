# Semantic Mesh Library

Purpose: keep the mesh lightweight so agents fetch only what they need.

How to use
- consult `catalog.yaml` to locate high-signal artefacts by id, tags, or path
- load individual files on demand (e.g., `rg "assays" semantic_mesh/library/catalog.yaml`)
- prefer `read_file`/`ripgrep` queries to targeted paths instead of bulk loading the full mesh

Notes
- catalog entries reference canonical artefacts already maintained elsewhere in the repo
- when a new artefact is added, append a concise item to `catalog.yaml` with sources and tags
- keep descriptions terse (<15 words) to stay under token budgets
