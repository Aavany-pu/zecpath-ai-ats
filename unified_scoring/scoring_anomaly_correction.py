def correct_scoring_anomaly(
    ai_score,
    reference_score,
    tolerance
):

    difference = abs(ai_score - reference_score)

    corrected_score = ai_score

    if difference > tolerance:

        corrected_score = reference_score

    return {
        "Original AI Score": ai_score,
        "Reference Score": reference_score,
        "Difference": round(difference, 2),
        "Corrected Score": round(corrected_score, 2)
    }