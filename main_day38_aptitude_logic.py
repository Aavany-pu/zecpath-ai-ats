from aptitude_logic.reasoning_questions import extract_questions
from aptitude_logic.scenario_generator import generate_scenarios
from aptitude_logic.ideal_answer_mapper import map_ideal_answers
from aptitude_logic.logical_reasoning_score import calculate_logical_reasoning_score
from aptitude_logic.problem_solving_clarity import evaluate_problem_solving_clarity
from aptitude_logic.aptitude_ai_design import build_aptitude_ai_design
from aptitude_logic.reasoning_model import build_reasoning_model
from aptitude_logic.scenario_framework import build_scenario_framework


def display_section(title, data):

    print("\n")
    print("=" * 90)
    print(title.center(90))
    print("=" * 90)

    if isinstance(data, list):

        for item in data:

            for key, value in item.items():

                print(f"{key:<30}: {value}")

            print("-" * 90)

    elif isinstance(data, dict):

        for key, value in data.items():

            print(f"{key:<30}: {value}")


print("\n")
print("=" * 90)
print("DAY 38 - APTITUDE LOGIC DESIGN".center(90))
print("=" * 90)

display_section(
    "1. REASONING QUESTIONS",
    extract_questions()
)

display_section(
    "2. SITUATIONAL JUDGMENT SCENARIOS",
    generate_scenarios()
)

display_section(
    "3. IDEAL ANSWER MAPPER",
    map_ideal_answers()
)

display_section(
    "4. LOGICAL REASONING SCORING",
    calculate_logical_reasoning_score()
)

display_section(
    "5. PROBLEM SOLVING CLARITY",
    evaluate_problem_solving_clarity()
)

display_section(
    "6. APTITUDE AI DESIGN",
    build_aptitude_ai_design()
)

display_section(
    "7. LOGICAL REASONING MODEL",
    build_reasoning_model()
)

display_section(
    "8. SCENARIO EVALUATION FRAMEWORK",
    build_scenario_framework()
)

print("\n")
print("=" * 90)
print("DAY 38 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)