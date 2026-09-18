def analyze_prediction_errors(actual_results, predicted_results):
    false_positives = []
    false_negatives = []

    for item in predicted_results:
        if item not in actual_results:
            false_positives.append(item)

    for item in actual_results:
        if item not in predicted_results:
            false_negatives.append(item)

    return {
        "Status": "Prediction Error Analysis Completed",
        "False Positives": false_positives,
        "False Negatives": false_negatives
    }