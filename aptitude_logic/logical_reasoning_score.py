from aptitude_logic.ideal_answer_mapper import map_ideal_answers


def calculate_logical_reasoning_score():

    answers = map_ideal_answers()

    results = []

    for item in answers:

        structure = item["Ideal Answer Structure"]

        if structure == "Excellent":

            score = 100

        elif structure == "Good":

            score = 80

        elif structure == "Average":

            score = 60

        else:

            score = 40

        if score >= 90:

            level = "Excellent"

        elif score >= 75:

            level = "Good"

        elif score >= 60:

            level = "Average"

        else:

            level = "Needs Improvement"

        results.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Logical Reasoning Score": score,

            "Reasoning Level": level

        })

    return results