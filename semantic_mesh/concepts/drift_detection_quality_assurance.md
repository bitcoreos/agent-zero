# Drift Detection and Quality Assurance

updated_utc: 2025-10-05T13:19:00Z  
sources: `semantic_mesh/concepts/protocols.md`, `research_plans/initial_plan/gaps_risks.md`, `semantic_mesh/concepts/validation_evaluation_logic.md`

## Monitoring Metrics
- **Surprisal KL divergence**: compare submission vs. training distribution per assay.
- **Entropy delta**: flag if entropy tier proportions shift >10%.
- **Charge distribution shift**: monitor CDR net charge histograms for PR_CHO.

## QA Gates
- Sequence alphabet validation (only 20 canonical amino acids).
- Fold membership integrity (no missing CV folds).
- Ensemble sanity checks: ensure predictions remain within historical min/max ± safety margin.

## Alerting Workflow
1. Run drift checks after each validation cycle.
2. If thresholds breached, tag run as `blocked` and assign follow-up in issue tracker.
3. Document remediation steps in `reports/drift/`.

## Evidence Logging
- Capture validation logs, drift metrics, and plots in artifacts folder with timestamp.
- Record responsible reviewer and decision outcome per incident.

## Continuous Improvement
- Review drift metrics at sprint retrospectives.
- Update thresholds based on historical analysis and leaderboard feedback.

## Related Mesh Topics
- `semantic_mesh/concepts/validation_evaluation_logic.md`
- `semantic_mesh/concepts/submission_automation.md`
- `semantic_mesh/concepts/dataset_access_controls.md`
