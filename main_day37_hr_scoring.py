from hr_scoring_engine.answer_relevance import evaluate_answer_relevance
from hr_scoring_engine.communication_loader import load_communication_scores
from hr_scoring_engine.confidence_loader import load_confidence_scores
from hr_scoring_engine.consistency_checker import check_consistency
from hr_scoring_engine.weight_configuration import get_weight_configuration
from hr_scoring_engine.hr_score_engine import generate_hr_scores
from hr_scoring_engine.score_breakdown import generate_score_breakdown
from hr_scoring_engine.interview_normalizer import normalize_interview_scores
from hr_scoring_engine.candidate_report import generate_candidate_report


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
print("DAY 37 - HR INTERVIEW SCORING ENGINE".center(90))
print("=" * 90)

display_section(
    "1. ANSWER RELEVANCE",
    evaluate_answer_relevance()
)

display_section(
    "2. COMMUNICATION SCORE",
    load_communication_scores()
)

display_section(
    "3. CONFIDENCE SCORE",
    load_confidence_scores()
)

display_section(
    "4. CONSISTENCY CHECKER",
    check_consistency()
)

display_section(
    "5. WEIGHT CONFIGURATION",
    get_weight_configuration()
)

display_section(
    "6. HR INTERVIEW SCORING ENGINE",
    generate_hr_scores()
)

display_section(
    "7. SCORE BREAKDOWN",
    generate_score_breakdown()
)

display_section(
    "8. INTERVIEW NORMALIZER",
    normalize_interview_scores()
)

display_section(
    "9. CANDIDATE HR SCORE REPORT",
    generate_candidate_report()
)

print("\n")
print("=" * 90)
print("DAY 37 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)