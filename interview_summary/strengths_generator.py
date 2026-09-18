from hr_scoring_engine.candidate_report import generate_candidate_report


def generate_strengths():

    report = generate_candidate_report()

    strengths = []

    for item in report:

        score = item["Final HR Score"]

        if score >= 90:

            strength = "Excellent overall interview performance"

        elif score >= 75:

            strength = "Good communication and reasoning"

        elif score >= 60:

            strength = "Average performance"

        else:

            strength = "Needs improvement"

        strengths.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Strength": strength

        })

    return strengths