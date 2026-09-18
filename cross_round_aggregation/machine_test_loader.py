def load_machine_test_score(scoring_model):

    if not isinstance(scoring_model, dict):
        raise ValueError(
            "Invalid machine test scoring data."
        )

    machine_test_score = scoring_model.get(
        "Final Score"
    )

    if not isinstance(
        machine_test_score,
        (int, float)
    ):
        raise ValueError(
            "Numerical machine test score not found."
        )

    return round(
        machine_test_score,
        2
    )


def get_machine_test_score(scoring_model):

    return load_machine_test_score(
        scoring_model
    )