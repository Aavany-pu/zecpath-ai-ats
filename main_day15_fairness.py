import os

from parsers.resume_parser import read_pdf
from parsers.skill_extractor import extract_skills

from fairness.normalization import normalize_resume
from fairness.bias_reduction import mask_personal_information
from fairness.fair_scoring import calculate_fair_score

resume_folder = "data/resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        normalized_resume = normalize_resume(
            file_path
        )

        masked_resume = mask_personal_information(
            normalized_resume
        )

        skills = extract_skills(
            normalized_resume
        )

        score = calculate_fair_score(
            len(skills)
        )

        print("\n" + "=" * 60)

        print("RESUME :", file)

        print("SKILLS :", skills)

        print("FAIR SCORE :", score)

        print()

        print("MASKED RESUME")

        print(masked_resume[:300])

        print("=" * 60)