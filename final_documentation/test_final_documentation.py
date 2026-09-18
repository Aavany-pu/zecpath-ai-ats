from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from final_documentation.final_documentation_validator import validate_final_documentation


print("=" * 90)
print("FINAL DOCUMENTATION VALIDATION")
print("=" * 90)

result = validate_final_documentation(PROJECT_ROOT)

print(f"{'Status':<25}: {result['Status']}")
print(f"{'Required Items':<25}: {result['Required Items']}")
print(f"{'Existing Items':<25}: {len(result['Existing Items'])}")
print(f"{'Missing Items':<25}: {len(result['Missing Items'])}")

if result["Missing Items"]:
    print()
    print("MISSING ITEMS")
    print("-" * 90)

    for item in result["Missing Items"]:
        print(f"- {item}")

print("=" * 90)