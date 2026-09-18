import time


def measure_processing_time(process_function, *args, **kwargs):
    start_time = time.perf_counter()

    result = process_function(*args, **kwargs)

    end_time = time.perf_counter()

    processing_time = end_time - start_time

    return {
        "Status": "Processing Time Measured",
        "Processing Time": processing_time,
        "Result": result
    }


def analyze_processing_performance(processing_time):
    if processing_time < 0:
        status = "Invalid Processing Time"
    else:
        status = "Processing Performance Measured"

    return {
        "Status": status,
        "Processing Time": processing_time
    }