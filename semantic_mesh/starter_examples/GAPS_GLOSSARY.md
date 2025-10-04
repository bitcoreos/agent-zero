# Glossary (seed)

Format for each entry:
- Preferred label | Short definition | Ontology URI | Provenance | Canonical impl path (if any)

1. CDR (Complementarity-determining region)
- Definition: Amino-acid segments in antibody variable regions that determine antigen specificity.
- URI: 
- Provenance: research_plans/initial_plan/gaps.md (CDR mentions)
- Impl: features/anarci.py::extract_cdrs

2. FR (Framework region)
- Definition: Structural regions flanking CDRs.
- URI: 
- Provenance: research_plans/initial_plan/gaps.md

3. Surprisal
- Definition: Negative log-probability per residue under a reference language model.
- URI: 
- Provenance: semantic_mesh/semantic/semantic_mesh_concepts.md
- Calculation note: use model log-probabilities normalized by residue count.

4. Entropy
- Definition: Predictive entropy of a model's output distribution; used as uncertainty measure.
- URI: 

5. Fold (CV fold)
- Definition: Cross-validation fold assignment (0..4) used for training/evaluation splits.
- URI: 
- Provenance: semantic_mesh/semantic/evaluation_metrics.md

6. PBT_sw_hydro_max (example feature)
- Definition: Sliding-window max hydropathy (window sizes 7,11,15).
- URI: 
- Impl: features/sliding_window.py::max_hydropathy(window)

(Seed list — expand to top-50 terms, each entry must include URI, provenance, and canonical implementation path where available.)