# Ensembling and Post-Processing Strategies

updated_utc: 2025-10-05T13:17:00Z  
sources: `research_plans/initial_plan/plan.md`, `semantic_mesh/concepts/semantic_mesh_concepts.md`, `semantic_mesh/concepts/protocols.md`

## Ensemble Blueprint
- **Member models**: gradient boosted trees, multi-task FFN, transformer fine-tune, Markov regression head.
- **Stacking**: train ridge/meta-learner on out-of-fold predictions; enforce sum of weights = 1.
- **Diversity levers**: vary LM layers, k-mer ranges, and hyperparameters per member.

## Calibration
- Apply temperature scaling per assay using validation folds.
- Perform isotonic regression as fallback if calibration drift detected.

## Post-Processing Steps
1. Clip predictions to training label range ± (1.5 × IQR) to prevent leaderboard rejections.
2. Blend ensemble outputs; log component contributions.
3. Recalculate metrics post-blend to confirm improvement.
4. Package final predictions with provenance metadata (model IDs, weights, calibration constants).

## Monitoring
- Track ensemble diversity metrics (pairwise Spearman, error correlation).
- Flag if any member dominates (>0.7 weight) across assays — indicates over-reliance.

## Maintenance
- Update ensemble roster after each major model addition/removal.
- Document calibration drifts and mitigation steps in `reports/calibration/`.

## Related Mesh Topics
- `semantic_mesh/concepts/model_architectures_training.md`
- `semantic_mesh/concepts/validation_evaluation_logic.md`
- `semantic_mesh/concepts/ai_finetuning_pipeline.md`
