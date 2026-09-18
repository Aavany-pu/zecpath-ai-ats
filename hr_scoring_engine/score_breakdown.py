from hr_scoring_engine.answer_relevance import evaluate_answer_relevance
from hr_scoring_engine.communication_loader import load_communication_scores
from hr_scoring_engine.confidence_loader import load_confidence_scores
from hr_scoring_engine.consistency_checker import check_consistency
from hr_scoring_engine.hr_score_engine import generate_hr_scores


def generate_score_breakdown():

    relevance = evaluate_answer_relevance()

    communication = load_communication_scores()

    confidence = load_confidence_scores()

    consistency = check_consistency()

    hr_scores = generate_hr_scores()

    breakdown = []

    total_questions = len(hr_scores)

    for i in range(total_questions):

        breakdown.append({

            "Question ID": hr_scores[i]["Question ID"],

            "Question": hr_scores[i]["Question"],

            "Answer Relevance": relevance[i]["Answer Score"],

            "Communication Score": communication[i]["Communication Score"],

            "Confidence Score": confidence[i]["Confidence Score"],

            "Consistency Score": consistency[i]["Consistency Score"],

            "Final HR Score": hr_scores[i]["HR Interview Score"],

            "Performance": hr_scores[i]["Performance"]

        })

    return breakdown