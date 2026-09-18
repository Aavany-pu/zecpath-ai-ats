import json


def load_ats_score(file_path):

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    if "final_ats_score" not in data:
        raise KeyError(
            "final_ats_score not found in ATS score file."
        )

    return data["final_ats_score"]


def get_ats_score(file_path):

    return load_ats_score(file_path)