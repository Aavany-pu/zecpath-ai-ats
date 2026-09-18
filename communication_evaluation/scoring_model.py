from communication_evaluation.fluency_analyzer import evaluate_fluency
from communication_evaluation.grammar_evaluator import evaluate_grammar
from communication_evaluation.vocabulary_analyzer import evaluate_vocabulary
from communication_evaluation.clarity_evaluator import evaluate_clarity
from communication_evaluation.filler_word_detector import detect_filler_words
from communication_evaluation.answer_structure import evaluate_answer_structure
from communication_evaluation.communication_score import calculate_communication_score
from communication_evaluation.score_normalizer import normalize_scores


def build_scoring_model():

    model = {

        "Fluency Analysis": evaluate_fluency(),

        "Grammar Evaluation": evaluate_grammar(),

        "Vocabulary Analysis": evaluate_vocabulary(),

        "Clarity Evaluation": evaluate_clarity(),

        "Filler Word Detection": detect_filler_words(),

        "Answer Structure": evaluate_answer_structure(),

        "Communication Score": calculate_communication_score(),

        "Normalized Score": normalize_scores()

    }

    return model