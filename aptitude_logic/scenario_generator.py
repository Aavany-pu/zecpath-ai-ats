from aptitude_logic.reasoning_questions import extract_questions


def generate_scenarios():

    questions = extract_questions()

    scenarios = []

    for item in questions:

        scenario = (
            "Based on the interview question, explain how you would "
            "handle a real-world situation related to: "
            + item["Question"]
        )

        scenarios.append({

            "Question ID": item["Question ID"],

            "Interview Question": item["Question"],

            "Scenario": scenario

        })

    return scenarios