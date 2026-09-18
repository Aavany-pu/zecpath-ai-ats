def build_behavioral_framework(
    signals,
    indicators,
    mappings,
    scoring_framework
):
    framework = []

    for signal in signals:
        framework.append({
            "Signal": signal,
            "Indicator": indicators.get(signal, "Not Defined"),
            "Behavioral Insight": mappings.get(signal, "Not Defined"),
            "Scoring Framework": scoring_framework.get(
                signal,
                "Not Defined"
            )
        })

    if not framework:
        return {
            "Status": "Behavioral Framework Empty",
            "Framework": []
        }

    return {
        "Status": "Behavioral Analysis Framework Created",
        "Framework": framework
    }