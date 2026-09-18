def process_reviewer_feedback(feedback):
    if not feedback:
        return {
            "Status": "No Reviewer Feedback Available",
            "Feedback": []
        }

    valid_feedback = []

    for item in feedback:
        if not isinstance(item, dict):
            continue

        valid_feedback.append({
            "Reviewer": item.get("Reviewer"),
            "Area": item.get("Area"),
            "Feedback": item.get("Feedback")
        })

    if not valid_feedback:
        return {
            "Status": "No Valid Reviewer Feedback Available",
            "Feedback": []
        }

    return {
        "Status": "Reviewer Feedback Processed",
        "Feedback": valid_feedback
    }