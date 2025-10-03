# Antibody Developability Competition — Updated Step-by-Step Plan (with new additions)

(verified against the official leaderboard code and rules)

Links
- Competition: https://datapoints.ginkgo.bio/ai-competitions/2025-abdev-competition

- Dataset (GDPa1): https://huggingface.co/datasets/ginkgo-datapoints/GDPa1

- Leaderboard / submission app: https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard

- Leaderboard source files (schema, metrics, validation): https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/tree/main

- Official Rules PDF (Ginkgo): https://euphsfcyogalqiqsawbo.supabase.co/storage/v1/object/public/gdpweb/pdfs/2025%20Ginkgo%20Antibody%20Developability%20Prediction%20Competition%202025-08-28-v2.pdf

---------------------------------------------------------------------

## 0) Non-negotiables (as implemented in the leaderboard)
Properties and “higher is better”

- Exact column names: **AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer**

- Higher-is-better flags: **HIC=False, PR_CHO=False, AC-SINS_pH7.4=False, Tm2=True, Titer=True**  

  Source: constants.py (ASSAY_LIST, ASSAY_HIGHER_IS_BETTER)  
  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/constants.py

Deadline and prizes

- Deadline: see blog / rules; Nov 1, 2025.  

- Prizes up to ~$60k value and recognition for top open-source entry.  
  Sources: blog and Official Rules PDF  
  https://huggingface.co/blog/ginkgo-datapoints/2025-abdev-competition  
  https://euphsfcyogalqiqsawbo.supabase.co/storage/v1/object/public/gdpweb/pdfs/2025%20Ginkgo%20Antibody%20Developability%20Prediction%20Competition%202025-08-28-v2.pdf

Primary metrics used by the app

- **Spearman** per property.  

- **Top-10% recall** (computed after flipping sign for “lower is better”).  
  Source: evaluation.py (get_metrics, recall_at_k)  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/evaluation.py

Tracks and file checks

- Tracks: **GDPa1** (full) and **GDPa1_cross_validation** (CV).

- Required columns (minimum): `antibody_name` + at least one assay column.

- For **CV**: must include `hierarchical_cluster_IgG_isotype_stratified_fold` with the **canonical** fold per antibody.

- The app rejects: missing columns, NaNs in submitted columns, duplicate `antibody_name`, unknown/missing names, wrong CV folds, and suspiciously high public-set Spearman (>0.9).  

  Source: validation.py  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/validation.py

Dataset versions used by the app
- Public table path used for scoring parity: 
 
  `hf://datasets/ginkgo-datapoints/GDPa1/GDPa1_v1.2_20250814.csv`  
  Source: constants.py (dataset paths)  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/constants.py

Example CSV

- Leaderboard provides `data/example-predictions.csv`.  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/data/example-predictions.csv

Note on naming inconsistencies

- The Official Rules PDF mentions PSP_CHO or Tm1 in places. The **leaderboard code** defines live column names: **PR_CHO** and **Tm2**. Always use the leaderboard names.  

  Sources: constants.py vs. Rules PDF (links above)

---------------------------------------------------------------------

## 1) Accounts and workspace

1. Create a Hugging Face account.
2. Open GDPa1 and read the README and license.  
   https://huggingface.co/datasets/ginkgo-datapoints/GDPa1
3. Open the leaderboard Space and download `example-predictions.csv`.  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard

**Output**: Project folder with dataset files and example CSV.

---------------------------------------------------------------------

## 2) Targets, metric, and deadline

1. Predict five properties: **AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer** (exact names).

2. Track **Spearman** on validation folds; also track **top-10% recall** for sanity.  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/evaluation.py
   
3. Finish before **Nov 1, 2025**.  
   https://huggingface.co/blog/ginkgo-datapoints/2025-abdev-competition

**Output**: Run logs reporting Spearman and optional top-10% recall per property.

---------------------------------------------------------------------

## 3) Prepare sequences and regions
1. Number antibody heavy/light chains with **ANARCI** to mark FR and CDR1/2/3 boundaries.  
   Paper (OUP): https://academic.oup.com/bioinformatics/article/32/2/298/1743894  
   PubMed: https://pubmed.ncbi.nlm.nih.gov/26424857/
   
2. Store: chain type, CDR boundaries, lengths.

**Output**: Table with FR/CDR boundaries for each chain.

---------------------------------------------------------------------

## 4) Simple sequence features

1. From ANARCI output compute:  
   - CDR3 length (heavy and light), CDR1/2 lengths.  
   - CDR composition: % hydrophobic, % charged, % aromatic.  
   - Approximate net charge per chain.  
   Amino-acid properties: https://en.wikipedia.org/wiki/Amino_acid#Chemical_properties
   
