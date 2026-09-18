def load_retention_configuration(file_path):
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


def evaluate_retention_policy(configuration):
    if not configuration:
        return {
            "Status": "Retention Configuration Not Available",
            "Configuration": {}
        }

    return {
        "Status": "Data Retention Policy Loaded",
        "Configuration": configuration
    }