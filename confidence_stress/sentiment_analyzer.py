import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def analyze_sentiment():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    positive_words = [

        "confident",
        "successful",
        "improved",
        "achieved",
        "completed",
        "learned",
        "developed",
        "excellent",
        "happy",
        "positive"

    ]

    negative_words = [

        "difficult",
        "failed",
        "problem",
        "weak",
        "confused",
        "stress",
        "unable",
        "bad",
        "negative",
        "worried"

    ]

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

            words = [

                word.strip(".,!?").lower()

                for word in answer.split()

            ]

            positive_count = 0

            negative_count = 0

            for word in words:

                if word in positive_words:

                    positive_count += 1

                elif word in negative_words:

                    negative_count += 1

            if positive_count > negative_count:

                sentiment = "Positive"

            elif negative_count > positive_count:

                sentiment = "Negative"

            else:

                sentiment = "Neutral"

            sentiment_score = positive_count - negative_count

            results.append({

                "Question ID": question_id,

                "Question": question,

                "Answer": answer,

                "Positive Words": positive_count,

                "Negative Words": negative_count,

                "Sentiment Score": sentiment_score,

                "Sentiment": sentiment

            })

            question_id += 1

    return results