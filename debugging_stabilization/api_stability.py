def validate_api_output(output):
    if output is None:
        return {
            "Status": "Invalid API Output",
            "Valid": False,
            "Error": "Output is missing"
        }

    if not isinstance(output, dict):
        return {
            "Status": "Invalid API Output",
            "Valid": False,
            "Error": "Output must be a dictionary"
        }

    if "Status" not in output:
        return {
            "Status": "Invalid API Output",
            "Valid": False,
            "Error": "Status field is missing"
        }

    return {
        "Status": "API Output Validated",
        "Valid": True,
        "Output": output
    }


def stabilize_api_output(output):
    validation_result = validate_api_output(output)

    if not validation_result["Valid"]:
        return validation_result

    return {
        "Status": "API Output Stabilized",
        "Output": output
    }