def generate_technical_evaluation_report(
    engine_result
):
    if not isinstance(engine_result, dict):
        return {
            "Status": "Invalid Evaluation Data",
            "Report": {}
        }

    report = {
        "Question Type": engine_result.get(
            "Question Type"
        ),
        "Answer Analysis": engine_result.get(
            "Answer Analysis"
        ),
        "Score Normalization": engine_result.get(
            "Score Normalization"
        ),
        "Explainable Evaluation": engine_result.get(
            "Explainable Evaluation"
        )
    }

    return {
        "Status": "Technical Evaluation Report Generated",
        "Report": report
    }