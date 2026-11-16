# Published motion, association and flow-prior equations

This chapter documents the **kinematic prediction, weak physical constraints, association scores and PIV-assisted flow interpolation used with MHT-X**, based on the three peer-reviewed papers listed below and the pinned source. **MHT-X is a tracker, not a numerical solver of the Navier–Stokes or bubble-interface equations.** The physics enters primarily through statistical priors and admissibility constraints.

Source papers (numbering in the published PDFs is preserved in the crosswalk, while numbered equations *on this page* use separate MathJax numbering):

1. **Zvejnieks et al. (2022)**, *MHT-X: offline multiple hypothesis tracking with algorithm X*, [Experiments in Fluids **63**, 55](https://doi.org/10.1007/s00348-022-03399-5) (hereafter **Z22**).
2. **Birjukovs et al. (2022)**, *Particle tracking velocimetry in liquid gallium flow around a cylindrical obstacle*, [Experiments in Fluids **63**, 99](https://doi.org/10.1007/s00348-022-03445-2) (hereafter **B22**).
3. **Birjukovs et al. (2024)**, *Particle tracking velocimetry and trajectory curvature statistics for particle-laden liquid metal flow in the wake of a cylindrical obstacle*, [Experiments in Fluids **65**, 67](https://doi.org/10.1007/s00348-024-03793-1) (hereafter **B24**).

**Implementation reference:** the frozen [MHT-X-v2 source](https://github.com/Mihails-Birjukovs/MHT-X-v2/tree/3f1343f90ce29ba42eede6d4de84531d8168768e) at commit \`3f1343f90ce29ba42eede6d4de84531d8168768e\`. Published mathematical descriptions and frozen source behavior are identified separately below: an equation in an article does **not** by itself certify the current code reproduces that equation literally.

## 1. Trajectory extrapolation — Z22, Eqs. (3)–(4)

The paper starts with a trajectory-to-spline operator; a trajectory \(T_k\) is mapped to a piecewise polynomial \(g_k\) of time.

$$
\widehat{\mathcal S}:T_k\longmapsto g_k(t)
\label{eq:z22-spline}
$$

The forward/backward extrapolations in published Z22 Eq. (4) use an endpoint position and a slightly displaced spline derivative. A consolidated reading, separating the two directions, is:

$$
\widehat{\mathbf r}_k(t)=
\begin{cases}
g_k(t_k)+g'_k(t_k-a)(t-t_k),&t>t_k,\\[2pt]
g_k(t_1)+g'_k(t_1+a)(t-t_1),&t<t_1.
\end{cases}
\label{eq:z22-extrap}
$$

Here \(t_1\) and \(t_k\) are the first/last sample times and \(a\) offsets derivative evaluation away from spline endpoints. This notation makes the derivative-evaluation point explicit, using the **frozen bubble source's** \`extrapolate\` implementation to disambiguate the printed layout; it is an editorially consolidated transcription, not a claim that the journal printed the same unified notation.

The source's single-branch equivalent is:

$$
\widehat{\mathbf r}(t)=
g(t_\star)+g'\!\left(t_\star-
a\,\operatorname{sgn}(t-t_\star)\right)(t-t_\star),
\quad a=0.5\ \text{(frozen bubble implementation)}.
\label{eq:source-bubble-extrap}
$$

The extrapolation model is a *prediction heuristic*, not an equation of dynamical force balance.

## 2. Bubble associations and weak physical constraints — Z22, Eqs. (10)–(14)

A candidate pair first satisfies a size-dependent spatial sphere-of-influence restriction:

$$
\|\mathbf r_0-\mathbf r_k\|<C\,r_{\mathrm{SOI}}(S).
\label{eq:z22-soi}
$$

For translation of two existing trajectory fragments, the two acceleration bounds compare their observed velocities with the proposed connecting velocity:

$$
\begin{aligned}
\frac{2\|\mathbf v_k-\mathbf v_1\|}{\Delta t_k+\Delta t_1}&<a_c,\\
\frac{2\|\mathbf v_2-\mathbf v_k\|}{\Delta t_2+\Delta t_k}&<a_c.
\end{aligned}
\label{eq:z22-accel}
$$

The published angular bounds become stricter at higher speed:

$$
\begin{aligned}
\arccos\!\left(
\frac{\mathbf v_k\!\cdot\!\mathbf v_1}
{\|\mathbf v_k\|\,\|\mathbf v_1\|}\right)
&<(\pi+\varepsilon)e^{-\|\mathbf v_1\|/\lambda},\\[3pt]
\arccos\!\left(
\frac{\mathbf v_2\!\cdot\!\mathbf v_k}
{\|\mathbf v_2\|\,\|\mathbf v_k\|}\right)
&<(\pi+\varepsilon)e^{-\|\mathbf v_k\|/\lambda}.
\end{aligned}
\label{eq:z22-angle}
$$

Translation consistency also constrains the change in projected area:

$$
\frac{|\langle S_1\rangle-\langle S_2\rangle|}
{\max(\langle S_1\rangle,\langle S_2\rangle)}
<\varepsilon_t\,\frac{\sigma_k}{\langle S_k\rangle}.
\label{eq:z22-area-translation}
$$

For split/merge, projected-area conservation is used instead of a simple individual momentum constraint:

$$
\frac{\left|S_0-\sum_k\langle S_k\rangle\right|}
{\max\!\left(S_0,\sum_k\langle S_k\rangle\right)}
<\varepsilon_s\,\frac{\sigma_k}{\langle S_k\rangle}.
\label{eq:z22-area-branch}
$$

**Source fidelity caveat:** Z22 Eqs. (13)–(14) use the printed \(k\)-indexed relative area standard deviation on their right-hand sides; the current frozen \`combination_constraint\` computes a mean of relative spreads across all participating fragments. Do not substitute one for the other in a benchmark without checking parameters and denominators. Likewise, projected bubble area is **not** bubble mass: Z22 explicitly identifies this weak conservation approximation as physically imperfect.

## 3. Bubble likelihoods, endpoints and global optimization — Z22, Eqs. (15)–(18), (20)–(22)

MHT-X seeks the most probable **compatible** association configuration, subject to its predefined candidate model:

$$
X^\star=\underset{X}{\arg\max}\;p(X\mid A),
\qquad p(X\mid A)\propto p(A\mid X)\,p(X).
\label{eq:z22-map}
$$

The article's factorization and binary-association term are:

$$
p(A\mid X)=\prod_i p(A_i\mid X_i),
\qquad
p(A_i\mid X_i)=
\begin{cases}
f(A_i),&X_i=1,\\
1-f(A_i),&X_i=0.
\end{cases}
\label{eq:z22-factorization}
$$

For clarity, the normalized univariate Gaussian density with *standard deviation* \(\sigma\) is denoted by:

$$
\mathcal N(x;\mu,\sigma)=
\frac{\exp[-(x-\mu)^2/(2\sigma^2)]}{\sqrt{2\pi}\,\sigma}.
\label{eq:gaussian-std}
$$

The Z22 translation score combines normalized spatial and projected-area consistency:

$$
f_1=\alpha\,
\frac{\mathcal N(\delta r;0,\sigma_{\delta r})}
{\mathcal N(0;0,\sigma_{\delta r})}
+(1-\alpha)\,
\frac{\mathcal N(\delta S;0,\sigma_{\delta S})}
{\mathcal N(0;0,\sigma_{\delta S})}.
\label{eq:z22-f1}
$$

The entry/exit statistical function is a direction-dependent sigmoid:

$$
f_2(y)=\frac{1}{1+\exp[a(y-b)]}.
\label{eq:z22-entry}
$$

Two calls of the bubble source select opposite signs of \(a\) and different vertical limits. **The particle branch is different:** the frozen particle implementation deliberately disables this sigmoid and returns a constant score, with its own parameters.

Z22 Eq. (22) gives the published split/merge score in terms of projected-area agreement and the predicted displacement of the group. Its original notation is preserved here, using \(\delta\) for the area discrepancy and angle brackets for the participating trajectories' mean quantities:

$$
f_3=\beta\,
\mathcal N\!\left(\delta(S_0,S_k);0,\langle\sigma_{S_k}\rangle\right)
+(1-\beta)\frac{M_s}{M}\,
\mathcal N\!\left(\langle\mathbf r_k\rangle-\mathbf r_0;
0,\sigma_{\delta r}\right).
\label{eq:z22-f3-published}
$$

The paper uses the same Gaussian symbol for scalar area discrepancy and position-vector discrepancy; its printed notation should not be read as an independently specified multivariate covariance model. An author-uploaded [preprint full text](https://www.researchgate.net/publication/348447911_MHT-X_Offline_Multiple_Hypothesis_Tracking_with_Algorithm_X) also confirms the term ordering and \(M_s/M\) placement. The frozen code is **not algebraically identical in its explicit normalization and group aggregation**, so its separately source-verified executable version follows below.

For the frozen bubble source's split/merge implementation, the candidate group's projected position is area-weighted, with exponent \(p=1.5\) by default:

$$
\mathbf r_{\mathrm{group}}=
\frac{\displaystyle\sum_{j=1}^{M_s}S_j^{p}\,
\widehat{\mathbf r}_{j}(t_0)}
{\displaystyle\sum_{j=1}^{M_s}S_j^{p}},
\qquad p=1.5.
\label{eq:source-group-centroid}
$$

Its area and displacement score components are, respectively:

$$
\begin{aligned}
\ell_S&=
\frac{\mathcal N(S_0-\sum_j S_j;0,\sigma_S)}
{\mathcal N(0;0,\sigma_S)},\\
\ell_r&=\frac{M_s}{M}\,
\frac{\mathcal N(\|\mathbf r_{\mathrm{group}}-\mathbf r_0\|;
0,\sigma_r\overline{\Delta t})}
{\mathcal N(0;0,\sigma_r\overline{\Delta t})}.
\end{aligned}
\label{eq:source-branch-components}
$$

The source combines those two components as follows:

$$
f_{\mathrm{split/merge}}=k\,\ell_r+(1-k)\,\ell_S.
\label{eq:source-branch-score}
$$

In these code-equivalent formulas, \(M_s\) is the number of group trajectories with available extrapolations and \(M\) the total number of group trajectories. The frozen code uses a specified Gaussian PDF *divided by its peak*, which is important when interpreting the numerical range of likelihood factors. **Comparison note:** the preceding published Z22 equation and these frozen-source equations have deliberately different aggregation/normalization details. They are retained separately instead of being claimed mathematically identical.

## 4. PIV-assisted particle extrapolation — B22, Eqs. (7)–(8)

Unlike the bubble branch, the particle model combines a spline-derived velocity with a precomputed PIV velocity projected onto each detected particle:

$$
\widehat{\mathbf r}(t_0\pm\Delta t)=
\mathbf r(t_0)\pm
\left[\alpha\,\mathbf v_s+(1-\alpha)\,\mathbf v_{\mathrm{PIV}}\right]\Delta t.
\label{eq:b22-position}
$$

The original particle sphere-of-influence (SOI) radius shrinks as the blended velocity increases:

$$
R=R_{\max}\exp\!\left[
-\frac{\|\alpha\mathbf v_s+(1-\alpha)\mathbf v_{\mathrm{PIV}}\|}
{\lambda_{\mathrm{SOI}}}\right].
\label{eq:b22-soi}
$$

B22 sets the spline contribution to zero when insufficient trajectory history is available. In the frozen particle branch, endpoint data \`Vx\`/\`Vy\` can already contain projected PIV/DFI velocity; replaying the tracker against those saved columns **does not** reproduce the upstream PIV or interpolation process.

## 5. Particle association likelihood — B22, Eqs. (9)–(12)

The paper defines positional, acceleration and directional consistency using Gaussian functions:

$$
p_{\mathrm{pos}}=
\mathcal N(\delta r;0,\sigma_{\mathrm{pos}}\Delta t).
\label{eq:b22-ppos}
$$

$$
p_{\mathrm{acc}}=\mathcal N(a;0,\sigma_a).
\label{eq:b22-pacc}
$$

$$
p_{\mathrm{dir}}=
\mathcal N\!\left(\delta\varphi;
0,\pi\exp[-\|\mathbf v\|/\lambda]\right).
\label{eq:b22-pdir}
$$

The B22 publication combines these components with two nested weights:

$$
p=\beta_1 p_{\mathrm{pos}}+
(1-\beta_1)\left[\beta_2p_{\mathrm{acc}}
+(1-\beta_2)p_{\mathrm{dir}}\right].
\label{eq:b22-combined}
$$

Here \(a\) in the acceleration score denotes *acceleration*, not the \(a\) sigmoid parameter in Equation \(\eqref{eq:z22-entry}\). **Implementation fidelity:** the frozen particle source normalizes each Gaussian density by its value at zero; its code parameter \`w2\` multiplies the **direction** score, whereas published \(\beta_2\) multiplies the **acceleration** score. Parameter names/weights should therefore be mapped deliberately, never treated as identical.

## 6. Divergence-free PIV interpolation used upstream — B24, Eqs. (1)–(2)

B24 introduced physics-informed divergence-free interpolation (DFI) of the *input PIV field* used for motion hints. The matrix-valued RBF kernel is described by:

$$
\boldsymbol\Phi(\mathbf x)=
\left[-\nabla^2\mathbf I+\nabla\otimes\nabla\right]
\phi_\delta(\mathbf x).
\label{eq:b24-dfi-kernel}
$$

The article's scaled radial basis is of the form:

$$
\phi_\delta(\mathbf x)=
\delta^{-d}\phi_{d,k}\!\left(\frac{\|\mathbf x\|}{\delta}\right).
\label{eq:b24-scaled-rbf}
$$

Here \(d\) is motion-space dimension, \(\delta\) the support scale, and \(\phi_{d,k}\) the selected Wendland basis. The article describes a near-incompressible quasi-2D velocity field and discrete no-slip conditions at the channel/obstacle boundaries, represented symbolically as:

$$
\nabla\cdot\mathbf u_{\mathrm{DFI}}=0,
\qquad
\mathbf u_{\mathrm{DFI}}\big|_{\partial\Omega_{\mathrm{wall}}}=\mathbf 0.
\label{eq:b24-dfi-physics}
$$

The last displayed statement is a **compact rendering of the physical conditions explained in B24**, not an additional numbered equation copied from that paper. B24 reports a non-multilevel DFI implementation. **DFI is an upstream velocity-field calculation, not a routine embedded in the frozen MHT-X source.** Existing exact historical tracking replay accepts precomputed projected velocities and does not independently establish complete PIV-to-DFI numerical parity.

## 7. Re-evaluation and downstream curvature

B24 additionally reevaluates existing association edge likelihoods after full graph sweeps with more trajectory context. This reuses the motion/statistical functions above; it is **not a new differential equation of motion**. The trajectory curvature statistics analyzed in B24 are post-tracking observables rather than MHT-X's candidate motion law. Do not conflate the turbulence/curvature analysis with tracker association scoring.

## Source-to-equation crosswalk

| Publication | Original printed equation(s) | This chapter | Boundary |
|---|---|---|---|
| Z22 | (3)–(4) | Spline map and forward/backward extrapolation | Printed notation consolidated with code check |
| Z22 | (10)–(12) | SOI, acceleration, direction | Weak admissibility heuristics |
| Z22 | (13)–(14) | Translation and branching area ratios | Projected area ≠ mass; source ratio differs in detail |
| Z22 | (15)–(18) | MAP and factorization | Offline association/selection, not calibrated generative multi-target RFS |
| Z22 | (20)–(21) | Bubble translation and endpoint scores | Current bubble branch |
| Z22 | (22) | Published split/merge likelihood **and** frozen-source group centroid and score | Original expression distinguished from implementation-specific form |
| B22 | (7)–(8) | Blended extrapolation and SOI | PIV hints are upstream data |
| B22 | (9)–(12) | Particle position, acceleration, direction and combined likelihood | Source uses peak-normalized Gaussian, different weight orientation |
| B24 | (1)–(2) | DFI kernel and scaled RBF | Upstream interpolation, distinct codebase |

**Not published as an accepted MHT-X motion model:** our C3 causal Bernoulli/PPP existence filter and C4-A2 joint real/ghost hypotheses. Those remain [research-stage candidates](research.md), with synthetic-only structural gates and independent physical validation pending.

**Editorial review ledger:** The published Z22 Eq. (22) and frozen-source form are documented side by side, without claiming their normalization/aggregation is identical. Z22 Eqs. (13)–(14) use \(k\)-indexed relative spreads, while the frozen code averages over participating tracks. The B22 source/paper \(\beta_2\) versus \`w2\` weight convention differs. B24's scaled-RBF formula still requires final equation-layout verification before a production claim of literal transcription.
