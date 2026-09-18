import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_answer_structure():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    structure_results = []

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

            sentences = [

                sentence.strip()

                for sentence in answer.replace("!", ".")
                                      .replace("?", ".")
                                      .split(".")

                if sentence.strip()

            ]

            word_count = len(answer.split())

            sentence_count = len(sentences)

            if word_count == 0:

                structure = "Poor"

                score = 0

            elif sentence_count >= 3:

                structure = "Excellent"

                score = 100

            elif sentence_count == 2:

                structure = "Good"

                score = 80

            elif sentence_count == 1 and word_count >= 8:

                structure = "Average"

                score = 60

            else:

                structure = "Poor"

                score = 40

            structure_results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Sentence Count": sentence_count,

                "Word Count": word_count,

                "Structure Score": score,

                "Structure": structure

            })

            question_id += 1

    return structure_results