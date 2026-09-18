def generate_performance_report(
    inference_result,
    latency_result,
    batch_result,
    memory_result,
    scaling_result,
    load_result
):
    report = {
        "Inference Performance": inference_result,
        "API Latency": latency_result,
        "Resume Batching": batch_result,
        "Memory and Cache": memory_result,
        "Horizontal Scaling": scaling_result,
        "Load Testing": load_result
    }

    return {
        "Status": "Performance Benchmark Report Generated",
        "Report": report
    }