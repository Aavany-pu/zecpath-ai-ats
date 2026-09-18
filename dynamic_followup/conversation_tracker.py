from dynamic_followup.difficulty_adapter import adapt_question_difficulty


def track_conversation():

    adaptive_questions = adapt_question_difficulty()

    conversation_state = []

    asked_questions = set()

    for item in adaptive_questions:

        question = item["Original Question"]

        if question in asked_questions:

            status = "Repeated"

        else:

            status = "New"

            asked_questions.add(question)

        conversation_state.append({

            "Question ID": item["Question ID"],

            "Question": question,

            "Difficulty Level": item["Difficulty Level"],

            "Conversation Status": status,

            "Adaptive Question": item["Adaptive Question"]

        })

    return conversation_state