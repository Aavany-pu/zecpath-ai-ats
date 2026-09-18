def calculate_monitoring_metrics(
    response_times,
    correct_results,
    total_results,
    failed_requests,
    total_requests
):
    metrics = {}

    # Response time
    if response_times:
        metrics["Average Response Time"] = (
            sum(response_times) / len(response_times)
        )
    else:
        metrics["Average Response Time"] = None

    # Accuracy
    if total_results > 0:
        metrics["Accuracy"] = (
            correct_results / total_results
        ) * 100
    else:
        metrics["Accuracy"] = None

    # Failure rate
    if total_requests > 0:
        metrics["Failure Rate"] = (
            failed_requests / total_requests
        ) * 100
    else:
        metrics["Failure Rate"] = None

    return {
        "Status": "Monitoring Metrics Calculated",
        "Metrics": metrics
    }