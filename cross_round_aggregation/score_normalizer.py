def normalize_score(score):

    if not isinstance(score, (int, float)):
        raise ValueError(
            "Score must be numeric."
        )

    if score < 0 or score > 100:
        raise ValueError(
            "Score must be between 0 and 100."
        )

    return round(score, 2)


def normalize_evaluation_scores(scores):

    normalized_scores = {}

    for round_name, score in scores.items():

        if score is None:
            normalized_scores[round_name] = None
            continue

        normalized_scores[round_name] = (
            normalize_score(score)
        )

    return normalized_scores


def get_normalized_scores(scores):

    return normalize_evaluation_scores(
        scores
    )