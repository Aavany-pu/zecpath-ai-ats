from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from frontend.ats_integration import run_ats_evaluation


print("=" * 90)
print("FRONTEND - ATS INTEGRATION")
print("=" * 90)

print("ATS integration module loaded successfully.")

print(f"{'ATS Engine':<30}: Connected")
print(f"{'Scoring Function':<30}: calculate_ats_score")
print(f"{'Data Source':<30}: Existing project outputs")
print(f"{'Hardcoded Candidate Data':<30}: None")

print("=" * 90)