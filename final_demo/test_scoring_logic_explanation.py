from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from final_demo.scoring_logic_explanation import (
    generate_scoring_logic_explanation
)


print("=" * 90)
print("- SCORING LOGIC EXPLANATION")
print("=" * 90)

scoring_data = {}

result = generate_scoring_logic_explanation(scoring_data)

print(f"{'Status':<30}: {result['Status']}")
print(f"{'Scoring Components':<30}: "
      f"{len(result['Scoring Logic'])}")

print("=" * 90)