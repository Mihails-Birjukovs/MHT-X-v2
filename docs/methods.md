# Association, probability and event models

## Current method boundaries

The frozen particle branch combines displacement/acceleration and direction-related evidence with optional precomputed PIV velocity hints. The bubble branch includes additional projected-area-guided split/merge events and weak conservation constraints. Algorithm X optimizes selected weighted hypotheses **within** the provided objective: exact-cover optimality does not validate underlying physics or probability calibration.

**New: [Published motion equations](published-motion-equations.md)** reconstructs and cross-references the kinematic predictions, physical constraints, statistical association functions and upstream divergence-free PIV interpolation from the 2022 and 2024 research papers. The chapter explicitly flags source-code-versus-publication differences and unfinished verification.

## Branch-specific entry and exit

The original bubble \`custom_methods.py\` defines \`exit_entry_func\` with logistic form:

$$
f(y)=\frac{1}{1+\exp[a(y-b)]}.
\label{eq:method-bubble-endpoint}
$$

Two bubble \`main.py\` calls use opposite signs of \(a\) and different vertical boundaries. This embeds a direction-sensitive boundary preference; coordinate direction and physical flux must be checked against each application.

The particle \`custom_methods.py\` currently disables the sigmoid and uses a flat, location-independent score, with \`A_prime = 0.001\` in the frozen \`main.py\`. This is a **branch-specific implementation difference**, not a universal MHT-X condition.

## Binary versus higher-order events

The experimental \`max_k=2\` cap permits 1-to-2 and 2-to-1 events. It suppresses one false 1-to-3 split in a cluttered development scenario, but fails true 1-to-3 and 3-to-1 controls; retaining a configurable \`max_k=3\` is scientifically necessary.

## Unreleased research

C3's causal single-target Bernoulli/PPP estimator and innovation gate passed bounded synthetic structural/model-matched evaluations but failed an adverse persistent-clutter scenario. C4-A/C4-A2 now has an isolated exact small multi-target reference with exclusive observation assignment and explicit persistent-ghost hypotheses; neither is part of the frozen source or accepted as a calibrated physical tracker.

Still needed: validated detector-origin and false-object persistence models, actual segmented-object confidence/shape observations, consistent physical branching and missed-detection normalization, causal locally adaptive flow priors and independent full-tracker evaluation. Solver replacements remain a separate research branch.
