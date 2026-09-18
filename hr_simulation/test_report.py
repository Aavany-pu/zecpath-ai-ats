from hr_simulation.interview_sessions import simulate_interview_sessions
from hr_simulation.candidate_type_detector import detect_candidate_type
from hr_simulation.ai_manual_comparison import compare_ai_manual_scores
from hr_simulation.scoring_inconsistency import identify_scoring_inconsistencies
from hr_simulation.accuracy_evaluation import evaluate_accuracy
from hr_simulation.improvement_recommendations import generate_improvement_recommendations


def generate_test_report():

    sessions = simulate_interview_sessions()

    candidate_types = detect_candidate_type()

    comparison = compare_ai_manual_scores()

    inconsistencies = identify_scoring_inconsistencies()

    accuracy = evaluate_accuracy()

    recommendations = generate_improvement_recommendations()

    report = []

    total_questions = len(sessions)

    for i in range(total_questions):

        report.append({

            "Session ID":
                sessions[i]["Session ID"],

            "Question":
                sessions[i]["Question"],

            "Candidate Type":
                candidate_types[i]["Candidate Type"],

            "AI Score":
                comparison[i]["AI Score"],

            "Manual Score":
                comparison[i]["Manual Score"],

            "Difference":
                comparison[i]["Difference"],

            "Consistency":
                inconsistencies[i]["Consistency Status"],

            "Accuracy":
                accuracy[i]["Accuracy (%)"],

            "Recommendation":
                recommendations[i]["Recommendations"]

        })

    return report