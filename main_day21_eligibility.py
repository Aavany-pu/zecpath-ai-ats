import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills
from parsers.experience_parser import extract_experience

from eligibility.eligibility_engine import (
    check_eligibility
)

resume_folder = "data/resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(path)

        skills = extract_skills(
            resume_text
        )

        experience = extract_experience(
            resume_text
        )

        ats_score = len(skills) * 10

        if ats_score > 100:
            ats_score = 100

        status = check_eligibility(
            ats_score,
            skills,
            experience
        )

        print("\n")
        print("=" * 50)

        print("Resume :", file)

        print("Skills :", skills)

        print(
            "Experience :",
            experience
        )

        print(
            "ATS Score :",
            ats_score
        )

        print(
            "Eligibility :",
            status
        )

        print("=" * 50)