def improve_clarity(explanation_data):
    if explanation_data is None:
        return {
            "Status": "No Explanation Data Available",
            "Improved Explanation": {}
        }

    if not isinstance(explanation_data, dict):
        return {
            "Status": "Invalid Explanation Data",
            "Improved Explanation": {}
        }

    improved_explanation = {}

    for section, content in explanation_data.items():
        section_name = str(section).strip()

        if content is None:
            improved_explanation[section_name] = (
                "Explanation needs to be added."
            )

        elif isinstance(content, str):
            cleaned_content = " ".join(content.split())

            improved_explanation[section_name] = cleaned_content

        else:
            improved_explanation[section_name] = content

    return {
        "Status": "Explanation Clarity Improved",
        "Improved Explanation": improved_explanation
    }