2. Add global stats: total length; 20-aa frequency vector.

**Output**: 10–40 numeric features per antibody pair.

---------------------------------------------------------------------

## 5) Markov / HMM features

1. Build **k-mer** statistics (n-grams) on training sequences for heavy and light.  
   k-mer overview: https://en.wikipedia.org/wiki/K-mer
2. Compute per sequence:  
   - Average k-mer **log-probability**.  
   - Average **surprisal** (information content).  
   Surprisal: https://en.wikipedia.org/wiki/Information_content
3. Optional profile-HMMs with **HMMER3**; record per-sequence **log-odds**.  
   HMMER: https://hmmer.org/  
   HMMER3 (Eddy 2011): https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002195

**Output**: 2–6 extra columns per sequence: k-mer log-prob, mean surprisal, optional HMM log-odds.

---------------------------------------------------------------------

## 6) Optional structure-lite features

1. Run **IgFold** for quick structure predictions.  
   Nature Communications 2023: https://www.nature.com/articles/s41467-023-38063-x  
   Code: https://github.com/Graylab/IgFold
2. Extract: loop lengths, simple heavy–light contact counts, confidence.

**License note**: JHU Academic Software License; confirm suitability or use a compatible fork.  
https://github.com/Graylab/IgFold

**Output**: 3–10 structure summaries per pair.

---------------------------------------------------------------------

## 7) Choose a base model to fine-tune

Options
- **ESM-2** (general protein LM; strong baseline).  
  Science 2023: https://www.science.org/doi/10.1126/science.ade2574  
  Repo: https://github.com/facebookresearch/esm
  
- **AntiBERTa** (antibody-specific).  
  Patterns/Cell Press 2022 (PDF): https://www.cell.com/patterns/pdf/S2666-3899%2822%2900105-2.pdf  
  ScienceDirect: https://www.sciencedirect.com/science/article/pii/S2666389922001052
  
- **AbLang / AbLang-2** (antibody-specific).  
  AbLang (Bioinformatics Advances 2022): https://academic.oup.com/bioinformaticsadvances/article/2/1/vbac046/6609807  
  AbLang-2 (Bioinformatics 2024): https://academic.oup.com/bioinformatics/article/40/11/btae618/7845256
  
- **BALM** (recent antibody LM).  
  Briefings in Bioinformatics 2024: https://academic.oup.com/bib/article/25/4/bbae245/7682462

Input wiring

- Use default tokenizer.

- Add extra features as short **prefix tokens** (e.g., `[CDR3H_LEN=14][KMER_BIN=3]`) or as a small **numeric side vector** concatenated in the prediction head.

**Output**: One training script that reads sequences + features and returns five predictions per pair.

---------------------------------------------------------------------

## 8) Targets and multi-task head

1. Build a shared encoder with a **5-output head** (AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer).

2. Use both heavy and light sequences (concatenate with a separator token or dual-input if supported).

**Output**: Single model that predicts all five properties.

---------------------------------------------------------------------

## 9) Cross-validation (exactly as the app enforces)
1. Use **5-fold CV**.

2. Split by **pair identity** so the same pair never appears in train and validation.

3. For **CV submissions**, include the official fold column:  
   `hierarchical_cluster_IgG_isotype_stratified_fold`  
   
   and match **exactly** the canonical folds provided by the app's sequences CSV.  
   Sources: constants.py, validation.py  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/constants.py  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/validation.py
4. Log Spearman per property and the mean across properties per fold.

**Output**: Five validation scores; best checkpoint per fold.

---------------------------------------------------------------------

## 10) Fine-tune procedure

1. **Loss**  
   - Regression heads: **MSE**.  
   - If any head is binary: **BCE**.  
   - Add a **rank-aware** term (choose one):  
     • Differentiable sorting / SoftRank overview: https://arxiv.org/abs/1912.07753  
     • ListNet (listwise ranking): https://www.jmlr.org/papers/volume10/cao09a/cao09a.pdf  
     • OT-based ranking example: https://arxiv.org/abs/2002.02497
     
2. **Optimizer**: AdamW; start with LR recommended by your base model docs.

3. **Early stopping**: best **validation Spearman** (average across properties).

4. Save the best checkpoint per fold.

**Output**: Trained model per fold with metrics.

---------------------------------------------------------------------

## 11) Ensemble

