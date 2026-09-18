def load_technical_score(engine_result):

    if not isinstance(engine_result, dict):
        raise ValueError(
            "Invalid technical evaluation data."
        )

    score_normalization = engine_result.get(
        "Score Normalization"
    )

    if not isinstance(score_normalization, dict):
        raise ValueError(
            "Technical score normalization data not found."
        )

    technical_score = score_normalization.get(
        "Final Score"
    )

    if not isinstance(technical_score, (int, float)):
        raise ValueError(
            "Numerical technical score not found."
        )

    return round(technical_score, 2)


def get_technical_score(engine_result):

    return load_technical_score(
        engine_result
    )