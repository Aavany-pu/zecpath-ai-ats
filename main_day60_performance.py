from performance_scalability.inference_optimizer import measure_inference_time
from performance_scalability.api_latency_optimizer import measure_api_latency
from performance_scalability.resume_batch_processor import process_resume_batch
from performance_scalability.memory_cache_optimizer import (
    MemoryCache,
    optimize_memory
)
from performance_scalability.horizontal_scaling import create_scaling_strategy
from performance_scalability.load_tester import run_load_test
from performance_scalability.performance_report import (
    generate_performance_report
)


def test_inference(data):
    return {
        "Status": "Inference Completed",
        "Data": data
    }


def test_api(data):
    return {
        "Status": "API Response Completed",
        "Data": data
    }


def process_request(request):
    return {
        "Status": "Request Processed",
        "Request": request
    }


print("=" * 90)
print("DAY 60 - COMPLETE SYSTEM TEST")
print("=" * 90)


# Step 1
inference_result = measure_inference_time(
    test_inference,
    "Resume Processing"
)

print("\n[1] INFERENCE TEST")
print(f"{'Status':<30}: {inference_result['Status']}")
print(f"{'Execution Time':<30}: "
      f"{inference_result['Execution Time']:.6f} seconds")


# Step 2
latency_result = measure_api_latency(
    test_api,
    "ATS Scoring Request"
)

print("\n[2] API LATENCY TEST")
print(f"{'Status':<30}: {latency_result['Status']}")
print(f"{'API Latency':<30}: "
      f"{latency_result['Latency']:.6f} seconds")


# Step 3
resume_inputs = [
    "Resume 1",
    "Resume 2",
    "Resume 3",
    "Resume 4"
]

batch_result = process_resume_batch(
    resume_inputs,
    2
)

print("\n[3] RESUME BATCH TEST")
print(f"{'Status':<30}: {batch_result['Status']}")
print(f"{'Total Resumes':<30}: {batch_result['Total Resumes']}")
print(f"{'Batch Size':<30}: {batch_result['Batch Size']}")


# Step 4
cache = MemoryCache()

cache.store(
    "resume_batch",
    batch_result
)

cached_result = cache.retrieve("resume_batch")

memory_result = optimize_memory(cached_result)

print("\n[4] MEMORY & CACHE TEST")
print(f"{'Status':<30}: {memory_result['Status']}")
print(f"{'Cache Entries':<30}: {cache.size()}")
print(f"{'Memory Before':<30}: "
      f"{memory_result['Memory Before']} bytes")
print(f"{'Memory After':<30}: "
      f"{memory_result['Memory After']} bytes")


# Step 5
services = [
    "Resume Processing",
    "ATS Scoring",
    "Screening AI",
    "Interview AI",
    "Decision AI"
]

scaling_result = create_scaling_strategy(services)

print("\n[5] HORIZONTAL SCALING TEST")
print(f"{'Status':<30}: {scaling_result['Status']}")
print(f"{'Load Balancing':<30}: "
      f"{scaling_result['Load Balancing']}")
print(f"{'Microservice Scaling':<30}: "
      f"{scaling_result['Microservice Scaling']}")


# Step 6
requests = [
    "Request 1",
    "Request 2",
    "Request 3",
    "Request 4",
    "Request 5"
]

load_result = run_load_test(
    process_request,
    requests
)

print("\n[6] LOAD TEST")
print(f"{'Status':<30}: {load_result['Status']}")
print(f"{'Total Requests':<30}: {load_result['Total Requests']}")
print(f"{'Successful Requests':<30}: "
      f"{load_result['Successful Requests']}")
print(f"{'Failed Requests':<30}: "
      f"{load_result['Failed Requests']}")
print(f"{'Total Time':<30}: "
      f"{load_result['Total Time']:.6f} seconds")
print(f"{'Average Response Time':<30}: "
      f"{load_result['Average Response Time']:.6f} seconds")


# Step 7
performance_report = generate_performance_report(
    inference_result,
    latency_result,
    batch_result,
    memory_result,
    scaling_result,
    load_result
)

print("\n[7] FINAL PERFORMANCE REPORT")
print(f"{'Status':<30}: {performance_report['Status']}")
print(f"{'Report Sections':<30}: "
      f"{len(performance_report['Report'])}")


print("\n" + "=" * 90)
print("TEST COMPLETED")
print("=" * 90)