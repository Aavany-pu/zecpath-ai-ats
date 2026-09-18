import json
import os


def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


def load_text(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.read()

    return ""


def run_demo():

    final_report = load_json(
        "data/screening_reports/final_report.json"
    )

    test_report = load_json(
        "data/screening_reports/test_report.json"
    )

    transcript = load_text(
        "data/transcripts/interview_transcript.txt"
    )

    demo = {

        "Candidate Report": final_report,

        "Testing Report": test_report,

        "Interview Transcript": transcript

    }

    return demo