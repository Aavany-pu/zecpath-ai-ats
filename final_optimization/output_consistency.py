def check_output_consistency(module_results):
    if module_results is None:
        return {
            "Status": "No Output Results Available",
            "Consistent": False,
            "Issues": []
        }

    if not isinstance(module_results, dict):
        return {
            "Status": "Invalid Output Results",
            "Consistent": False,
            "Issues": ["Output results must be provided as a dictionary"]
        }

    issues = []

    for module, result in module_results.items():

        if result is None:
            issues.append({
                "Module": str(module),
                "Issue": "Output is missing"
            })

        elif not isinstance(result, dict):
            issues.append({
                "Module": str(module),
                "Issue": "Output format is inconsistent"
            })

        elif "Status" not in result:
            issues.append({
                "Module": str(module),
                "Issue": "Status field is missing"
            })

    return {
        "Status": (
            "Output Consistency Passed"
            if not issues
            else "Output Consistency Issues Detected"
        ),
        "Consistent": not issues,
        "Issues": issues
    }