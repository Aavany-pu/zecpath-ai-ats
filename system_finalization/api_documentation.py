import json
import os


def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


def generate_api_documentation():

    final_report = load_json(
        "data/screening_reports/final_report.json"
    )

    test_report = load_json(
        "data/screening_reports/test_report.json"
    )

    api_documentation = {

        "API Name": "AI Screening API",

        "Input": {

            "Resume": "data/resumes/",

            "Interview Transcript":
            "data/transcripts/interview_transcript.txt"

        },

        "Processing": {

            "Final Report": final_report,

            "Testing Report": test_report

        },

        "Output": final_report

    }

    return api_documentation