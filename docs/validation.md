# Validation and limitations

- The archived 2022 PIV-assisted particle case was reproduced **at the tracking stage with precomputed velocity hints**, not by recomputing PIV or DFI.
- The first synthetic archive contains 172 source-frozen bubble graph exports corresponding to 46 unique graph topology/fixture images, with graph Jaccard, exact split/merge metrics, family-clustering Jaccard and continuity measures.
- Original particle smoke: straight_12x48 PASS, 564/564 consecutive internal links; crossing_4x48 FAIL from likelihood-model degeneracy; its exploratory clipping attempt also failed. Eight additional generic particle tests have source input/truth but not source tracking graphs.
- Binary max_k=2 versus original max_k=3 was compared without changes to the frozen Algorithm X.
- Additional 2026-11-15 gate: 12 source-frozen tracking runs across true 1-to-3/3-to-1 events and no-event/clutter negatives. The binary restriction necessarily misses genuine higher-order events, and does not prevent false binary associations in clutter. All 732 new control review images passed integrity checks.
- The established local source regression suite passed 51 tests across 13 suites at this gate.

Synthetic kinematic proxies are not real hydrodynamic bubble simulations, detector/segmentation image-formation data or experimental performance certificates. Reserved noise/geometric holdouts have not been used.

[Original interactive archive](archive/index.html) · [New event/clutter controls](archive/controls/index.html).
