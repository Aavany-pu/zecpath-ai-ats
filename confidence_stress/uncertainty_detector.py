import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def detect_uncertainty():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    uncertainty_phrases = [

        "i think",
        "maybe",
        "probably",
        "not sure",
        "i guess",
        "possibly",
        "perhaps"

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

            detected = []

            count = 0

            for phrase in uncertainty_phrases:

                occurrences = answer_lower.count(phrase)

                if occurrences > 0:

                    detected.append(phrase)

                    count += occurrences

            if count == 0:

                level = "Low"

            elif count <= 2:

                level = "Moderate"

            else:

                level = "High"

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Uncertainty Count": count,

                "Detected Phrases": detected,

                "Uncertainty Level": level

            })

            question_id += 1

    return results