1. Train at least three variants:  
   - **A**: base LM only.  
   - **B**: base LM + CDR features.  
   - **C**: base LM + CDR + Markov/HMM features.  
   - **D (optional)**: add structure-lite features.
   
2. Average predictions across folds and models.

**Reference**  
- Deep Ensembles: NeurIPS 2017  
  PDF: https://papers.neurips.cc/paper/7219-simple-and-scalable-predictive-uncertainty-estimation-using-deep-ensembles.pdf  
  arXiv: https://arxiv.org/abs/1612.01474

**Output**: Final blended predictions.

---------------------------------------------------------------------

## 12) Calibration and post-processing

1. If a head is classification, calibrate on validation folds:  
   - Temperature scaling: https://arxiv.org/abs/1706.04599  
   - Isotonic regression: https://www.cs.columbia.edu/~jebara/4771/notes/isotonic.pdf
   
2. Clip extreme regression outputs if needed.

**Output**: Calibrated predictions.

---------------------------------------------------------------------

## 13) Local parity with the app

1. Load the public table used by the app:  
   `hf://datasets/ginkgo-datapoints/GDPa1/GDPa1_v1.2_20250814.csv`  
   Source: constants.py  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/constants.py
   
2. Compute Spearman per property locally with the same column names and "higher-is-better" flips as in evaluation.py.  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/evaluation.py

**Output**: Local CV scores aligned with the leaderboard's logic.

---------------------------------------------------------------------

## 14) Build the submission CSV

1. Allowed columns:  
   - Required: `antibody_name`  
   - Optional: `vh_protein_sequence`, `vl_protein_sequence`  
   - Any subset of `{AC-SINS_pH7.4, PR_CHO, HIC, Tm2, Titer}`  
   - For **CV only**: add `hierarchical_cluster_IgG_isotype_stratified_fold`  
   Source: validation.py  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/validation.py
   
2. Constraints enforced by the app:  
   - At least one assay column present.  
   - No NaNs in submitted columns.  
   - Exactly one row per `antibody_name`.  
   - All `antibody_name` values must match the official list.  
   - For CV: folds must match the canonical mapping.  
   - Public-set Spearman > 0.9 triggers a warning (possible leakage).  
   Source: validation.py
   
3. Compare against `data/example-predictions.csv`.  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/data/example-predictions.csv

**Output**: Valid CSV.

---------------------------------------------------------------------

## 15) Upload on the leaderboard

1. In the Space "✉️ Submit" tab select `GDPa1` or `GDPa1_cross_validation`.

2. Provide username, model name, registration code, and upload CSV.  
   https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard

**Output**: Submission visible on the leaderboard.

---------------------------------------------------------------------
# NEW ADDITIONS (integrated; keep all prior steps)

## 5+. Region-aware n-grams (FR vs CDR; heavy vs light)
**Actions**

1. Train **separate k-gram models** for FR-only and CDR-only regions, and **separately** for heavy vs light chains.  

2. Emit features both **global** and **CDR-only**:  
   - **Entropy rate** (average conditional entropy) per region/model.  
   - **Mean surprisal** per region/model.  
   - **% tokens above threshold τ** (flag rare positions).  
   Entropy rate / surprisal definitions:  
   https://en.wikipedia.org/wiki/Entropy_rate  
   https://en.wikipedia.org/wiki/Information_content
   
3. Add a **bidirectional Markov** score: compute forward and reverse chain statistics and average.

**References**  
- K-mer and Markov modeling background: https://en.wikipedia.org/wiki/K-mer  
- Entropy rate: https://en.wikipedia.org/wiki/Entropy_rate

---------------------------------------------------------------------

## 10+. Markov-driven training control

**Curriculum by surprisal**
- Start training on **lowest-surprisal** pairs; add higher-surprisal tiers each epoch.  

  Curriculum learning: Bengio et al. (ICML 2009) https://dl.acm.org/doi/10.1145/1553374.1553380

**Loss reweighting**
- Use **weight = 1 + λ·z(surprisal)** to emphasize rarer motifs while keeping stability.  

  Difficulty-based weighting is a standard extension of curriculum; related ideas include focal-style emphasis for rare/"hard" cases: Lin et al. (ICCV 2017) https://arxiv.org/abs/1708.02002

**Uncertainty shrinkage at inference**
- For **top-q surprisal** items, shrink predictions toward the **fold mean** (per property). This is a ridge-style pull that reduces variance on OOD-like items.  

  Shrinkage intuition: ridge regression/Tikhonov regularization lowers variance under uncertainty (Hoerl & Kennard 1970). Brief overview: https://en.wikipedia.org/wiki/Ridge_regression

---------------------------------------------------------------------

