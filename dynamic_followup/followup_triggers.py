from dynamic_followup.response_analyzer import analyze_responses


def generate_followup_triggers():

    responses = analyze_responses()

    followups = []

    for response in responses:

        response_type = response["Response Type"]

        if response_type == "Incomplete":

            followup_type = "Clarification"

            followup_question = (
                "Could you please explain your answer in more detail?"
            )

        elif response_type == "Vague":

            followup_type = "Deepening"

            followup_question = (
                "Can you provide more details about your response?"
            )

        else:

            followup_type = "Example"

            followup_question = (
                "Can you give a real example from your experience?"
            )

        followups.append({

            "Question ID": response["Question ID"],

            "Original Question": response["Question"],

            "Candidate Answer": response["Answer"],

            "Response Type": response_type,

            "Follow-up Type": followup_type,

            "Follow-up Question": followup_question

        })

    return followups