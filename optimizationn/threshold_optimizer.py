def load_threshold_configuration(file_path):
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


def optimize_scoring_thresholds(configuration, error_analysis):
    false_positives = error_analysis.get("False Positives", [])
    false_negatives = error_analysis.get("False Negatives", [])

    if false_positives and false_negatives:
        optimization_status = "Threshold Review Required"
    elif false_positives:
        optimization_status = "Review Thresholds for False Positive Reduction"
    elif false_negatives:
        optimization_status = "Review Thresholds for False Negative Reduction"
    else:
        optimization_status = "No Threshold Adjustment Evidence Available"

    return {
        "Status": "Scoring Threshold Analysis Completed",
        "Optimization Status": optimization_status,
        "Configured Thresholds": configuration
    }