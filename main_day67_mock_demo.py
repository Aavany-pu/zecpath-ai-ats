from mock_demo.mock_demo_structure import (
    create_mock_demo_structure
)

from mock_demo.stakeholder_questions import (
    create_stakeholder_questions
)

from mock_demo.explanation_analyzer import (
    analyze_explanation
)

from mock_demo.clarity_improver import (
    improve_clarity
)

from mock_demo.demo_timing import (
    create_demo_timing
)

from mock_demo.demo_feedback_report import (
    generate_demo_feedback_report
)

from mock_demo.improved_presentation import (
    create_improved_presentation
)

from mock_demo.final_demo_readiness import (
    check_demo_readiness
)


print("=" * 90)
print("- FINAL MOCK DEMO TEST")
print("=" * 90)


# STEP 1
demo = create_mock_demo_structure()

print()
print("STEP 1 - MOCK DEMO STRUCTURE")
print("-" * 90)
print(f"{'Status':<30}: {demo['Status']}")


# STEP 2
questions = create_stakeholder_questions()

print()
print("STEP 2 - STAKEHOLDER Q&A")
print("-" * 90)
print(f"{'Status':<30}: {questions['Status']}")
print(f"{'Questions':<30}: {questions['Total Questions']}")


# STEP 3
explanation_result = analyze_explanation({
    "Problem Statement": "Prepared",
    "AI Solution": "Prepared",
    "System Architecture": "Prepared",
    "Demo Flow": "Prepared"
})

print()
print("STEP 3 - EXPLANATION ANALYSIS")
print("-" * 90)
print(f"{'Status':<30}: {explanation_result['Status']}")
print(
    f"{'Weak Areas':<30}: "
    f"{len(explanation_result['Weak Areas'])}"
)


# STEP 4
clarity_result = improve_clarity({
    "Problem Statement": "Prepared",
    "AI Solution": "Prepared",
    "System Architecture": "Prepared",
    "Demo Flow": "Prepared"
})

print()
print("STEP 4 - CLARITY IMPROVEMENT")
print("-" * 90)
print(f"{'Status':<30}: {clarity_result['Status']}")


# STEP 5
timing_result = create_demo_timing(
    demo["Stages"]
)

print()
print("STEP 5 - DEMO TIMING")
print("-" * 90)
print(f"{'Status':<30}: {timing_result['Status']}")
print(f"{'Stages':<30}: {timing_result['Total Stages']}")


# STEP 6
feedback_report = generate_demo_feedback_report(
    explanation_result,
    clarity_result,
    timing_result,
    questions
)

print()
print("STEP 6 - DEMO FEEDBACK REPORT")
print("-" * 90)
print(f"{'Status':<30}: {feedback_report['Status']}")
print(
    f"{'Report Sections':<30}: "
    f"{len(feedback_report['Report'])}"
)


# STEP 7
improved_presentation = create_improved_presentation(
    feedback_report,
    demo
)

print()
print("STEP 7 - IMPROVED PRESENTATION")
print("-" * 90)
print(f"{'Status':<30}: {improved_presentation['Status']}")


# STEP 8
readiness = check_demo_readiness(
    demo,
    questions,
    feedback_report,
    improved_presentation
)

print()
print("STEP 8 - FINAL DEMO READINESS")
print("-" * 90)
print(f"{'Status':<30}: {readiness['Status']}")
print(
    f"{'Missing Components':<30}: "
    f"{len(readiness['Missing Components'])}"
)


# STEP 9
print()
print("STEP 9 - FINAL VALIDATION")
print("-" * 90)

results = [
    demo,
    questions,
    explanation_result,
    clarity_result,
    timing_result,
    feedback_report,
    improved_presentation,
    readiness
]

failed = []

for result in results:
    if not isinstance(result, dict):
        failed.append("Invalid component")

    elif not result.get("Status"):
        failed.append("Missing status")


if not failed:
    print(f"{'Validation Status':<30}: PASSED")
    print(f"{'Components Tested':<30}: {len(results)}")
else:
    print(f"{'Validation Status':<30}: FAILED")
    print(f"{'Failed Components':<30}: {len(failed)}")


print()
print("=" * 90)

if not failed:
    print("COMPLETED")
else:
    print("TEST FAILED")

print("=" * 90)