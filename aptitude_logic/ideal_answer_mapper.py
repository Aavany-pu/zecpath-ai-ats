import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def map_ideal_answers():

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

            word_count = len(answer.split())

            if word_count >= 25:

                structure = "Excellent"

            elif word_count >= 15:

                structure = "Good"

            elif word_count >= 8:

                structure = "Average"

            else:

                structure = "Needs Improvement"

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Word Count": word_count,

                "Ideal Answer Structure": structure

            })

            question_id += 1

    return results