def explain_score(

    semantic_object,

    normalized_score

):

    explanation = {

        "intent":

        semantic_object["intent"],

        "score":

        normalized_score,

        "status":

        "Completed"
    }

    return explanation