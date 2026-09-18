def analyze_performance(results):
    issues = []

    if not results:
        return {
            "Status": "No Performance Data Available",
            "Performance Issues": issues
        }

    if not isinstance(results, dict):
        return {
            "Status": "Invalid Performance Data",
            "Performance Issues": issues
        }

    for component, details in results.items():

        if not isinstance(details, dict):
            continue

        status = details.get("Status")

        if status and status.lower() not in {
            "normal",
            "stable",
            "passed",
            "healthy"
        }:
            issues.append({
                "Component": component,
                "Status": status,
                "Details": details
            })

    if issues:
        status = "Performance Issues Identified"
    else:
        status = "No Performance Issues Identified"

    return {
        "Status": status,
        "Performance Issues": issues
    }