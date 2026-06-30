def check_eligibility(ats_score, skills, experience):

    mandatory_skills = [
        "Python",
        "SQL"
    ]

    matched_skills = 0

    for skill in mandatory_skills:

        if skill in skills:
            matched_skills += 1

    if (
        ats_score >= 40
        and matched_skills >= 2
    ):
        return "Eligible"

    elif ats_score >= 20:
        return "Review"

    else:
        return "Rejected"