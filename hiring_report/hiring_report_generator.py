def generate_hiring_report(
    sections,
    evaluation_report,
    strengths_weaknesses,
    risk_indicators,
    recommendation
):
    return {
        "Report Status": "Hiring Intelligence Report Generated",
        "Report Sections": sections,
        "Evaluation Insights": evaluation_report,
        "Strengths": strengths_weaknesses.get(
            "Strengths",
            []
        ),
        "Weaknesses": strengths_weaknesses.get(
            "Weaknesses",
            []
        ),
        "Risk Indicators": risk_indicators.get(
            "Risk Indicators",
            []
        ),
        "Final Recommendation": recommendation.get(
            "Final Recommendation"
        )
    }