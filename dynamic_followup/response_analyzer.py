import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def analyze_responses():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    responses = []

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

            if word_count == 0:

                response_type = "Incomplete"

            elif word_count <= 5:

                response_type = "Vague"

            else:

                response_type = "Complete"

            responses.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Word Count": word_count,

                "Response Type": response_type

            })

            question_id += 1

    return responses