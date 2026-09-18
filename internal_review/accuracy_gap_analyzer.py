def identify_accuracy_gaps(expected_results, actual_results):
    gaps = []

    if expected_results is None or actual_results is None:
        return {
            "Status": "Accuracy Comparison Requires Results",
            "Accuracy Gaps": gaps
        }

    if not isinstance(expected_results, dict):
        return {
            "Status": "Invalid Expected Results",
            "Accuracy Gaps": gaps
        }

    if not isinstance(actual_results, dict):
        return {
            "Status": "Invalid Actual Results",
            "Accuracy Gaps": gaps
        }

    all_keys = set(expected_results) | set(actual_results)

    for key in all_keys:
        expected_value = expected_results.get(key)
        actual_value = actual_results.get(key)

        if expected_value != actual_value:
            gaps.append({
                "Field": key,
                "Expected": expected_value,
                "Actual": actual_value
            })

    if gaps:
        status = "Accuracy Gaps Detected"
    else:
        status = "No Accuracy Gaps Detected"

    return {
        "Status": status,
        "Accuracy Gaps": gaps
    }