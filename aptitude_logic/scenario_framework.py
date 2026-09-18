from aptitude_logic.scenario_generator import generate_scenarios
from aptitude_logic.reasoning_model import build_reasoning_model


def build_scenario_framework():

    scenarios = generate_scenarios()

    reasoning = build_reasoning_model()

    framework = []

    total_questions = len(scenarios)

    for i in range(total_questions):

        framework.append({

            "Question ID":
                scenarios[i]["Question ID"],

            "Interview Question":
                scenarios[i]["Interview Question"],

            "Scenario":
                scenarios[i]["Scenario"],

            "Logical Reasoning Score":
                reasoning[i]["Final Logical Score"],

            "Logical Thinking":
                reasoning[i]["Logical Thinking"],

            "Evaluation":

                "Suitable"

                if reasoning[i]["Final Logical Score"] >= 75

                else

                "Needs Improvement"

        })

    return framework