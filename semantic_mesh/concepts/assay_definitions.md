# Competition Assay Definitions

Source of record: `competition_public/GDPa1 Dataset Overview.md` (PROPHET-Ab platform) and leaderboard constants (`research_plans/initial_plan/plan.md`).

## AC-SINS_pH7.4 — Self-Association
- **What it measures**: Gold nanoparticle shift indicating antibody self-interaction at physiological pH.
- **Why it matters**: High signal flags colloidal instability and viscosity risks during formulation.
- **Notes for modeling**: Lower is better. Leaderboard flips the sign before computing recall.

## PR_CHO — Polyreactivity (CHO Lysate)
- **What it measures**: Bead-based polyspecificity particle (PSP) binding against CHO membrane proteins.
- **Why it matters**: Elevated polyreactivity often predicts nonspecific binding and clearance issues.
- **Notes for modeling**: Lower is better. Track alongside PR_Ova for QA even though it is not scored.

## HIC — Hydrophobic Interaction Chromatography
- **What it measures**: Retention on a high-salt hydrophobic column (longer retention = more hydrophobicity).
- **Why it matters**: High hydrophobicity correlates with aggregation and manufacturability risks.
- **Notes for modeling**: Lower is better. Feature engineering should capture CDR hydropathy signals.

## Tm2 — Thermostability (Fab Domain)
- **What it measures**: Second nanoDSF transition capturing Fab melting temperature.
- **Why it matters**: Higher Tm2 indicates stronger thermal robustness and storage stability.
- **Notes for modeling**: Encode IgG subclass and Markov surprisal to model systematic shifts.

## Titer — Expression Yield
- **What it measures**: Valita titer output (mg/L) from HEK293F expression.
- **Why it matters**: Serves as a production proxy; higher yields reduce cost of goods.
- **Notes for modeling**: Watch for distributional skew; curriculum may need surprisal-aware weighting.