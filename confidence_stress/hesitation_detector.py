import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def detect_hesitation():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    hesitation_words = [

        "um",
        "uh",
        "erm",
        "hmm"

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

            words = answer.lower().split()

            count = sum(

                1

                for word in words

                if word.strip(".,!?") in hesitation_words

            )

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

                "Hesitation Count": count,

                "Hesitation Level": level

            })

            question_id += 1

    return results