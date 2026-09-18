from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from final_demo.code_walkthrough import generate_code_walkthrough


print("=" * 90)
print("DAY 70 - CODE WALKTHROUGH")
print("=" * 90)

result = generate_code_walkthrough(PROJECT_ROOT)

print(f"{'Status':<30}: {result['Status']}")

print()
print("PROJECT MODULES")
print("-" * 90)

for item in result["Walkthrough"]:
    print(
        f"{item['Module']:<30}: "
        f"{item['Python Files']} Python files"
    )

print("=" * 90)