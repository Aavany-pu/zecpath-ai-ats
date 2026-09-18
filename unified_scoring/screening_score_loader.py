from screening_engine.screening_score import calculate_screening_score


def load_screening_score():

    screening_result = calculate_screening_score()

    results = []

    for item in screening_result:

        results.append({

            "Candidate": item["Candidate"],

            "Screening Score": item["Screening Score"]

        })

    return results