def extract_final_recommendation(evaluation_report):
    recommendation = None

    for section, content in evaluation_report.items():

        if not isinstance(content, dict):
            continue

        if "Final Recommendation" in content:
            recommendation = content["Final Recommendation"]
            break

        if "Recommendation" in content:
            recommendation = content["Recommendation"]
            break

        if "Decision" in content:
            recommendation = content["Decision"]
            break

    if recommendation is None:
        return {
            "Status": "Recommendation Not Available",
            "Final Recommendation": None
        }

    return {
        "Status": "Final Recommendation Extracted",
        "Final Recommendation": recommendation
    }