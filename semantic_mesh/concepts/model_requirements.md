# Antibody Developability Competition Model Requirements# Antibody Developability Competition Model Requirements



updated_utc: 2025-10-05T00:00:00Z  ## Overview

sources: `research_plans/initial_plan/plan.md`, `research_plans/initial_plan/gaps.md`, `research_plans/initial_plan/gaps_risks.md`, `competition_public/GDPa1 Dataset Overview.md`This document specifies the requirements for predictive models in the Antibody Developability Competition. These requirements ensure that all submissions are comparable, reproducible, and scientifically valid.



## Submission Contract## Input Requirements

- Submit predictions for any subset of `{AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer}` with the canonical `antibody_name` key.

- Cross-validation track requires the provided `hierarchical_cluster_IgG_isotype_stratified_fold` column; heldout track omits it.### 1. Input Data

- Local validation must mirror leaderboard checks (per `evaluation_metrics.md`) before upload.- **Primary Input**: Antibody amino acid sequences in FASTA format

- **Sequence Format**: Single-letter amino acid code (ACDEFGHIKLMNPQRSTVWY)

## Data Intake & Preprocessing- **Sequence Length**: Variable length sequences (typically 110-140 amino acids for VH domain)

- Operate on `competition_public/dataset/GDPa1_v1.2_sequences.csv`; record file hashes for every run.- **Input Representation**: Models may use any sequence encoding method (one-hot, BLOSUM, embeddings, etc.)

- Run ANARCI numbering on VH/VL chains prior to feature derivation to preserve FR/CDR boundaries.- **Additional Features**: Models may incorporate physicochemical properties or structural predictions

- Reject sequences containing non-canonical amino-acid tokens; log incidents in the run record.

- Fit scalers, encoders, and feature statistics within each training fold only to prevent leakage.### 2. Data Preprocessing

- **Sequence Validation**: All input sequences must be validated for correct amino acid alphabet

## Feature Stack Expectations- **Error Handling**: Invalid sequences should be flagged and excluded from analysis

- **Sequence anatomy**: per-region lengths, composition, charge, hydropathy (see `context_terms.yaml`).- **Normalization**: Any feature scaling must be performed using training set statistics only

- **Markov & surprisal**: region-aware n-gram log probabilities, surprisal tiers, entropy rates (`gaps.md §5`).- **Cross-Validation**: Preprocessing pipelines must be fitted on training folds only to prevent data leakage

- **Pattern-based tests (PBT)**: deterministic heuristics (two-pointer, sliding window, trie hits, dynamic-programming alignments) to surface structural red flags.

- **Protein language models**: embeddings from ESM-2, AntiBERTa, AbLang, BALM feeding multi-output heads or ensembles.## Model Architecture Requirements

- **Structure-lite (optional)**: IgFold loop metrics and contacts once licensing is cleared (`gaps_risks.md`).

### 1. Algorithm Flexibility

## Training Protocol & Curriculum- **Allowed Methods**: Any machine learning or deep learning approach is permitted

- Use five-fold hierarchical IgG-isotype stratified CV; save per-fold checkpoints and logs.  - Traditional ML: Random Forest, Gradient Boosting, SVM, etc.

- Apply surprisal curriculum: begin with low-surprisal tiers, then unlock higher surprisal sequences after convergence checks.  - Deep Learning: CNN, RNN, Transformer, Graph Neural Networks, etc.

- Weight losses and calibration steps by entropy when Markov features contribute; shrink high-entropy predictions toward fold means when QA flags trigger.  - Hybrid approaches combining multiple methods

- Capture deterministic seeds (`random`, `numpy`, `torch`, etc.) alongside configuration hashes for reproducibility.  - Physics-based or knowledge-guided models

- **Pretrained Models**: Use of pretrained protein language models (e.g., ESM, ProtBERT) is allowed

## Output & QA Gates- **Ensemble Methods**: Model ensembles are permitted with proper documentation

- Refuse to emit NaN/Inf; persist submission CSV hash plus per-property Spearman/recall metrics in experiment notes.

- Run QA suite before submission: amino-acid alphabet validation, surprisal drift (KL), duplicate/chain swap detection, entropy-threshold warnings (`protocols.md`).### 2. Architecture Constraints

- Log leaderboard leakage warnings (>0.9 public Spearman) and investigate before re-submitting.- **Reproducibility**: All random seeds must be fixed for full reproducibility

- **Deterministic Execution**: Models should produce identical outputs for identical inputs

## Governance & Reproducibility Hooks- **Memory Limit**: Training and inference must complete within 32GB of RAM

- Maintain environment manifests (`requirements.txt`, Conda env, or Docker digest) per run and include hardware usage notes.- **Time Limit**: Full cross-validation must complete within 7 days on a single machine

- Verify licensing for external artefacts (IgFold, AntiBERTa, HMMER3) prior to integration; record decisions in `gaps_risks.md`.

- Update `mesh_manifest.yaml` and `library/catalog.yaml` when new artefacts or validators land in the mesh.## Output Specifications

- Follow `AGENTS.md` validation gates—diff hygiene, rollback planning, evidence logging—before merging modeling changes into `main`.

### 1. Prediction Format

## Outstanding Build Items- **Required Outputs**: Predictions for all five antibody properties:

- Surprisal assets (`surprisal_buckets.yaml`, `kmer_config.yaml`, `entropy_gate_notes.md`) remain staged in `markov_notes.md`.  - AC-SINS_pH7.4

- Mesh validator script and data manifest (`data/MANIFEST.yaml`) are still pending; see `mesh_bootstrap.md` for backlog context.  - Tm2

  - [Additional properties to be specified]
- **Output Type**: Continuous numerical values in the same units as the training data
- **Confidence Intervals**: Optional, but not required

### 2. Submission File Structure
```csv
sequence_id,AC-SINS_pH7.4,Tm2,[additional_properties],fold
seq_001,0.85,65.2,[values],0
seq_002,0.72,68.1,[values],1
...
```

## Validation and Testing Protocol

### 1. Cross-Validation Requirements
- **Fold Structure**: 5-fold cross-validation with predefined fold assignments
- **Fold Preservation**: Models must respect the exact fold assignments provided in the dataset
- **Training Procedure**: 
  - Train on 4 folds
  - Validate on 1 held-out fold
  - Repeat for all 5 fold combinations
  - Average performance across folds
- **No Fold Leakage**: Absolutely no information from test folds may be used during training

### 2. Evaluation Procedure
- **Primary Evaluation**: Models will be evaluated on a hidden test set not available to participants
- **Metric Calculation**: 
  - Spearman correlation calculated for each property independently
  - Top-10% recall calculated for each property
  - Final score = (0.6 × Average Spearman) + (0.4 × Average Recall)
- **Statistical Significance**: Performance differences will be assessed for statistical significance

## Reproducibility Requirements

### 1. Code Submission
- **Required Components**: