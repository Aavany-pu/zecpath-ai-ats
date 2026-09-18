import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_grammar():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    grammar_results = []

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

            total_words = len(words)

            capital_letter = answer[:1].isupper()

            punctuation = answer.endswith((".", "!", "?"))

            grammar_score = 0

            if total_words > 0:
                grammar_score += 40

            if capital_letter:
                grammar_score += 30

            if punctuation:
                grammar_score += 30

            if grammar_score >= 90:

                grammar = "Excellent"

            elif grammar_score >= 70:

                grammar = "Good"

            elif grammar_score >= 40:

                grammar = "Average"

            else:

                grammar = "Poor"

            grammar_results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Grammar Score": grammar_score,

                "Grammar Quality": grammar

            })

            question_id += 1

    return grammar_results