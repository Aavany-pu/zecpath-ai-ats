from behavior_analysis.confidence_analyzer import (
    analyze_confidence
)

from behavior_analysis.sentiment_analyzer import (
    analyze_sentiment
)

from behavior_analysis.behavior_report import (
    create_behavior_report
)

with open(

    "speech_processing/transcript_output.txt",

    "r",

    encoding="utf-8"

) as file:

    transcript = file.read()

confidence = analyze_confidence(
    transcript
)

sentiment = analyze_sentiment(
    transcript
)

report = create_behavior_report(

    confidence,

    sentiment
)

print()

print("=" * 60)

print("DAY 27 - CONFIDENCE & SENTIMENT ANALYSIS")

print("=" * 60)

print()

print(

    "Confidence Analysis"

)

print(

    confidence

)

print()

print(

    "Sentiment Analysis"

)

print(

    sentiment

)

print()

print(

    "Behavior Report"

)

print(

    report
)