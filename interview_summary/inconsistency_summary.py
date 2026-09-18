from confidence_stress.contradiction_detector import detect_contradictions


def generate_inconsistency_summary():

    contradictions = detect_contradictions()

    results = []

    for item in contradictions:

        if item["Status"] == "Contradiction Found":

            summary = "Candidate responses contain contradictions."

        else:

            summary = "No contradictions detected."

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Contradiction Status": item["Status"],

            "Summary": summary

        })

    return results