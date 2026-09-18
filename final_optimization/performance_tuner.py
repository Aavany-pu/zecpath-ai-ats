import time


def measure_performance(function, *args, **kwargs):
    if function is None:
        return {
            "Status": "No Function Available",
            "Execution Time": None
        }

    if not callable(function):
        return {
            "Status": "Invalid Function",
            "Execution Time": None
        }

    start_time = time.perf_counter()

    try:
        result = function(*args, **kwargs)

        end_time = time.perf_counter()

        execution_time = end_time - start_time

        return {
            "Status": "Performance Measurement Completed",
            "Execution Time": execution_time,
            "Result": result
        }

    except Exception as error:
        end_time = time.perf_counter()

        return {
            "Status": "Performance Test Failed",
            "Execution Time": end_time - start_time,
            "Error": str(error)
        }