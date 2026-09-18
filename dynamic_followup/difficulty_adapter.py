from dynamic_followup.followup_triggers import generate_followup_triggers


def adapt_question_difficulty():

    followups = generate_followup_triggers()

    adaptive_questions = []

    for item in followups:

        followup_type = item["Follow-up Type"]

        if followup_type == "Clarification":

            difficulty = "Easy"

            next_question = (
                "Can you explain your answer in a simple way?"
            )

        elif followup_type == "Deepening":

            difficulty = "Medium"

            next_question = (
                "Can you explain your answer with more details?"
            )

        else:

            difficulty = "Hard"

            next_question = (
                "Can you describe a real project or situation where you applied this?"
            )

        adaptive_questions.append({

            "Question ID": item["Question ID"],

            "Difficulty Level": difficulty,

            "Original Question": item["Original Question"],

            "Candidate Answer": item["Candidate Answer"],

            "Adaptive Question": next_question

        })

    return adaptive_questions