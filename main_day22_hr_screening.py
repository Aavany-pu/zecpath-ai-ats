import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills
from parsers.experience_parser import extract_experience

from screening.question_generation
 import (
    generate_questions
)

resume_folder = "data/resumes"

for file in os.listdir(
    resume_folder
):

    if file.endswith(".pdf"):

        path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            path
        )

        skills = extract_skills(
            resume_text
        )

        experience = extract_experience(
            resume_text
        )

        questions = generate_questions(
            skills,
            experience
        )

        print("\n")
        print("=" * 60)

        print(
            "Resume :",
            file
        )

        for q in questions:

            print(
                q["category"],
                "->",
                q["question"]
            )