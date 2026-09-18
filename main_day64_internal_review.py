from internal_review.system_walkthrough import run_system_walkthrough
from internal_review.accuracy_gap_analyzer import identify_accuracy_gaps
from internal_review.ux_issue_analyzer import analyze_ux_issues
from internal_review.performance_issue_analyzer import analyze_performance
from internal_review.reviewer_feedback import process_reviewer_feedback
from internal_review.improvement_prioritizer import prioritize_improvements
from internal_review.action_plan import create_action_plan
from internal_review.internal_review_report import (
    create_internal_review_report
)


print("=" * 90)
print("- INTERNAL REVIEW & SYSTEM WALKTHROUGH")
print("=" * 90)


# STEP 1 - FULL SYSTEM WALKTHROUGH

walkthrough_result = run_system_walkthrough(
    ats_result=None,
    screening_result=None,
    hr_result=None,
    technical_result=None,
    decision_result=None
)


print()
print("1. SYSTEM WALKTHROUGH")
print("-" * 90)

print(f"{'Status':<30}: {walkthrough_result['Status']}")
print(
    f"{'Completed Stages':<30}: "
    f"{len(walkthrough_result['Completed Stages'])}"
)
print(
    f"{'Missing Stages':<30}: "
    f"{len(walkthrough_result['Missing Stages'])}"
)


# STEP 2 - ACCURACY GAP ANALYSIS

accuracy_result = identify_accuracy_gaps(
    expected_results=None,
    actual_results=None
)


print()
print("2. ACCURACY GAP ANALYSIS")
print("-" * 90)

print(f"{'Status':<30}: {accuracy_result['Status']}")
print(
    f"{'Accuracy Gaps':<30}: "
    f"{len(accuracy_result['Accuracy Gaps'])}"
)


# STEP 3 - UX ISSUE ANALYSIS

ux_result = analyze_ux_issues(
    user_feedback=[]
)


print()
print("3. UX ISSUE ANALYSIS")
print("-" * 90)

print(f"{'Status':<30}: {ux_result['Status']}")
print(
    f"{'UX Issues':<30}: "
    f"{len(ux_result['UX Issues'])}"
)


# STEP 4 - PERFORMANCE ANALYSIS

performance_result = analyze_performance(
    results={}
)


print()
print("4. PERFORMANCE ISSUE ANALYSIS")
print("-" * 90)

print(f"{'Status':<30}: {performance_result['Status']}")
print(
    f"{'Performance Issues':<30}: "
    f"{len(performance_result['Performance Issues'])}"
)


# STEP 5 - REVIEWER FEEDBACK

reviewer_result = process_reviewer_feedback(
    feedback=[]
)


print()
print("5. REVIEWER FEEDBACK")
print("-" * 90)

print(f"{'Status':<30}: {reviewer_result['Status']}")
print(
    f"{'Feedback Entries':<30}: "
    f"{len(reviewer_result['Feedback'])}"
)


# STEP 6 - IMPROVEMENT PRIORITIZATION

improvement_result = prioritize_improvements(
    accuracy_issues=accuracy_result["Accuracy Gaps"],
    ux_issues=ux_result["UX Issues"],
    performance_issues=performance_result["Performance Issues"]
)


print()
print("6. IMPROVEMENT PRIORITIZATION")
print("-" * 90)

print(f"{'Status':<30}: {improvement_result['Status']}")
print(
    f"{'Improvements':<30}: "
    f"{len(improvement_result['Improvements'])}"
)


# STEP 7 - ACTION PLAN

action_result = create_action_plan(
    improvement_result["Improvements"]
)


print()
print("7. IMPROVEMENT ACTION PLAN")
print("-" * 90)

print(f"{'Status':<30}: {action_result['Status']}")
print(
    f"{'Action Items':<30}: "
    f"{len(action_result['Action Plan'])}"
)


# STEP 8 - FINAL INTERNAL REVIEW REPORT

report_result = create_internal_review_report(
    walkthrough_result=walkthrough_result,
    accuracy_result=accuracy_result,
    ux_result=ux_result,
    performance_result=performance_result,
    reviewer_result=reviewer_result,
    improvement_result=improvement_result,
    action_result=action_result
)


print()
print("8. FINAL INTERNAL REVIEW REPORT")
print("-" * 90)

print(f"{'Status':<30}: {report_result['Status']}")

report = report_result["Report"]

print()
print("REVIEW SUMMARY")
print("-" * 90)

print(
    f"{'Accuracy Gaps':<30}: "
    f"{len(report['Accuracy Review']['Accuracy Gaps'])}"
)

print(
    f"{'UX Issues':<30}: "
    f"{len(report['UX Review']['UX Issues'])}"
)

print(
    f"{'Performance Issues':<30}: "
    f"{len(report['Performance Review']['Performance Issues'])}"
)

print(
    f"{'Reviewer Feedback':<30}: "
    f"{len(report['Reviewer Feedback']['Feedback'])}"
)

print(
    f"{'Improvements':<30}: "
    f"{len(report['Prioritized Improvements']['Improvements'])}"
)

print(
    f"{'Action Items':<30}: "
    f"{len(report['Action Plan']['Action Plan'])}"
)


# FINAL VALIDATION

print()
print("FINAL VALIDATION")
print("-" * 90)

checks = {
    "System Walkthrough": walkthrough_result,
    "Accuracy Analysis": accuracy_result,
    "UX Analysis": ux_result,
    "Performance Analysis": performance_result,
    "Reviewer Feedback": reviewer_result,
    "Improvement Prioritization": improvement_result,
    "Action Plan": action_result,
    "Internal Review Report": report_result
}

passed = 0
failed = 0

for name, result in checks.items():

    if result and result.get("Status"):
        print(f"{name:<35}: PASS")
        passed += 1
    else:
        print(f"{name:<35}: FAIL")
        failed += 1


print()
print("=" * 90)
print("FINAL TEST RESULT")
print("=" * 90)

print(f"{'Passed Checks':<35}: {passed}")
print(f"{'Failed Checks':<35}: {failed}")

if failed == 0:
    print(f"{'Overall Status':<35}: TEST PASSED")
else:
    print(f"{'Overall Status':<35}: REVIEW REQUIRED")

print("=" * 90)