import json
import os


def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


def generate_evaluation_report():

    final_report = load_json(
        "data/screening_reports/final_report.json"
    )

    test_report = load_json(
        "data/screening_reports/test_report.json"
    )

    evaluation = {

        "Candidate Summary": final_report.get(
            "Candidate Summary",
            {}
        ),

        "Screening Report": final_report,

        "Testing Report": test_report

    }

    return evaluation