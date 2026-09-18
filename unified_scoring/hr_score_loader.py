from hr_scoring_engine.hr_score_engine import generate_hr_scores


def load_hr_score():

    hr_result = generate_hr_scores()

    results = []

    for item in hr_result:

        results.append({

            "Candidate": item["Candidate"],

            "HR Interview Score": item["HR Interview Score"]

        })

    return results