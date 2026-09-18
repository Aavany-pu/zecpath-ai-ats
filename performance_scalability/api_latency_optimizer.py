import time


def measure_api_latency(api_function, request_data):
    start_time = time.perf_counter()

    response = api_function(request_data)

    end_time = time.perf_counter()

    latency = end_time - start_time

    return {
        "Status": "API Latency Measured",
        "Latency": latency,
        "Response": response
    }