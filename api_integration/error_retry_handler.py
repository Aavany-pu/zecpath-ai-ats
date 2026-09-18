def handle_api_error(error, retry_count=0, max_retries=3):
    if error is None:
        return {
            "Status": "No API Error",
            "Retry Required": False,
            "Retry Count": retry_count
        }

    if retry_count < max_retries:
        return {
            "Status": "API Error Detected",
            "Retry Required": True,
            "Retry Count": retry_count + 1,
            "Message": str(error)
        }

    return {
        "Status": "Maximum Retry Limit Reached",
        "Retry Required": False,
        "Retry Count": retry_count,
        "Message": str(error)
    }