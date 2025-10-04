## Glossary of Terms

### AC-SINS (Affinity-Capture Self-Interaction Nanoparticle Spectroscopy)
A biophysical assay for antibody self-association. Antibodies are immobilized on gold nanoparticles and the plasmon wavelength shift is measured under varying salt. High self-association (often correlating with hydrophobicity) causes large plasmon shifts[1].

### Antibody (Ab)
Y-shaped immunoglobulin proteins produced by B-cells, composed of two heavy and two light chains. Antibodies bind specific antigens and have variable and constant regions. They are large polypeptides with four domains per Fab arm[2]. In developability context, therapeutic IgG antibodies (especially IgG1) are evaluated for manufacturability.

### Antigen
A molecule (often protein) that binds to an antibody's variable region (paratope) to elicit an immune response[2]. (Included as background; not a direct competition element.)

### AUC (Area Under the ROC Curve)
A performance metric for binary classification. It is the area under the Receiver Operating Characteristic curve, representing the probability that a classifier ranks a random positive instance higher than a random negative one. (The rules mention AUC for any binary tasks.) Citation not found in provided sources; see general ML references.

### Curriculum Learning
A training strategy where a model is fed training data in order of increasing difficulty or complexity[3]. Models start on easier examples and progressively tackle harder ones, improving convergence or generalization[3].

### Denaturation Midpoint (Tm)
The temperature at which 50% of protein molecules (e.g. antibody domains) are unfolded, reflecting thermostability[4]. Protein melting (Tm) is where folded and unfolded states are equally populated[4]. In antibodies, "Tm" often refers to melting of the Fab or CH2 domain.

### Developability
The likelihood that a therapeutic antibody can be successfully developed. It combines intrinsic biophysical parameters (Aggregation, Solubility, Stability, Hydrophobicity, etc.) that affect manufacturability and performance[5]. Poor developability (e.g. high polyreactivity or low stability) causes clinical failures[5].

### Ensemble Learning
A machine-learning technique combining multiple base models ("learners") to improve overall predictive accuracy[6]. By aggregating diverse models (e.g. via voting or averaging), ensemble models reduce variance and bias, often outperforming single models[6].

### Entropy (Information Entropy)
In information theory, a measure of uncertainty or unpredictability of a probability distribution[7]. A uniform distribution has maximum entropy (most uncertain); a peaked one has lower entropy[8][7]. In ML, output entropy can gauge model confidence. "Entropy gating" refers to filtering predictions by their entropy[7].

### GDPa1 Dataset
The public training dataset ("Ginkgo Datapoints Ab developability 1") of 246 antibodies with 10 biophysical assays (PROPHET-Ab platform). Assays include Hydrophobicity (HIC), Polyreactivity (bead-based PSP against CHO/OVA), Self-Association (AC-SINS), Thermostability (nanoDSF), Titer (expression yield) among others[9][10]. The competition focuses on five assays: HIC, PSP (polyreactivity), AC-SINS, Tm, and Titer.

### GDPa1_v1.2
A specific processed version of the GDPa1 data, with PR score corrected and AC-SINS (pH7.4) data added[11]. Contains folds including an "IgG isotype stratified" split[12].

### HAC (Heparin Affinity Chromatography)
An assay where antibodies are tested for binding to immobilized heparin, indicating heparin-binding affinity (colloidal stability factor). Not a target prediction in this contest, but part of broader developability profiling[9].

### HIC (Hydrophobic Interaction Chromatography)
A chromatographic assay for antibody hydrophobicity. Antibodies are run on a high-salt column to enhance hydrophobic binding; longer retention indicates higher hydrophobicity[13]. Used here as the "Hydrophobicity" score to predict.

### IgG Isotype (Subclass)
Variants of IgG antibodies (e.g. IgG1, IgG2, IgG4) with different Fc-region sequences. IgG1 was used for dataset diversity; developability properties (e.g. Tm) vary by isotype. The training data is split to preserve isotype ratios[14].

### JSON-LD
A Linked Data serialization format using JSON. It enables expressing data with semantic context. "JSON-LD is a method of encoding Linked Data using JSON"[15]. We use JSON-LD for schema definitions (with "@context" and "@type").

### Markov Chain
A stochastic process where the next state depends only on the current state ("memoryless" property)[16]. In sequences, a Markov model defines probabilities of each amino acid given the previous one.

### Hidden Markov Model (HMM)
A Markov model with unobserved (hidden) states: observations (e.g. amino acids) are emitted by a latent Markov chain[17]. HMMs (especially profile-HMMs) are classic models for biological sequence families.

### Partition/Fold (Cross-Validation)
Divisions of data for model validation. The GDPa1_v1.2 splits into 5 folds by hierarchical sequence clustering ("hierarchical_cluster_IgG_isotype_stratified_fold") to ensure low sequence identity and balanced IgG subclasses in each fold[14]. This prevents leakage.

### Polyreactivity (Non-Specificity)
The tendency of an antibody to bind multiple unrelated antigens (nonspecific binding). IgM antibodies often show polyreactivity, meaning they bind many distinct antigens[2]. Measured here by a bead-based assay against CHO membrane proteins and ovalbumin (originally "PSP" assay[18]), and denoted "PR_CHO" (was PSP_CHO) in data.

### PSP Assay (Polyspecificity Particle Assay)
A high-throughput polyreactivity assay. Antibodies are immobilized on beads and incubated with a panel of polyspecificity reagents; nonspecific binding is read via fluorescence[18]. In GDPa1, reagents include CHO cell lysate (membrane proteins) and ovalbumin[18]. The competition label "PR_CHO" corresponds to this polyreactivity measure[19][9].

### ROC (Receiver Operating Characteristic) and ROC AUC
A metric/curve for binary classifiers. ROC plots true positive vs false positive rate; AUC is its area. Mentioned as evaluation for any binary tasks (though primary tasks are regression). Definition omitted here (well-known).

### Schema (Ontological)
Formal structure defining classes and properties. JSON-LD uses "@context" and "@type" to give semantic identity[15][20]. In this competition, we define schemas for Antibody, DevelopabilityAssay, Prediction, etc.

### Self-Association
A property measuring antibody propensity to aggregate with itself. Assayed by AC-SINS (see above[1]) or by other methods. High self-association predicts poor developability (high viscosity or aggregation).

### Spearman Rank Correlation (ρ)
A nonparametric metric of monotonic relationship between two ranked variables. ρ ranges from –1 to 1, measuring how well a monotonic function describes the relationship[21]. It is the primary leaderboard metric for regression targets.

### Top-Decile Recall
The fraction of true positives that appear in the top 10% of model-ranked predictions. Used to emphasize high-ranking positives (e.g. worst-developability antibodies). (No direct citation found, but common in ranking metrics.)

### Titer
The concentration or yield of antibody produced in expression (e.g. mg/L). Measured here by a ValitaQuant assay and predicted as "Titer"[9]. High titer indicates easier manufacturing.

### Tm1 / Tm2
Subdomains' melting temperatures. Tm1 refers to the lower-temperature CH2 domain melt, and Tm2 to the higher-temperature Fab domain melt. In GDPa1, Tm2 (Fab) was ultimately used for prediction as "Thermostability"[9][19]. Tm values are from nanoDSF measurements.

### Validation Set
The private hold-out set (80 antibodies) provided without assay values[10]. Teams submit predictions on these sequences; final scoring occurs against their withheld true values.