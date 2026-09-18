import time


def measure_processing_speed(process_function, data):

    start_time = time.perf_counter()

    result = process_function(data)

    end_time = time.perf_counter()

    processing_time = end_time - start_time

    return {
        "Result": result,
        "Processing Time (seconds)": round(
            processing_time,
            6
        )
    }