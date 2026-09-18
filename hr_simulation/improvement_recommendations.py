from hr_simulation.accuracy_evaluation import evaluate_accuracy
from hr_simulation.scoring_inconsistency import identify_scoring_inconsistencies


def generate_improvement_recommendations():

    accuracy = evaluate_accuracy()

    inconsistency = identify_scoring_inconsistencies()

    results = []

    total_questions = len(accuracy)

    for i in range(total_questions):

        recommendations = []

        if accuracy[i]["Accuracy (%)"] < 85:

            recommendations.append(
                "Improve AI scoring accuracy."
            )

        if inconsistency[i]["Consistency Status"] == "Major Difference":

            recommendations.append(
                "Review scoring logic."
            )

        elif inconsistency[i]["Consistency Status"] == "Minor Difference":

            recommendations.append(
                "Fine-tune score weights."
            )

        if len(recommendations) == 0:

            recommendations.append(
                "Current evaluation is satisfactory."
            )

        results.append({

            "Question ID":
                accuracy[i]["Question ID"],

            "Question":
                accuracy[i]["Question"],

            "Recommendations":
                recommendations

        })

    return results