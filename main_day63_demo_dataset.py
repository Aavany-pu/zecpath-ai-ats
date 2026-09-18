import os

from demo_dataset.resume_loader import load_existing_resumes
from demo_dataset.job_description_loader import (
    load_existing_job_descriptions
)
from demo_dataset.candidate_response_loader import (
    load_existing_candidate_responses
)
from demo_dataset.ats_result_loader import (
    load_existing_ats_results
)
from demo_dataset.screening_output_loader import (
    load_existing_screening_outputs
)
from demo_dataset.interview_output_loader import (
    load_existing_interview_outputs
)
from demo_dataset.pipeline_builder import (
    build_hiring_pipeline
)
from demo_dataset.simulation_runner import (
    run_end_to_end_simulation
)


print("=" * 90)
print("- DEMO DATASET FULL SYSTEM TEST")
print("=" * 90)


# ============================================================
# STEP 1 - EXISTING RESUMES
# ============================================================

print()
print("[1] EXISTING RESUME DATASET")
print("-" * 90)

resume_result = load_existing_resumes(
    "data/resumes"
)

resume_count = resume_result.get(
    "Resume Count",
    0
)

print(f"{'Status':<35}: {resume_result['Status']}")
print(f"{'Resume Count':<35}: {resume_count}")

if resume_count > 0:
    print(f"{'Test Result':<35}: PASS")
else:
    print(f"{'Test Result':<35}: FAIL")

print("-" * 90)

for resume in resume_result.get("Resumes", []):
    print(f"{'Resume':<35}: {resume['File Name']}")


# ============================================================
# STEP 2 - JOB DESCRIPTIONS
# ============================================================

print()
print("[2] JOB DESCRIPTION DATASET")
print("-" * 90)

job_result = load_existing_job_descriptions(
    "data/job_descriptions"
)

job_count = job_result.get(
    "Job Description Count",
    0
)

print(f"{'Status':<35}: {job_result['Status']}")
print(f"{'Job Description Count':<35}: {job_count}")

if job_count > 0:
    print(f"{'Test Result':<35}: PASS")
else:
    print(f"{'Test Result':<35}: FAIL")

print("-" * 90)

for job in job_result.get("Job Descriptions", []):
    print(f"{'Job Description':<35}: {job['File Name']}")


# ============================================================
# STEP 3 - CANDIDATE RESPONSES
# ============================================================

print()
print("[3] CANDIDATE RESPONSE DATASET")
print("-" * 90)

response_result = load_existing_candidate_responses(
    "data/candidate_responses"
)

response_count = response_result.get(
    "Response Count",
    0
)

print(f"{'Status':<35}: {response_result['Status']}")
print(f"{'Response Count':<35}: {response_count}")

if response_count > 0:
    print(f"{'Test Result':<35}: PASS")
else:
    print(f"{'Test Result':<35}: FAIL")

print("-" * 90)

for response in response_result.get("Responses", []):
    print(f"{'Response':<35}: {response['File Name']}")


# ============================================================
# STEP 4 - ATS RESULTS
# ============================================================

print()
print("[4] ATS RESULTS")
print("-" * 90)

ats_result = load_existing_ats_results(
    "data/ats"
)

ats_count = ats_result.get(
    "Result Count",
    0
)

print(f"{'Status':<35}: {ats_result['Status']}")
print(f"{'ATS Result Count':<35}: {ats_count}")

if ats_count > 0:
    print(f"{'Test Result':<35}: PASS")
else:
    print(f"{'Test Result':<35}: FAIL")

print("-" * 90)

for result in ats_result.get("Results", []):
    print(f"{'ATS Result':<35}: {result['File Name']}")


# ============================================================
# STEP 5 - SCREENING OUTPUTS
# ============================================================

print()
print("[5] SCREENING OUTPUTS")
print("-" * 90)

screening_result = load_existing_screening_outputs(
    "data/screening"
)

screening_count = screening_result.get(
    "Output Count",
    0
)

print(f"{'Status':<35}: {screening_result['Status']}")
print(f"{'Screening Output Count':<35}: {screening_count}")

if screening_count > 0:
    print(f"{'Test Result':<35}: PASS")
else:
    print(f"{'Test Result':<35}: FAIL")

print("-" * 90)

for output in screening_result.get("Outputs", []):
    print(f"{'Screening Output':<35}: {output['File Name']}")


# ============================================================
# STEP 6 - INTERVIEW OUTPUTS
# ============================================================

print()
print("[6] INTERVIEW OUTPUTS")
print("-" * 90)

