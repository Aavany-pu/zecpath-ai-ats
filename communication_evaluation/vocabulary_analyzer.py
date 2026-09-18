import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_vocabulary():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    vocabulary_results = []

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

            unique_words = len(set(words))

            total_words = len(words)

            if unique_words >= 20:

                vocabulary = "Excellent"

            elif unique_words >= 12:

                vocabulary = "Good"

            elif unique_words >= 6:

                vocabulary = "Average"

            else:

                vocabulary = "Basic"

            vocabulary_results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Total Words": total_words,

                "Unique Words": unique_words,

                "Vocabulary Level": vocabulary

            })

            question_id += 1

    return vocabulary_results