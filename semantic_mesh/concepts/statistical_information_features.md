# Statistical and Information-Theory Features

updated_utc: 2025-10-05T13:18:00Z  
sources: `semantic_mesh/concepts/markov_notes.md`, `semantic_mesh/concepts/semantic_mesh_concepts.md`, `research_plans/initial_plan/gaps.md`

## Markov Modeling
- Train k-mer models (k = 2–5) per chain and region.
- Retain transition matrices, backoff counts, and smoothing parameters.
- Emit surprisal per residue, aggregated statistics per region (mean, max, percentile bins).

## Entropy & Surprisal
- Compute Shannon entropy rate and conditional entropy for each sequence.
- Bucket sequences into surprisal tiers (low, medium, high) used by curriculum and QA gates.
- Store entropy thresholds that trigger gating for ensemble members.

## Information-Theoretic Features
- Mutual information between heavy/light chain k-mer distributions.
- Jensen–Shannon divergence between sequence and training distribution; flag OOD risk.
- Cross-entropy between observed sequences and reference germline models.

## Smoothing Techniques
- Kneser–Ney (absolute discounting) for higher-order n-grams; capture `D1`, `D2`, `D3` values.
- Witten–Bell for backoff; store `T` (unique continuation counts).

## Storage Schema
```yaml
markov_models:
  - id: vh_k4
    train_fold: 0
    smoothing: kneser_ney
    discount: [0.75, 0.5, 0.25]
    entropy_rate: 1.87
surprisal_buckets:
  - tier: low
    min: 0.0
    max: 1.5
  - tier: medium
    min: 1.5
    max: 3.0
```

## Maintenance
- Refresh models when dataset expands or new sequences added.
- Version configuration files (`markov_notes.md`) and align with feature registry.
