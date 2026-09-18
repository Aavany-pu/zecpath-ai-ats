from hr_scoring_engine.answer_relevance import evaluate_answer_relevance
from hr_scoring_engine.communication_loader import load_communication_scores
from hr_scoring_engine.confidence_loader import load_confidence_scores
from hr_scoring_engine.consistency_checker import check_consistency
from hr_scoring_engine.weight_configuration import get_weight_configuration


def generate_hr_scores():

    relevance = evaluate_answer_relevance()

    communication = load_communication_scores()

    confidence = load_confidence_scores()

    consistency = check_consistency()

    weights = get_weight_configuration()

    hr_scores = []

    total_questions = len(relevance)

    for i in range(total_questions):

        answer_score = relevance[i]["Answer Score"]

        communication_score = communication[i]["Communication Score"]

        confidence_score = confidence[i]["Confidence Score"]

        consistency_score = consistency[i]["Consistency Score"]

        final_score = (

            answer_score * weights["Answer Relevance"]

            +

            communication_score * weights["Communication Score"]

            +

            confidence_score * weights["Confidence Score"]

            +

            consistency_score * weights["Consistency"]

        )

        final_score = round(final_score, 2)

        if final_score >= 90:

            grade = "Excellent"

        elif final_score >= 75:

            grade = "Good"

        elif final_score >= 60:

            grade = "Average"

        else:

            grade = "Needs Improvement"

        hr_scores.append({

            "Question ID": relevance[i]["Question ID"],

            "Question": relevance[i]["Question"],

            "HR Interview Score": final_score,

            "Performance": grade

        })

    return hr_scores