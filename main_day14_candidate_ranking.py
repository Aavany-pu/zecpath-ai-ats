import os
from parsers.resume_parser import read_pdf

candidates = []

resume_folder = "data/resumes"

skills_list = [
    "python",
    "sql",
    "java",
    "machine learning",
    "power bi",
    "django",
    "flask",
    "aws",
    "networking",
    "cybersecurity"
]

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            file_path
        )

        lines = resume_text.split("\n")

        candidate_name = "Unknown"

        for line in lines:

            line = line.strip()

            if len(line) > 3:

                candidate_name = line

                break

        score = 0

        text = resume_text.lower()

        for skill in skills_list:

            if skill in text:

                score += 10

        if score >= 60:
            status = "Shortlisted"

        elif score >= 30:
            status = "Review"

        else:
            status = "Rejected"

        candidates.append(
            {
                "name": candidate_name,
                "score": score,
                "status": status,
                "resume": file
            }
        )

ranked_candidates = sorted(
    candidates,
    key=lambda x: x["score"],
    reverse=True
)

print("\nRANKED CANDIDATES\n")

for rank, candidate in enumerate(
    ranked_candidates,
    start=1
):

    print(
        f"Rank {rank} | "
        f"{candidate['name']} | "
        f"Score {candidate['score']} | "
        f"{candidate['status']}"
    )