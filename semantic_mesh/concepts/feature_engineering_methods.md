# Feature Engineering Methods Guide

updated_utc: 2025-10-05T13:12:00Z  
sources: `research_plans/initial_plan/plan.md`, `research_plans/initial_plan/gaps.md`, `semantic_mesh/concepts/semantic_mesh_concepts.md`

## Statistical Feature Stack
1. **Markov n-gram models** — Train chain-specific models (k = 3, 4, 5) on GDPa1 training folds; emit log-probability, surprisal, entropy, and backoff counts. Reference configs live in `semantic_mesh/concepts/markov_notes.md`.
2. **Smoothing** — Apply Kneser–Ney and Witten–Bell smoothing; store discount parameters per fold.
3. **Region-specific scaling** — Normalize surprisal within each FR/CDR to avoid over-representing long regions.

## Physicochemical Feature Stack
- **Hydropathy profiles** (Kyte–Doolittle) aggregated per region.
- **Charge descriptors**: net charge at pH 4, 7.4, and 9; isoelectric point estimates via IPC (document method in run logs).
- **Aromatic/Aliphatic ratios**: flagged for self-association risk.
- **Glycosylation and deamidation motifs**: count `NXS/T`, `DSX`, `NG` patterns.

## Language-Model Embeddings
- **ESM-2** (650M or 3B) pooled embeddings; store layer selection and pooling strategy.
- **AntiBERTa** heavy/light embeddings; align to ANARCI numbering for per-position features.
- **AbLang** germline-corrected embeddings for OOD mitigation.

### Dimensionality Reduction
- Run PCA/UMAP within each fold for interpretability exports; keep full embeddings for model input.
- Record explained variance ratios and component loadings.

## Pattern-Based Tests (PBT)
- Deterministic heuristics capturing red-flag motifs (e.g., `DPW`, `YY` clusters) with references to curated rule set.
- Sliding-window hydrophobic patch detector, two-pointer charge-run detector, and motif trie lookups.

## Feature Registry Schema
Store metadata in `features/registry.yaml` (pending automation) with fields:
```yaml
- id: cdrh3_hydropathy_mean
  source: sequence_structural_features
  method: kyte_doolittle
  window: full_region
  citations: [KyteDoolittle1982]
- id: vh_markov_surprisal_k4
  source: statistical_information_features
  method: markov_ngram
  params:
    k: 4
    smoothing: kneser_ney
  citations: [MarkovNotes]
```

## Maintenance Hooks
- Attach Git commit SHA and dataset hash to each derived feature batch.
- Update this document whenever a new feature enters production; append citation IDs to `semantic_mesh/REFERENCES.md`.

## Related Mesh Topics
- `semantic_mesh/concepts/sequence_structural_features.md`
- `semantic_mesh/concepts/ai_finetuning_pipeline.md`
- `semantic_mesh/concepts/statistical_information_features.md`
