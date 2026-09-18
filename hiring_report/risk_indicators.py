def extract_risk_indicators(evaluation_report):
    risk_indicators = []

    for section, content in evaluation_report.items():

        if not isinstance(content, dict):
            continue

        section_risks = content.get(
            "Risk Indicators",
            []
        )

        section_flags = content.get(
            "Behavioral Flags",
            []
        )

        if isinstance(section_risks, list):
            risk_indicators.extend(section_risks)

        if isinstance(section_flags, list):
            risk_indicators.extend(section_flags)

    return {
        "Status": "Risk Indicators Extracted",
        "Risk Indicators": risk_indicators
    }