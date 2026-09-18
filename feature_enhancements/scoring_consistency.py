def validate_score_consistency(score_results):
    if not score_results:
        return {
            "Status": "No Score Results Available",
            "Consistent": False,
            "Issues": []
        }

    issues = []

    if not isinstance(score_results, list):
        return {
            "Status": "Invalid Score Results",
            "Consistent": False,
            "Issues": ["Score results must be provided as a list"]
        }

    for index, result in enumerate(score_results):
        if result is None:
            issues.append({
                "Position": index + 1,
                "Issue": "Missing score result"
            })

    if issues:
        return {
            "Status": "Score Consistency Issues Detected",
            "Consistent": False,
            "Issues": issues
        }

    return {
        "Status": "Score Results Consistent",
        "Consistent": True,
        "Issues": []
    }