import os


def load_transcript(file_path):

    if os.path.exists(file_path):

        with open(file_path, "r", encoding="utf-8") as file:

            return file.readlines()

    return []


def build_interview_state():

    transcript = load_transcript(
        "data/transcripts/interview_transcript.txt"
    )

    interview_state = []

    question_id = 1

    current_question = ""

    current_answer = ""

    for line in transcript:

        line = line.strip()

        if line.startswith("Question:"):

            current_question = line.replace(
                "Question:",
                ""
            ).strip()

        elif line.startswith("Answer:"):

            current_answer = line.replace(
                "Answer:",
                ""
            ).strip()

            follow_up = False

            if current_answer == "":

                follow_up = True

            interview_state.append({

                "Question ID": question_id,

                "Question": current_question,

                "Candidate Response": current_answer,

                "Follow-up Eligibility": follow_up

            })

            question_id += 1

    return interview_state