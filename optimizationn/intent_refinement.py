def load_intent_configuration(file_path):
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


def refine_intent_detection(configuration, intent_results):
    if not intent_results:
        refinement_status = "Intent Evaluation Results Not Available"
    else:
        refinement_status = "Intent Detection Refinement Available"

    return {
        "Status": "Intent Detection Analysis Completed",
        "Refinement Status": refinement_status,
        "Configuration": configuration,
        "Intent Results": intent_results
    }