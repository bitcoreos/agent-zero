# Antibody Developability Competition Evaluation Metrics

## Primary Metrics

### 1. Spearman Correlation
- Measures the rank correlation between predicted and actual values
- Calculated for each of the five antibody properties independently
- Final score is the average Spearman correlation across all properties
- Range: -1 to 1, where 1 indicates perfect positive correlation

### 2. Top-10% Recall
- Measures the proportion of true top 10% performers that are correctly identified in the predicted top 10%
- Calculated for each property where higher values are better
- Final score is the average recall across all applicable properties
- Range: 0 to 1, where 1 indicates perfect recall

## Metric Calculation
```
Spearman = mean(spearman_corr(property_i)) for i in [1,5]
Recall = mean(top_10_recall(property_i)) for applicable properties
```

# Evaluation Metrics & Validation

Sources: leaderboard repository (`evaluation.py`, `validation.py` referenced in `research_plans/initial_plan/plan.md`).

## Metrics Computed by the Leaderboard
- **Spearman correlation (per property)**: ranks predictions vs. ground truth for each of the five assays. Output is per-property plus the mean across submitted columns.
- **Top-10% recall**: after flipping the sign for assays where *lower is better* (HIC, PR_CHO, AC-SINS_pH7.4), recall is measured on the top decile of the adjusted predictions and labels.
- No weighted blend is published; leaderboard tables show both metrics separately. Plan to monitor both.

### Reference Implementation Notes
```python
# evaluation.py snippets (HF Space)
metrics = [spearman(pred[col], truth[col]) for col in submitted_cols]
recall = [recall_at_k(pred[col], truth[col], k=0.1) for col in submitted_cols]
```
- `recall_at_k` handles the sign flip internally for assays flagged `lower_is_better`.
- Public leaderboard uses held-out public labels; final ranking uses private labels unseen by participants.

## Submission Schema Expectations
- **Required column**: `antibody_name` (must match canonical list exactly).
- **Assay columns**: any subset of `{AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer}`; at least one is required. Leave others out rather than emitting NaN.
- **Optional columns**: `vh_protein_sequence`, `vl_protein_sequence` (allowed for reproducibility), metadata columns are ignored.
- **Cross-validation track**: add `hierarchical_cluster_IgG_isotype_stratified_fold` with the exact integer fold provided in GDPa1.
- **Heldout track**: omit fold column; just supply `antibody_name` plus the predicted assays.

## Validation Gate Summary
- **Column check**: rejects missing required columns, unknown column names, or duplicate `antibody_name` rows.
- **Value check**: rejects NaN/Inf, non-numeric entries, or wildly large values (heuristic guardrails in validation script).
- **Fold check**: ensures CV submissions use canonical fold IDs; mismatch is a hard error.
- **Leakage heuristic**: if public-set Spearman > 0.9, the Space raises a warning about potential leakage.

## Local Parity Checklist
- Reuse the leaderboard evaluation code (mirrored under `research_plans/initial_plan/plan.md` references) to score CV predictions locally.
- Confirm that “lower is better” assays have their signs flipped before computing recall or Spearman during local validation.
- Log both metrics per property plus the macro average; compare against public leaderboard once uploaded.

## Reporting
- Include Spearman + recall per property in experiment logs (see `protocols.md`).
- Annotate whether submission targeted GDPa1 public, CV, or heldout track.
- Record GDPa1 CSV hash and commit SHA for each submission to guarantee reproducibility.