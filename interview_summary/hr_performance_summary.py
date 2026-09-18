from hr_scoring_engine.candidate_report import generate_candidate_report
from interview_summary.cultural_fit import evaluate_cultural_fit
from interview_summary.risk_flags import generate_risk_flags


def generate_hr_performance_summary():

    report = generate_candidate_report()

    cultural_fit = evaluate_cultural_fit()

    risk_flags = generate_risk_flags()

    results = []

    total_questions = len(report)

    for i in range(total_questions):

        hr_score = report[i]["Final HR Score"]

        culture = cultural_fit[i]["Cultural Fit"]

        risks = risk_flags[i]["Risk Flags"]

        if hr_score >= 90:

            performance = "Excellent"

        elif hr_score >= 75:

            performance = "Good"

        elif hr_score >= 60:

            performance = "Average"

        else:

            performance = "Needs Improvement"

        results.append({

            "Question ID": report[i]["Question ID"],

            "Question": report[i]["Question"],

            "HR Score": hr_score,

            "Performance": performance,

            "Cultural Fit": culture,

            "Risk Flags": risks

        })

    return results