from technical_scoring.scoring_parameters import (
    get_scoring_parameters
)

from technical_scoring.question_rubric import (
    get_question_rubric
)

from technical_scoring.answer_depth import (
    detect_answer_depth
)

from technical_scoring.score_normalizer import (
    normalize_score
)

from technical_scoring.explainable_scoring import (
    generate_explainable_score
)

from technical_scoring.technical_scoring_engine import (
    evaluate_technical_answer
)

from technical_scoring.technical_evaluation_report import (
    generate_technical_evaluation_report
)


PARAMETERS_FILE = (
    "data/technical_scoring/"
    "scoring_parameters.txt"
)

RUBRIC_FILE = (
    "data/technical_scoring/"
    "question_rubrics.txt"
)

NORMALIZATION_FILE = (
    "data/technical_scoring/"
    "score_normalization.txt"
)


print("=" * 90)
print("DAY 47 - TECHNICAL SKILL SCORING MODEL")
print("=" * 90)


# ================================================================
# STEP 1 - SCORING PARAMETERS
# ================================================================

print("\n[STEP 1] TECHNICAL SCORING PARAMETERS")
print("-" * 90)

parameter_result = get_scoring_parameters(
    PARAMETERS_FILE
)

for key, value in parameter_result.items():
    if key != "Parameters":
        print(f"{key:<35}: {value}")

print("\nParameters:")

for index, parameter in enumerate(
    parameter_result["Parameters"],
    start=1
):
    print(f"{index}. {parameter}")


# ================================================================
# STEP 2 - QUESTION RUBRIC
# ================================================================

print("\n[STEP 2] QUESTION TYPE SCORING RUBRIC")
print("-" * 90)

question_type = input(
    "Enter question type: "
)

rubric_result = get_question_rubric(
    RUBRIC_FILE,
    question_type
)

for key, value in rubric_result.items():
    if key != "Parameters":
        print(f"{key:<35}: {value}")

print("\nRubric Parameters:")

for index, parameter in enumerate(
    rubric_result["Parameters"],
    start=1
):
    print(f"{index}. {parameter}")


# ================================================================
# STEP 3 - ANSWER DEPTH
# ================================================================

print("\n[STEP 3] ANSWER DEPTH DETECTION")
print("-" * 90)

answer = input(
    "Enter technical interview answer: "
)

depth_result = detect_answer_depth(
    answer
)

for key, value in depth_result.items():
    print(f"{key:<35}: {value}")


# ================================================================
# STEP 4 - SCORE NORMALIZATION
# ================================================================

print("\n[STEP 4] SCORE NORMALIZATION")
print("-" * 90)

difficulty = input(
    "Enter question difficulty: "
)

score_input = input(
    "Enter technical score: "
)

try:
    technical_score = float(
        score_input
    )

    normalization_result = normalize_score(
        technical_score,
        difficulty,
        NORMALIZATION_FILE
    )

except ValueError:

    normalization_result = {
        "Status": "Invalid Score",
        "Difficulty": difficulty,
        "Original Score": None,
        "Normalized Score": None
    }

for key, value in normalization_result.items():
    print(f"{key:<35}: {value}")


# ================================================================
# STEP 5 - EXPLAINABLE SCORING
# ================================================================

print("\n[STEP 5] EXPLAINABLE TECHNICAL SCORING")
print("-" * 90)

explainable_result = generate_explainable_score(
    question_type,
    depth_result,
    normalization_result
)

for key, value in explainable_result.items():
    if key != "Explanation":
        print(f"{key:<35}: {value}")

print("\nScoring Explanation:")

for index, explanation in enumerate(
    explainable_result["Explanation"],
    start=1
):
    print(f"{index}. {explanation}")


# ================================================================
# STEP 6 - TECHNICAL SCORING ENGINE
# ================================================================

print("\n[STEP 6] TECHNICAL SCORING ENGINE")
print("-" * 90)

engine_result = evaluate_technical_answer(
    question_type,
    answer,
    technical_score,
    difficulty,
    NORMALIZATION_FILE
)

print(
    f"{'Status':<35}: "
    "Technical Evaluation Generated"
)

print("\nQuestion Type:")
print(engine_result["Question Type"])

print("\nAnswer Analysis:")
print(engine_result["Answer Analysis"])

print("\nScore Normalization:")
print(engine_result["Score Normalization"])

print("\nExplainable Evaluation:")
print(engine_result["Explainable Evaluation"])


# ================================================================
# STEP 7 - EVALUATION REPORT
# ================================================================

print("\n[STEP 7] TECHNICAL EVALUATION REPORT")
print("-" * 90)

report_result = generate_technical_evaluation_report(
    engine_result
)

print(
    f"{'Status':<35}: "
    f"{report_result['Status']}"
)

print("\nReport:")

for section, value in report_result[
    "Report"
].items():

    print(f"\n{section}:")
    print(value)


# ================================================================
# FINAL STATUS
# ================================================================

print("\n" + "=" * 90)
print("TECHNICAL SKILL SCORING MODEL COMPLETED")
print("=" * 90)