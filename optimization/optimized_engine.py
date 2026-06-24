import re

def extract_text(text):

    text = text.lower()

    text = re.sub(
        r'[^a-zA-Z0-9\s]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()

def detect_skills(
    resume_text,
    skills_db
):

    detected = []

    for skill in skills_db:

        if skill.lower() in resume_text:

            detected.append(skill)

    return list(
        set(detected)
    )
    
def calculate_ats_score(
    candidate_skills,
    required_skills
):

    matched = len(
        set(candidate_skills)
        &
        set(required_skills)
    )

    total = len(
        required_skills
    )

    score = (
        matched / total
    ) * 100

    return round(
        score,
        2
    )
    
def rank_candidate(score):

    if score >= 80:

        return "Highly Recommended"

    elif score >= 60:

        return "Recommended"

    elif score >= 40:

        return "Average Match"

    else:

        return "Not Recommended"