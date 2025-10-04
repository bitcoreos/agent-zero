# Antibody Developability Competition Structure

## Overview
This document outlines the structure of the Antibody Developability Competition, which focuses on predicting five key properties of antibodies using the GDPa1 dataset.

## Competition Timeline
- Start Date: [To be determined]
- Deadline: November 1, 2025
- Winner Announcement: [To be determined]

## Key Components
1. **Dataset**: GDPa1 dataset from Hugging Face
2. **Properties to Predict**:
   - AC-SINS_pH7.4
   - Tm2
   - [Additional properties to be specified]
3. **Evaluation Metrics**:
   - Spearman correlation
   - Top-10% recall
4. **Submission Requirements**:
   - Required columns in submission file
   - No NaN values allowed
   - Exact fold matching for cross-validation

## Technical Constraints
- Model must be reproducible
- No data leakage allowed
- Cross-validation folds must be preserved

## Resources
- Hugging Face dataset: [link to GDPa1 dataset]
- Leaderboard space: [link to leaderboard]
- Example predictions: [link to example predictions]