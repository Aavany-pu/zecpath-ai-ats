def determine_experience_level(years_of_experience):
    if years_of_experience < 0:
        return {
            "Status": "Invalid Experience",
            "Experience Level": None,
            "Difficulty": None
        }

    if years_of_experience <= 2:
        level = "0-2 Years"
        difficulty = "Basic"

    elif years_of_experience <= 5:
        level = "3-5 Years"
        difficulty = "Intermediate"

    else:
        level = "5+ Years"
        difficulty = "Advanced/System Design"

    return {
        "Status": "Experience Level Determined",
        "Experience Level": level,
        "Difficulty": difficulty
    }