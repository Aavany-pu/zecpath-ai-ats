def process_manager_feedback(feedback_data):
    if feedback_data is None:
        return {
            "Status": "No Manager Feedback Available",
            "Feedback": []
        }

    if not isinstance(feedback_data, list):
        return {
            "Status": "Invalid Manager Feedback",
            "Feedback": []
        }

    feedback = []

    for item in feedback_data:
        if item is None:
            continue

        feedback.append(item)

    return {
        "Status": "Manager Feedback Processed",
        "Feedback": feedback
    }