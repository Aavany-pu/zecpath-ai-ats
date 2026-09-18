from answer_engine.intent_classifier import classify_intent
from answer_engine.answer_understanding import understand_answer
from answer_engine.semantic_formatter import create_semantic_object

from scoring_engine.question_scorer import score_question
from scoring_engine.score_normalizer import normalize_score
from scoring_engine.score_aggregator import aggregate_score

from behavior_analysis.confidence_analyzer import analyze_confidence
from behavior_analysis.sentiment_analyzer import analyze_sentiment
from behavior_analysis.behavior_report import create_behavior_report

from report_generator.report_builder import build_screening_report
from report_generator.recruiter_report import recruiter_report
from report_generator.sample_report import generate_sample_report


with open(
    "speech_processing/transcript_output.txt",
    "r",
    encoding="utf-8"
) as file:

    transcript = file.read()


intent = classify_intent(transcript)

information = understand_answer(transcript)

semantic_object = create_semantic_object(
    intent,
    information
)

question_score = score_question(
    semantic_object
)

normalized_score = normalize_score(
    question_score
)

screening_score = aggregate_score(
    [normalized_score]
)

confidence = analyze_confidence(
    transcript
)

sentiment = analyze_sentiment(
    transcript
)

behavior_report = create_behavior_report(
    confidence,
    sentiment
)

report = build_screening_report(
    semantic_object,
    screening_score,
    behavior_report
)

recruiter_view = recruiter_report(
    report
)

final_report = generate_sample_report(
    recruiter_view
)
import json

with open(
    "data/screening_reports/final_report.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        final_report,
        file,
        indent=4
    )

print("Final report saved successfully.")
print(final_report)