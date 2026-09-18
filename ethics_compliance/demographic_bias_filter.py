def remove_demographic_signals(candidate_data):
    if not isinstance(candidate_data, dict):
        return {
            "Status": "Review Required",
            "Filtered Data": {},
            "Removed Fields": []
        }

    filtered_data = {}
    removed_fields = []

    demographic_terms = {
        "gender",
        "sex",
        "age",
        "race",
        "ethnicity",
        "religion",
        "nationality",
        "marital_status",
        "marital status",
        "disability",
        "photo",
        "date_of_birth",
        "date of birth"
    }

    for field, value in candidate_data.items():

        normalized_field = str(field).strip().lower()

        if normalized_field in demographic_terms:
            removed_fields.append(field)
        else:
            filtered_data[field] = value

    return {
        "Status": "Demographic Signals Removed",
        "Filtered Data": filtered_data,
        "Removed Fields": removed_fields
    }