import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills


def parse_resume(file_path):

    resume_text = read_pdf(
        file_path
    )

    skills = extract_skills(
        resume_text
    )

    candidate_name = "Unknown"

    lines = resume_text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 3:

            candidate_name = line

            break

    return {
        "candidate_name": candidate_name,
        "skills": skills,
        "resume_text": resume_text
    }