## 11+. Diversity for ensembling
**Actions**

1. Train **C variants** with differences in:  
   - k ∈ {3,4,5},  
   
   - smoothing (**Kneser–Ney** vs **Witten–Bell**),  
   
   - scope (global vs CDR-only Markov).  
   Kneser–Ney: Chen & Goodman (1999) https://aclanthology.org/J99-2004/  
   Witten–Bell: Witten & Bell (1991) http://www.cs.waikato.ac.nz/~ml/publications/1991/WittenBell.pdf
   
2. Blend with **entropy-aware weights** so **high-entropy** items rely more on the LM-only path (reduces overconstraint).

**Reference**  
- Deep ensembles: https://arxiv.org/abs/1612.01474

---------------------------------------------------------------------

## 12+. OOD gate and guardrails
**Actions**

1. **Gate**: α = σ(a − b·entropy_rate) for **late fusion**; as entropy increases, reduce Markov influence.  

   Entropy-based gating is a common uncertainty heuristic; see predictive entropy as an uncertainty signal: Gal (2016, PhD thesis) https://mlg.eng.cam.ac.uk/yarin/thesis/thesis.pdf
   
2. **Abstain surrogate**: if entropy_rate > τ, increase **softmax temperature** and apply **ridge-style shrinkage** toward the prior mean; log a flag.  
   Temperature scaling: Guo et al. (ICML 2017) https://arxiv.org/abs/1706.04599
   
3. **Data QA** via Markov:  
   - Reject non-ACDEFGHIKLMNPQRSTVWY tokens (invalid aa).  
   - Flag **chain-type swaps** and duplicates via near-zero **surprisal distance**.  
   - Keep a QA report before CSV writing.

**Drift check**
- Fail the submission build if the **submit-set surprisal distribution** drifts from train by **KL > δ** (simple unsupervised drift guard).  
  KL divergence: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence

---------------------------------------------------------------------

## 8+. Pairwise coupling features (H3–L3 co-motifs)
**Actions**

1. **Cross-CDR co-motifs**: count **rare k-mers** that co-occur in **CDRH3** and **CDRL3**.  

2. **Length-matched offsets**: align H3 and L3 by center; compute a **local cross-correlation** score between k-mer rarity tracks.  

   Cross-correlation definition: https://en.wikipedia.org/wiki/Cross-correlation
   
3. Feed these coupling features as a **side vector** to the head.

**Rationale**  

