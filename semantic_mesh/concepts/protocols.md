# Antibody Developability Protocol Stack

Aligned with `research_plans/initial_plan/plan.md`, `flow.md`, and `gaps.md`.

## 1. Data Intake & Hygiene
- Download GDPa1_v1.2 via Hugging Face (authenticated) and record SHA256.
- Verify antibodies align with canonical `antibody_name` list; halt if extras or duplicates appear.
- Preserve provided fold column `hierarchical_cluster_IgG_isotype_stratified_fold` for CV workstreams.

## 2. Feature Build Loop
- **ANARCI pass** → emit FR/CDR boundaries, chain types, numbering sanity checks.
- **Sequence anatomy** → compute lengths, charge, hydropathy, amino-acid frequencies per region.
- **Markov/surprisal** → train fold-specific n-gram models (k=3/4/5, forward & reverse) and gather log-prob, surprisal, entropy rate.
- **Pattern-based tests (PBT)** → deterministic heuristics (two-pointer, sliding window, trie hits, DP alignment) with per-region outputs.
- **Optional structure-lite** → IgFold loop summaries and contact counts once licensing is cleared (see `gaps_risks.md`).

## 3. Training Cycle
- Use 5-fold stratified CV; maintain per-fold checkpoints and logs.
- Curriculum schedule: order batches by surprisal tiers, elevate high-surprisal examples gradually.
- Integrate LM embeddings (ESM-2/AntiBERTa/AbLang/BALM) either as features or joint encoder; record model hash and config.
- Apply entropy-aware loss weighting and consider shrinkage toward fold means for high-entropy predictions.

## 4. Evaluation & QA
- Compute Spearman + top-10% recall locally using mirrored leaderboard scripts; log per-property metrics.
- Run QA gates: amino-acid alphabet validation, fold integrity, surprisal drift (KL), duplicate detection, entropy thresholds, and PBT anomaly scans.
- Flag submissions where public-set Spearman exceeds 0.9 before upload; investigate leakage.

## 5. Submission Workflow
- Compose CSV with `antibody_name` + predicted assays (and fold column for CV track).
- Exclude NaNs; round only for presentation after QA passes.
- Record submission hash, metrics, runtime environment, and mesh node references in the run log.
- Upload via HF leaderboard submit tab using registered code; archive response + timestamps.

## 6. Governance Hooks
- Enforce `AGENTS.md` validation gates: diff hygiene, rollback plan, reproducibility, evidence logs.
- Track external artefact licenses (IgFold, HMMER3, AntiBERTa) and document approvals.
- Update `mesh_manifest.yaml` and `library/catalog.yaml` when new artefacts reach “ready” state.