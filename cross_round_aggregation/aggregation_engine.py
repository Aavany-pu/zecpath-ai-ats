def aggregate_scores(scores, weights):

    if not isinstance(scores, dict):
        raise ValueError(
            "Scores must be provided as a dictionary."
        )

    if not isinstance(weights, dict):
        raise ValueError(
            "Weights must be provided as a dictionary."
        )

    weighted_total = 0
    applied_weight = 0

    for round_name, score in scores.items():

        if score is None:
            continue

        weight = weights.get(round_name)

        if weight is None:
            continue

        if not isinstance(score, (int, float)):
            continue

        if not isinstance(weight, (int, float)):
            continue

        weighted_total += score * weight
        applied_weight += weight

    if applied_weight == 0:
        raise ValueError(
            "No valid scores and weights available."
        )

    final_score = (
        weighted_total / applied_weight
    )

    return round(final_score, 2)


def get_aggregated_score(scores, weights):

    return aggregate_scores(
        scores,
        weights
    )