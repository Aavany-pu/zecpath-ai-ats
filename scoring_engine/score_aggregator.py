def aggregate_score(scores):

    total = sum(
        scores
    )

    average = total / len(scores)

    return round(
        average,
        2
    )