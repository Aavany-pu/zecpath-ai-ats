def create_api_response(data, status="success"):
    if data is None:
        return {
            "status": "error",
            "data": {},
            "message": "No data available"
        }

    if not isinstance(data, dict):
        return {
            "status": "error",
            "data": {},
            "message": "Invalid data format"
        }

    return {
        "status": status,
        "data": data,
        "message": "Request processed successfully"
    }


def prepare_ui_data(data):
    if data is None:
        return {
            "Status": "No UI Data Available",
            "UI Data": {}
        }

    if not isinstance(data, dict):
        return {
            "Status": "Invalid UI Data",
            "UI Data": {}
        }

    ui_data = {}

    for key, value in data.items():
        ui_data[str(key).strip()] = value

    return {
        "Status": "UI Data Prepared",
        "UI Data": ui_data
    }