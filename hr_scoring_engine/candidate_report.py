from hr_scoring_engine.answer_relevance import evaluate_answer_relevance
from hr_scoring_engine.communication_loader import load_communication_scores
from hr_scoring_engine.confidence_loader import load_confidence_scores
from hr_scoring_engine.consistency_checker import check_consistency
from hr_scoring_engine.interview_normalizer import normalize_interview_scores


def generate_candidate_report():

    answer_scores = evaluate_answer_relevance()

    communication_scores = load_communication_scores()

    confidence_scores = load_confidence_scores()

    consistency_scores = check_consistency()

    normalized_scores = normalize_interview_scores()

    report = []

    total_questions = len(normalized_scores)

    for i in range(total_questions):

        report.append({

            "Question ID":
                normalized_scores[i]["Question ID"],

            "Question":
                normalized_scores[i]["Question"],

            "Answer Relevance":
                answer_scores[i]["Answer Score"],

            "Communication":
                communication_scores[i]["Communication Score"],

            "Confidence":
                confidence_scores[i]["Confidence Score"],

            "Consistency":
                consistency_scores[i]["Consistency Score"],

            "Final HR Score":
                normalized_scores[i]["Normalized Score"]

        })

    return report