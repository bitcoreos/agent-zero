# Antibody Developability Competition Assay Definitions

## Overview
This document defines the key assays used in the Antibody Developability Competition to evaluate antibody properties. These assays measure various biophysical and biochemical characteristics that influence the developability of therapeutic antibodies.

## Assay List

### 1. AC-SINS_pH7.4
- **Full Name**: Acid-induced Conformational Stability by Intrinsic Fluorescence Spectroscopy at pH 7.4
- **Purpose**: Measures the conformational stability of antibodies under acidic conditions
- **Method**: Intrinsic fluorescence spectroscopy is used to monitor changes in tryptophan fluorescence as pH is decreased
- **Significance**: Antibodies with higher AC-SINS values are more resistant to acid-induced unfolding, which is important for endosomal escape and recycling
- **Interpretation**: Higher values indicate greater conformational stability at pH 7.4
- **Typical Range**: [To be determined based on dataset]

### 2. Tm2 (Thermal Melting Temperature 2)
- **Full Name**: Second Thermal Transition Midpoint Temperature
- **Purpose**: Measures the thermal stability of the antibody's CH2 domain
- **Method**: Differential scanning calorimetry (DSC) or differential scanning fluorimetry (DSF) to measure heat absorption as temperature increases
- **Significance**: The CH2 domain is often the least stable region of IgG antibodies. A higher Tm2 indicates better thermal stability, which correlates with longer serum half-life and reduced aggregation
- **Interpretation**: Higher values indicate greater thermal stability of the CH2 domain
- **Typical Range**: [To be determined based on dataset]

### 3. [Additional Assay - To be specified]
- **Full Name**: [Full assay name]
- **Purpose**: [Purpose of the assay]
- **Method**: [Experimental method used]
- **Significance**: [Biological or developability significance]
- **Interpretation**: [How to interpret the values]
- **Typical Range**: [Typical value range]

## Assay Relevance to Developability

### Conformational Stability (AC-SINS)
- **Aggregation Resistance**: Antibodies with high conformational stability are less likely to aggregate during production and storage
- **Manufacturing Yield**: Stable antibodies typically have higher expression yields in cell culture
- **Formulation Development**: Stable antibodies are easier to formulate at high concentrations
- **In Vivo Half-life**: Stable antibodies may have improved pharmacokinetics

### Thermal Stability (Tm2)
- **Storage Stability**: Higher Tm2 values correlate with longer shelf life at recommended storage temperatures
- **Shipping Requirements**: Antibodies with higher Tm2 can tolerate temperature excursions during shipping
- **Dosing Frequency**: More stable antibodies may allow for less frequent dosing
- **Cost of Goods**: Higher stability can reduce manufacturing costs by decreasing product loss

## Assay Measurement Protocols

### AC-SINS_pH7.4 Protocol
1. Prepare antibody solution at 0.1 mg/mL in phosphate-buffered saline (PBS)
2. Transfer to quartz cuvette with 1 cm path length
3. Record intrinsic fluorescence spectrum (excitation: 280 nm, emission: 300-400 nm) at pH 7.4
4. Gradually decrease pH using small additions of 0.1M HCl
5. Monitor fluorescence intensity at 340 nm as pH decreases
6. Determine midpoint of transition (pH at which 50% of fluorescence change has occurred)
7. Report as AC-SINS_pH7.4 value

### Tm2 Measurement Protocol
1. Prepare antibody solution at 0.5 mg/mL in PBS
2. Add fluorescent dye (e.g., SYPRO Orange) to monitor protein unfolding
3. Load into real-time PCR machine or differential scanning fluorimeter
4. Heat from 25°C to 95°C at a rate of 1°C per minute
5. Monitor fluorescence as temperature increases
6. Identify thermal transitions from derivative plot
7. Report the temperature of the second transition peak as Tm2

## Quality Control Metrics
- **AC-SINS_pH7.4**: Coefficient of variation (CV) should be < 5% across technical replicates
- **Tm2**: CV should be < 2°C across technical replicates
- All measurements should be performed in triplicate
- Buffer conditions must be standardized across all measurements

## Data Normalization
- Raw values may be normalized to reference antibodies included in each batch
- Normalization formula: `Normalized Value = (Sample Value - Negative Control) / (Positive Control - Negative Control)`
- Batch effects should be corrected using appropriate statistical methods