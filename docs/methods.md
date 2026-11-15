# Association, probability and event models

## Current method boundaries

The frozen particle branch combines displacement/acceleration and direction-related evidence with optional precomputed PIV velocity hints. The bubble branch includes additional projected-area-guided split/merge events and weak conservation constraints. Algorithm X optimizes selected weighted hypotheses **within** the provided objective: exact-cover optimality does not validate underlying physics or probability calibration.

## Branch-specific Entry and Exit

The original bubble custom_methods.py defines exit_entry_func with logistic form:

\[
f(y)=\frac{1}{1+\exp[a(y-b)]}.
\]

Two main.py calls use opposite signs of a and different vertical boundaries. This embeds a direction-sensitive boundary preference; coordinate direction and physical flux must be checked against each application.

The particle custom_methods.py currently disables the sigmoid and returns a_prime + 0 times x, with A_prime = 0.001 in its frozen main.py. This active particle score is constant, independent of location or direction.

## Binary versus higher-order events

The experimental max_k=2 cap permits 1-to-2 and 2-to-1 events. It suppresses one false 1-to-3 split in a cluttered development scenario, but fails true 1-to-3 and 3-to-1 controls; retaining a configurable max_k=3 is scientifically necessary.

## Research candidates, not currently implemented

Explicit probabilistic clutter/null detections; consistent survival, death and birth priors; position-dependent detection probability; coherent group-motion likelihoods for resolved individuals; random-matrix cluster models when groups are not individually resolvable; and weighted exact-cover solver alternatives.
