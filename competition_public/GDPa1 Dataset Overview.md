# GDPa1: Antibody Developability Dataset

**Source:** [Hugging Face Datasets — ginkgo-datapoints/GDPa1](https://huggingface.co/datasets/ginkgo-datapoints/GDPa1)  
**Maintainer:** Ginkgo Datapoints  
**Modalities:** Tabular, text  
**File Format:** CSV  
**Dataset Size:** 246 antibodies (<1K rows)  
**Tags:** biology, protein, antibody  
**Primary Libraries:** `datasets`, `pandas`

## Access Requirements
- The dataset is **gated**: acceptance of the license/terms and an authenticated Hugging Face session (e.g., via `huggingface-cli login`) are required before any files can be downloaded.  
- Files reside at `hf://datasets/ginkgo-datapoints/GDPa1/` and become accessible only after authentication is completed.

## Dataset Contents
- Developability assays for 242 antibodies across nine assays, derived from the PROPHET-Ab high-throughput platform.  
- Primary CSV versions include `GDPa1_v1.1_20250612.csv` (median-aggregated tidy data) and `GDPa1_v1.2_20250814.csv` (latest release referenced in usage examples).  
- Each record provides paired VH/VL sequences alongside assay measurements and precomputed cross-validation folds.

### Developability Assays
- **Production QC:** Valita titer, rCE-SDS purity, SEC % monomer.  
- **Hydrophobicity:** HIC, SMAC.  
- **Self interaction:** AC-SINS (pH 6.0 and 7.4), DLS-kD (subset of antibodies).  
- **Polyreactivity:** CHO and ovalbumin bead-based scores.  
- **Thermostability:** nanoDSF (Tonset, Tm1, Tm2) and DSF measurements.  
- **Functional / clearance indicators:** FcRn binding, heparin binding, functional assays from the full datasheet.  
- **Metadata:** IgG heavy/light chain subtype, clinical status, production fold assignments.

### Cross-Validation Columns
- `random_fold`: random splits.  
- `hierarchical_cluster_fold`: MMseqs2 sequence-identity clustering.  
- `hierarchical_cluster_IgG_isotype_stratified_fold`: cluster-based splits with IgG subclass balancing (recommended for reporting).

### Schema Highlights (from the dataset viewer)
- **Identifiers & metadata:** `antibody_id`, `antibody_name`, heavy/light chain subtype, clinical Phase status as of Feb 2025, estimated development status.  
- **Production & quality metrics:** `Titer`, `Purity`, `SEC %Monomer`, along with column averages shown in the viewer to set expectations (e.g., titer ≈34.4, purity ≈61.5).  
- **Hydrophobicity & colloidal metrics:** `SMAC`, `HIC`, `HAC`.  
- **Polyreactivity scores:** `PR_CHO`, `PR_Ova`.  
- **Self-interaction assays:** `AC-SINS_pH6.0`, `AC-SINS_pH7.4`.  
- **Thermostability:** `Tonset`, `Tm1`, `Tm2`.  
- **Sequence fields:** VH/VL protein sequences (100–150 AHO-aligned residues), heavy/light DNA sequences (≈700–1,400 bp), and aligned AHO numbering strings.  
- **Fold assignment helpers:** `hierarchical_cluster_fold`, `random_fold`, `hierarchical_cluster_IgG_isotype_stratified_fold`.  
- **Example viewer row:** antibody `GDPa1-001` (abagovomab) illustrates typical field coverage with full heavy/light sequences and associated assay values.

### Antibody Production Notes
- Antibodies were expressed in HEK293F cells and purified with Protein A chromatography prior to assay measurements.  
- DLS-kD measurements used an additional polishing SEC step.  
- A subset of 20 IgGs was produced in ExpiCHO cells and purified via Protein A chromatography.

## Full Datasheet (Excel)
- Column header definitions for auxiliary tables.  
- Antibody sequences.  
- Tidy-format assay data (one row per replicate).  
- Summary statistics (average, standard deviation, replicates).  
- nanoDSF vs. DSF data with matched ramp rates.  
- Prior-literature comparisons aligned with GDPa1 metrics.  
- A "Versioning" sheet catalogs changes across releases.

## Data Processing Pipeline
1. Select only the first production batch (contains all 246 antibodies; removes constant-region variation).  
2. Aggregate replicates by median to generate the main CSV table.  
3. Append cross-validation fold assignments as described above.

## Changelog Highlights
- **2025-08-18:** Updated AC-SINS data with improved curve fitting, corrected PR score calculation, and added the "Versioning" sheet to the Excel datasheet.  
- **2025-07-03:** Added ABodyBuilder3 predicted structures.

## Usage Examples
```python
import pandas as pd

# Requires `huggingface-cli login`
df = pd.read_csv("hf://datasets/ginkgo-datapoints/GDPa1/GDPa1_v1.2_20250814.csv")
```

```python
from datasets import load_dataset

ds = load_dataset("ginkgo-datapoints/GDPa1")
```

## Additional Resources
- PROPHET-Ab preprint describing the platform and assays.  
- Antibody Developability Competition leaderboard: [ginkgo-datapoints/abdev-leaderboard](https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard).  
- General information: [https://datapoints.ginkgo.bio/](https://datapoints.ginkgo.bio/).  
- Contact for dataset questions: [datapoints@ginkgobioworks.com](mailto:datapoints@ginkgobioworks.com).

## PROPHET-Ab Platform (Figure Summary)
- **HT Antibody Production:** Transient IgG, VHH-Fc, VHH-His, and multispecific formats expressed in HEK or CHO cells, followed by high-throughput purification compatible with downstream automation.  
- **Automated Developability Assays:** Robotic workflows capture production QC (titer, % monomer, % purity), polyreactivity (CHO/Ova), clearance proxies (FcRn and heparin binding), hydrophobicity (HIC, SMAC), self-interaction (AC-SINS, DLS-kD), thermostability (nanoDSF/DSF), and functional binding assays. Methods are tuned for throughput, reproducibility, and quality control.  
- **AI/ML-Ready Outputs:** Data pipelines log raw and processed assay results with efficient tracking, enabling direct export for modelling tasks. Example dashboard snapshots in the figure show structured tables and chromatograms.  
- **Applications:** The platform feeds AI/ML model training, antibody discovery campaigns, lead optimization, and drug development loops.  
- **LIMS & Robotics Backbone:** External or internal antibody sources are received, scheduled via Ginkgo OrganiCK workflow design, executed on robotics platforms, analysed on instrumentation, processed through Ginkgo Airflow pipelines, and archived in managed datastores—providing end-to-end traceability for the GDPa1 dataset.
