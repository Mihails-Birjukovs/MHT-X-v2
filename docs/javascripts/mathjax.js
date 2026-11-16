// MathJax 3.2.2, pinned CDN runtime configured before loading.
// Required by Library /Tools/GitHub_Zensical_Documentation_Sites v1.1.0.
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    tags: "all",
    tagSide: "right",
    useLabelIds: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  }
};
if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (typeof MathJax === "undefined" || !MathJax.startup) return;
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
}
