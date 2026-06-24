import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills

resume_folder = "data/resumes"

print("\nATS TECHNICAL DOCUMENTATION")
print("=" * 60)

resume_count = 0
total_skills = 0

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        resume_count += 1

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

        total_skills += len(
            skills
        )

        print("\nResume :", file)

        print(
            "Skills Extracted :",
            len(skills)
        )

print("\n" + "=" * 60)

print(
    "Total Resumes Processed :",
    resume_count
)

print(
    "Total Skills Extracted :",
    total_skills
)

print(
    "Average Skills Per Resume :",
    round(
        total_skills /
        resume_count,
        2
    )
)

print("\nATS PIPELINE")

print(
    "Resume Upload -> "
    "Resume Parsing -> "
    "Skill Extraction -> "
    "ATS Scoring -> "
    "Ranking -> "
    "Shortlisting"
)

print("\nDocumentation Generated Successfully")