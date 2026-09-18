def create_scoring_model(
    evaluation_metrics,
    task_evaluation,
    time_scoring
):
    scoring_model = {
        "Evaluation Metrics": evaluation_metrics,
        "Task Evaluation": task_evaluation,
        "Time Based Evaluation": time_scoring,
        "Scoring Status": "Requires Evaluation Data"
    }

    return scoring_model