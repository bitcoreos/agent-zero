# Antibody Developability Competition Model Requirements

## Overview
This document specifies the requirements for predictive models in the Antibody Developability Competition. These requirements ensure that all submissions are comparable, reproducible, and scientifically valid.

## Input Requirements

### 1. Input Data
- **Primary Input**: Antibody amino acid sequences in FASTA format
- **Sequence Format**: Single-letter amino acid code (ACDEFGHIKLMNPQRSTVWY)
- **Sequence Length**: Variable length sequences (typically 110-140 amino acids for VH domain)
- **Input Representation**: Models may use any sequence encoding method (one-hot, BLOSUM, embeddings, etc.)
- **Additional Features**: Models may incorporate physicochemical properties or structural predictions

### 2. Data Preprocessing
- **Sequence Validation**: All input sequences must be validated for correct amino acid alphabet
- **Error Handling**: Invalid sequences should be flagged and excluded from analysis
- **Normalization**: Any feature scaling must be performed using training set statistics only
- **Cross-Validation**: Preprocessing pipelines must be fitted on training folds only to prevent data leakage

## Model Architecture Requirements

### 1. Algorithm Flexibility
- **Allowed Methods**: Any machine learning or deep learning approach is permitted
  - Traditional ML: Random Forest, Gradient Boosting, SVM, etc.
  - Deep Learning: CNN, RNN, Transformer, Graph Neural Networks, etc.
  - Hybrid approaches combining multiple methods
  - Physics-based or knowledge-guided models
- **Pretrained Models**: Use of pretrained protein language models (e.g., ESM, ProtBERT) is allowed
- **Ensemble Methods**: Model ensembles are permitted with proper documentation

### 2. Architecture Constraints
- **Reproducibility**: All random seeds must be fixed for full reproducibility
- **Deterministic Execution**: Models should produce identical outputs for identical inputs
- **Memory Limit**: Training and inference must complete within 32GB of RAM
- **Time Limit**: Full cross-validation must complete within 7 days on a single machine

## Output Specifications

### 1. Prediction Format
- **Required Outputs**: Predictions for all five antibody properties:
  - AC-SINS_pH7.4
  - Tm2
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
  - Complete training code
  - Inference code
  - Environment specification (requirements.txt or Dockerfile)
  - Detailed README with execution instructions
- **Code Quality**:
  - Well-commented and documented
  - Modular and readable
  - Includes error handling
  - Unit tests for critical components

### 2. Environment Specification
- **Python Version**: 3.8-3.10 recommended
- **Dependency Management**: requirements.txt, environment.yml, or Dockerfile
- **Hardware Requirements**: Must specify GPU/TPU requirements if applicable
- **Cloud Compatibility**: Code should be runnable on standard cloud instances

### 3. Execution Protocol
```bash
# Example execution workflow
python setup.py install
python preprocess.py --input data/train.csv --output data/processed/
python train.py --data data/processed/ --folds 5 --output models/
python predict.py --model models/best_model.pkl --test data/test.csv --output predictions/
```

## Performance Expectations

### 1. Baseline Performance
- **Random Baseline**: Spearman correlation ≈ 0.0
- **Simple Baseline**: Linear regression with amino acid composition ≈ 0.3 Spearman
- **State-of-the-Art**: Previous competition winners achieved ≈ 0.6-0.7 Spearman

### 2. Target Performance
- **Competitive Model**: > 0.5 average Spearman correlation
- **Strong Model**: > 0.6 average Spearman correlation
- **Exceptional Model**: > 0.7 average Spearman correlation

## Ethical and Scientific Standards

### 1. Data Usage
- **Permitted Use**: Data may only be used for the Antibody Developability Competition
- **Prohibited Use**: 
  - Commercial applications without permission
  - Redistribution of the dataset
  - Use in publications without proper attribution
- **Attribution**: Any work using this data must cite the competition organizers

### 2. Model Transparency
- **Interpretability**: While not required, interpretable models are encouraged
- **Feature Importance**: Participants are encouraged to analyze and report important features
- **Bias Assessment**: Models should be evaluated for potential biases in predictions

## Submission and Evaluation Timeline

1. **Code Submission Deadline**: October 15, 2025
2. **Model Training Period**: October 15-25, 2025
3. **Hidden Test Set Evaluation**: October 26-30, 2025
4. **Results Announcement**: November 1, 2025

## Technical Support and Clarifications
- **Q&A Forum**: Questions should be posted on the official competition forum
- **Response Time**: Organizers will respond to questions within 3 business days
- **Clarification Updates**: Important clarifications will be posted on the competition website
- **Deadline Extensions**: Only granted for exceptional circumstances

# Model Requirements (Execution Plan Extract)

Sources: `research_plans/initial_plan/plan.md`, `research_plans/initial_plan/gaps.md`, `research_plans/initial_plan/gaps_risks.md`.

## Inputs & Preprocessing
- Work from `competition_public/dataset/GDPa1_v1.2_sequences.csv`; log file hashes for every run.
- Operate on paired VH/VL protein sequences (single-letter alphabet). Run ANARCI numbering before deriving FR/CDR features.
- Fit scalers, encoders, and feature stats within each training fold only. Reject sequences containing non-standard amino-acid tokens.
- Preserve metadata columns (`antibody_name`, assays, `hierarchical_cluster_IgG_isotype_stratified_fold`) so CV joins remain lossless.

## Feature Stack Expectations
- **Sequence anatomy**: per-region lengths, composition, charge, hydropathy (maps to `context_terms.yaml`).
- **Markov & surprisal**: region-aware n-gram log probabilities, entropy rates, forward/reverse averages (`gaps.md §5`).
- **Pattern-based tests (PBT)**: deterministic heuristics (two-pointer, sliding window, trie hits, DP alignment) for redundancy and QA.
- **Protein language models**: at least one embedding route (ESM-2, AntiBERTa, AbLang, BALM) feeding a shared multi-output head or ensemble.
- **Structure-lite (optional)**: IgFold-derived loop summaries and contact counts when licensing clears (`gaps_risks.md`).

## Training Protocol
- Use 5-fold hierarchical IgG-stratified CV. Train on four folds, validate on the held-out fold, retain per-fold checkpoints and metrics.
- Apply surprisal curriculum: begin with lowest-surprisal tiers and progressively unlock high-surprisal sequences.
- Weight losses and calibration steps by entropy where Markov features contribute; shrink high-uncertainty predictions toward fold means before export if QA flags trigger.
- Capture deterministic seeds (`random`, `numpy`, `torch`, etc.) alongside run identifiers and configuration hashes.

## Output & Submission
- Emit predictions for any subset of `{AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer}` with `antibody_name` as the join key.
- CV submissions must add the canonical `hierarchical_cluster_IgG_isotype_stratified_fold`; heldout submissions omit it.
- Refuse to write rows containing NaN/Inf. Persist submission CSV hash plus per-property Spearman/recall in experiment notes.
- Store ancillary artefacts (feature manifests, model weights) with links back to mesh nodes in `mesh_manifest.yaml`.

## Governance & Reproducibility Hooks
- Maintain environment manifests (`requirements.txt`, Conda env, or Docker digest) per run and track GPU/CPU resources consumed.
- Verify licensing for external assets (IgFold, AntiBERTa, HMMER3) before integration; document decisions in `gaps_risks.md`.
- Run QA suite before submission: amino-acid alphabet check, surprisal distribution drift (KL), duplicate/chain swap detection, entropy-gated warnings (`protocols.md`).
- Follow `AGENTS.md` validation gates—diff hygiene, rollback plan, evidence logs—before merging modeling changes into main.