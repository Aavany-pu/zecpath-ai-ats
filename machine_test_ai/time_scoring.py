def load_time_scoring_configuration(file_path):
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


def create_time_scoring_framework(file_path):
    configuration = load_time_scoring_configuration(
        file_path
    )

    if not configuration:
        return {
            "Status": "No Time Scoring Configuration Found",
            "Time Scoring Framework": {}
        }

    return {
        "Status": "Time-Based Scoring Framework Created",
        "Time Scoring Framework": configuration
    }