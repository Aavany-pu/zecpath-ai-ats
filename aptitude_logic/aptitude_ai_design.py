from aptitude_logic.reasoning_questions import extract_questions
from aptitude_logic.scenario_generator import generate_scenarios
from aptitude_logic.ideal_answer_mapper import map_ideal_answers
from aptitude_logic.logical_reasoning_score import calculate_logical_reasoning_score
from aptitude_logic.problem_solving_clarity import evaluate_problem_solving_clarity


def build_aptitude_ai_design():

    questions = extract_questions()

    scenarios = generate_scenarios()

    ideal_answers = map_ideal_answers()

    reasoning_scores = calculate_logical_reasoning_score()

    clarity = evaluate_problem_solving_clarity()

    aptitude_results = []

    total_questions = len(questions)

    for i in range(total_questions):

        aptitude_results.append({

            "Question ID":
                questions[i]["Question ID"],

            "Question":
                questions[i]["Question"],

            "Scenario":
                scenarios[i]["Scenario"],

            "Ideal Structure":
                ideal_answers[i]["Ideal Answer Structure"],

            "Reasoning Score":
                reasoning_scores[i]["Logical Reasoning Score"],

            "Reasoning Level":
                reasoning_scores[i]["Reasoning Level"],

            "Problem Solving":
                clarity[i]["Problem Solving Clarity"],

            "Problem Solving Score":
                clarity[i]["Problem Solving Score"]

        })

    return aptitude_results