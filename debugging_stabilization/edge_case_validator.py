def validate_edge_case(input_data):
    if input_data is None:
        return {
            "Status": "Edge Case Detected",
            "Valid": False,
            "Issue": "Input is missing"
        }

    if isinstance(input_data, str) and not input_data.strip():
        return {
            "Status": "Edge Case Detected",
            "Valid": False,
            "Issue": "Input is empty"
        }

    if isinstance(input_data, (list, dict)) and not input_data:
        return {
            "Status": "Edge Case Detected",
            "Valid": False,
            "Issue": "Input contains no data"
        }

    return {
        "Status": "Edge Case Validation Passed",
        "Valid": True,
        "Issue": None
    }


def validate_pipeline_edge_cases(pipeline_inputs):
    results = {}

    for stage, input_data in pipeline_inputs.items():
        results[stage] = validate_edge_case(input_data)

    detected = [
        stage
        for stage, result in results.items()
        if not result["Valid"]
    ]

    if detected:
        status = "Edge Cases Detected"
    else:
        status = "No Edge Cases Detected"

    return {
        "Status": status,
        "Detected Stages": detected,
        "Results": results
    }