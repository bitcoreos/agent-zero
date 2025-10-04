# Antibody Developability Competition Evaluation Metrics

## Primary Metrics

### 1. Spearman Correlation
- Measures the rank correlation between predicted and actual values
- Calculated for each of the five antibody properties independently
- Final score is the average Spearman correlation across all properties
- Range: -1 to 1, where 1 indicates perfect positive correlation

### 2. Top-10% Recall
- Measures the proportion of true top 10% performers that are correctly identified in the predicted top 10%
- Calculated for each property where higher values are better
- Final score is the average recall across all applicable properties
- Range: 0 to 1, where 1 indicates perfect recall

## Metric Calculation
```
Spearman = mean(spearman_corr(property_i)) for i in [1,5]
Recall = mean(top_10_recall(property_i)) for applicable properties
```

## Validation Rules
- **No NaN values**: Submissions containing NaN values will be disqualified
- **Exact fold matching**: Cross-validation folds must match the provided fold assignments exactly
- **No data leakage**: Models must not use information from test sets during training
- **Reproducibility**: Results must be reproducible with the provided code and data

## Submission Requirements
- File format: CSV
- Required columns:
  - `sequence_id`: Unique identifier for each antibody sequence
  - `AC-SINS_pH7.4`: Predicted value for AC-SINS assay at pH 7.4
  - `Tm2`: Predicted value for Tm2 (thermal melting temperature)
  - [Additional property columns as specified]
  - `fold`: Cross-validation fold assignment (0-4)
- No additional columns allowed
- File size must not exceed 10MB

## Leaderboard Rules
- Submissions are evaluated on a hidden test set
- Participants can submit up to 5 times per day
- The best score on the public leaderboard will be considered for final ranking
- Final evaluation will use a separate, held-out test set

## Scoring Weighting
- Spearman correlation: 60% of final score
- Top-10% recall: 40% of final score
- Final Score = (0.6 × Average Spearman) + (0.4 × Average Recall)