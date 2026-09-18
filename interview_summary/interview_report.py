from interview_summary.strengths_generator import generate_strengths
from interview_summary.weaknesses_generator import generate_weaknesses
from interview_summary.cultural_fit import evaluate_cultural_fit
from interview_summary.risk_flags import generate_risk_flags
from interview_summary.inconsistency_summary import generate_inconsistency_summary
from interview_summary.hr_performance_summary import generate_hr_performance_summary


def generate_interview_report():

    strengths = generate_strengths()

    weaknesses = generate_weaknesses()

    culture = evaluate_cultural_fit()

    risks = generate_risk_flags()

    inconsistencies = generate_inconsistency_summary()

    performance = generate_hr_performance_summary()

    report = []

    total_questions = len(performance)

    for i in range(total_questions):

        summary = (

            f"The candidate demonstrated "

            f"{performance[i]['Performance']} performance "

            f"with a cultural fit of "

            f"{culture[i]['Cultural Fit']}. "

            f"Strength: {strengths[i]['Strength']}. "

            f"Weakness: {weaknesses[i]['Weakness']}. "

            f"Inconsistency: {inconsistencies[i]['Summary']}. "

            f"Risk: {', '.join(risks[i]['Risk Flags'])}."

        )

        report.append({

            "Question ID": performance[i]["Question ID"],

            "Question": performance[i]["Question"],

            "Interview Report": summary

        })

    return report