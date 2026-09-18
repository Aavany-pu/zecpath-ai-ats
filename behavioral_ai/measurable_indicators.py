def load_measurable_indicators(file_path):
    indicators = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            name, description = line.split(":", 1)

            indicators[name.strip()] = description.strip()

    return indicators


def get_measurable_indicators(file_path):
    indicators = load_measurable_indicators(file_path)

    if not indicators:
        return {
            "Status": "No Measurable Indicators Found",
            "Indicators": {}
        }

    return {
        "Status": "Measurable Indicators Loaded",
        "Indicators": indicators
    }