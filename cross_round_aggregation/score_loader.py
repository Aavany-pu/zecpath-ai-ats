import json


def load_ats_score(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if "final_ats_score" not in data:
        raise KeyError(
            "final_ats_score not found in ATS score file."
        )

    return data["final_ats_score"]


def load_screening_score(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    candidate_summary = data.get(
        "Candidate Summary",
        {}
    )

    if "Screening Score" not in candidate_summary:
        raise KeyError(
            "Screening Score not found in screening report."
        )

    return candidate_summary["Screening Score"]


def load_evaluation_scores(
    ats_file,
    screening_file
):
    ats_score = load_ats_score(ats_file)

    screening_score = load_screening_score(
        screening_file
    )

    return {
        "ATS": ats_score,
        "Screening": screening_score
    }


def get_evaluation_scores(
    ats_file,
    screening_file
):
    return load_evaluation_scores(
        ats_file,
        screening_file
    )