import unittest,subprocess,pathlib,tempfile,os
ROOT=pathlib.Path(__file__).resolve().parent
class Security(unittest.TestCase):
 def test_no_direct_updater(self):
  for name in ['coolpi.sh','controls-fullscreen.sh','update-coolpi.sh']:
   s=(ROOT/name).read_text();self.assertNotIn('/tmp/coolpi_update.sh',s);self.assertNotIn('curl -sfL "$SCRIPT_URL"',s);self.assertNotIn('ensure_symlink\n',s)
 def test_update_helper_no_network(self):
  p=subprocess.run(['bash',str(ROOT/'update-coolpi.sh')],capture_output=True,text=True,timeout=3);self.assertEqual(p.returncode,0);self.assertIn('disabled',p.stdout)
 def test_source_quit_without_update(self):
  p=subprocess.run(['bash',str(ROOT/'coolpi.sh')],input='0\n',capture_output=True,text=True,timeout=3);self.assertEqual(p.returncode,0);self.assertNotIn('Checking for script updates',p.stdout)
if __name__=='__main__':unittest.main()
