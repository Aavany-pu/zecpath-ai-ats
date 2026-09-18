def calculate_cross_round_score(
    ats_score,
    screening_score,
    hr_score,
    ats_weight,
    screening_weight,
    hr_weight
):

    ats_part = ats_score * ats_weight

    screening_part = screening_score * screening_weight

    hr_part = hr_score * hr_weight

    unified_score = (
        ats_part
        + screening_part
        + hr_part
    )

    return round(unified_score, 2)