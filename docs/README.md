# MHT-X synthetic archive — offline and GitHub Pages

This is a public snapshot of algorithmically generated synthetic tracking visuals, not experimental measurements. Open index.html on GitHub Pages or from the extracted portable ZIP without a server or internet connection.

The archive covers 23 synthetic cases; 172 actual bubble tracking graph exports represented by 46 distinct canonical graph visual groups. Each graph has a full 60-frame visual sequence, split and merge closeups and event storyboards. Ten particle truth/input sequences are included. Separately, the original 2026 particle branch successfully tracked straight_12x48 with 564/564 correct internal links (48-frame truth-versus-selected visualization); crossing_4x48 is a recorded FAILED test with no invented tracking output.

All published image assets are pixel-identical lossless WebP conversions from original PNGs on X:. Individual run graph CSV files and independent synthetic truth JSONs are included under data/, and their original hashes are preserved under machine/.

To serve from GitHub Pages after review/merge: use Settings > Pages > Deploy from branch > main > /docs. Expected project URL: https://mihails-birjukovs.github.io/MHT-X-v2/. A PR is not a deployed website.

Scientific caveats: synthetic kinematic proxies are not microscopy, physical CFD, or PIV-to-DFI reproduction. Binary max_k=2 is experimental model selection, not a universal default. MHTX-CLUTTER-01 is research-only, not implemented; Algorithm X remains the frozen exact-cover reference. FST-PSO explores parameter choices only. Reserved holdouts and raw experimental data are NOT included.

Source baseline: Mihails-Birjukovs/MHT-X-v2 @ 3f1343f90ce29ba42eede6d4de84531d8168768e.
