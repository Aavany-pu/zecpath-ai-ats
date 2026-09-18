def load_confidence_configuration(file_path):
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


def create_confidence_framework(file_path):
    configuration = load_confidence_configuration(
        file_path
    )

    return {
        "Status": "Confidence Framework Configured",
        "Confidence Source": configuration.get(
            "Confidence Source",
            ""
        ),
        "Confidence Status": configuration.get(
            "Confidence Status",
            ""
        ),
        "Confidence Output": configuration.get(
            "Confidence Output",
            ""
        )
    }