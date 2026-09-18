def validate_conversation_flow(conversation_steps):
    errors = []

    if not conversation_steps:
        return {
            "Status": "No Conversation Steps Available",
            "Errors": []
        }

    for index, step in enumerate(conversation_steps):
        if step is None:
            errors.append({
                "Step": index + 1,
                "Error": "Missing Conversation Step"
            })

    if errors:
        status = "Conversation Logic Errors Detected"
    else:
        status = "Conversation Flow Validated"

    return {
        "Status": status,
        "Errors": errors
    }