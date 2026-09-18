def prioritize_improvements(
    accuracy_issues,
    ux_issues,
    performance_issues
):
    improvements = []

    issue_groups = [
        ("Accuracy", accuracy_issues),
        ("UX", ux_issues),
        ("Performance", performance_issues)
    ]

    for category, issues in issue_groups:

        if not issues:
            continue

        for issue in issues:
            improvements.append({
                "Category": category,
                "Issue": issue
            })

    if improvements:
        status = "Improvements Prioritized"
    else:
        status = "No Improvements Available"

    return {
        "Status": status,
        "Improvements": improvements
    }