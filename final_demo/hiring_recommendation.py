def extract_hiring_recommendation(score_data):
    if not isinstance(score_data, dict):
        return {
            "Status": "Invalid Score Data",
            "Recommendation": None
        }

    recommendation_fields = [
        "Hiring Recommendation",
        "Final Recommendation",
        "Recommendation"
    ]

    for field in recommendation_fields:
        if field in score_data:
            return {
                "Status": "Recommendation Found",
                "Recommendation": score_data[field]
            }

    return {
        "Status": "Recommendation Not Available",
        "Recommendation": None
    }