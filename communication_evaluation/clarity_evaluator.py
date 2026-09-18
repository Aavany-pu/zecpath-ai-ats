import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_clarity():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    clarity_results = []

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

            word_count = len(words)

            unique_words = len(set(words))

            if word_count == 0:

                clarity = "Poor"

                clarity_score = 0

            elif unique_words >= word_count * 0.80:

                clarity = "Excellent"

                clarity_score = 100

            elif unique_words >= word_count * 0.60:

                clarity = "Good"

                clarity_score = 80

            elif unique_words >= word_count * 0.40:

                clarity = "Average"

                clarity_score = 60

            else:

                clarity = "Poor"

                clarity_score = 40

            clarity_results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Clarity Score": clarity_score,

                "Clarity": clarity

            })

            question_id += 1

    return clarity_results