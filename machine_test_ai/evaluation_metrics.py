def load_evaluation_metrics(file_path):
    metrics = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            metrics.append(line)

    return metrics


def get_evaluation_metrics(file_path):
    metrics = load_evaluation_metrics(file_path)

    if not metrics:
        return {
            "Status": "No Evaluation Metrics Found",
            "Metrics": []
        }

    return {
        "Status": "Evaluation Metrics Loaded",
        "Metrics": metrics
    }