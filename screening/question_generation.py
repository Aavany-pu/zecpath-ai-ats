def generate_questions(
    skills,
    experience
):

    questions = []

    questions.append(
        {
            "category":
            "Introduction",

            "question":
            "Please introduce yourself."
        }
    )

    questions.append(
        {
            "category":
            "Experience",

            "question":
            f"Tell me about your {experience} years of experience."
        }
    )

    for skill in skills:

        questions.append(
            {
                "category":
                "Skills",

                "question":
                f"Rate your proficiency in {skill}."
            }
        )

    questions.append(
        {
            "category":
            "Location",

            "question":
            "Are you willing to relocate?"
        }
    )

    questions.append(
        {
            "category":
            "Salary",

            "question":
            "What are your salary expectations?"
        }
    )

    return questions