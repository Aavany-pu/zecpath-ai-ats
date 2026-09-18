def handle_system_error(error, stage):
    return {
        "Status": "System Error Handled",
        "Stage": stage,
        "Error Type": type(error).__name__,
        "Error Message": str(error),
        "Recovery Required": True
    }


def execute_safely(process_function, stage, *args, **kwargs):
    try:
        result = process_function(*args, **kwargs)

        return {
            "Status": "Execution Successful",
            "Stage": stage,
            "Result": result
        }

    except Exception as error:
        return handle_system_error(
            error,
            stage
        )