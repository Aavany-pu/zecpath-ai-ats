from unified_scoring.weight_configuration import get_cross_round_weights


def adjust_weights_by_role(role):

    base_weights = get_cross_round_weights()

    role = role.lower().strip()

    weights = {}

    for key, value in base_weights.items():

        weights[key] = value

    if role == "technical":

        weights["ATS Score"] = 0.40
        weights["Screening Score"] = 0.35
        weights["HR Interview Score"] = 0.25

    elif role == "hr":

        weights["ATS Score"] = 0.25
        weights["Screening Score"] = 0.30
        weights["HR Interview Score"] = 0.45

    elif role == "management":

        weights["ATS Score"] = 0.25
        weights["Screening Score"] = 0.25
        weights["HR Interview Score"] = 0.50

    return weights