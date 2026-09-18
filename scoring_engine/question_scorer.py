def score_question(semantic_object):

    information = semantic_object["information"]

    score = {}

    score["clarity"] = 10 if information else 0

    score["relevance"] = 10 if "skills" in information else 5

    score["completeness"] = len(
        information.keys()
    ) * 2

    score["consistency"] = 10

    return score