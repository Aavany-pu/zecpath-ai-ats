from parsers.resume_parser import read_pdf
import os

candidates = []

resume_folder = "data/resumes"

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

        candidate_name = lines[0]

        candidate = {
            "name": candidate_name,
            "resume_file": file
        }

        candidates.append(candidate)

print("EXTRACTED CANDIDATES")

for candidate in candidates:

    print(candidate)