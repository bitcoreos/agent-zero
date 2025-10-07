# Validation and Evaluation Logic

updated_utc: 2025-10-05T13:14:00Z  
sources: `semantic_mesh/concepts/evaluation_metrics.md`, `semantic_mesh/concepts/protocols.md`, `competition_public/AbDev Leaderboard Overview.md`

## Metric Replication
- Mirror leaderboard scripts locally (Spearman, top-10% recall).
- Flip sign for assays where lower is better (HIC, PR_CHO, AC-SINS_pH7.4) before recall/Spearman.
- Log per-property metrics, macro averages, and confidence intervals (bootstrap 1k resamples).

## Validation Pipeline
1. **Schema validation** — ensure required columns present, no unknown columns, unique `antibody_name`.
2. **Value checks** — detect NaN, Inf, or out-of-range predictions; enforce guardrails documented in `protocols.md`.
3. **Drift assays** — run KL divergence on surprisal distributions against training folds.
4. **Leakage detection** — raise warning if public Spearman > 0.9 or if predictions nearly match labels (>0.99 Pearson).

## Reporting
- Persist validation reports under `reports/validation/` with timestamp and commit SHA.
- Record metric deltas versus previous run to capture regression improvements.

## Governance Hooks
- Validation must pass before packaging submission artifacts.
- Attach validation report to PRs touching modeling code; reference `AGENTS.md` QA gate checklist.

## Related Mesh Topics
- `semantic_mesh/concepts/evaluation_metrics.md`
- `semantic_mesh/concepts/submission_automation.md`
- `semantic_mesh/concepts/drift_detection_quality_assurance.md`
