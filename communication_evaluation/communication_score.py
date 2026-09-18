from communication_evaluation.fluency_analyzer import evaluate_fluency
from communication_evaluation.grammar_evaluator import evaluate_grammar
from communication_evaluation.vocabulary_analyzer import evaluate_vocabulary
from communication_evaluation.clarity_evaluator import evaluate_clarity
from communication_evaluation.filler_word_detector import detect_filler_words
from communication_evaluation.answer_structure import evaluate_answer_structure


def calculate_communication_score():

    fluency = evaluate_fluency()

    grammar = evaluate_grammar()

    vocabulary = evaluate_vocabulary()

    clarity = evaluate_clarity()

    filler = detect_filler_words()

    structure = evaluate_answer_structure()

    communication_scores = []

    total_questions = len(fluency)

    for i in range(total_questions):

        score = 0

        if fluency[i]["Fluency"] == "Excellent":
            score += 20

        elif fluency[i]["Fluency"] == "Good":
            score += 16

        elif fluency[i]["Fluency"] == "Basic":
            score += 10

        if grammar[i]["Grammar Quality"] == "Excellent":
            score += 20

        elif grammar[i]["Grammar Quality"] == "Good":
            score += 16

        elif grammar[i]["Grammar Quality"] == "Average":
            score += 10

        if vocabulary[i]["Vocabulary Level"] == "Excellent":
            score += 20

        elif vocabulary[i]["Vocabulary Level"] == "Good":
            score += 16

        elif vocabulary[i]["Vocabulary Level"] == "Average":
            score += 10

        score += clarity[i]["Clarity Score"] / 5

        score += structure[i]["Structure Score"] / 5

        score -= filler[i]["Filler Count"] * 2

        score = max(0, min(100, round(score)))

        communication_scores.append({

            "Question ID": fluency[i]["Question ID"],

            "Question": fluency[i]["Question"],

            "Communication Score": score

        })

    return communication_scores