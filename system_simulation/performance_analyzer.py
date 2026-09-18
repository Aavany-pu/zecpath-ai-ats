import time


def analyze_system_performance(process_function, *args, **kwargs):
    start_time = time.perf_counter()

    result = process_function(*args, **kwargs)

    end_time = time.perf_counter()

    processing_time = end_time - start_time

    return {
        "Status": "System Performance Analysis Completed",
        "Processing Time": processing_time,
        "Result": result
    }