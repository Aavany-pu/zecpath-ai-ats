from technical_scoring.answer_depth import detect_answer_depth
from technical_scoring.score_normalizer import normalize_score
from technical_scoring.explainable_scoring import (
    generate_explainable_score
)


def evaluate_technical_answer(
    question_type,
    answer,
    technical_score,
    difficulty,
    normalization_file
):
    depth_result = detect_answer_depth(answer)

    normalization_result = normalize_score(
        technical_score,
        difficulty,
        normalization_file
    )

    explainable_result = generate_explainable_score(
        question_type,
        depth_result,
        normalization_result
    )

    return {
        "Question Type": question_type,
        "Answer Analysis": depth_result,
        "Score Normalization": normalization_result,
        "Explainable Evaluation": explainable_result
    }