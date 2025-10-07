# Submission Automation Checklist

sources: `competition_public/AbDev Leaderboard Overview.md`, `semantic_mesh/concepts/submission_schema_standards.md`, `competition_public/How to Train an Antibody Developability Model.md`

## Credential Handling
- Store the Hugging Face submission code in a secrets manager; inject via environment variable at runtime.
- Rotate the code if exposure is suspected and log rotation in governance records.

## Cross-Validation Package
- Emit `cv_predictions_<assay>.csv` containing `antibody_name`, fold column, and predicted values; enforce schema from `submission_schema_standards.md`.
- Attach per-fold metrics (Spearman/top-decile recall) in `cv_metrics.json` to support leaderboard audits.

## Private Test Submission
- Load heldout sequences from `competition_public/dataset/heldout-set-sequences.csv` in read-only mode.
- Generate predictions with the locked model checkpoint, hash the output, and export `test_predictions_<assay>.csv`.

## Validation & QA
- Run schema validator + checksum check before upload; block submission if column order, dtype, or hash deviates.
- Include dry-run upload using the Hugging Face API sandbox when available to confirm acceptance.

## Logging & Traceability
- Log timestamp, git commit, model artefact ID, and submission hash in `submissions/log.csv`.
- Archive zipped submission bundles for reproducibility and potential prize audits.

## Related Mesh Topics
- `semantic_mesh/concepts/submission_schema_standards.md`
- `semantic_mesh/concepts/validation_evaluation_logic.md`
- `semantic_mesh/concepts/dataset_access_controls.md`
