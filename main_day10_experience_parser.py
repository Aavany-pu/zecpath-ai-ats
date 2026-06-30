import os

from parsers.resume_parser import read_pdf
from parsers.experience_parser import extract_experience


resume_folder = "data/resumes"

print("=" * 60)
print("DAY 10 - EXPERIENCE EXTRACTION")
print("=" * 60)

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(path)

        experience = extract_experience(
            resume_text
        )

        print()

        print(
            "Resume :",
            file
        )

        print(
            "Experience :",
            experience,
            "Years"
        )

        print("-" * 60)