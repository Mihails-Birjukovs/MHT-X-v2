"""Fail-closed source-tree publication validator for synthetic-only MHT-X Pages."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
DOC=ROOT/"docs"
ARCH=DOC/"archive"
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for c in iter(lambda:f.read(1<<20),b""):h.update(c)
 return h.hexdigest()
def validate():
 for name in ("index.md","benchmarks.md","methods.md","published-motion-equations.md","licensing.md",
              "stylesheets/inm-mhtx-v1.css","javascripts/mathjax.js","assets/inm-horizontal.svg","assets/inm-mark.svg","assets/inm-square-footer.svg","assets/mhtx-header-placeholder.svg",
              "assets/mhtx-footer-placeholder.svg","archive/index.html",
              "archive/controls/index.html","archive/PUBLICATION_MANIFEST.json",
              "archive/controls/NARY_AND_CLUTTER_CONTROL_RESULTS.csv"):
  if not (DOC/name).is_file():raise ValueError("Required public file missing "+name)
 receipt=json.loads((ARCH/"PUBLICATION_MANIFEST.json").read_text(encoding="utf-8"))
 if receipt["new_control_tracker_runs"]!=12 or receipt["original_bubble_graph_exports"]!=172:
  raise ValueError("Misclassified original versus new result coverage")
 if receipt["reserved_holdouts_included"] or receipt["unpublished_experimental_data_included"]:
  raise ValueError("Forbidden unpublished source content")
 listed=receipt["offline_package_content_list"]
 for record in listed:
  p=ARCH/record["path"]
  if not p.is_file() or sha(p)!=record["sha256"]:
   raise ValueError("Corrupted original evidence path "+record["path"])
 actual={str(p.relative_to(ARCH)).replace("\\","/") for p in ARCH.rglob("*") if p.is_file()
         and "downloads" not in p.relative_to(ARCH).parts
         and p.name!="PUBLICATION_MANIFEST.json"}
 expected={r["path"] for r in listed}
 if actual!=expected:raise ValueError("Unexpected added/removed public evidence files "+repr((actual-expected,expected-actual)))
 controls=json.loads((ARCH/"controls"/"NARY_AND_CLUTTER_CONTROL_RESULTS.json").read_text(encoding="utf-8"))
 if controls["status"]!="PASS_ALL" or len(controls["results"])!=12:
  raise ValueError("Missing completed negative/ternary scientific controls")
 source=json.loads((ARCH/"machine"/"PUBLIC_SOURCE_MANIFEST.json").read_text(encoding="utf-8"))
 if len(source["source_run_files"])!=172:raise ValueError("Wrong original graph run count")
 zipfile=ARCH/"downloads"/"MHTX_Synthetic_Visual_Archive_Portable_2026-11-15_v2.zip"
 hashfile=Path(str(zipfile)+".sha256")
 if not zipfile.is_file() or zipfile.stat().st_size>=100_000_000 or not hashfile.is_file():
  raise ValueError("Portable ZIP missing or above single-file limit")
 expectedhash=hashfile.read_text(encoding="utf-8").split()[0]
 if sha(zipfile)!=expectedhash:raise ValueError("Standalone portable archive SHA mismatch")
 for p in DOC.rglob("*"):
  if p.is_symlink():raise ValueError("Symlink forbidden "+str(p))
  if not p.is_file():continue
  if p.suffix.lower() not in (".md",".css",".html",".json",".csv",".webp",".gif",".zip",".sha256",".svg",".txt",".js",""):
   raise ValueError("Unexpected file type "+str(p))
  if p.suffix.lower()==".js" and p.relative_to(DOC).as_posix()!="javascripts/mathjax.js":
   raise ValueError("Unexpected Javascript asset "+str(p))
  if p.suffix.lower() in (".md",".html",".json",".csv",".css",".svg",".js"):
   txt=p.read_text(encoding="utf-8")
   for pattern in (r"X:\\",r"X:/",r"C:\\Users\\",r"C:/Users/",r"github_pat_[A-Za-z0-9_]{20,}",r"ghp_[A-Za-z0-9]{25,}"):
    if re.search(pattern,txt):raise ValueError("Sensitive string found in "+str(p))
 approved={"inm-horizontal.svg":"33938b2a9a6ae442b3ede153fb79187a31040a68",
           "inm-mark.svg":"b3a5154d96b0daf24cd44711fa13980689119287",
           "inm-square-footer.svg":"327ffd7d447e8475e4c8f0e0d0fa68f465be841b"}
 for name,blob in approved.items():
  raw=(DOC/"assets"/name).read_bytes()
  actual_blob=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\x00"+raw).hexdigest()
  if actual_blob!=blob:raise ValueError("Institutional image source drift "+name)
  if re.search(rb"<script|<foreignObject|onload=|javascript:|<image\b|<a\b|href=",raw,re.I):
   raise ValueError("Unexpected active SVG content "+name)
 conf=(ROOT/"zensical.toml").read_text(encoding="utf-8")
 js=(DOC/"javascripts"/"mathjax.js").read_text(encoding="utf-8")
 if "mathjax@3.2.2" not in conf or "pymdownx.arithmatex.generic = true" not in conf or 'tags: "all"' not in js:
  raise ValueError("MathJax numbering configuration not pinned")
 for name in ("methods.md","published-motion-equations.md"):
  body=(DOC/name).read_text(encoding="utf-8")
  if body.count("$$")%2 or body.count("\\label{eq:")<1:
   raise ValueError("Unmatched display equation or missing label "+name)
  labels=re.findall(r"\\label\{([^}]+)\}",body)
  if len(labels)!=len(set(labels)):
   raise ValueError("Duplicate math label in "+name)
 print("PUBLIC_SOURCE_QA_PASS",len(listed),"curated evidence objects, 12 new controls, 172 original runs; 3 approved INM SVG blobs; numbered math")
if __name__=="__main__":
 try:validate()
 except Exception as e:
  print("PUBLIC_SOURCE_QA_FAIL",repr(e),file=sys.stderr);sys.exit(2)
