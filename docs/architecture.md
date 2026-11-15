# Architecture and original implementation

Frozen source reference: Mihails-Birjukovs/MHT-X-v2 commit 3f1343f90ce29ba42eede6d4de84531d8168768e. Particle and bubble models are not interchangeable.

| Aspect | Particle branch | Bubble branch |
|---|---|---|
| Tracked objects | Individual point-like detections | Bubble detections including fusion/fragmentation hypotheses |
| Motion likelihood | Displacement, acceleration, angular and velocity information; optional PIV assistance | Translation plus weak area-conservation and event geometry |
| Entry/Exit | Current constant a_prime score | Logistic score based on extrapolated vertical coordinate |
| Branching | No corresponding native split/merge implementation | Up to n-ary merge/split candidate associations |
| Hypothesis selection | Original Algorithm X exact cover | Original Algorithm X exact cover |

Hypothesis generation, physical/statistical likelihoods, combinatorial selection, reevaluation and visualization are separate engineering boundaries. Proposed MHTX-CLUTTER-01, weighted exact-cover solver alternatives, and coherent group-motion inference are independent research branches.

Modernization work does not import the separate MNNT tracker as a dependency.
