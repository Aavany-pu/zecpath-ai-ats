from aptitude_logic.logical_reasoning_score import calculate_logical_reasoning_score
from aptitude_logic.problem_solving_clarity import evaluate_problem_solving_clarity


def build_reasoning_model():

    reasoning_scores = calculate_logical_reasoning_score()

    clarity_scores = evaluate_problem_solving_clarity()

    results = []

    total_questions = len(reasoning_scores)

    for i in range(total_questions):

        reasoning_score = reasoning_scores[i]["Logical Reasoning Score"]

        problem_score = clarity_scores[i]["Problem Solving Score"]

        final_score = round(

            (reasoning_score * 0.60)

            +

            (problem_score * 0.40),

            2

        )

        if final_score >= 90:

            level = "Excellent"

        elif final_score >= 75:

            level = "Good"

        elif final_score >= 60:

            level = "Average"

        else:

            level = "Needs Improvement"

        results.append({

            "Question ID":
                reasoning_scores[i]["Question ID"],

            "Question":
                reasoning_scores[i]["Question"],

            "Reasoning Score":
                reasoning_score,

            "Problem Solving Score":
                problem_score,

            "Final Logical Score":
                final_score,

            "Logical Thinking":
                level

        })

    return results