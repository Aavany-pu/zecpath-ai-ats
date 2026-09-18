def detect_bugs(module_results):
    if module_results is None:
        return {
            "Status": "No Module Results Available",
            "Bugs": []
        }

    if not isinstance(module_results, dict):
        return {
            "Status": "Invalid Module Results",
            "Bugs": []
        }

    bugs = []

    for module, result in module_results.items():

        if result is None:
            bugs.append({
                "Module": str(module),
                "Issue": "Module returned no result"
            })

        elif not isinstance(result, dict):
            bugs.append({
                "Module": str(module),
                "Issue": "Module returned invalid result format"
            })

        elif "Status" not in result:
            bugs.append({
                "Module": str(module),
                "Issue": "Module result does not contain Status"
            })

    return {
        "Status": (
            "Bugs Detected"
            if bugs
            else "No Minor Bugs Detected"
        ),
        "Bugs": bugs,
        "Bug Count": len(bugs)
    }