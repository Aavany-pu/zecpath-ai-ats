def load_integration_configuration(file_path):
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


def integrate_behavioral_signals(
    file_path,
    behavioral_signals,
    integrity_signals
):
    configuration = load_integration_configuration(
        file_path
    )

    return {
        "Status": "Behavioral and Integrity Signals Integrated",
        "Behavioral Signal Source": configuration.get(
            "Behavioral Signal Source",
            ""
        ),
        "Integrity Signal Source": configuration.get(
            "Integrity Signal Source",
            ""
        ),
        "Integration Mode": configuration.get(
            "Integration Mode",
            ""
        ),
        "Decision Mode": configuration.get(
            "Decision Mode",
            ""
        ),
        "Behavioral Signals": behavioral_signals,
        "Integrity Signals": integrity_signals
    }