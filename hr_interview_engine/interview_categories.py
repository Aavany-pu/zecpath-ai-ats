import json
import os


def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


def build_interview_categories():

    report = load_json(
        "data/screening_reports/final_report.json"
    )

    summary = report.get("Candidate Summary", {})

    categories = {

        "Self Introduction": {
            "Skills": summary.get("Skills", []),
            "Experience": summary.get("Experience", "")
        },

        "Career Journey": {
            "Experience": summary.get("Experience", "")
        },

        "Strengths And Weaknesses": {
            "Skills": summary.get("Skills", [])
        },

        "Teamwork And Culture Fit": {},

        "Career Goals": {},

        "Availability And Commitment": {
            "Availability": summary.get("Availability", "")
        }

    }

    return categories