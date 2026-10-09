import json, pathlib, subprocess, unittest
ROOT = pathlib.Path(__file__).resolve().parent
class Packaging(unittest.TestCase):
    def test_syntax(self):
        for path in ROOT.glob("*.sh"):
            self.assertEqual(subprocess.run(["bash", "-n", str(path)], capture_output=True).returncode, 0, path.name)
    def test_marker(self):
        self.assertIn("# pi-app-store: 1", (ROOT/"app-store.sh").read_text().splitlines()[:5])
    def test_version(self):
        self.assertEqual(json.loads((ROOT/"app-version.json").read_text())["version"], "1.0.0")
    def test_safe_install(self):
        self.assertEqual(subprocess.run(["bash", "app-store.sh", "install"], cwd=ROOT, capture_output=True).returncode, 0)
    def test_entry(self):
        self.assertTrue((ROOT/"coolpi.sh").is_file())
if __name__ == "__main__": unittest.main()
