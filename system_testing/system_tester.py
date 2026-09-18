import json

from system_testing.intent_optimizer import optimize_intent
from system_testing.score_optimizer import optimize_score


def run_system_test(final_report):

    test_report = {}

    candidate = final_report["Candidate Summary"]

    skills = candidate.get("Skills", [])

    experience = candidate.get("Experience", "Unknown")

    score = candidate.get("Screening Score", 0)

    behavior = candidate.get("Behavior", {})

    # Read intent from extracted resume skills
    if len(skills) > 0:

        intent = optimize_intent(

            " ".join(skills)

        )

    else:

        intent = "unknown"

    score_result = optimize_score(score)

    test_report["intent"] = intent

    test_report["experience"] = experience

    test_report["optimized_score"] = score_result["optimized_score"]

    test_report["decision"] = score_result["decision"]

    test_report["behavior"] = behavior

    return test_report


def save_test_report(test_report):

    output_file = "data/screening_reports/test_report.json"

    with open(

        output_file,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            test_report,

            file,

            indent=4

        )

    return output_file