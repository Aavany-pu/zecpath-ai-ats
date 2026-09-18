def retry_message(retry_count):

    if retry_count == 1:

        return (
            "I didn't catch that. Could you please repeat your answer?"
        )

    elif retry_count == 2:

        return (
            "Let's move to the next question."
        )

    return None