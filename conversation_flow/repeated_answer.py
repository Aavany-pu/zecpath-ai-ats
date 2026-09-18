def is_repeated(previous_answer, current_answer):

    previous_answer = previous_answer.strip().lower()

    current_answer = current_answer.strip().lower()

    if previous_answer == current_answer:

        return True

    return False