# Semantic Mesh of Terms and Concepts for Antibody Developability Models

Semantic Mesh of Terms and Concepts for Antibody Developability Models

This document organises the diverse concepts involved in the Antibody Developability Prediction task into a semantic mesh. It illustrates how sequence properties, statistical modelling, machine‑learning techniques and calibration methods interrelate. Citations are provided for factual definitions and algorithmic details.

Conceptual Relationships
Sequence and Region Features

Framework (FR) and Complementarity‑Determining Regions (CDR) – Antibody variable domains are divided into four framework regions and three CDRs. ANARCI uses profile hidden‑Markov models to classify heavy/light chain types and assign canonical numbering that marks FR/CDR boundaries
pmc.ncbi.nlm.nih.gov
. The CDRs, particularly CDR3, capture antigen specificity. Derived features include CDR lengths, amino‑acid composition, net charge, and overall amino‑acid frequencies.

k‑mers and n‑gram models – A sequence of length L contains L‑k+1 k‑mers; there are n^k possible k‑mers for an alphabet of size n
en.wikipedia.org
. k‑mer counts underpin Markov and hidden‑Markov models that estimate the probability of observing a sequence. Region‑aware n‑gram models are built separately for FR and CDR segments and for heavy and light chains to capture context‑specific statistics.

Surprisal and entropy rate – Surprisal (information content) of an event x is −log(P(x)). Average surprisal over a sequence yields an estimate of how unusual it is under a given model. The entropy rate of a stationary process is the limit of average conditional entropy per symbol
en.wikipedia.org
; it quantifies uncertainty of the Markov chain and supports gating and uncertainty measures.

Cross‑correlation – To measure coupling between heavy and light CDRs, cross‑correlation compares two signals by shifting one and computing correlations
statisticshowto.com
. It is mathematically defined via convolution
mathworld.wolfram.com
.

Statistical Smoothing and Sequence Models

Kneser–Ney smoothing – A discounting method that adjusts n‑gram counts and the backoff distribution based on context diversity
geeksforgeeks.org
. It improves probability estimates for rare k‑mers.

Witten–Bell smoothing – A technique that interpolates maximum‑likelihood estimates with a fallback distribution; unseen n‑gram probability is proportional to the number of unique continuations
geeksforgeeks.org
.

Hidden‑Markov models (HMM) – Profile HMMs model position‑specific residue distributions and gaps. HMMER3 accelerates profile HMM searches while retaining sensitivity
pmc.ncbi.nlm.nih.gov
. HMM log‑odds scores can be used as features.

Base Language Models

ESM‑2 / ESMFold – Large protein language models trained on millions of sequences. ESM‑2 learns multi‑scale representations and forms the backbone of ESMFold, which predicts protein structures without alignments
huggingface.co
huggingface.co
.

AntiBERTa – A 12‑layer transformer trained on antibody sequences; captures binding‑site features and biological context
alchemab.com
.

AbLang / AbLang‑2 – Language models trained on antibody sequences to restore missing residues and reduce germline bias
raw.githubusercontent.com
raw.githubusercontent.com
.

BALM / BALMFold – Bio‑inspired LM that uses positional encoding and adaptive masking; 336 M sequences and 150 M parameters. BALMFold integrates a BAformer and structure module to predict antibody structures and functions
creative-proteomics.com
.

Training Strategies and Loss Design

Curriculum learning – Introduces training data from easy to hard examples. Models may start with easy examples, then gradually incorporate harder ones
en.wikipedia.org
en.wikipedia.org
. In the context of Markov surprisal, sequences with low surprisal (common motifs) form the early curriculum; high‑surprisal sequences are added later.

Loss reweighting – Weighting the loss by 1 + λ·z(surprisal) emphasises rare motifs. Focal loss similarly down‑weights well‑classified examples and focuses on hard cases
milvus.io
.

Rank‑aware losses – Differentiable sorting or listwise ranking (e.g., ListNet) encourages correct ranking of predictions. These augment MSE/BCE to align optimisation with Spearman correlation.

Calibration and Uncertainty

Predictive entropy – Measures uncertainty of the predictive distribution; high entropy indicates that the model is uncertain
cs.ox.ac.uk
cs.ox.ac.uk
.

Temperature scaling – A post‑hoc calibration technique that divides logits by a learned scalar, yielding well‑calibrated probabilities without retraining
geoffpleiss.com
.

Ridge‑style shrinkage – Adds a penalty term to regression weights; reduces variance at the cost of bias
en.wikipedia.org
en.wikipedia.org
. Used when predictions for high‑surprisal sequences are uncertain.

KL divergence – Quantifies divergence between two probability distributions
statisticshowto.com
. Used for drift detection when comparing train and submission surprisal distributions.

Ensemble and Gate Mechanisms

