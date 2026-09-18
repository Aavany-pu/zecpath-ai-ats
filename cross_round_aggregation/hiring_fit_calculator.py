def calculate_hiring_fit(aggregated_score):

    if not isinstance(
        aggregated_score,
        (int, float)
    ):
        raise ValueError(
            "Aggregated score must be numeric."
        )

    if aggregated_score < 0:
        raise ValueError(
            "Aggregated score cannot be negative."
        )

    if aggregated_score > 100:
        raise ValueError(
            "Aggregated score cannot exceed 100."
        )

    hiring_fit = round(
        aggregated_score,
        2
    )

    return hiring_fit


def get_hiring_fit(aggregated_score):

    return calculate_hiring_fit(
        aggregated_score
    )