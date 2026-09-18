import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def extract_questions():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    questions = []

    question_id = 1

    for line in transcript:

        line = line.strip()

        if line.startswith("Question:"):

            question = line.replace(
                "Question:",
                ""
            ).strip()

            questions.append({

                "Question ID": question_id,

                "Question": question

            })

            question_id += 1

    return questions