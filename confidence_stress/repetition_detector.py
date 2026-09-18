import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def detect_repetition():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

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

            words = [

                word.strip(".,!?").lower()

                for word in answer.split()

            ]

            repeated_words = []

            checked = set()

            for word in words:

                if word not in checked:

                    occurrences = words.count(word)

                    if occurrences > 1:

                        repeated_words.append({

                            "Word": word,

                            "Count": occurrences

                        })

                    checked.add(word)

            repetition_count = len(repeated_words)

            if repetition_count == 0:

                level = "Low"

            elif repetition_count <= 2:

                level = "Moderate"

            else:

                level = "High"

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Repeated Words": repeated_words,

                "Repetition Count": repetition_count,

                "Repetition Level": level

            })

            question_id += 1

    return results