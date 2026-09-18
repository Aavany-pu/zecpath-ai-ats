from communication_evaluation.communication_score import calculate_communication_score


def normalize_scores():

    communication_scores = calculate_communication_score()

    normalized_scores = []

    for item in communication_scores:

        score = item["Communication Score"]

        if score >= 90:

            normalized = 95

        elif score >= 80:

            normalized = 85

        elif score >= 70:

            normalized = 75

        elif score >= 60:

            normalized = 65

        elif score >= 50:

            normalized = 55

        else:

            normalized = score

        normalized_scores.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Original Score": score,

            "Normalized Score": normalized

        })

    return normalized_scores