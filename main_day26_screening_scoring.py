from answer_engine.intent_classifier import classify_intent

from answer_engine.answer_understanding import understand_answer

from answer_engine.semantic_formatter import create_semantic_object

from scoring_engine.question_scorer import score_question

from scoring_engine.score_normalizer import normalize_score

from scoring_engine.score_aggregator import aggregate_score

from scoring_engine.explainable_score import explain_score


with open(

    "speech_processing/transcript_output.txt",

    "r",

    encoding="utf-8"

) as file:

    transcript = file.read()


intent = classify_intent(
    transcript
)

information = understand_answer(
    transcript
)

semantic = create_semantic_object(

    intent,

    information
)

question_score = score_question(
    semantic
)

normalized = normalize_score(
    question_score
)

final_score = aggregate_score(
    [normalized]
)

explanation = explain_score(

    semantic,

    final_score
)

print()

print("=" * 60)

print("DAY 26 SCREENING SCORING ENGINE")

print("=" * 60)

print()

print(

    "Question Score :",

    question_score
)

print()

print(

    "Normalized Score :",

    normalized
)

print()

print(

    "Final Screening Score :",

    final_score
)

print()

print(

    "Explainable Output :"

)

print(

    explanation
)