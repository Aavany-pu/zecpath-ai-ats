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


def build_system_summary():

    summary = {}

    summary["Final Report"] = load_json(
        "data/screening_reports/final_report.json"
    )

    summary["Testing Report"] = load_json(
        "data/screening_reports/test_report.json"
    )

    summary["Interview Transcript"] = load_text(
        "data/transcripts/interview_transcript.txt"
    )

    return summary