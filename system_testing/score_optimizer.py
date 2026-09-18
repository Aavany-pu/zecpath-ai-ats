DECISION_THRESHOLDS = {

    "pass": 65,

    "review": 45

}


def get_decision(score):

    if score >= DECISION_THRESHOLDS["pass"]:

        return "PASS"

    elif score >= DECISION_THRESHOLDS["review"]:

        return "REVIEW"

    else:

        return "REJECT"


def optimize_score(score):

    if score < 0:

        score = 0

    elif score > 100:

        score = 100

    decision = get_decision(score)

    return {

        "optimized_score": score,

        "decision": decision

    }