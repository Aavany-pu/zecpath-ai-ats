import os
import time

from parsers.resume_parser import read_pdf

from optimization.optimized_engine import (
    extract_text,
    detect_skills,
    calculate_ats_score,
    rank_candidate
)

job_skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "AWS",
    "Power BI"
]

resume_folder = "data/resumes"

start_time = time.time()

for file in os.listdir(
    resume_folder
):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            file_path
        )

        clean_text = extract_text(
            resume_text
        )

        candidate_skills = detect_skills(
            clean_text,
            job_skills
        )

        score = calculate_ats_score(
            candidate_skills,
            job_skills
        )

        result = rank_candidate(
            score
        )

        print("\n")
        print("=" * 60)

        print(
            "Resume :",
            file
        )

        print(
            "Detected Skills :",
            candidate_skills
        )

        print(
            "ATS Score :",
            score
        )

        print(
            "Recommendation :",
            result
        )

end_time = time.time()

print("\n")
print("=" * 60)

print(
    "Execution Time :",
    round(
        end_time -
        start_time,
        4
    ),
    "seconds"
)