import csv
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicScoutTest(unittest.TestCase):
    def test_public_script_generates_outputs(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/run_public_scout.py"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn("Loaded 6 public demo rows", result.stdout)
        self.assertTrue((ROOT / "outputs/public_demo_ranked_candidates.csv").exists())
        self.assertTrue((ROOT / "outputs/public_demo_explanation_cards.md").exists())
        self.assertTrue((ROOT / "outputs/public_demo_rows.svg").exists())

    def test_public_rows_match_allowlist(self) -> None:
        allowed_case_ids = {
            "COUMARIN-WATER-DIRECT",
            "CG-CB8-6MC-001",
            "TCA-CB8-FAMILY",
            "TCA-GCD-FAMILY",
            "CESTER-PD-NANOCAGE-FAMILY",
            "SCHEMA-PUBLIC-MECHANICS",
        }
        with (ROOT / "data/public_demo_cases.csv").open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 6)
        for row in rows:
            self.assertIn(row["case_id"], allowed_case_ids)


if __name__ == "__main__":
    unittest.main()
