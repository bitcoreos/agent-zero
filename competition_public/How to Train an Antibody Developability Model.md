# How to Train an Antibody Developability Model

**Source:** [Hugging Face Blog](https://huggingface.co/blog/ginkgo-datapoints/making-antibody-embeddings-and-predictions)  
**Published:** September 17, 2025  
**Authors:** Georgia Channing (cgeorgiaw), Lood van Niekerk (loodvanniekerkginkgo), Ginkgo Datapoints (ginkgo-datapoints)

## Introduction
Antibody development aims to engineer therapeutic antibodies with favorable biophysical properties such as strong expression, high stability, and low aggregation risk. Unlike simple protein point mutations, optimizing antibodies is challenging because pairing VH (variable heavy) and VL (variable light) domains generates a vast sequence space where small modifications can radically change folding, binding, or developability. Laboratory assays that probe these effects are costly and time-intensive, motivating machine learning approaches that learn from antibody sequence data. Protein language models can capture sequence–structure–function relationships and guide antibody design decisions.

## The GDPa1 Dataset
The GDPa1 dataset contains paired VH/VL antibody sequences with experimentally measured developability assays, including expression yield, hydrophobicity, stability, and self-interaction. The dataset serves as a benchmark for evaluating whether models such as p-IgGen can produce embeddings that generalize across assays and predict developability outcomes.

### Available Assays
- **Titer:** Expression yield in mammalian cells.  
- **HIC (Hydrophobic Interaction Chromatography):** Proxy for hydrophobicity and aggregation propensity.  
- **PR_CHO:** Polyreactivity in Chinese hamster ovary (CHO) cells.  
- **Tm2:** Thermal stability (melting temperature of the CH2 domain).  
- **AC-SINS_pH7.4:** Self-interaction propensity; higher values often indicate poor developability.

### Isotype Effects
GDPa1 antibodies span multiple IgG subclasses (IgG1, IgG2, IgG4). Measurements such as Tm2 are strongly influenced by subclass identity, which can overshadow sequence-level variation. Including the subclass as a feature can improve model performance. A boxplot of Tm2 grouped by isotype illustrates these systematic differences.

## Workflow Overview
1. **Embed VH/VL pairs with p-IgGen.**  
2. **Train regression models on individual assay targets.**  
3. **Evaluate generalization with cluster- and isotype-aware cross-validation.**

## Data Preparation and Exploration
Using Hugging Face Datasets, the GDPa1 training split is loaded into a Pandas DataFrame. Analysts inspect assay columns, count missing values, and choose a target assay (e.g., HIC). Rows lacking measurements for the target are dropped to prepare the dataset for training and evaluation.

```python
from datasets import load_dataset
import pandas as pd

df = load_dataset("ginkgo-datapoints/GDPa1")['train'].to_pandas()
target = "HIC"
df = df.dropna(subset=[target])
```

## Sequence Tokenization for p-IgGen
VH and VL protein sequences are concatenated with special tokens marking the start and end of the paired sequence. The tokenizer from `ollieturnbull/p-IgGen` converts these strings into model-ready inputs.

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ollieturnbull/p-IgGen")
sequences = [
    "1" + " ".join(heavy) + " ".join(light) + "2"
    for heavy, light in zip(df['vh_protein_sequence'], df['vl_protein_sequence'])
]
```

## Generating Embeddings
The p-IgGen model produces hidden-state embeddings for each tokenized sequence. Mean pooling across tokens yields a fixed-length representation per antibody.

```python
import torch
import numpy as np
from tqdm.auto import tqdm
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("ollieturnbull/p-IgGen").to(device)
batch_size = 16
embeddings = []
for i in tqdm(range(0, len(sequences), batch_size)):
    batch = tokenizer(sequences[i:i+batch_size], return_tensors="pt", padding=True, truncation=True)
    outputs = model(batch["input_ids"].to(device), return_rep_layers=[-1], output_hidden_states=True)
    hidden_states = outputs["hidden_states"][-1].detach().cpu().numpy()
    embeddings.append(hidden_states.mean(axis=1))
X = np.concatenate(embeddings)
```

*Processing time example:* approximately 60 seconds for 242 sequences on CPU and 1.1 seconds on GPU.

## Baseline Regression Model
A ridge regression trained on mean-pooled embeddings demonstrates predictive power for developability assays. The example below uses HIC as the target and reports Spearman correlation on a held-out test set.

```python
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from scipy.stats import spearmanr

y = df[target].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = Ridge().fit(X_train, y_train)
y_pred = model.predict(X_test)
print(spearmanr(y_pred, y_test))  # ≈ 0.41 Spearman correlation
```

A scatter plot of predicted versus true HIC values highlights model calibration and variance.

## Isotype-Aware Cross-Validation
To avoid label leakage from near-identical antibodies, isotype- and cluster-aware cross-validation splits are used. Fold assignments are provided in the column `hierarchical_cluster_IgG_isotype_stratified_fold`. Training a fresh ridge model on each fold yields an average Spearman correlation of approximately 0.324 across folds, offering a more realistic generalization estimate.

```python
fold_col = "hierarchical_cluster_IgG_isotype_stratified_fold"
folds = df[fold_col].dropna().unique()
per_fold_stats = []
y_pred_all = np.full(len(df), np.nan)

for fold in folds:
    test_idx = df.index[df[fold_col] == fold]
    train_idx = df.index[df[fold_col] != fold]

    model = Ridge().fit(X[train_idx], y[train_idx])
    fold_pred = model.predict(X[test_idx])
    y_pred_all[test_idx] = fold_pred
    rho = spearmanr(y[test_idx], fold_pred).statistic
    per_fold_stats.append((int(fold), rho))
```

## Preparing Competition Submissions
Predictions are written to CSV files for leaderboard submission. The GDPa submission file includes antibody identifiers, sequences, fold assignments, and predicted assay values.

```python
submission = df[[
    'antibody_name',
    'vh_protein_sequence',
    'vl_protein_sequence',
    'hierarchical_cluster_IgG_isotype_stratified_fold'
]].copy()
submission[target] = y_pred_all
submission.to_csv('gpda_cv_submission.csv', index=False)
```

For held-out test sequences supplied by the competition, embeddings are generated and predictions exported using the trained model.

```python
test_df = pd.read_csv('heldout-set-sequences.csv')
test_sequences = [
    "1" + " ".join(heavy) + " ".join(light) + "2"
    for heavy, light in zip(test_df['vh_protein_sequence'], test_df['vl_protein_sequence'])
]
# ... embed as above ...
submission = test_df[['antibody_name', 'vh_protein_sequence', 'vl_protein_sequence']].copy()
submission[target] = model.predict(test_embeddings)
submission.to_csv('testset_submission.csv', index=False)
```

Competition submissions appear on the [Antibody Developability Competition leaderboard](https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard).
