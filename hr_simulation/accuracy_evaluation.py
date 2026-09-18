from hr_simulation.ai_manual_comparison import compare_ai_manual_scores


def evaluate_accuracy():

    comparison = compare_ai_manual_scores()

    results = []

    for item in comparison:

        difference = item["Difference"]

        accuracy = round(100 - difference, 2)

        if accuracy < 0:

            accuracy = 0

        if accuracy >= 95:

            rating = "Excellent"

        elif accuracy >= 85:

            rating = "Good"

        elif accuracy >= 70:

            rating = "Average"

        else:

            rating = "Poor"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "AI Score": item["AI Score"],

            "Manual Score": item["Manual Score"],

            "Accuracy (%)": accuracy,

            "Accuracy Rating": rating

        })

    return results