# Model Architectures and Training Protocols

updated_utc: 2025-10-05T13:13:00Z  
sources: `research_plans/initial_plan/plan.md`, `research_plans/initial_plan/flow.md`, `semantic_mesh/concepts/protocols.md`

## Architecture Palette
- **Gradient Boosted Trees** on engineered features (baseline parity).
- **Multi-task Feedforward Network** ingesting concatenated statistical + LM embeddings.
- **Transformer fine-tuning** for sequence-to-property prediction; share encoder across assays with property-specific heads.
- **Stacked ensemble governor** combining tree, FFN, and transformer predictions.

## Training Protocol
1. **Fold setup** — Use hierarchical IgG-isotype stratified 5-fold splits from GDPa1.
2. **Curriculum** — Order batches by surprisal tier; unlock higher surprisal sequences after plateau detection (5 epochs without improvement).
3. **Optimization** — AdamW (`lr=3e-4`) for deep models, `num_boost_round=2000` for tree ensembles with early stopping on validation Spearman.
4. **Regularisation** — Apply dropout (p=0.2) and weight decay (1e-5); add ridge penalty on final layer for uncertainty control.
5. **Checkpointing** — Save per-fold checkpoints with config/seed metadata; log to `runs/` manifest.

## Calibration and Post-Processing
- Temperature scaling per assay using validation fold; record scaling constants.
- Quantile mapping for Titer to align with historical distribution.
- Capture ensemble weights and blending logic (`ensembling_postprocessing.md`).

## Deployment Hooks
- Package inference scripts with deterministic seeding.
- Emit prediction CSV plus metadata JSON (model versions, feature hashes, commit SHA).
- Register artefacts in `semantic_mesh/library/catalog.yaml` when promoted to production.

## Open Items
- Prototype lightweight diffusion or protein-GNN heads (tracked in `research_plans/initial_plan/gaps.md`).
- Integrate structural adapters once IgFold licensing is resolved.
