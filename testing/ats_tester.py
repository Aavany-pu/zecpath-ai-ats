import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills


def test_resume(resume_folder):

    results = []

    for file in os.listdir(resume_folder):

        if file.endswith(".pdf"):

            file_path = os.path.join(
                resume_folder,
                file
            )

            resume_text = read_pdf(
                file_path
            )

            skills = extract_skills(
                resume_text
            )

            score = len(skills) * 10

            results.append(
                {
                    "resume": file,
                    "skills_found": len(skills),
                    "score": score
                }
            )

    return results