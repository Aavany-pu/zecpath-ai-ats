from communication_evaluation.fluency_analyzer import evaluate_fluency
from communication_evaluation.grammar_evaluator import evaluate_grammar
from communication_evaluation.vocabulary_analyzer import evaluate_vocabulary
from communication_evaluation.clarity_evaluator import evaluate_clarity
from communication_evaluation.filler_word_detector import detect_filler_words
from communication_evaluation.answer_structure import evaluate_answer_structure
from communication_evaluation.communication_score import calculate_communication_score
from communication_evaluation.score_normalizer import normalize_scores
from communication_evaluation.scoring_model import build_scoring_model


def display_section(title, data):

    print("\n" + "=" * 80)
    print(title.center(80))
    print("=" * 80)

    if isinstance(data, list):

        for item in data:

            for key, value in item.items():

                print(f"{key:<30}: {value}")

            print("-" * 80)

    elif isinstance(data, dict):

        for key, value in data.items():

            print(f"\n{key}")

            print("-" * 80)

            if isinstance(value, list):

                for row in value:

                    for k, v in row.items():

                        print(f"{k:<30}: {v}")

                    print("-" * 80)

            else:

                print(value)


print("\n")
print("=" * 80)
print("DAY 35 - COMMUNICATION SKILL EVALUATION".center(80))
print("=" * 80)


display_section(
    "1. FLUENCY ANALYSIS",
    evaluate_fluency()
)

display_section(
    "2. GRAMMAR EVALUATION",
    evaluate_grammar()
)

display_section(
    "3. VOCABULARY ANALYSIS",
    evaluate_vocabulary()
)

display_section(
    "4. CLARITY EVALUATION",
    evaluate_clarity()
)

display_section(
    "5. FILLER WORD DETECTION",
    detect_filler_words()
)

display_section(
    "6. ANSWER STRUCTURE",
    evaluate_answer_structure()
)

display_section(
    "7. COMMUNICATION SCORE",
    calculate_communication_score()
)

display_section(
    "8. NORMALIZED SCORE",
    normalize_scores()
)

display_section(
    "9. COMMUNICATION SCORING MODEL",
    build_scoring_model()
)

print("\n")
print("=" * 80)
print("DAY 35 COMPLETED SUCCESSFULLY".center(80))
print("=" * 80)