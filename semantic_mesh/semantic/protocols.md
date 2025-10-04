# Antibody Developability Competition Protocols

This document outlines the standard protocols and procedures for the Antibody Developability Competition, covering data processing, feature engineering, model training, and evaluation workflows.

## Data Acquisition & Processing

### Dataset Acquisition
- Obtain the GDPa1 dataset (246 antibody sequences with 10 developability assays[10]) from Hugging Face
- Use the GDPa1_v1.2 version which includes PR score correction and AC-SINS (pH7.4) data[11]
- Ensure data integrity by verifying checksums and file completeness

### Data Processing
- Use only the first production batch for each antibody to avoid batch effects
- Compute median of any replicates to consolidate data[22]
- Handle missing values according to the dataset documentation (GDPa1_v1.2 cleaned PR score[11])
- Normalize assay values if required by the modeling approach
- Store processed data in a structured format (e.g., CSV or Parquet)

## Train/Test Splitting

### Cross-Validation Strategy
- Follow the provided fold splits from GDPa1_v1.2
- Use the hierarchical isotype-stratified clusters (5 folds) to train and internally validate models[14]
- This ensures:
  - No heavy chain identity >~70% between folds
  - Equal IgG1/4 ratios in each fold[14]
  - Prevention of data leakage

### Split Implementation
- Load the fold assignments from the dataset metadata
- Verify the stratification by checking isotype distribution across folds
- Optionally explore random or simple stratification folds for comparison
- The balanced-cluster fold is recommended for primary analysis

## Feature Engineering

### Sequence Descriptors
- Compute amino-acid composition (frequency of each amino acid)
- Calculate physicochemical properties:
  - Charge (isoelectric point)
  - Hydrophobic moment
  - Aliphatic index
  - Instability index
- Extract CDR (Complementarity Determining Region) features:
  - Length of CDR1, CDR2, CDR3 regions
  - Amino acid composition of CDR regions
  - Net charge of CDR regions
- These features capture solubility and stability cues[5]

### Embedding Representations
- Use pretrained protein language models:
  - ESM (Evolutionary Scale Modeling) family
  - ProtTrans models
  - AntiBERTy
- Generate embeddings by:
  - Feeding sequences through the model
  - Extracting hidden states (mean or CLS token vectors)
  - Using these as features for downstream models
- NLP techniques with transformers trained on large protein corpora have advanced antibody ML[23]

### Evolutionary Features
- If multiple sequence alignments or homologs are available:
  - Compute conservation scores (e.g., Jensen-Shannon divergence)
  - Calculate covariance ("coupling") features between residue pairs[24]
- Coupling analysis (a form of co-evolutionary modeling) identifies residue-residue interactions important for structure/function[24]
- Use direct coupling analysis (DCA) or plmDCA to extract evolutionary constraints

### Structural Features
- Predict 3D structure using:
  - ABodyBuilder (antibody-specific structure prediction)
  - AlphaFold2 or RoseTTAFold
  - Other protein structure prediction tools
- Derive features from predicted structures:
  - Solvent-accessible surface area (SASA)
  - Predicted stability scores (e.g., ΔΔG for mutations)
  - Inter-residue contacts and distances
  - Electrostatic potential maps
- As in Bashour et al.[25], calculate structure-derived developability parameters

### Isotype/Metadata Features
- Encode IgG subclass (IgG1, IgG2, IgG3, IgG4) using one-hot encoding
- Include chain type (heavy chain, light chain, Fv, Fab) as categorical feature
- Add metadata such as expression system, purification method if available
- IgG1 vs IgG4 can affect thermostability and polyreactivity

## Model Training

### Baseline Models
- Start with simple models for benchmarking:
  - Linear regression (Ridge, Lasso)
  - Decision trees and random forests
  - Support vector machines
  - Gaussian processes
- These provide a performance baseline and help identify informative features

### Neural Networks and Language Models
- Use feedforward neural networks on engineered features
- Fine-tune transformer language models on sequences with regression heads:
  - Use ESM or ProtTrans as encoders[23]
  - Add regression head for each target property
  - Implement multi-task learning for all five properties
