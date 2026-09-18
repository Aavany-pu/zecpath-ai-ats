def generate_feature_enhancement_report(results):
    if results is None:
        return {
            "Status": "No Enhancement Results Available",
            "Report": {}
        }

    if not isinstance(results, dict):
        return {
            "Status": "Invalid Enhancement Results",
            "Report": {}
        }

    report = {}

    for component, result in results.items():
        report[str(component).strip()] = result

    return {
        "Status": "Feature Enhancement Report Generated",
        "Report": report
    }