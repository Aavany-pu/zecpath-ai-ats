def validate_final_system(
    bug_result,
    edge_case_result,
    module_validation,
    consistency_result,
    performance_result,
    bug_fix_report
):
    results = {
        "Bug Detection": bug_result,
        "Edge-Case Validation": edge_case_result,
        "Module Validation": module_validation,
        "Output Consistency": consistency_result,
        "Performance Tuning": performance_result,
        "Bug Fix Report": bug_fix_report
    }

    failed_components = []

    for component, result in results.items():

        if result is None:
            failed_components.append(component)

        elif not isinstance(result, dict):
            failed_components.append(component)

        elif not result.get("Status"):
            failed_components.append(component)

    if failed_components:
        return {
            "Status": "Final System Validation Failed",
            "Validated Components": len(results) - len(failed_components),
            "Failed Components": failed_components
        }

    return {
        "Status": "Final System Validation Passed",
        "Validated Components": len(results),
        "Failed Components": []
    }