from confidence_stress.confidence_score import calculate_confidence_score


def load_confidence_scores():

    confidence_scores = calculate_confidence_score()

    results = []

    for item in confidence_scores:

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Confidence Score": item["Confidence Score"],

            "Confidence Level": item["Confidence Level"]

        })

    return results