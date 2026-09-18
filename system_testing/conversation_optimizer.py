def adaptive_retry_logic(issue, retry_count):

    issue = issue.lower()

    if issue == "silence":

        if retry_count == 0:

            return "retry"

        elif retry_count == 1:

            return "simplify_question"

        else:

            return "skip_question"

    elif issue == "confusion":

        return "clarify"

    elif issue == "repeat":

        return "ask_example"

    return "next"


def optimize_conversation(issue, retry_count):

    action = adaptive_retry_logic(

        issue,

        retry_count

    )

    messages = {

        "retry": "I didn't hear your response. Could you please answer again?",

        "simplify_question": "Let me ask the question in a simpler way.",

        "skip_question": "We'll skip this question and continue.",

        "clarify": "Could you explain your answer more clearly?",

        "ask_example": "Could you give an example from your experience?",

        "next": "Moving to the next question."

    }

    return {

        "action": action,

        "message": messages[action]

    }