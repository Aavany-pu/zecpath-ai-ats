from hr_scoring_engine.candidate_report import generate_candidate_report


def generate_weaknesses():

    report = generate_candidate_report()

    weaknesses = []

    for item in report:

        score = item["Final HR Score"]

        if score >= 90:

            weakness = "No major weaknesses identified"

        elif score >= 75:

            weakness = "Can improve answer depth"

        elif score >= 60:

            weakness = "Needs better communication and reasoning"

        else:

            weakness = "Requires significant interview preparation"

        weaknesses.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Weakness": weakness

        })

    return weaknesses