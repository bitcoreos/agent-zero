# Bioinformatics Pipeline Guardrails

sources: `competition_public/GDPa1 Dataset Overview.md`, `competition_public/dataset/README.md`, `competition_public/How to Train an Antibody Developability Model.md`

## Authentication & Intake
- Accept the GDPa1 license and authenticate with `huggingface-cli login` before touching any artefact.
- Cache the raw CSVs via Hugging Face URLs (`hf://datasets/...`) and immediately record SHA256 hashes.
- Maintain read-only mounts for `competition_public/dataset/*`; deviations violate the critical handling directive.

## Sequence & Table Sanitation
- Reject malformed rows: enforce uppercase amino-acid alphabet, strip whitespace, and preserve chain-length parity (VH/VL rows must co-exist).
- Validate that fold columns (`random_fold`, `hierarchical_cluster_fold`, `hierarchical_cluster_IgG_isotype_stratified_fold`) contain integers in the expected range.
- Capture null counts per assay target and drop only rows missing the modeling target (e.g., `HIC`) to preserve cohort statistics.

## Alignment & Numbering Fidelity
- Trust the provided AHO-aligned strings; re-numbering is optional but, if performed, use ANARCI/IgBLAST with explicit version logging.
- Preserve pairing identifiers (`antibody_id`, `antibody_name`) alongside alignment outputs so VH/VL linkage survives downstream merges.

## Structure Asset Handshake
- Link GDPa1 antibodies to the ABodyBuilder3 structures added in the 2025-07-03 update; store URIs + hash manifests next to sequence rows.
- Flag antibodies lacking structures so feature builders can fall back to sequence-only descriptors.

## Output Artifacts
- Emit a `bioinformatics_pipeline_report.json` capturing hashes, null audits, alignment tool versions, and structure availability.
- Persist cleaned tables with suffix `clean.csv` and include fold columns untouched to keep cross-validation integrity.

## Related Mesh Topics
- `semantic_mesh/concepts/dataset_access_controls.md`
- `semantic_mesh/concepts/cross_validation_integrity.md`
- `competition_public/GDPa1 Dataset Overview.md`
