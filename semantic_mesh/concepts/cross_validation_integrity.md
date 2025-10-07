# Cross-Validation and Data Integrity Rules

updated_utc: 2025-10-05T13:15:00Z  
sources: `competition_public/dataset/README.md`, `semantic_mesh/concepts/protocols.md`, `research_plans/initial_plan/plan.md`

## Fold Stewardship
- Use `hierarchical_cluster_IgG_isotype_stratified_fold` exactly as provided; never reshuffle globally.
- Maintain consistent fold ordering across experiments to simplify comparisons.
- Track fold membership hashes in `data/fold_hashes.json` (pending automation).

## Leakage Prevention
- Fit preprocessing (scalers, PCA, feature selection) on training folds only.
- Prohibit cross-fold feature sharing (e.g., Markov models, embedding finetunes) without explicit leakage audit.
- For ensembling, restrict meta-learner training to out-of-fold predictions.

## Data Provenance
- Record SHA256 of GDPa1 CSVs and any derived datasets; log to `semantic_mesh/library/catalog.yaml`.
- Document external feature tables (IgFold, LM embeddings) with generation date and script hash.

## Integrity Checks
- Duplicate/alias detection via sequence hashing and Levenshtein radius <= 2.
- Sequence alphabet validation; reject sequences containing non-canonical amino acids.
- Fold stratification audit — ensure class balance of assays remains within ±5% across folds.

## Related Mesh Topics
- `semantic_mesh/concepts/bioinformatics_pipeline.md`
- `semantic_mesh/concepts/dataset_access_controls.md`
- `semantic_mesh/concepts/validation_evaluation_logic.md`
