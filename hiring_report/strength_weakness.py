def extract_strengths_and_weaknesses(evaluation_report):
    strengths = []
    weaknesses = []

    for section, content in evaluation_report.items():

        if not isinstance(content, dict):
            continue

        section_strengths = content.get(
            "Strengths",
            []
        )

        section_weaknesses = content.get(
            "Weaknesses",
            []
        )

        if isinstance(section_strengths, list):
            strengths.extend(section_strengths)

        if isinstance(section_weaknesses, list):
            weaknesses.extend(section_weaknesses)

    return {
        "Status": "Strengths and Weaknesses Extracted",
        "Strengths": strengths,
        "Weaknesses": weaknesses
    }