def validate_modules(module_results):
    if module_results is None:
        return {
            "Status": "No Module Results Available",
            "Validated Modules": [],
            "Failed Modules": []
        }

    if not isinstance(module_results, dict):
        return {
            "Status": "Invalid Module Results",
            "Validated Modules": [],
            "Failed Modules": []
        }

    validated_modules = []
    failed_modules = []

    for module, result in module_results.items():

        if result is None:
            failed_modules.append(str(module))
            continue

        if not isinstance(result, dict):
            failed_modules.append(str(module))
            continue

        if "Status" not in result:
            failed_modules.append(str(module))
            continue

        validated_modules.append(str(module))

    return {
        "Status": (
            "All Modules Validated"
            if not failed_modules
            else "Module Validation Issues Detected"
        ),
        "Validated Modules": validated_modules,
        "Failed Modules": failed_modules
    }
    