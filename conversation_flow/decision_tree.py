def decide_next_action(answer):

    answer = answer.strip().lower()

    if answer == "":
        return "SILENCE"

    if answer in [
        "i don't know",
        "don't know",
        "not sure"
    ]:
        return "CONFUSION"

    salary_keywords = [
        "lpa",
        "lakhs"
    ]

    availability_keywords = [
        "immediately",
        "30 days",
        "60 days"
    ]

    for word in salary_keywords:
        if word in answer:
            return "NORMAL"

    for word in availability_keywords:
        if word in answer:
            return "NORMAL"

    if len(answer.split()) < 3:
        return "SHORT"

    return "NORMAL"