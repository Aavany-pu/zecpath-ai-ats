def classify_intent(answer):

    answer = answer.lower()

    if any(word in answer for word in [
        "python",
        "sql",
        "django",
        "flask",
        "machine learning"
    ]):
        return "Skill"

    elif any(word in answer for word in [
        "year",
        "years",
        "experience"
    ]):
        return "Experience"

    elif any(word in answer for word in [
        "salary",
        "lpa",
        "lakhs"
    ]):
        return "Salary"

    elif any(word in answer for word in [
        "join",
        "available",
        "notice"
    ]):
        return "Availability"

    return "Unknown"