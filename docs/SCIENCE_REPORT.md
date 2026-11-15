# Scientific scope and synthetic benchmarking summary

Baseline: MHT-X bubble source 3f1343f90ce29ba42eede6d4de84531d8168768e, 15 November 2026.

Binary split/merge cap max_k=2 versus source original max_k=3: 32 source-frozen tracking runs in 16 paired comparisons, with seven pairs changing directed-edge topology. Under both historical and previously optimized FST settings, binary-only association recovers the true split and eliminates the false triple split for synthetic contact seed1701. Historical contact seed1702 false merges decline from four to two. Under first-FST settings and binary cap, both development seeds1701/1702 recover exact true split+merge TP1 FP0, directed internal Jaccard 0.9642857 and family-pairwise Jaccard 1.0. No unseen holdout or experimental generalization is claimed.

In source-original cap3 seed1701, correct two-child split positive p=0.843174 competes with spurious three-child split p=0.834467. Interior false detection Entry has p=0.007024. The original exact-cover selected component product exceeds the best forced-true-split by ~133x. This is an objective-model effect, NOT posterior confidence or an Algorithm X failure. Separate MHTX-CLUTTER-01 proposal (explicit false detection hypothesis) is NOT implemented.

Separate quarantined FST-PSO 1.9.0 tested 16 candidate radius/weight vectors on the two original development seeds with cap2 fixed; best radius 6.245278 and weight 0.156824, fitness 0.9873134. Twelve vectors tied at the best score, consistent with a local plateau, not proof of global optimality. No unseen reserved holdouts used.

Three independently shaped kinematic split/merge proxies show mixed transfer: better edge graph Jaccard does not ensure better family-lineage Jaccard. A test with genuine 1-to-3 or 3-to-1 events is needed before promoting binary-only mode.

General particle cases: original straight_12x48 source tracker PASS with 564/564 correct internal links; crossing_4x48 original source FAIL (zero product in exact-cover objective) and exploratory clipping retry FAIL. Eight other particle inputs NOT_RUN for source tracking. Input/latent-truth visualizations do not imply actual tracking on them.

Machine records under machine/ and per-run CSV/ground-truth JSON under data/ are authoritative. Images render synthetic coordinates and correct/incorrect selected directed edges; they are not raw imaging data. The 2022 PIV-assisted particle historical reproduction used existing precomputed velocity fields and did not recompute upstream DFI.
