from final_demo.interview_demo import run_interview_demo
from final_demo.scoring_breakdown import generate_scoring_breakdown
from final_demo.hiring_recommendation import (
    extract_hiring_recommendation
)
from final_demo.architecture_summary import (
    generate_architecture_summary,
    generate_scoring_logic_summary
)
from final_demo.manager_feedback import (
    generate_manager_feedback_report
)
from final_demo.final_improvements import (
    identify_improvements
)
from final_demo.handover_summary import (
    generate_handover_summary
)


TRANSCRIPT_FILE = "data/transcripts/interview_transcript.txt"
FEEDBACK_FILE = "data/demo/manager_feedback.txt"


print("=" * 90)
print("DAY 45 - HR INTERVIEW DEMO & FINALIZATION")
print("=" * 90)


# ================================================================
# STEP 1 - CANDIDATE INTERVIEW SIMULATION
# ================================================================

print("\n[STEP 1] CANDIDATE INTERVIEW SIMULATION")
print("-" * 90)

demo_result = run_interview_demo(
    TRANSCRIPT_FILE
)

for key, value in demo_result.items():
    if key != "Transcript":
        print(f"{key:<35}: {value}")

print("\nInterview Transcript:")
print("-" * 90)

if demo_result["Transcript"]:
    print(demo_result["Transcript"])
else:
    print("No interview transcript available.")


# ================================================================
# STEP 2 - SCORING BREAKDOWN
# ================================================================

print("\n[STEP 2] SCORING BREAKDOWN")
print("-" * 90)

# Temporary test container.
# Replace with actual Day 41 unified scoring output
# during final integration.

score_data = {}

scoring_result = generate_scoring_breakdown(
    score_data
)

print(
    f"{'Status':<35}: "
    f"{scoring_result['Status']}"
)

print("\nScore Components:")

if scoring_result["Breakdown"]:
    for category, score in scoring_result[
        "Breakdown"
    ].items():
        print(f"{category:<35}: {score}")
else:
    print("No scoring output available.")


# ================================================================
# STEP 3 - FINAL HIRING RECOMMENDATION
# ================================================================

print("\n[STEP 3] FINAL HIRING RECOMMENDATION")
print("-" * 90)

recommendation_result = extract_hiring_recommendation(
    score_data
)

for key, value in recommendation_result.items():
    print(f"{key:<35}: {value}")


# ================================================================
# STEP 4 - ARCHITECTURE & SCORING LOGIC
# ================================================================

print("\n[STEP 4] ARCHITECTURE & SCORING LOGIC")
print("-" * 90)

architecture_components = [
    "Candidate Data",
    "ATS Evaluation",
    "Screening Evaluation",
    "HR Interview",
    "Follow-Up Logic",
    "Communication Evaluation",
    "Unified Scoring",
    "Ethics & Compliance"
]

scoring_components = [
    "ATS Score",
    "Screening Score",
    "HR Interview Score",
    "Unified Candidate Score",
    "Hiring Fit"
]

architecture_result = generate_architecture_summary(
    architecture_components
)

scoring_logic_result = generate_scoring_logic_summary(
    scoring_components
)

print(
    f"{'Architecture Status':<35}: "
    f"{architecture_result['Status']}"
)

print("\nArchitecture Components:")

for index, component in enumerate(
    architecture_result["Components"],
    start=1
):
    print(f"{index}. {component}")

print(
    f"\n{'Scoring Status':<35}: "
    f"{scoring_logic_result['Status']}"
)

print("\nScoring Components:")

for index, component in enumerate(
    scoring_logic_result["Components"],
    start=1
):
    print(f"{index}. {component}")


# ================================================================
# STEP 5 - MANAGER EVALUATION FEEDBACK
# ================================================================

print("\n[STEP 5] MANAGER EVALUATION FEEDBACK")
print("-" * 90)

feedback_result = generate_manager_feedback_report(
    FEEDBACK_FILE
)

for key, value in feedback_result.items():
    if key != "Feedback":
        print(f"{key:<35}: {value}")

print("\nManager Feedback:")

if feedback_result["Feedback"]:
    for key, value in feedback_result[
        "Feedback"
    ].items():
        print(f"{key:<35}: {value}")
else:
    print("No manager feedback available.")


# ================================================================
# STEP 6 - FINAL IMPROVEMENTS
# ================================================================

print("\n[STEP 6] FINAL IMPROVEMENTS")
print("-" * 90)

improvement_result = identify_improvements(
    feedback_result["Feedback"]
)

for key, value in improvement_result.items():
    if key != "Improvements":
        print(f"{key:<35}: {value}")

print("\nImprovement Actions:")

if improvement_result["Improvements"]:

    for index, item in enumerate(
        improvement_result["Improvements"],
        start=1
    ):
        print(f"{index}. {item['Area']}")
        print(
            f"   Action: {item['Action']}"
        )

else:
    print("No immediate improvements identified.")


# ================================================================
# STEP 7 - SYSTEM HANDOVER
# ================================================================

print("\n[STEP 7] SYSTEM HANDOVER")
print("-" * 90)

handover_result = generate_handover_summary(
    demo_result,
    scoring_result,
    recommendation_result,
    architecture_result,
    scoring_logic_result,
    feedback_result,
    improvement_result
)

for key, value in handover_result.items():
    print(f"{key:<35}: {value}")


# ================================================================
# FINAL STATUS
# ================================================================

print("\n" + "=" * 90)
print(" HR INTERVIEW AI DEMO COMPLETED")
print("=" * 90)