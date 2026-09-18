from hr_scoring_engine.candidate_report import generate_candidate_report


def compare_ai_manual_scores():

    report = generate_candidate_report()

    results = []

    for item in report:

        ai_score = item["Final HR Score"]

        communication = item["Communication"]

        confidence = item["Confidence"]

        consistency = item["Consistency"]

        manual_score = round(
            (communication + confidence + consistency) / 3,
            2
        )

        difference = round(
            abs(ai_score - manual_score),
            2
        )

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "AI Score": ai_score,

            "Manual Score": manual_score,

            "Difference": difference

        })

    return results