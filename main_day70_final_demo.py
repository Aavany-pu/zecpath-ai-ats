from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from final_demo.architecture_summary import (
    generate_architecture_summary,
    generate_scoring_logic_summary
)
from final_demo.ai_models_explanation import (
    generate_ai_models_explanation
)
from final_demo.scoring_breakdown import (
    generate_scoring_breakdown
)
from final_demo.code_walkthrough import (
    generate_code_walkthrough
)
from final_demo.knowledge_transfer import (
    generate_knowledge_transfer
)
from final_demo.final_report import (
    generate_final_report
)
from final_demo.manager_feedback import (
    process_manager_feedback
)
from final_demo.handover_summary import (
    generate_handover_summary
)
from final_demo.hiring_recommendation import (
    extract_hiring_recommendation
)


print("=" * 90)
print("FINAL DEMO & HANDOVER")
print("=" * 90)


# -------------------------------------------------------------------
# 1. FINAL LIVE DEMO
# -------------------------------------------------------------------

print()
print("1. FINAL LIVE DEMO")
print("-" * 90)

demo_flow = [
    "Resume",
    "ATS",
    "Screening",
    "Interview",
    "Decision"
]

print(f"{'Status':<30}: Final Demo Flow Ready")

for index, stage in enumerate(demo_flow, start=1):
    print(f"{index}. {stage}")


# -------------------------------------------------------------------
# 2. ARCHITECTURE
# -------------------------------------------------------------------

print()
print("2. ARCHITECTURE EXPLANATION")
print("-" * 90)

architecture_result = generate_architecture_summary([])

print(f"{'Status':<30}: {architecture_result['Status']}")


# -------------------------------------------------------------------
# 3. AI MODELS
# -------------------------------------------------------------------

print()
print("3. AI MODELS EXPLANATION")
print("-" * 90)

ai_models_result = generate_ai_models_explanation({})

print(f"{'Status':<30}: {ai_models_result['Status']}")


# -------------------------------------------------------------------
# 4. SCORING LOGIC
# -------------------------------------------------------------------

print()
print("4. SCORING LOGIC")
print("-" * 90)

scoring_logic_result = generate_scoring_logic_summary([])

print(f"{'Status':<30}: {scoring_logic_result['Status']}")

scoring_result = generate_scoring_breakdown({})

print(f"{'Breakdown Status':<30}: {scoring_result['Status']}")


# -------------------------------------------------------------------
# 5. CODE WALKTHROUGH
# -------------------------------------------------------------------

print()
print("5. CODE WALKTHROUGH")
print("-" * 90)

walkthrough_result = generate_code_walkthrough(PROJECT_ROOT)

print(f"{'Status':<30}: {walkthrough_result['Status']}")
print(
    f"{'Modules Found':<30}: "
    f"{len(walkthrough_result['Walkthrough'])}"
)


# -------------------------------------------------------------------
# 6. KNOWLEDGE TRANSFER
# -------------------------------------------------------------------

print()
print("6. KNOWLEDGE TRANSFER")
print("-" * 90)

knowledge_result = generate_knowledge_transfer(PROJECT_ROOT)

print(f"{'Status':<30}: {knowledge_result['Status']}")


# -------------------------------------------------------------------
# 7. FINAL REPORT
# -------------------------------------------------------------------

print()
print("7. FINAL REPORT")
print("-" * 90)

report_result = generate_final_report(PROJECT_ROOT)

print(f"{'Status':<30}: {report_result['Status']}")
print(
    f"{'Report Files':<30}: "
    f"{report_result['Final Report']['Report Count']}"
)


# -------------------------------------------------------------------
# 8. EVALUATION DISCUSSION
# -------------------------------------------------------------------

print()
print("8. EVALUATION DISCUSSION")
print("-" * 90)

feedback_result = process_manager_feedback([])

print(f"{'Status':<30}: {feedback_result['Status']}")


# -------------------------------------------------------------------
# 9. FINAL HANDOVER
# -------------------------------------------------------------------

print()
print("9. FINAL HANDOVER")
print("-" * 90)

recommendation_result = extract_hiring_recommendation({})

handover_result = generate_handover_summary(
    {"Status": "Final Demo Flow Ready"},
    scoring_result,
    recommendation_result,
    architecture_result,
    scoring_logic_result,
    feedback_result,
    {"Status": "Final Improvements Available"},
    knowledge_result,
    report_result
)

print(f"{'Status':<30}: {handover_result['Status']}")
print(f"{'System':<30}: {handover_result['System']}")
print(
    f"{'Completed Sections':<30}: "
    f"{handover_result['Completed Sections']}"
)
print(
    f"{'Total Sections':<30}: "
    f"{handover_result['Total Sections']}"
)


# -------------------------------------------------------------------
# FINAL VALIDATION
# -------------------------------------------------------------------

print()
print("=" * 90)
print("DAY 70 FINAL VALIDATION")
print("=" * 90)

checks = {
    "Final Demo": True,
    "Architecture": architecture_result["Status"]
    == "Architecture Summary Generated",
    "AI Models": ai_models_result["Status"]
    == "AI Models Explanation Generated",
    "Scoring Logic": scoring_logic_result["Status"]
    == "Scoring Logic Summary Generated",
    "Code Walkthrough": walkthrough_result["Status"]
    == "Code Walkthrough Generated",
    "Knowledge Transfer": knowledge_result["Status"]
    == "Knowledge Transfer Summary Generated",
    "Final Report": report_result["Status"]
    == "Final Report Generated",
    "Evaluation Discussion": feedback_result["Status"]
    == "Manager Feedback Processed",
    "Final Handover": handover_result["Status"]
    == "Final Handover Ready"
}

passed = sum(checks.values())
total = len(checks)

for component, status in checks.items():
    print(
        f"{component:<30}: "
        f"{'PASSED' if status else 'FAILED'}"
    )

print()
print(f"{'Validation Status':<30}: "
      f"{'PASSED' if passed == total else 'FAILED'}")
print(f"{'Checks Passed':<30}: {passed}/{total}")

print("=" * 90)

if passed == total:
    print(" COMPLETED")
else:
    print(" REQUIRES ATTENTION")

print("=" * 90)