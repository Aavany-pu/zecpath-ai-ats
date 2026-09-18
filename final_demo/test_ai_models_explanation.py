from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from final_demo.ai_models_explanation import generate_ai_models_explanation


print("=" * 90)
print(" AI MODELS EXPLANATION")
print("=" * 90)

model_data = {}

result = generate_ai_models_explanation(model_data)

print(f"{'Status':<30}: {result['Status']}")
print(f"{'Model Components':<30}: {len(result['Models'])}")

print("=" * 90)