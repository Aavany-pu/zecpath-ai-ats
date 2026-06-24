import os

from ats_api.parser import parse_resume
from ats_api.scoring import calculate_score
from ats_api.shortlist import shortlist

resume_folder = "data/resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        parsed = parse_resume(
            file_path
        )

        score = calculate_score(
            parsed["skills"]
        )

        status = shortlist(
            score
        )

        print("\n")
        print("=" * 60)

        print(
            "Candidate :",
            parsed["candidate_name"]
        )

        print(
            "Skills :",
            parsed["skills"]
        )

        print(
            "ATS Score :",
            score
        )

        print(
            "Status :",
            status
        )

        print("=" * 60)