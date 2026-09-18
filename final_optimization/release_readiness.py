def check_release_readiness(final_validation):
    if final_validation is None:
        return {
            "Status": "Not Release Ready",
            "Reason": "Final validation result is missing"
        }

    if not isinstance(final_validation, dict):
        return {
            "Status": "Not Release Ready",
            "Reason": "Invalid final validation result"
        }

    if final_validation.get("Status") != "Final System Validation Passed":
        return {
            "Status": "Not Release Ready",
            "Reason": "Final system validation did not pass"
        }

    if final_validation.get("Failed Components"):
        return {
            "Status": "Not Release Ready",
            "Reason": "Failed components are present"
        }

    return {
        "Status": "Release Ready",
        "Reason": "All final validation checks passed"
    }