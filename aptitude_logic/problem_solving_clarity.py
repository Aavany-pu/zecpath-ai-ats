import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def evaluate_problem_solving_clarity():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    results = []

    question = ""

    question_id = 1

    problem_solving_keywords = [

        "analyze",
        "identify",
        "solution",
        "implement",
        "improve",
        "resolve",
        "approach",
        "evaluate",
        "test",
        "optimize"

    ]

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

            answer_lower = answer.lower()

            keyword_count = 0

            for keyword in problem_solving_keywords:

                if keyword in answer_lower:

                    keyword_count += 1

            if keyword_count >= 5:

                clarity = "Excellent"

                score = 100

            elif keyword_count >= 3:

                clarity = "Good"

                score = 80

            elif keyword_count >= 1:

                clarity = "Average"

                score = 60

            else:

                clarity = "Needs Improvement"

                score = 40

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Problem Solving Score": score,

                "Problem Solving Clarity": clarity

            })

            question_id += 1

    return results