Deep ensembling – Combining multiple neural networks improves uncertainty estimation
creative-proteomics.com
. Ensemble diversity is promoted via varying k‑mer lengths, smoothing methods, and region scopes.

Entropy‑based gating – A gating function α = σ(a – b·entropy_rate) reduces the influence of Markov features at high entropy. Predictive entropy or surprisal thus determines the contribution of statistical features.

Data Quality and Quality Control

QA checks – Validate sequences for correct amino‑acid alphabet, detect heavy/light swaps and duplicates via surprisal distances. Generate QA flags for suspicious entries.

OOD detection – High entropy or extreme surprisal indicates out‑of‑distribution sequences. Temperature scaling and shrinkage protect against spurious predictions.



## Conceptual Framework

### Sequence and Region Features
- **Framework (FR) and CDR Regions**: Antibody variable domains divided into framework regions and complementarity-determining regions
- **ANARCI**: Uses profile HMMs to classify chain types and assign canonical numbering for FR/CDR boundaries
- **CDR Features**: Lengths, amino acid composition, net charge, and overall amino acid frequencies
- **k-mers and n-gram models**: Sequence analysis using k-mer counts for Markov and HMM models
- **Surprisal and entropy rate**: Information content measures for sequence unusualness and uncertainty quantification
- **Cross-correlation**: Measures coupling between heavy and light CDRs

### Statistical Smoothing and Sequence Models
- **Kneser-Ney smoothing**: Adjusts n-gram counts based on context diversity
- **Witten-Bell smoothing**: Interpolates maximum-likelihood estimates with fallback distribution
- **Hidden-Markov models (HMM)**: Profile HMMs for position-specific residue distributions and gaps

### Base Language Models
- **ESM-2 / ESMFold**: Large protein language models for multi-scale representations and structure prediction
- **AntiBERTa**: Transformer model trained on antibody sequences for binding-site features
- **AbLang / AbLang-2**: Language models for antibody sequences to restore missing residues
- **BALM / BALMFold**: Bio-inspired LM with positional encoding and adaptive masking for structure prediction

### Training Strategies and Loss Design
- **Curriculum learning**: Training from easy to hard examples based on surprisal
- **Loss reweighting**: Emphasizes rare motifs in training
- **Rank-aware losses**: Encourages correct ranking of predictions to align with Spearman correlation

### Calibration and Uncertainty
- **Predictive entropy**: Measures uncertainty of predictive distribution
- **Temperature scaling**: Post-hoc calibration technique for well-calibrated probabilities
- **Ridge-style shrinkage**: Reduces variance in regression weights
- **KL divergence**: Quantifies divergence between probability distributions for drift detection

### Ensemble and Gate Mechanisms
- **Deep ensembling**: Combines multiple neural networks for improved uncertainty estimation
- **Entropy-based gating**: Controls influence of Markov features based on entropy

### Data Quality and Quality Control
- **QA checks**: Validates sequences for correct amino acid alphabet and detects issues
- **OOD detection**: Identifies out-of-distribution sequences using entropy and surprisal

## Mermaid Graph

Mermaid Representation of the Semantic Mesh
graph TD
%% Sequence features
ANARCI("ANARCI: classify chain & mark FR/CDR")
CDRFeatures("CDR & FR composition, lengths, net charge")
kmer("k-mer & n-gram counts")
HMMER("Profile HMM scores (HMMER3)")
Surprisal("Surprisal & entropy rate")
CrossCorr("H3-L3 cross-correlation")

%% Statistical models
KN("Kneser–Ney smoothing")
WB("Witten–Bell smoothing")

%% Base models
ESM("ESM-2 / ESMFold")
AntiBERTa("AntiBERTa")
AbLang("AbLang/AbLang-2")
BALM("BALM & BALMFold")

%% Training
Curriculum("Curriculum learning & loss reweighting")
RankLoss("Rank-aware losses")

%% Calibration & uncertainty
Entropy("Predictive entropy & temperature scaling")
Ridge("Ridge shrinkage")
KL("KL divergence & drift check")

%% Ensemble & gating
Ensemble("Deep ensembling & diversity")
Gate("Entropy-based gating & OOD detection")

%% Connections
ANARCI --> CDRFeatures
ANARCI --> kmer
ANARCI --> CrossCorr
kmer --> Surprisal
HMMER --> Surprisal
CDRFeatures --> Surprisal
Surprisal --> Curriculum
Surprisal --> Gate
Surprisal --> Entropy

kmer --> KN
kmer --> WB

ESM --> Curriculum
AntiBERTa --> Curriculum
AbLang --> Curriculum
BALM --> Curriculum

Curriculum --> RankLoss
RankLoss --> Ensemble
Curriculum --> Ensemble

Entropy --> Gate
Entropy --> Ridge
Entropy --> KL

Ensemble --> Gate

CrossCorr --> Surprisal
CrossCorr --> Curriculum

## References