- H3–L3 interplay is known to be important in binding; co-motif signals can capture synergistic patterns (see general antibody CDR coupling principles e.g., Kunik & Ofran 2013, PNAS: https://www.pnas.org/doi/10.1073/pnas.1221615110 ).

---------------------------------------------------------------------

## 11++ Drop-in edits mapped to sections

- **§5 (Markov/HMM)**: add **CDR-only** and **FR-only** models; add **forward+reverse**; log **z-scored surprisal**, **entropy rate**, **backoff depth** (the number of times smoothing backs off).  
  Backoff/smoothing references: Chen & Goodman (1999) https://aclanthology.org/J99-2004/
  
- **§10 (Fine-tune)**: multiply loss by **(1 + λ·z(surprisal))**; scale the rank-aware term by **entropy** so it focuses where ordering is uncertain.
  
- **§11 (Ensemble)**: define variants by **k** and **region scope**; include smoothing choice.  

- **§12 (Calibration)**: for **high-entropy** items, apply **temperature > 1** before clipping.  

- **§13 (Local parity)**: add a QA step to **fail** build if **KL(train||submit) > δ** over surprisal.  

- **§14 (CSV writer)**: write an **auxiliary CSV** with columns `*_entropy_rate`, `*_mean_surprisal`, `backoff_depth`, and QA flags for audits (do **not** upload to the leaderboard).

---------------------------------------------------------------------

## Minimal ablation table (add to your log)
| Model        | k   | Scope     | Fusion  | Mean Spearman | Δ vs LM |
|--------------|-----|-----------|---------|---------------|---------|
| LM-only      | —   | —         | —       | …             | 0       |
| LM+Markov    | 3   | CDR       | early   | …             | …       |
| LM+Markov    | 5   | global    | gated   | …             | …       |
| LM+Markov    | 3+5 | CDR+FR    | late    | …             | …       |

---------------------------------------------------------------------

## Sanity checks to wire now
- Fit **n-grams per fold** only on **train** data (no leakage).

- **Z-score** Markov features within **each fold**.

- Verify **corr(feature_LM, feature_Markov)** is low–moderate. If high, reduce fusion weight β or drop redundant stats.

- Reproduce the app's **Spearman** and **top-10% recall** locally before submission.

---------------------------------------------------------------------

## Glossary
- Antibody pair: heavy and light protein sequences for one antibody.

- FR/CDR: framework regions and complementarity-determining regions (loops).

- ANARCI: tool to label FR and CDR boundaries by numbering schemes.  
  https://academic.oup.com/bioinformatics/article/32/2/298/1743894
  
- k-mer: short window of length k over a sequence; used to compute local stats.  
  https://en.wikipedia.org/wiki/K-mer
  
- Surprisal: information content; high means surprising under your model.  
  https://en.wikipedia.org/wiki/Information_content
  
- Entropy rate: average uncertainty per symbol along a stochastic process.  
  https://en.wikipedia.org/wiki/Entropy_rate
  
- Profile-HMM: position-specific Markov model for motif/family scoring (HMMER).  
  https://hmmer.org/
  
- Smoothing (Kneser–Ney, Witten–Bell): methods to make n-gram probabilities robust.  
  KN: https://aclanthology.org/J99-2004/ ; WB: http://www.cs.waikato.ac.nz/~ml/publications/1991/WittenBell.pdf
  
- Curriculum learning: start easy, then increase difficulty.  
  https://dl.acm.org/doi/10.1145/1553374.1553380
  
- Temperature scaling: post-hoc probability calibration.  
  https://arxiv.org/abs/1706.04599
  
- KL divergence: measure of distribution drift.  
  https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
  
- Cross-correlation: similarity vs relative shift.  
  https://en.wikipedia.org/wiki/Cross-correlation

---------------------------------------------------------------------

## Sources (direct links)
- Leaderboard constants (assays, higher-is-better, dataset path, CV column):  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/constants.py
  
- Leaderboard metrics (Spearman, top-10% recall, flips):  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/evaluation.py
  
- Leaderboard validation (schema checks, CV checks, leakage guard):  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/validation.py
  
- Example predictions CSV:  
  https://huggingface.co/spaces/ginkgo-datapoints/abdev-leaderboard/blob/main/data/example-predictions.csv
  
- Dataset main page:  
  https://huggingface.co/datasets/ginkgo-datapoints/GDPa1
  
- Official competition page and blog:  
  https://datapoints.ginkgo.bio/ai-competitions/2025-abdev-competition  
  https://huggingface.co/blog/ginkgo-datapoints/2025-abdev-competition
  
- Official Rules PDF:  
  https://euphsfcyogalqiqsawbo.supabase.co/storage/v1/object/public/gdpweb/pdfs/2025%20Ginkgo%20Antibody%20Developability%20Prediction%20Competition%202025-08-28-v2.pdf
- ANARCI:  
  https://academic.oup.com/bioinformatics/article/32/2/298/1743894
  
- HMMER and HMMER3 paper:  
  https://hmmer.org/  
  https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1002195
  
- IgFold:  
  https://www.nature.com/articles/s41467-023-38063-x  
  https://github.com/Graylab/IgFold
  
- ESM-2:  
  https://www.science.org/doi/10.1126/science.ade2574  
  https://github.com/facebookresearch/esm
  
- AntiBERTa, AbLang/AbLang-2, BALM:  
  https://www.cell.com/patterns/pdf/S2666-3899%2822%2900105-2.pdf  
  https://academic.oup.com/bioinformaticsadvances/article/2/1/vbac046/6609807  
  https://academic.oup.com/bioinformatics/article/40/11/btae618/7845256  
  https://academic.oup.com/bib/article/25/4/bbae245/7682462
  
- Curriculum learning:  
  https://dl.acm.org/doi/10.1145/1553374.1553380
  
- Focal-style emphasis (related concept for rare/hard cases):  
  https://arxiv.org/abs/1708.02002
  
- Kneser–Ney smoothing:  
  https://aclanthology.org/J99-2004/
  
- Witten–Bell smoothing:  
  http://www.cs.waikato.ac.nz/~ml/publications/1991/WittenBell.pdf
  
- Entropy-based uncertainty (Bayesian deep learning overview):  
  https://mlg.eng.cam.ac.uk/yarin/thesis/thesis.pdf
  
- Ridge regression/shrinkage (overview):  
  https://en.wikipedia.org/wiki/Ridge_regression
  
- KL divergence:  
  https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
  
- Cross-correlation:  
  https://en.wikipedia.org/wiki/Cross-correlation
  
- H3–L3 coupling (general evidence of CDR interplay):  
  https://www.pnas.org/doi/10.1073/pnas.1221615110