- Consider attention mechanisms to identify important sequence regions

### Markov/HMM Models
- Train hidden Markov models (HMMs) on sequence data to capture sequential dependency[17]
- Use profile HMMs for antibody families
- Implement mixture of HMMs to represent different antibody classes
- Use HMMs as generative sequence models to score sequences

### Coupling-based Models
- Use evolutionary coupling matrices as input to ML models
- Project direct coupling (DCA) scores into features
- Use graph neural networks on coupling matrices
- Combine coupling features with other feature types in ensemble models

### Curriculum Learning
- Implement training schedule from easy to hard examples[3]:
  - Sort training examples by antibody sub-family similarity
  - Sort by predicted confidence or uncertainty
  - Start with high-confidence predictions, progress to borderline cases
  - Use sequence diversity as difficulty metric
- This approach can improve convergence and generalization[3]

### Ensembling
- Combine multiple models to improve stability and performance[6]:
  - Average predictions from diverse model types (neural net, gradient boosting, LSTM)
  - Use voting for classification tasks
  - Implement stacking with a meta-model
  - Weight models by cross-validation performance
- Ensemble techniques reduce variance and bias, often outperforming single models[6]

## Training Validation

### Cross-Validation
- Perform 5-fold cross-validation using the provided fold assignments
- Train on 4 folds, validate on 1 held-out fold
- Repeat for all 5 fold combinations
- Average performance across folds

### Hyperparameter Tuning
- Use the validation fold to tune hyperparameters
- Evaluate Spearman correlation on left-out fold predictions
- Use grid search, random search, or Bayesian optimization
- Ensure no data leakage by using only training folds for feature scaling and preprocessing

### Regularization and Early Stopping
- Apply appropriate regularization techniques (L1, L2, dropout)
- Use early stopping based on validation performance
- Monitor for overfitting by comparing training and validation metrics

## Prediction Submission

### Prediction Generation
- Generate predictions for all 80 held-out sequences in the validation set[10]
- Ensure predictions are in the same units as training data
- Handle edge cases and outliers appropriately

### Submission File Format
- Create a CSV file with one row per antibody
- Include columns for each target property:
  - `sequence_id`: Unique identifier for each antibody
  - `Hydrophobicity`: Predicted HIC value
  - `Polyreactivity`: Predicted PR_CHO value
  - `Self-association`: Predicted AC-SINS value
  - `Thermostability`: Predicted Tm2 value
  - `Titer`: Predicted expression yield
  - `fold`: Cross-validation fold assignment (0-4)
- Ensure no NaN values in the submission

### Submission Process
- Validate submission file against the required format
- Compress file as ZIP if required
- Submit via the leaderboard platform
- Keep a local copy of the submission for reproducibility

## Evaluation Protocol

### Private Test Set
- The private test labels are withheld from participants
- After submission, organizers evaluate predictions against true values
- Final scoring occurs against the withheld true values[10]

### Leaderboard Updates
- Public leaderboard is updated with scores after submission
- Scores include:
  - Spearman correlation for each property
  - Top-10% recall for each property
  - Weighted combination of metrics
- Final ranking is based on the private test set performance

### Performance Analysis
- Analyze model performance by fold and isotype
- Identify systematic biases or limitations
- Perform error analysis on poorly predicted samples
- Document findings for model improvement

## Best Practices

### Reproducibility
- Fix random seeds for full reproducibility
- Document all preprocessing steps and hyperparameters
- Use version control for code and data
- Containerize the environment (Docker) if possible

### Data Leakage Prevention
- Never use test set information during training
- Fit preprocessing pipelines (scalers, encoders) only on training data
- Validate that no information from test sequences leaks into features

### Model Interpretability
- Analyze feature importance (SHAP values, permutation importance)
- Identify which sequence features drive predictions
- Visualize attention weights for transformer models
- Document key findings about developability determinants

### Computational Efficiency
- Optimize code for speed and memory usage
- Use efficient data structures and algorithms
- Parallelize computations when possible
- Monitor resource usage during training

This protocols document provides a comprehensive guide for participating in the Antibody Developability Competition, ensuring standardized approaches and reproducible results.