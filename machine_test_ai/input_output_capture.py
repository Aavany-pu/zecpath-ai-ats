def load_capture_configuration(file_path):
    configuration = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, description = line.split(":", 1)

            configuration[key.strip()] = description.strip()

    return configuration


def create_capture_framework(file_path):
    configuration = load_capture_configuration(
        file_path
    )

    if not configuration:
        return {
            "Status": "No Capture Configuration Found",
            "Capture Framework": {}
        }

    return {
        "Status": "Input/Output Capture Framework Created",
        "Capture Framework": configuration
    }