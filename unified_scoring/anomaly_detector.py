def detect_scoring_anomaly(ai_score, reference_score, tolerance):

    difference = abs(ai_score - reference_score)

    if difference <= tolerance:
        status = "Stable"

    elif ai_score > reference_score:
        status = "Possible False Positive"

    else:
        status = "Possible False Negative"

    return {
        "AI Score": ai_score,
        "Reference Score": reference_score,
        "Difference": round(difference, 2),
        "Status": status
    }