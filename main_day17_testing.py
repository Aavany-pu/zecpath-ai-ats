from testing.ats_tester import test_resume
from testing.metrics import calculate_metrics

resume_folder = "data/resumes"

results = test_resume(
    resume_folder
)

metrics = calculate_metrics(
    results
)

print("\nATS TEST REPORT\n")

for result in results:

    print(
        result["resume"],
        "| Skills:",
        result["skills_found"],
        "| Score:",
        result["score"]
    )

print("\n")

print("METRICS")

print(metrics)