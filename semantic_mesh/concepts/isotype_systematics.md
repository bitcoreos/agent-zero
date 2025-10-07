# IgG Isotype Systematics

sources: `competition_public/GDPa1 Dataset Overview.md`, `competition_public/How to Train an Antibody Developability Model.md`, `research_plans/initial_plan/plan.md`

## Distribution & Metadata
- GDPa1 spans IgG1, IgG2, and IgG4 subclasses; retain `heavy_chain_subclass` as a categorical feature.
- Document clinical status metadata alongside subclass to detect biases (e.g., approved therapeutics clustered in IgG1).

## Assay Impact
- Tm2 shows subclass-dependent shifts; encode subclass to prevent thermal predictions from reflecting isotype leakage.
- Expression and polyreactivity assays also inherit subclass effects through Fc and hinge biochemistry; monitor per-subclass residuals.

## Feature Encoding Strategy
- One-hot encode subclasses or embed via learned vectors; persist the mapping in config to keep CV reproducible.
- Include interaction terms between subclass and key sequence descriptors (e.g., CDR hydropathy) to capture coupled effects.

## Cross-Validation Guardrails
- Use `hierarchical_cluster_IgG_isotype_stratified_fold` for all leaderboard-facing metrics; it balances clusters by subclass.
- When forming custom folds, enforce subclass stratification and document the seed + clustering method.

## Monitoring & Diagnostics
- Produce per-subclass parity plots for each assay; deviations >0.05 Spearman vs overall signal require investigation.
- Alert if any fold lacks a subclass, which indicates leakage or dataset corruption.

## Related Mesh Topics
- `semantic_mesh/concepts/bioinformatics_pipeline.md`
- `semantic_mesh/concepts/ai_finetuning_pipeline.md`
- `semantic_mesh/concepts/validation_evaluation_logic.md`
