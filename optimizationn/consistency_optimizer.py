def load_consistency_configuration(file_path):
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


def analyze_round_consistency(configuration, round_results):
    if not round_results:
        consistency_status = "Round Evaluation Results Not Available"
    elif len(round_results) < 2:
        consistency_status = "Additional Round Results Required"
    else:
        consistency_status = "Multi-Round Consistency Analysis Available"

    return {
        "Status": "Round Consistency Analysis Completed",
        "Consistency Status": consistency_status,
        "Configuration": configuration,
        "Round Results": round_results
    }