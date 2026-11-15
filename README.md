Forked for modernization.

Implementation documented in the following papers:

https://link.springer.com/article/10.1007/s00348-022-03399-5
https://link.springer.com/article/10.1007/s00348-022-03445-2
https://link.springer.com/article/10.1007/s00348-024-03793-1

Further use cases reported in the following papers:

https://www.mdpi.com/2076-3417/11/20/9710
https://pubs.aip.org/aip/pof/article-abstract/33/8/083316/1079966/Dynamic-mode-decomposition-of-magnetohydrodynamic
https://www.sciencedirect.com/science/article/abs/pii/S0006349525003686
https://journals.asm.org/doi/10.1128/spectrum.02563-25

## Scientific documentation and synthetic benchmark archive

An INM-themed documentation site is staged in this repository using **Zensical** (Python 3.12, pinned `zensical==0.0.71`) and a main-only GitHub Pages Actions workflow. It includes separate current-implementation, model, validation, provenance, research and licensing pages. The original bubble/particle implementations remain unchanged by this documentation branch.

- **Documentation source:** [`docs/index.md`](docs/index.md) and [`zensical.toml`](zensical.toml).
- **Standalone synthetic archive:** [`docs/archive/index.html`](docs/archive/index.html); [true ternary/clutter controls](docs/archive/controls/index.html).
- **Downloadable offline edition:** [`docs/archive/downloads/MHTX_Synthetic_Visual_Archive_Portable_2026-11-15_v2.zip`](docs/archive/downloads/MHTX_Synthetic_Visual_Archive_Portable_2026-11-15_v2.zip).

Following reviewed merge and configuration of **Settings → Pages → GitHub Actions**, the expected project URL is `https://mihails-birjukovs.github.io/MHT-X-v2/`. A local successful build or unmerged branch does **not** imply deployment. This public snapshot includes synthetic benchmark data only, not laboratory raw data or licensed third-party figures. Official institution marks are not included.
