# Research roadmap and references

## Unreleased model directions

1. **MHTX-CLUTTER-01:** explicit Poisson false-detection hypotheses distinct from physical entry, missed detection and multiobject events; independently calibrate spatial background rates and detection probabilities.
2. **Entry/Exit:** compare bubble directional sigmoid to particle flat score; formulate isotropic and known-flow-aligned boundary flux and survival models.
3. **Collective motion:** first consider correlated velocity as an optional association prior for individually resolvable agents; separately study random-matrix extended-object tracking for unresolved groups.
4. **MHTX-SOLVER-01:** investigate alternative weighted exact-cover backends while preserving the source Algorithm X reference.
5. **Parameter sensitivity:** FST-PSO explores outer-loop parameters, but sensitivity/holdout evidence is independent.

## Starting literature

- Wolfgang Koch, 2008, Bayesian approach to extended object and cluster tracking using random matrices, IEEE TAES, DOI https://doi.org/10.1109/TAES.2008.4655362.
- Poisson multi-Bernoulli mixture tracking of resolvable groups, Digital Signal Processing (2024), DOI https://doi.org/10.1016/j.dsp.2023.104279.
- Chen, Tharmarasa, Pelletier & Kirubarajan (2013), [Integrated Bayesian Clutter Estimation with JIPDA/MHT Trackers](https://doi.org/10.1109/TAES.2013.6404111). Direct precedent for Bayesian nonhomogeneous clutter learning integrated with MHT.
- [Detection and Tracking of Coordinated Groups](https://doi.org/10.1109/TAES.2011.5705687) (2011). A stochastic group-dynamics and individual-target model with interacting group members, relevant to *resolvable* coherent motion.
- [Improved MHT using incomplete measurements for group targets](https://doi.org/10.1109/ICSIDP62679.2024.10869236) (2024). Adaptive detection and track-crossing probabilities in an MHT framework.
- [A New Multiple Hypothesis Tracker Integrated with Detection Processing](https://doi.org/10.3390/s19235278) (2019). An explicit clutter/new-target density and detection-probability log-score model.

These are candidates for scientific design, not implementation claims. Individual model priors and hyper-event constraints need independent, dimensionally consistent derivation for MHT-X.

- Rajapaksha, Gostar, Blair & Hoseinnezhad (2026), [Multisensor Swarm Tracking Using Labeled Multi-Bernoulli Filters: A Swarm Geometry-Informed Approach](https://doi.org/10.1109/TAES.2026.3741814), IEEE TAES (online 9 October 2026). The authors combine an SMC swarm-geometry estimator with individual-target LMB filtering and generalized covariance intersection across sensors. For MHT-X the most transferable idea is a **conditional individual-detection likelihood informed by independently established collective geometry**; its full multisensor architecture is not required by the current single-camera tracker. The institution-licensed source PDF is **not redistributed** in this repository.

The cited models are research candidates, not baseline MHT-X implementations. Chen et al. require association-event probabilities that the frozen best-cover optimizer does not directly expose, and Koch's unresolved extended-object model does not preserve member identities.
