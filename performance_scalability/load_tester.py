import time


def run_load_test(processing_function, requests):
    if not requests:
        return {
            "Status": "No Requests Available",
            "Total Requests": 0,
            "Successful Requests": 0,
            "Failed Requests": 0,
            "Total Time": 0,
            "Average Response Time": 0
        }

    start_time = time.perf_counter()

    successful_requests = 0
    failed_requests = 0

    for request in requests:
        try:
            processing_function(request)
            successful_requests += 1
        except Exception:
            failed_requests += 1

    end_time = time.perf_counter()

    total_time = end_time - start_time
    average_response_time = total_time / len(requests)

    return {
        "Status": "Load Test Completed",
        "Total Requests": len(requests),
        "Successful Requests": successful_requests,
        "Failed Requests": failed_requests,
        "Total Time": total_time,
        "Average Response Time": average_response_time
    }