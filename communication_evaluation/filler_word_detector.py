import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def detect_filler_words():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    filler_words = [

        "um",
        "uh",
        "like",
        "actually",
        "basically",
        "you know",
        "sort of",
        "kind of"

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

            for word in filler_words:

                occurrences = answer_lower.count(word)

                if occurrences > 0:

                    detected.append(word)

                    count += occurrences

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Filler Count": count,

                "Detected Fillers": detected

            })

            question_id += 1

    return results