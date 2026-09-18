from confidence_stress.hesitation_detector import detect_hesitation
from confidence_stress.uncertainty_detector import detect_uncertainty
from confidence_stress.repetition_detector import detect_repetition
from confidence_stress.sentiment_analyzer import analyze_sentiment
from confidence_stress.contradiction_detector import detect_contradictions
from confidence_stress.stress_indicator import measure_stress
from confidence_stress.confidence_score import calculate_confidence_score
from confidence_stress.behavioral_logic import build_behavioral_logic


def display_section(title, data):

    print("\n")
    print("=" * 90)
    print(title.center(90))
    print("=" * 90)

    if isinstance(data, list):

        for item in data:

            for key, value in item.items():

                print(f"{key:<30}: {value}")

            print("-" * 90)

    elif isinstance(data, dict):

        for key, value in data.items():

            print(f"\n{key}")

            print("-" * 90)

            print(value)


print("\n")
print("=" * 90)
print("DAY 36 - CONFIDENCE & STRESS INDICATORS".center(90))
print("=" * 90)

display_section(
    "1. HESITATION DETECTOR",
    detect_hesitation()
)

display_section(
    "2. UNCERTAINTY DETECTOR",
    detect_uncertainty()
)

display_section(
    "3. REPETITION DETECTOR",
    detect_repetition()
)

display_section(
    "4. SENTIMENT ANALYZER",
    analyze_sentiment()
)

display_section(
    "5. CONTRADICTION DETECTOR",
    detect_contradictions()
)

display_section(
    "6. STRESS INDICATOR",
    measure_stress()
)

display_section(
    "7. CONFIDENCE SCORE",
    calculate_confidence_score()
)

display_section(
    "8. BEHAVIORAL SIGNAL LOGIC",
    build_behavioral_logic()
)

print("\n")
print("=" * 90)
print("DAY 36 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)