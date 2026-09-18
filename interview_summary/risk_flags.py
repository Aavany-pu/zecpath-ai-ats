from hr_scoring_engine.candidate_report import generate_candidate_report
from confidence_stress.stress_indicator import measure_stress
from confidence_stress.contradiction_detector import detect_contradictions


def generate_risk_flags():

    report = generate_candidate_report()

    stress = measure_stress()

    contradiction = detect_contradictions()

    results = []

    total_questions = len(report)

    for i in range(total_questions):

        risk_flags = []

        if report[i]["Final HR Score"] < 60:

            risk_flags.append("Low HR Score")

        if stress[i]["Stress Level"] == "High":

            risk_flags.append("High Stress")

        if contradiction[i]["Status"] == "Contradiction Found":

            risk_flags.append("Inconsistent Answers")

        if len(risk_flags) == 0:

            risk_flags.append("No Major Risk")

        results.append({

            "Question ID": report[i]["Question ID"],

            "Question": report[i]["Question"],

            "Risk Flags": risk_flags

        })

    return results