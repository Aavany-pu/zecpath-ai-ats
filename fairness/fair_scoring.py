def calculate_fair_score(skill_count):

    score = skill_count * 10

    if score > 100:

        score = 100

    return score