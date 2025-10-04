⚠️ Gaps or Risks

License check for IgFold
JHU Academic Software License may restrict commercial use. If submission is for prize money, confirm eligibility or use an alternative fork.

Public vs private test leakage guard
Validation.py caps Spearman >0.9 on public set. The plan notes this but does not specify handling strategy—need explicit fallback (e.g., check CV/local parity before submission).

Loss/rank-aware term
Leaderboard only evaluates correlation and recall, not differentiable rank losses. Including them is fine but not required. Risk: training instability unless tuned carefully.

Ensembling weighting
Plan proposes entropy-aware weights. Must verify ensemble outputs still align with leaderboard metrics (especially top-10% recall). Suggest ablation logging as planned.

Deadlines
Must finalize and validate before Nov 1. Plan acknowledges this but should include a concrete timeline (data prep → feature builds → CV runs → submission tests).

----

Add third "track" label shown in the app: "Heldout Test Set." The app supports GDPa1, GDPa1_cross_validation, and Heldout Test Set in the submission UI. Your plan lists only the first two. Hugging Face

Submission UI may change to two CSV uploads (CV + Heldout) per recent commit text. Your current instructions match the live app today, but note possible switch. Keep an eye on the Submit tab language. Hugging Face

Minor: under "Primary metrics," note explicitly that the leaderboard table sorts by Spearman. Hugging Face

---

Add this as §5★ Pattern-based tests (PBT) right after §5.

5★) Pattern-based tests (PBT) — multi-lens feature capture

Goal
Probe each sequence with classic CS patterns to extract complementary, overlapping signals. Treat each pattern as a deterministic "test." Feed all PBT features alongside LM and Markov features. Let the model learn emergent structure.

Actions

Run per chain and per region (FR, CDR1/2/3). Compute on train-only within each fold. Z-score per fold. Prefix all names with PBT_.

Tests → features

Two-Pointer: scan inward/outward for symmetric or complementary residues.
Outputs: PBT_tp_sym_match_ratio, PBT_tp_min_gap_to_motif[X].

Fast–Slow Pointers: detect periodicity and repeats.
Outputs: PBT_fs_cycle_len_mode, PBT_fs_repeat_density.

Sliding Window (k=7,11,15): windowed hydropathy, charge, aromatics, disorder proxy.
Outputs: PBT_sw_hydro_max/mean/std, PBT_sw_charge_max, PBT_sw_aromatic_peaks.

Binary Search: threshold crossings for biophys limits.
Outputs: PBT_bs_first_cross_pI>T, PBT_bs_first_cross_hydro>T.

HashMap: exact k-mer counts and rarity bins.
Outputs: PBT_hm_k3_rare_frac, PBT_hm_k5_top10_unique.

Linked List: local transition legality (AA→AA bigram).
Outputs: PBT_ll_illegal_bigram_frac, PBT_ll_backoff_depth_mean.

Stacks: balanced "pairings" (e.g., cysteine pairing heuristics, charge pair closings).
Outputs: PBT_stk_cys_pair_score, PBT_stk_charge_balance_depth_max.

Heaps: top-k extremes.
Outputs: PBT_heap_topk_hydro{1,3,5}, PBT_heap_topk_surprisal{1,3,5}.

Prefix Sum: cumulative charge/hydropathy trajectories.
Outputs: PBT_pref_abs_drift_max, PBT_pref_zero_crossings.

Trees: hierarchical segmentation (FR→CDR→micro-segments) with stats per node.
Outputs: PBT_tree_var_by_level0/1/2, PBT_tree_entropy_by_level.

Tries: motif trie hits from public antibody motifs or mined train motifs.
Outputs: PBT_trie_hit_count, PBT_trie_longest_hit_len.

Graphs: if structure-lite available, build residue contact graph.
Outputs: PBT_graph_degree_mean, PBT_graph_bridge_count, PBT_graph_community_modularity.

Backtracking: constrained motif search (e.g., H3 regex with anchors).
Outputs: PBT_bt_constraint_sat_ratio, PBT_bt_min_edit_to_constraint.

Dynamic Programming: alignment scores to canonical germlines or templates.
Outputs: PBT_dp_sw_score, PBT_dp_gap_open_count.

Greedy: run-length compression on AA classes; local simplification cost.
Outputs: PBT_grd_rlc_len_mean, PBT_grd_merge_cost.

Intervals: interval logic on CDRs (overlaps with hydropathy/charge peaks).
Outputs: PBT_int_overlap_hydro_peaks, PBT_int_peak_density_per_len.

Outputs

A feature matrix per pair with ~50–150 PBT_* columns, region-scoped (_FR, _CDR3H, _CDR3L, etc.).

Integration points

§5: append PBT features to Markov/HMM outputs.

§10: allow surprisal-weighted loss and optionally PBT-uncertainty gates (e.g., if PBT_pref_abs_drift_max high, reduce Markov weight).

§11: include an ensemble variant B2 = LM + CDR + PBT and C2 = LM + Markov + PBT.

§12: log calibration metrics stratified by PBT_* quantiles to verify robustness.

§13: add drift check on a small PBT vector (e.g., KL over PBT_hm_k3_rare_frac, PBT_pref_abs_drift_max).

Minimal schema example

PBT_tp_sym_match_ratio_FR
PBT_fs_repeat_density_CDR3H
PBT_sw_hydro_max_CDRs_k11
PBT_hm_k3_rare_frac_L
PBT_trie_longest_hit_len_H
PBT_dp_sw_score_VH_germline
PBT_graph_degree_mean_pair   # needs structure-lite
PBT_int_overlap_hydro_peaks_CDR3L

This section converts CS patterns into systematic probes. It increases coverage, adds orthogonal signals, and preserves fold hygiene.
```

