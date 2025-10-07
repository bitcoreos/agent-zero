# Sequence and Structural Feature Ledger

updated_utc: 2025-10-05T13:10:00Z  
sources: `competition_public/GDPa1 Dataset Overview.md`, `semantic_mesh/concepts/context_terms.yaml`, `semantic_mesh/concepts/semantic_mesh_concepts.md`

## VH/VL Segmentation
- **ANARCI numbering** is the source of truth for FR/CDR boundaries. Persist numbering metadata next to derived features (`context_terms.yaml#anarci_numbering`).
- Record heavy/light chain pairing and isotype annotations; downstream models use these as conditioning inputs.

## Regional Descriptor Menu
| Region | Descriptor | Notes | Citation |
| --- | --- | --- | --- |
| CDR-H3 | Kyte–Doolittle mean hydropathy | Captures exposed hydrophobic patches driving HIC variation | [Kyte & Doolittle 1982](./competition_target_alignment.md#references) |
| CDR-L1 | Net charge at pH 7.4 | Signals polyreactive hotspots | [Jain et al. 2017](./competition_target_alignment.md#references) |
| Framework (FR1–FR4) | Aromatic residue density | High density correlates with self-association risk | [Jain et al. 2017](./competition_target_alignment.md#references) |
| VH/VL interface | Predicted hydrogen bonds (IgFold-lite) | Input to thermostability models | [Chennamsetty et al. 2009](./competition_target_alignment.md#references) |
| Whole chain | N-linked glycosylation motif count (`NXS/T`) | Impacts titer and manufacturability | [How to Train AbDev Baseline](./competition_target_alignment.md#references) |


## Related Mesh Topics
- `semantic_mesh/concepts/bioinformatics_pipeline.md`
- `semantic_mesh/concepts/isotype_systematics.md`
- `semantic_mesh/concepts/biophysics_interpretation.md`
## Structure-Lite Hooks

## Export Schema (YAML stub)
```yaml
vh_chain:
  cdr3:
    hydropathy_mean: float
    hydropathy_std: float
    net_charge_pH7: float
  framework:
    aromatic_density: float
    glyco_motif_count: int
vl_chain:
  cdrs:
    - id: CDR-L1
      net_charge_pH7: float
      hydropathy_mean: float
igfold:
  loops:
    H3:
      rmsd: float
      contacts: int
```

## Maintenance
- Validate feature ranges every sprint; drift beyond historical bounds triggers QA review.
- Update this ledger when new descriptors enter the production pipeline and add citations to `semantic_mesh/REFERENCES.md`.
