def validate_edge_cases(test_cases):
    if test_cases is None:
        return {
            "Status": "No Edge Cases Available",
            "Issues": []
        }

    if not isinstance(test_cases, list):
        return {
            "Status": "Invalid Edge Case Data",
            "Issues": ["Edge cases must be provided as a list"]
        }

    issues = []

    for index, test_case in enumerate(test_cases):
        if test_case is None:
            issues.append({
                "Case": index + 1,
                "Issue": "Empty test case"
            })

        elif not isinstance(test_case, dict):
            issues.append({
                "Case": index + 1,
                "Issue": "Invalid test case format"
            })

    return {
        "Status": (
            "Edge-Case Issues Detected"
            if issues
            else "Edge-Case Validation Passed"
        ),
        "Issues": issues,
        "Issue Count": len(issues)
    }