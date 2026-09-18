def normalize_score(score):

    total = (

        score["clarity"]

        +

        score["relevance"]

        +

        score["completeness"]

        +

        score["consistency"]

    )

    normalized = (

        total / 40

    ) * 100

    return round(
        normalized,
        2
    )