import json


def load_screening_score(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

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


def get_screening_score(file_path):

    return load_screening_score(
        file_path
    )