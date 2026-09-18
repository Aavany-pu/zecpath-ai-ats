def check_missing_answers(transcript_path):

    result = {

        "total_questions": 0,

        "answered_questions": 0,

        "missing_answers": [],

        "retry_required": False

    }

    with open(

        transcript_path,

        "r",

        encoding="utf-8"

    ) as file:

        lines = file.readlines()

    current_question = ""

    for line in lines:

        line = line.strip()

        if line.startswith("Question:"):

            result["total_questions"] += 1

            current_question = line.replace(

                "Question:",

                ""

            ).strip()

        elif line.startswith("Answer:"):

            answer = line.replace(

                "Answer:",

                ""

            ).strip()

            if answer:

                result["answered_questions"] += 1

            else:

                result["missing_answers"].append(

                    current_question

                )

    if len(result["missing_answers"]) > 0:

        result["retry_required"] = True

    return result


def retry_questions(result):

    retry_list = []

    for question in result["missing_answers"]:

        retry_list.append(

            {

                "question": question,

                "message": "No answer detected. Please answer the question again."

            }

        )

    return retry_list