# Submission Schema and File Standards

updated_utc: 2025-10-05T13:16:00Z  
sources: `competition_public/AbDev Leaderboard Overview.md`, `semantic_mesh/concepts/evaluation_metrics.md`, `semantic_mesh/concepts/protocols.md`

## CSV Schema
- Required columns: `antibody_name`, plus one or more of `{AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer}`.
- Cross-validation track additionally requires `hierarchical_cluster_IgG_isotype_stratified_fold`.
- Omit assays that are not predicted; do **not** include empty columns.

## Formatting Rules
- Sort rows by `antibody_name` for deterministic diffs.
- Use UTF-8 encoding without BOM; newline = `\n`.
- Numeric precision: store raw float outputs (no rounding) to avoid degrading metrics.

## Validation Metadata
- Provide companion JSON manifest with: model IDs, feature hashes, validation metrics, dataset SHA256, timestamp, Git commit.
- Retain local artifact path to validation report for reproducibility.

## Submission Workflow
1. Run validation pipeline (`validation_evaluation_logic.md`).
2. Generate CSV + manifest; compute SHA256 and log under `submissions/ledger.csv`.
3. Upload via leaderboard interface; capture response ID and store in ledger.

## Change Management
- Document schema changes in PR description and update `mesh_topics.yaml`.
- Notify governance lead before altering submission column logic.
