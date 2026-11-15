# MHT-X higher-order branch and clutter negative controls

**Gate:** source-frozen kinematic-proxy experimental model comparison, 2026-11-15.
**Status:** 12 of 12 actual tracking executions completed. This gate was separately preregistered before model comparison, and did not retune historical or FST parameters.

## Independent synthetic controls

- ternary_true_no_clutter: true 1-to-3 split at frames 20->21, then 3-to-1 merge at frames 40->41, with additive projected areas, historical radius-5 pair gating and three daughter circle contacts through a connected cluster. Independent bystander. The 3-child split and 3-parent merge are intentionally **simultaneous hyper-events**, not sequential binary events. **No validated three-dimensional bubble fragmentation physics or image segmentation model** is claimed.
- near_pass_clean: no true split/merge, two physically distinct close-passing rising tracks, one independent bystander; intentionally a no-event control.
- near_pass_with_clutter: same no-event structure but with artificial spurious interior detections around the near-contact windows; none is a physical entrant or part of a true branch.

All cases have independent truth, explicit canonical (frame,id) edge sets, deterministic seeds, fixed measurement noise and SHA-256 input/truth manifests.

## Source model intervention

Original bubble associator max_k=3 versus binary-only max_k=2. Each run uses unchanged 2026 bubble association scoring, Entry/Exit sigmoid, reevaluation, original Algorithm X exact-cover implementation and a source-frozen branch checkout (commit 3f1343f90ce29ba42eede6d4de84531d8168768e). Exactly two fixed parameter vectors: historic 300sccm and an older first-FST candidate. NO optimization or validation/holdout transfer was performed in this new gate.

## Exhaustive result table

| Case | Params | Branch cap | Split TP/FP | Merge TP/FP | Internal J | Family J |
|---|---|---:|---:|---:|---:|---:|
| ternary_true_no_clutter | historical | 3 | 1/0 | 1/0 | 0.6438 | 0.3387 |
| ternary_true_no_clutter | historical | 2 | 0/1 | 0/1 | 0.6312 | 0.3321 |
| ternary_true_no_clutter | previous_first_FST | 3 | 1/1 | 1/0 | 0.8944 | 0.7580 |
| ternary_true_no_clutter | previous_first_FST | 2 | 0/2 | 0/1 | 0.8820 | 0.7460 |
| near_pass_clean | historical | 3 | 0/0 | 0/2 | 0.7278 | 0.3720 |
| near_pass_clean | historical | 2 | 0/0 | 0/2 | 0.7278 | 0.3720 |
| near_pass_clean | previous_first_FST | 3 | 0/0 | 0/0 | 0.9777 | 0.9565 |
| near_pass_clean | previous_first_FST | 2 | 0/0 | 0/0 | 0.9777 | 0.9565 |
| near_pass_with_clutter | historical | 3 | 0/1 | 0/3 | 0.7011 | 0.4162 |
| near_pass_with_clutter | historical | 2 | 0/1 | 0/3 | 0.7011 | 0.4162 |
| near_pass_with_clutter | previous_first_FST | 3 | 0/3 | 0/1 | 0.9405 | 0.9058 |
| near_pass_with_clutter | previous_first_FST | 2 | 0/3 | 0/1 | 0.9405 | 0.9058 |

## Scientific conclusions

1. Genuine 1-to-3 and 3-to-1 events are directly recoverable by original max_k=3 on the clean positive control, so restricting max_k=2 has a scientific opportunity cost: it **cannot reproduce exact three-child/three-parent truth** even when that truth is geometrically and statistically admissible.
2. With historical parameters, original max_k=3 recovers the exact true ternary split and merge without false events; max_k=2 misses both and produces alternative false binary events. The previously fitted FST profile with max_k=3 also recovers both exact events, but adds one false split. Under cap2 it misses both; false binary events still occur.
3. On clean near-passing tracks, historical parameters generate two false merges at either cap, whereas the first FST profile generates no false branching events at either cap.
4. With artificially clustered interior clutter, historical parameters generate one false split and three false merges at BOTH caps. First FST parameters generate three false splits and one false merge at BOTH caps. Thus binary-only restriction CANNOT correct the original model's general false-detection/near-contact errors.
5. These observations support a configurable branch limit rather than a universal max_k=2 switch, and make MHTX-CLUTTER-01 (a separately calibrated null-detection/clutter explanation) an independently motivated next scientific direction.

**Do not interpret synthetic no-event FP rates as experimental false-positive rates.** The artificial pixel-noise/false-detection distribution is not calibrated to bubble imaging, microscopy or segmentation. Exact event recognition is stricter than point/edge graph overlap, and total Jaccard/family-clustering metrics remain independent gates.

## Human and machine evidence

- This report, the top-level index.html with frame scrubber, and 12 source-linked visual sequences.
- visuals/CASE/PROFILE/CAP/frames/frame_001.png ... frame_060.png for all 12 tracking outputs; each frame has independent truth on the left and actual MHT-X source graph on the right (blue true, green correctly selected, red false selected, purple x simulated false detection).
- 12 paired 8-frame EVENT_STORYBOARD.png sheets with true/false event windows (19-22 and 39-42).
- Per-run VISUAL_MANIFEST.json with 60 image SHA hashes, original input/graph/truth SHA and exact metric summary; machine VISUAL_INDEX.json.
- NARY_AND_CLUTTER_CONTROL_RESULTS.json and .csv (all 12 source-frozen runs), generation QA, design preregistration and individual trial reports/stderr logs.

## Admission decisions and next work

Binary max_k=2 is a configurable hypothesis family, not a generally superior tracker. Explore true ternary events and clutter under varied area imbalance, false-positive count and spatial density. Independently calibrate clutter with manually reviewed detection negatives and repeat with real image labels. Preserve all previously reserved holdouts 2901-2904 and vortex_shear_holdout, and do not tune FST on these controls then claim validation on them.

No original source, Algorithm X code, historical experimental observations or protected holdouts were modified. No change was committed or pushed to GitHub for this new control gate; its data/figures remain on X:.
