def compare_with_human(ai_result, human_result):

    if ai_result == human_result:
        return "MATCH"

    return "MISMATCH"