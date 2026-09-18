def create_recommendation_output(
    decision,
    confidence,
    risk_factors,
    explanation
):
    return {
        "Decision": decision,
        "Confidence": confidence,
        "Risk Factors": risk_factors,
        "Explanation": explanation,
        "Output Status": "Decision Output Structured"
    }