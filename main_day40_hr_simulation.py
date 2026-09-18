from hr_simulation.interview_sessions import simulate_interview_sessions
from hr_simulation.candidate_type_detector import detect_candidate_type
from hr_simulation.ai_manual_comparison import compare_ai_manual_scores
from hr_simulation.scoring_inconsistency import identify_scoring_inconsistencies
from hr_simulation.accuracy_evaluation import evaluate_accuracy
from hr_simulation.improvement_recommendations import generate_improvement_recommendations
from hr_simulation.test_report import generate_test_report
from hr_simulation.simulation_summary import generate_simulation_summary


def display_section(title, data):

    print("\n")
    print("=" * 90)
    print(title.center(90))
    print("=" * 90)

    if isinstance(data, list):

        for item in data:

            for key, value in item.items():

                print(f"{key:<30}: {value}")

            print("-" * 90)

    elif isinstance(data, dict):

        for key, value in data.items():

            print(f"{key:<30}: {value}")


print("\n")
print("=" * 90)
print("DAY 40 - HR INTERVIEW SIMULATION".center(90))
print("=" * 90)

display_section(
    "1. INTERVIEW SESSION SIMULATION",
    simulate_interview_sessions()
)

display_section(
    "2. CANDIDATE TYPE DETECTOR",
    detect_candidate_type()
)

display_section(
    "3. AI VS MANUAL COMPARISON",
    compare_ai_manual_scores()
)

display_section(
    "4. SCORING INCONSISTENCY",
    identify_scoring_inconsistencies()
)

display_section(
    "5. ACCURACY EVALUATION",
    evaluate_accuracy()
)

display_section(
    "6. IMPROVEMENT RECOMMENDATIONS",
    generate_improvement_recommendations()
)

display_section(
    "7. HR INTERVIEW TEST REPORT",
    generate_test_report()
)

display_section(
    "8. HR SIMULATION SUMMARY",
    generate_simulation_summary()
)

print("\n")
print("=" * 90)
print("DAY 40 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)