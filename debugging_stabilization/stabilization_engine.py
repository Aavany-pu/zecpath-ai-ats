def evaluate_stabilization(debugging_report):
    issues = []

    sections = [
        "Scoring Debugging",
        "Conversation Debugging",
        "Pipeline Debugging",
        "Error Handling",
        "API Stability",
        "Edge Case Validation"
    ]

    for section in sections:
        result = debugging_report.get(section)

        if not isinstance(result, dict):
            issues.append({
                "Section": section,
                "Issue": "Missing debugging result"
            })
            continue

        status = result.get("Status", "")

        if "Detected" in status or "Invalid" in status:
            issues.append({
                "Section": section,
                "Issue": status
            })

    if issues:
        stabilization_status = "Stabilization Issues Detected"
    else:
        stabilization_status = "System Stabilization Passed"

    return {
        "Status": stabilization_status,
        "Issues": issues,
        "Debugging Report": debugging_report
    }