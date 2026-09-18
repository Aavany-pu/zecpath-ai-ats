from hr_scoring_engine.hr_score_engine import generate_hr_scores


def normalize_interview_scores():

    hr_scores = generate_hr_scores()

    total_questions = len(hr_scores)

    normalized_results = []

    if total_questions == 0:

        return normalized_results

    for item in hr_scores:

        normalized_score = round(
            (item["HR Interview Score"] / 100) * 100,
            2
        )

        normalized_results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Original Score": item["HR Interview Score"],

            "Normalized Score": normalized_score,

            "Interview Length": total_questions

        })

    return normalized_results