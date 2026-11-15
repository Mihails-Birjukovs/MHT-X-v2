"""Inspect local strict Zensical build output; not a live GitHub Pages test."""
from pathlib import Path
import sys,re
ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/"site"
def check():
 pages=("index.html","getting-started/index.html","architecture/index.html",
   "methods/index.html","validation/index.html","benchmarks/index.html",
   "data-provenance/index.html","research/index.html","credits/index.html",
   "licensing/index.html","archive/index.html","archive/controls/index.html")
 for page in pages:
  f=SITE/page
  if not f.is_file():raise ValueError("Site page absent "+page)
 css=SITE/"stylesheets"/"inm-mhtx-v1.css"
 if not css.is_file():raise ValueError("Official INM themed source CSS missing")
 style=css.read_text(encoding="utf-8")
 for tag in (".inm-hero",".inm-identity",".md-footer","--inm-orange","#f47b20"):
  if tag not in style:raise ValueError("INM design token missing "+tag)
 home=(SITE/"index.html").read_text(encoding="utf-8")
 if "inm-hero" not in home or "inm-mhtx-v1.css" not in home:
  raise ValueError("Site home lacks active INM style link")
 browser=(SITE/"benchmarks/index.html").read_text(encoding="utf-8")
 if 'href="../archive/index.html"' not in browser or 'href="../archive/controls/index.html"' not in browser:
  raise ValueError("Main/control reviewer HTML links do not resolve under project subpath")
 for asset in ("assets/mhtx-header-placeholder.svg","assets/mhtx-footer-placeholder.svg",
  "archive/controls/NARY_AND_CLUTTER_CONTROL_RESULTS.csv",
  "archive/controls/SCIENCE_REPORT.txt","archive/SCIENCE_REPORT.txt",
  "archive/README.txt","archive/machine/ARCHIVE_QA.json",
  "archive/machine/PARTICLE_SYNTHETIC_REGRESSION_INVENTORY.csv",
  "archive/downloads/MHTX_Synthetic_Visual_Archive_Portable_2026-11-15_v2.zip",
  "archive/controls/data/truth/ternary_true_no_clutter.json"):
  if not (SITE/asset).is_file():raise ValueError("Built site missing evidence "+asset)
 print("ZENSICAL_GENERATED_SITE_PASS",len(pages),"pages + CSS and data/ZIP")
if __name__=="__main__":
 try:check()
 except Exception as e:
  print("ZENSICAL_GENERATED_SITE_FAIL",repr(e),file=sys.stderr);sys.exit(2)
