def create_action_plan(improvements):
    action_items = []

    if not improvements:
        return {
            "Status": "No Improvement Actions Available",
            "Action Plan": action_items
        }

    for number, improvement in enumerate(improvements, start=1):
        action_items.append({
            "Action ID": number,
            "Category": improvement.get("Category"),
            "Issue": improvement.get("Issue"),
            "Action": "Review and resolve identified issue"
        })

    return {
        "Status": "Improvement Action Plan Created",
        "Action Plan": action_items
    }