import json

from system_testing.system_tester import (
    run_system_test,
    save_test_report
)

from system_testing.conversation_optimizer import (
    optimize_conversation
)


# Load Final Screening Report (Day 28)
with open(
    "data/screening_reports/final_report.json",
    "r",
    encoding="utf-8"
) as file:

    final_report = json.load(file)


# Run Screening System Test
test_report = run_system_test(
    final_report
)


# Save Test Report
output_file = save_test_report(
    test_report
)


# Conversation Optimization
conversation = optimize_conversation(
    "silence",
    0
)


print()

print("=" * 60)
print("DAY 30 - SCREENING SYSTEM TESTING & OPTIMIZATION")
print("=" * 60)

print()

print("Candidate Experience")
print(test_report["experience"])

print()

print("Detected Intent")
print(test_report["intent"])

print()

print("Optimized Score")
print(test_report["optimized_score"])

print()

print("Final Decision")
print(test_report["decision"])

print()

print("Conversation Action")
print(conversation["action"])

print()

print("Conversation Message")
print(conversation["message"])

print()

print("Test Report Saved")

print(output_file)

print()

print("=" * 60)
print("COMPLETED SUCCESSFULLY")
print("=" * 60)