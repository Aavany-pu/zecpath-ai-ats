def handle_error(error, component="Unknown Component"):
    if error is None:
        return {
            "Status": "No Error",
            "Component": component,
            "Error Type": "",
            "Message": ""
        }

    error_type = type(error).__name__
    message = str(error)

    return {
        "Status": "Error Handled",
        "Component": component,
        "Error Type": error_type,
        "Message": message
    }


def validate_input(data, component="Unknown Component"):
    if data is None:
        return {
            "Status": "Validation Failed",
            "Component": component,
            "Message": "Input data is missing"
        }

    return {
        "Status": "Input Valid",
        "Component": component,
        "Message": "Input data is available"
    }