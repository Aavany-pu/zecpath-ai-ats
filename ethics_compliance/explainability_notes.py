def generate_explainability_notes(score_data):
    if not isinstance(score_data, dict):
        return {
            "Status": "Review Required",
            "Notes": []
        }

    notes = []

    for field, value in score_data.items():
        field_name = str(field).strip()

        if value is None:
            notes.append(
                f"{field_name}: No evaluation result was available."
            )
        else:
            notes.append(
                f"{field_name}: Evaluation result = {value}."
            )

    return {
        "Status": "Explainability Notes Generated",
        "Notes": notes
    }