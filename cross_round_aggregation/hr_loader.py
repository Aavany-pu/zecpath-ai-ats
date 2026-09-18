from hr_scoring_engine.hr_score_engine import generate_hr_scores


def load_hr_score():

    hr_scores = generate_hr_scores()

    if not hr_scores:
        raise ValueError(
            "No HR interview scores were generated."
        )

    total_score = 0
    valid_scores = 0

    for item in hr_scores:

        score = item.get(
            "HR Interview Score"
        )

        if isinstance(score, (int, float)):
            total_score += score
            valid_scores += 1

    if valid_scores == 0:
        raise ValueError(
            "No valid HR interview scores found."
        )

    final_hr_score = total_score / valid_scores

    return round(final_hr_score, 2)


def get_hr_score():

    return load_hr_score()