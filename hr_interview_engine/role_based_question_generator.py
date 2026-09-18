import json
import os


def load_json(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return json.load(file)

    return {}


def generate_role_information():

    report = load_json(
        "data/screening_reports/final_report.json"
    )

    summary = report.get("Candidate Summary", {})

    skills = summary.get("Skills", [])

    experience = summary.get(
        "Experience",
        "Unknown"
    )

    if experience == "Not Available" or experience == "Unknown":

        experience_level = "Fresher"

    else:

        experience_level = "Experienced"

    technical_keywords = [

        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "AI",
        "Django",
        "React",
        "Cloud"

    ]

    role_type = "Non-Technical"

    for skill in skills:

        if skill.lower() in [

            word.lower()

            for word in technical_keywords

        ]:

            role_type = "Technical"

            break

    role_information = {

        "Experience Level": experience_level,

        "Role Type": role_type,

        "Skills": skills

    }

    return role_information