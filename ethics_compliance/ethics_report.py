def generate_ethics_report(
    consent_result,
    fairness_result,
    bias_filter_result,
    explainability_result,
    retention_result,
    compliance_result
):
    report = {
        "Ethics Review": {
            "Consent": consent_result,
            "Fairness": fairness_result,
            "Demographic Bias": bias_filter_result,
            "Explainability": explainability_result,
            "Data Retention": retention_result
        },
        "Compliance Readiness": compliance_result
    }

    return report