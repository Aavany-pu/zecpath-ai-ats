def create_explainable_decision(
    decision,
    decision_evidence,
    confidence,
    risk_factors
):
    return {
        "Decision": decision,
        "Decision Evidence": decision_evidence,
        "Confidence": confidence,
        "Risk Factors": risk_factors,
        "Explanation Status": "Evidence-Based Explanation"
    }