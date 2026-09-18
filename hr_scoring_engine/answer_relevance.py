import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_answer_relevance():

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

            answer_length = len(answer.split())

            if answer_length == 0:

                relevance = "Poor"

                score = 20

            elif answer_length <= 5:

                relevance = "Average"

                score = 50

            elif answer_length <= 15:

                relevance = "Good"

                score = 80

            else:

                relevance = "Excellent"

                score = 100

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Answer Score": score,

                "Relevance": relevance

            })

            question_id += 1

    return results