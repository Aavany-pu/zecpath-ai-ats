from hr_simulation.ai_manual_comparison import compare_ai_manual_scores


def identify_scoring_inconsistencies():

    comparison = compare_ai_manual_scores()

    results = []

    for item in comparison:

        difference = item["Difference"]

        if difference <= 5:

            status = "Consistent"

        elif difference <= 10:

            status = "Minor Difference"

        else:

            status = "Major Difference"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "AI Score": item["AI Score"],

            "Manual Score": item["Manual Score"],

            "Difference": difference,

            "Consistency Status": status

        })

    return results