interview_result = load_existing_interview_outputs(
    {
        "HR Interview": "data/hr",
        "Technical Interview": "data/technical_scoring"
    }
)

interview_outputs = interview_result.get(
    "Interview Outputs",
    {}
)

interview_count = 0

for interview_type, details in interview_outputs.items():

    count = details.get(
        "Output Count",
        0
    )

    interview_count += count

    print(f"{interview_type:<35}: {details['Status']}")
    print(
        f"{'Output Count':<35}: {count}"
    )

if interview_count > 0:
    interview_test = "PASS"
else:
    interview_test = "FAIL"

print(f"{'Test Result':<35}: {interview_test}")


# ============================================================
# STEP 7 - COMPLETE PIPELINE
# ============================================================

print()
print("[7] COMPLETE HIRING PIPELINE")
print("-" * 90)

pipeline_result = build_hiring_pipeline(
    resume_result,
    job_result,
    response_result,
    ats_result,
    screening_result,
    interview_result
)

pipeline = pipeline_result.get(
    "Pipeline"
)

required_sections = [
    "Resume Data",
    "Job Description Data",
    "Candidate Response Data",
    "ATS Results",
    "Screening Outputs",
    "Interview Outputs"
]

pipeline_valid = (
    pipeline is not None
    and all(
        section in pipeline
        for section in required_sections
    )
)

print(f"{'Status':<35}: {pipeline_result['Status']}")

if pipeline_valid:
    print(f"{'Pipeline Validation':<35}: PASS")
else:
    print(f"{'Pipeline Validation':<35}: FAIL")

print("-" * 90)

for section in required_sections:
    print(f"{section:<35}: Available")


# ============================================================
# STEP 8 - END-TO-END SIMULATION
# ============================================================

print()
print("[8] END-TO-END SIMULATION")
print("-" * 90)

if pipeline_valid:

    simulation_result = run_end_to_end_simulation(
        pipeline
    )

else:

    simulation_result = {
        "Status": "Simulation Not Started",
        "Completed Stages": []
    }


simulation_stages = simulation_result.get(
    "Completed Stages",
    []
)

print(
    f"{'Status':<35}: "
    f"{simulation_result['Status']}"
)

print()

for number, stage in enumerate(
    simulation_stages,
    start=1
):
    print(f"{number:<5}: {stage}")

expected_stage_count = 6

if len(simulation_stages) == expected_stage_count:
    simulation_test = "PASS"
else:
    simulation_test = "FAIL"

print()
print(f"{'Simulation Validation':<35}: {simulation_test}")


# ============================================================
# STEP 9 - REAL DATA VALIDATION
# ============================================================

print()
print("[9] REAL DATA VALIDATION")
print("-" * 90)

data_checks = {
    "Existing Resumes": resume_count > 0,
    "Job Descriptions": job_count > 0,
    "Candidate Responses": response_count > 0,
    "ATS Results": ats_count > 0,
    "Screening Outputs": screening_count > 0,
    "Interview Outputs": interview_count > 0
}

real_data_passed = 0
real_data_failed = 0

for name, passed in data_checks.items():

    if passed:
        print(f"{name:<35}: PASS")
        real_data_passed += 1
    else:
        print(f"{name:<35}: FAIL")
        real_data_failed += 1


# ============================================================
# STEP 10 - FINAL DAY 63 RESULT
# ============================================================

print()
print("=" * 90)
print("DAY 63 FINAL RESULT")
print("=" * 90)

all_tests = {
    "Resume Dataset": resume_count > 0,
    "Job Description Dataset": job_count > 0,
    "Candidate Responses": response_count > 0,
    "ATS Results": ats_count > 0,
    "Screening Outputs": screening_count > 0,
    "Interview Outputs": interview_count > 0,
    "Pipeline Construction": pipeline_valid,
    "End-to-End Simulation": simulation_test == "PASS"
}

passed = sum(
    1 for result in all_tests.values()
    if result
)

failed = len(all_tests) - passed

for name, result in all_tests.items():

    if result:
        print(f"{name:<35}: PASS")
    else:
        print(f"{name:<35}: FAIL")

print("-" * 90)

print(f"{'Total Tests':<35}: {len(all_tests)}")
print(f"{'Passed':<35}: {passed}")
print(f"{'Failed':<35}: {failed}")

print("-" * 90)

if failed == 0:
    print(
        f"{'Overall Status':<35}: "
        "COMPLETED SUCCESSFULLY"
    )
else:
    print(
        f"{'Overall Status':<35}: "
        "REVIEW REQUIRED"
    )

print("=" * 90)