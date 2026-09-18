from confidence_stress.contradiction_detector import detect_contradictions


def check_consistency():

    contradictions = detect_contradictions()

    results = []

    for item in contradictions:

        if item["Status"] == "No Contradiction":

            consistency_score = 100

            consistency = "Consistent"

        else:

            consistency_score = 50

            consistency = "Inconsistent"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Consistency Score": consistency_score,

            "Consistency": consistency

        })

    return results