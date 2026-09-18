import time


def measure_inference_time(inference_function, input_data):
    start_time = time.perf_counter()

    result = inference_function(input_data)

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    return {
        "Status": "Inference Time Measured",
        "Execution Time": execution_time,
        "Result": result
    }