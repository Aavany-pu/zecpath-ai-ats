def validate_usability(input_data):
    issues = []

    if input_data is None:
        issues.append("Input data is missing")

    elif not isinstance(input_data, dict):
        issues.append("Input data format is invalid")

    else:
        for key, value in input_data.items():

            if value is None:
                issues.append(
                    f"Missing value for: {key}"
                )

            elif isinstance(value, str) and not value.strip():
                issues.append(
                    f"Empty value for: {key}"
                )

    if issues:
        status = "Usability Issues Detected"
    else:
        status = "Usability Validation Passed"

    return {
        "Status": status,
        "Issues": issues
    }