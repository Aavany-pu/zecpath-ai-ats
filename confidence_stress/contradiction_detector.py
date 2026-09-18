import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def detect_contradictions():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    contradiction_pairs = [

        ("yes", "no"),
        ("always", "never"),
        ("confident", "not confident"),
        ("experienced", "no experience"),
        ("can", "cannot")

    ]

    results = []

    question = ""

    question_id = 1

    for line in transcript:

        line = line.strip()

        if line.startswith("Question:"):

            question = line.replace(
                "Question:",
                ""
            ).strip()

        elif line.startswith("Answer:"):

            answer = line.replace(
                "Answer:",
                ""
            ).strip()

            answer_lower = answer.lower()

            contradictions = []

            for first, second in contradiction_pairs:

                if first in answer_lower and second in answer_lower:

                    contradictions.append(
                        f"{first} <-> {second}"
                    )

            if len(contradictions) == 0:

                status = "No Contradiction"

            else:

                status = "Contradiction Found"

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Contradictions": contradictions,

                "Status": status

            })

            question_id += 1

    return results