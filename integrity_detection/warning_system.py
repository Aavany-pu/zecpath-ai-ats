def load_warning_configuration(file_path):
    configuration = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            configuration[key.strip()] = value.strip()

    return configuration


def create_warning_system(file_path, detection_logic):
    configuration = load_warning_configuration(file_path)

    warning_system = {}

    for signal in detection_logic:
        warning_system[signal] = {
            "Signal": signal,
            "Real-Time Alert": configuration.get(
                "Real-Time Alert",
                ""
            ),
            "Interview Risk Tag": configuration.get(
                "Interview Risk Tag",
                ""
            ),
            "Alert Status": configuration.get(
                "Alert Status",
                ""
            ),
            "Risk Status": configuration.get(
                "Risk Status",
                ""
            )
        }

    if not warning_system:
        return {
            "Status": "No Warning Rules Found",
            "Warning System": {}
        }

    return {
        "Status": "Warning and Risk Flagging System Created",
        "Warning System": warning_system
    }