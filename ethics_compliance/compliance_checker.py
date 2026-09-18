def check_compliance(
    consent_result,
    fairness_result,
    bias_filter_result,
    explainability_result,
    retention_result
):
    checks = {}

    checks["Consent"] = (
        consent_result.get("Status") == "Ready for Review"
    )

    checks["Fairness"] = (
        fairness_result.get("Status") == "Fairness Check Passed"
    )

    checks["Demographic Bias"] = (
        bias_filter_result.get("Status")
        == "Demographic Signals Removed"
    )

    checks["Explainability"] = (
        explainability_result.get("Status")
        == "Explainability Notes Generated"
    )

    checks["Data Retention"] = (
        retention_result.get("Status")
        == "Retention Policy Available"
    )

    passed_checks = sum(checks.values())
    total_checks = len(checks)

    if passed_checks == total_checks:
        status = "Compliance Ready"
    else:
        status = "Review Required"

    return {
        "Overall Status": status,
        "Passed Checks": passed_checks,
        "Total Checks": total_checks,
        "Compliance Checks": checks
    }