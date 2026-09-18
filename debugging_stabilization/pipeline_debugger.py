def validate_data_pipeline(pipeline_data):
    errors = []

    if pipeline_data is None:
        errors.append("Pipeline data is missing")

    elif not isinstance(pipeline_data, dict):
        errors.append("Pipeline data must be a dictionary")

    else:
        for key, value in pipeline_data.items():
            if value is None:
                errors.append(
                    f"Missing pipeline value: {key}"
                )

    if errors:
        status = "Data Pipeline Issues Detected"
    else:
        status = "Data Pipeline Validated"

    return {
        "Status": status,
        "Errors": errors
    }