from ats_engine.ats_scoring import calculate_ats_score


def load_ats_score(candidate_skills, required_skills):

    result = calculate_ats_score(
        candidate_skills,
        required_skills
    )

    return result