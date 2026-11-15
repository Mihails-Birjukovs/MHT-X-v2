import unittest,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_mhtx_public_site import validate
class TestPublicDocumentation(unittest.TestCase):
 def test_source_allowlist_and_rights(self):
  validate()
 def test_required_source_theme(self):
  style=(ROOT/"docs/stylesheets/inm-mhtx-v1.css").read_text(encoding="utf-8")
  self.assertIn(".inm-hero",style)
  self.assertIn("#f47b20",style)
 def test_no_private_mark(self):
  logo=(ROOT/"docs/assets/mhtx-footer-placeholder.svg").read_text(encoding="utf-8")
  self.assertIn("PLACEHOLDER",logo)
if __name__=="__main__":unittest.main()
