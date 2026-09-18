def generate_explainable_score(
    question_type,
    depth_result,
    normalization_result
):
    explanation = []

    if depth_result.get("Answer Depth"):
        explanation.append(
            "Answer depth: "
            + str(depth_result["Answer Depth"])
        )

    if depth_result.get("Word Count") is not None:
        explanation.append(
            "Answer word count: "
            + str(depth_result["Word Count"])
        )

    if normalization_result.get("Normalized Score") is not None:
        explanation.append(
            "Normalized technical score: "
            + str(normalization_result["Normalized Score"])
        )

    return {
        "Status": "Explainable Score Generated",
        "Question Type": question_type,
        "Answer Depth": depth_result.get(
            "Answer Depth"
        ),
        "Original Score": normalization_result.get(
            "Original Score"
        ),
        "Normalized Score": normalization_result.get(
            "Normalized Score"
        ),
        "Explanation": explanation
    }