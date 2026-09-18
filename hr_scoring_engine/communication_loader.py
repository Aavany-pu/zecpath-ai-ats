from communication_evaluation.communication_score import calculate_communication_score


def load_communication_scores():

    communication_scores = calculate_communication_score()

    results = []

    for item in communication_scores:

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Communication Score": item["Communication Score"]

        })

    return results