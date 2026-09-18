def generate_architecture_summary(architecture_components):
    if not isinstance(architecture_components, list):
        return {
            "Status": "Invalid Architecture Data",
            "Components": []
        }

    return {
        "Status": "Architecture Summary Generated",
        "Components": architecture_components
    }


def generate_scoring_logic_summary(scoring_components):
    if not isinstance(scoring_components, list):
        return {
            "Status": "Invalid Scoring Data",
            "Components": []
        }

    return {
        "Status": "Scoring Logic Summary Generated",
        "Components": scoring_components
    }