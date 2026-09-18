def compare_scores(score_results):
    if not score_results:
        return {
            "Status": "No Score Results Available",
            "Inconsistencies": []
        }

    inconsistencies = []

    reference_score = score_results[0]

    for score in score_results[1:]:
        if score != reference_score:
            inconsistencies.append({
                "Reference Score": reference_score,
                "Compared Score": score
            })

    if inconsistencies:
        status = "Scoring Inconsistencies Detected"
    else:
        status = "Scoring Results Consistent"

    return {
        "Status": status,
        "Inconsistencies": inconsistencies
    }