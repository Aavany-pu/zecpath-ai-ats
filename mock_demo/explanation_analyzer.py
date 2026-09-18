def analyze_explanation(explanation_data):
    if explanation_data is None:
        return {
            "Status": "No Explanation Data Available",
            "Weak Areas": []
        }

    if not isinstance(explanation_data, dict):
        return {
            "Status": "Invalid Explanation Data",
            "Weak Areas": []
        }

    weak_areas = []

    for section, content in explanation_data.items():
        if content is None:
            weak_areas.append({
                "Section": str(section),
                "Issue": "Explanation is missing"
            })

        elif isinstance(content, str) and not content.strip():
            weak_areas.append({
                "Section": str(section),
                "Issue": "Explanation is empty"
            })

    return {
        "Status": (
            "Weak Explanation Areas Identified"
            if weak_areas
            else "No Missing Explanation Areas Detected"
        ),
        "Weak Areas": weak_areas
    }