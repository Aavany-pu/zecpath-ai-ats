import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_fluency():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    fluency_results = []

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

            words = answer.split()

            sentence_length = len(words)

            if sentence_length == 0:

                fluency = "Poor"

            elif sentence_length <= 5:

                fluency = "Basic"

            elif sentence_length <= 15:

                fluency = "Good"

            else:

                fluency = "Excellent"

            fluency_results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Word Count": sentence_length,

                "Fluency": fluency

            })

            question_id += 1

    return fluency_results