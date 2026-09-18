def build_screening_report(

    semantic_object,

    screening_score,

    behavior_report

):

    report = {

        "candidate_intent":
        semantic_object["intent"],

        "candidate_information":
        semantic_object["information"],

        "screening_score":
        screening_score,

        "behavior_analysis":
        behavior_report

    }

    return report