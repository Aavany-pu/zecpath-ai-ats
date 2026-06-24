SKILL_DICTIONARY = [
    "Python",
    "SQL",
    "Machine Learning",
    "Java",
    "Spring Boot",
    "MySQL",
    "Power BI",
    "Excel"
]

def extract_skills(text):
    extracted_skills = []

    for skill in SKILL_DICTIONARY:
        if skill.lower() in text.lower():
            extracted_skills.append(skill)

    return extracted_skills


def skill_confidence(skills):
    confidence_scores = {}

    for skill in skills:
        confidence_scores[skill] = 95

    return confidence_scores