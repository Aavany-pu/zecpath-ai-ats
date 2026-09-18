from hr_scoring_engine.candidate_report import generate_candidate_report


def detect_candidate_type():

    report = generate_candidate_report()

    results = []

    for item in report:

        hr_score = item["Final HR Score"]

        communication = item["Communication"]

        confidence = item["Confidence"]

        if hr_score >= 90 and confidence >= 90:

            candidate_type = "Confident"

        elif confidence < 60:

            candidate_type = "Hesitant"

        elif hr_score < 60:

            candidate_type = "Inexperienced"

        elif hr_score >= 95 and communication >= 95:

            candidate_type = "Overqualified"

        else:

            candidate_type = "Average"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "HR Score": hr_score,

            "Communication Score": communication,

            "Confidence Score": confidence,

            "Candidate Type": candidate_type

        })

    return results