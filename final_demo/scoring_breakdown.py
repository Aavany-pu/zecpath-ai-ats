def generate_scoring_breakdown(score_data):
    if not isinstance(score_data, dict):
        return {
            "Status": "Invalid Score Data",
            "Breakdown": {}
        }

    breakdown = {}

    for category, score in score_data.items():
        breakdown[category] = score

    return {
        "Status": "Scoring Breakdown Generated",
        "Breakdown": breakdown
    }