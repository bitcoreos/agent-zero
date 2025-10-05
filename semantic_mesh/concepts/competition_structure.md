# Competition Structure Snapshot

Sources: `competition_public/2025 AbDev Competition Overview.md`, `competition_public/AbDev Leaderboard Overview.md`, `research_plans/initial_plan/plan.md`.

## Tracks & Artefacts
- **GDPa1 (public)**: 246 paired VH/VL antibodies with assays and canonical folds.
- **GDPa1_cross_validation**: submissions must include `hierarchical_cluster_IgG_isotype_stratified_fold` column.
- **Heldout test set**: 80 antibodies without labels, scored privately after final submissions.

## Targets
- Five leaderboard properties: HIC, PR_CHO, AC-SINS_pH7.4, Tm2, Titer.
- Additional assays (e.g., SMAC, PR_Ova, Tonset) exist in GDPa1 but are not scored; use for QA only.

## Timeline
- Early scoring window: per plan, align internal dry-run by **2025-10-13**.
- Final submission deadline: **2025-11-01** (per Ginkgo rules PDF).
- Winners announced: November 2025.

## Registration & Submission Flow
1. Accept GDPa1 license on Hugging Face and log in (HF CLI recommended for scripts).
2. Register team via Ginkgo Datapoints form to receive submission code.
3. Produce CSV conforming to leaderboard schema (see `evaluation_metrics.md` for column rules).
4. Upload via Hugging Face Space submit tab; expect validation checks covering columns, NaNs, duplicate antibodies, and fold mismatches.

## Guardrails From Leaderboard Code
- Submissions with public-set Spearman > 0.9 trigger leakage warnings.
- Missing or extra columns, NaNs, or wrong fold assignments cause hard failures.
- Both public and CV tracks enforce one row per `antibody_name` drawn from the canonical list.

## Internal Coordination Hooks
- Reference `mesh_manifest.yaml` to keep track-to-artifact mapping explicit.
- Log every submission in run records with hash of GDPa1 CSV used.
- Keep surprise-checks (KL on surprisal distributions, QA flags) wired before upload as described in `protocols.md`.