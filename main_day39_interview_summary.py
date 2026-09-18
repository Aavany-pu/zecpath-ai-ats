from interview_summary.strengths_generator import generate_strengths
from interview_summary.weaknesses_generator import generate_weaknesses
from interview_summary.cultural_fit import evaluate_cultural_fit
from interview_summary.risk_flags import generate_risk_flags
from interview_summary.inconsistency_summary import generate_inconsistency_summary
from interview_summary.hr_performance_summary import generate_hr_performance_summary
from interview_summary.interview_report import generate_interview_report
from interview_summary.summary_template import generate_summary_template


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
print("DAY 39 - INTERVIEW SUMMARY GENERATOR".center(90))
print("=" * 90)

display_section(
    "1. CANDIDATE STRENGTHS",
    generate_strengths()
)

display_section(
    "2. CANDIDATE WEAKNESSES",
    generate_weaknesses()
)

display_section(
    "3. CULTURAL FIT INDICATORS",
    evaluate_cultural_fit()
)

display_section(
    "4. RISK FLAGS",
    generate_risk_flags()
)

display_section(
    "5. INCONSISTENCY SUMMARY",
    generate_inconsistency_summary()
)

display_section(
    "6. HR PERFORMANCE SUMMARY",
    generate_hr_performance_summary()
)

display_section(
    "7. AI INTERVIEW REPORT",
    generate_interview_report()
)

display_section(
    "8. STRUCTURED SUMMARY TEMPLATE",
    generate_summary_template()
)

print("\n")
print("=" * 90)
print("DAY 39 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)