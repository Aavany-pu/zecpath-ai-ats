from hr_scoring_engine.candidate_report import generate_candidate_report


def evaluate_cultural_fit():

    report = generate_candidate_report()

    results = []

    for item in report:

        communication = item["Communication"]

        confidence = item["Confidence"]

        consistency = item["Consistency"]

        average = round(

            (communication + confidence + consistency) / 3,

            2

        )

        if average >= 90:

            fit = "Excellent"

        elif average >= 75:

            fit = "Good"

        elif average >= 60:

            fit = "Average"

        else:

            fit = "Low"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Communication Score": communication,

            "Confidence Score": confidence,

            "Consistency Score": consistency,

            "Cultural Fit Score": average,

            "Cultural Fit": fit

        })

    return results