def review_fairness(score_data):
    review_points = []

    if not isinstance(score_data, dict):
        return {
            "Status": "Review Required",
            "Fairness Points": ["Invalid scoring data format."]
        }

    demographic_fields = []

    for field in score_data.keys():
        field_name = str(field).lower()

        if any(term in field_name for term in [
            "gender",
            "sex",
            "age",
            "race",
            "ethnicity",
            "religion",
            "nationality",
            "marital",
            "disability"
        ]):
            demographic_fields.append(field)

    if demographic_fields:
        review_points.append(
            "Demographic fields detected and should not influence scoring."
        )
        status = "Review Required"
    else:
        review_points.append(
            "No demographic scoring signals detected in the provided data."
        )
        status = "Fairness Check Passed"

    return {
        "Status": status,
        "Demographic Fields Detected": demographic_fields,
        "Fairness Points": review_points
    }