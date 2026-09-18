from interview_summary.strengths_generator import generate_strengths
from interview_summary.weaknesses_generator import generate_weaknesses
from interview_summary.cultural_fit import evaluate_cultural_fit
from interview_summary.risk_flags import generate_risk_flags
from interview_summary.inconsistency_summary import generate_inconsistency_summary
from interview_summary.hr_performance_summary import generate_hr_performance_summary


def generate_summary_template():

    strengths = generate_strengths()

    weaknesses = generate_weaknesses()

    cultural_fit = evaluate_cultural_fit()

    risk_flags = generate_risk_flags()

    inconsistencies = generate_inconsistency_summary()

    performance = generate_hr_performance_summary()

    summary = []

    total_questions = len(performance)

    for i in range(total_questions):

        summary.append({

            "Question ID":
                performance[i]["Question ID"],

            "Question":
                performance[i]["Question"],

            "Strength":
                strengths[i]["Strength"],

            "Weakness":
                weaknesses[i]["Weakness"],

            "Cultural Fit":
                cultural_fit[i]["Cultural Fit"],

            "Risk Flags":
                risk_flags[i]["Risk Flags"],

            "Inconsistency":
                inconsistencies[i]["Summary"],

            "Overall Performance":
                performance[i]["Performance"]

        })

    return summary