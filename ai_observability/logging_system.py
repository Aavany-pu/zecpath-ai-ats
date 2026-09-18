from datetime import datetime


def create_log_entry(log_type, component, message, details=None):
    log_entry = {
        "Timestamp": datetime.now().isoformat(),
        "Log Type": log_type,
        "Component": component,
        "Message": message,
        "Details": details
    }

    return log_entry


def create_observability_logs():
    logs = {
        "API Logs": create_log_entry(
            "API",
            "AI API",
            "API activity recorded"
        ),
        "Model Output Logs": create_log_entry(
            "MODEL_OUTPUT",
            "AI Model",
            "Model output recorded"
        ),
        "Error Logs": create_log_entry(
            "ERROR",
            "AI System",
            "System error recorded"
        )
    }

    return {
        "Status": "Observability Logging Structure Created",
        "Logs": logs
    }