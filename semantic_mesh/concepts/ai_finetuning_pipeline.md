# AI Fine-Tuning Pipeline

sources: `competition_public/How to Train an Antibody Developability Model.md`, `research_plans/initial_plan/plan.md`, `semantic_mesh/concepts/model_architectures_training.md`

## Embedding Backbone
- Use p-IgGen (`ollieturnbull/p-IgGen`) to generate paired VH/VL embeddings; tokenize with start/end markers as in the tutorial.
- Record model revision, tokenizer hash, and device (CPU/GPU) to keep embedding reproducibility.

## Compute & Throughput Budgets
- Baseline: 242 sequences embed in ~60 s on CPU or ~1 s on GPU (per tutorial); log actual throughput for capacity planning.
- Cap batch size at 16 without gradient checkpointing; document any deviations when scaling up fine-tuning.

## Fine-Tuning Loop
- Start with ridge/linear probes for fast baselines, then graduate to shallow MLP heads or light fine-tuning on assay-specific adapters.
- Apply L2 regularization sweeps (α grid) and track Spearman on validation folds; store configs in version-controlled YAML.

## Cross-Validation Discipline
- Train per `hierarchical_cluster_IgG_isotype_stratified_fold`; persist fold predictions for downstream ensembling and drift checks.
- Aggregate metrics with both mean and standard deviation; flag folds deviating >0.1 Spearman from median.

## Packaging & Reproducibility
- Export embeddings, model weights, and config under `artifacts/finetune/<assay>/<timestamp>/` with hash manifests.
- Provide a `train.py --resume` entrypoint that rehydrates tokenizer, model, and data splits for the open-source prize track.

## Related Mesh Topics
- `semantic_mesh/concepts/model_architectures_training.md`
- `semantic_mesh/concepts/feature_engineering_methods.md`
- `semantic_mesh/concepts/submission_automation.md`
