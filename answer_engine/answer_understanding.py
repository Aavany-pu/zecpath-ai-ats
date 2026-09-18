import re


def understand_answer(answer):

    result = {}

    answer = answer.lower()

    skills = []

    skill_keywords = [

        "python",

        "sql",

        "django",

        "flask",

        "machine learning",

        "power bi",

        "excel"

    ]

    for skill in skill_keywords:

        if skill in answer:

            skills.append(skill.title())

    result["skills"] = skills

    experience = re.search(

        r"(\d+)\s*(year|years|yr|yrs)",

        answer,

        re.IGNORECASE

    )

    if experience:

        result["experience"] = experience.group(1)

    salary = re.search(

        r"(\d+)\s*(lpa|lakhs)",

        answer,

        re.IGNORECASE

    )

    if salary:

        result["salary"] = salary.group(1)

    if "immediately" in answer:

        result["availability"] = "Immediate"

    elif "30 days" in answer:

        result["availability"] = "30 Days"

    elif "60 days" in answer:

        result["availability"] = "60 Days"

    return result