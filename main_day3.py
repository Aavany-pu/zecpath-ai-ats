from parsers.resume_parser import read_pdf
import os

candidates = []

resume_folder = "data/resumes"

score = 100

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            file_path
        )

        candidate_name = resume_text.split("\n")[0]

        candidates.append(
            {
                "name": candidate_name,
                "score": score
            }
        )

        score -= 2

ranked = sorted(
    candidates,
    key=lambda x: x["score"],
    reverse=True
)

print("RANKED CANDIDATES")

for rank, candidate in enumerate(ranked, start=1):

    print(
        f"Rank {rank} | "
        f"{candidate['name']} | "
        f"Score {candidate['score']}"
    )