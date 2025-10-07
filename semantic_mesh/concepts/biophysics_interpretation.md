# Biophysics Interpretation Ledger

sources: `competition_public/GDPa1 Dataset Overview.md`, `competition_public/2025 AbDev Competition Overview.md`, `competition_public/How to Train an Antibody Developability Model.md`

## Production Context
- GDPa1 antibodies were produced in HEK293F (primary) or ExpiCHO (subset) cells and purified by Protein A; record cell-line provenance because expression cofactors bias Titer.
- DLS-kD assays include an extra SEC polish step; annotate these samples for downstream comparability checks.

## Hydrophobicity & Aggregation Signals
- HIC retention time and SMAC readings quantify surface hydrophobicity; higher values correlate with aggregation and viscosity risk.
- Couple sequence hydropathy profiles (CDR-focused) with chromatography outputs to triangulate hotspots.

## Self-Association Pathways
- AC-SINS (pH 6.0/7.4) and DLS-kD capture colloidal stability; elevated shifts indicate self-interaction risk during formulation.
- Monitor AC-SINS_pH7.4 specifically for leaderboard scoring and cross-reference with AC-SINS_pH6.0 for mechanistic diagnosis.

## Polyreactivity Drivers
- PR_CHO and PR_Ova bead assays reflect nonspecific binding; high scores imply clearance issues and off-target liabilities.
- Track polyspecificity alongside FcRn/heparin binding measurements when assessing clearance-relevant designs.

## Thermostability Landscape
- nanoDSF-derived Tonset, Tm1, Tm2 profiles reveal unfolding transitions; Tm2 (Fab domain) is leaderboard-critical.
- Compare nanoDSF vs DSF readings to ensure assay agreement; large divergences flag instrumentation drift.

## Expression Yield & Quality
- Valita titer, SEC % monomer, and rCE-SDS purity expose expression bottlenecks and aggregation consequences.
- When optimizing yield, monitor hydrophobicity/self-association metrics to prevent trading stability for productivity.

## Related Mesh Topics
- `semantic_mesh/concepts/assay_definitions.md`
- `semantic_mesh/concepts/sequence_structural_features.md`
- `competition_public/GDPa1 Dataset Overview.md`
