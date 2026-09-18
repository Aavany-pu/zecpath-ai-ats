from ethics_compliance.consent_checker import check_consent_requirements
from ethics_compliance.fairness_reviewer import review_fairness
from ethics_compliance.demographic_bias_filter import (
    remove_demographic_signals
)
from ethics_compliance.explainability_notes import (
    generate_explainability_notes
)
from ethics_compliance.data_retention import review_data_retention
from ethics_compliance.compliance_checker import check_compliance
from ethics_compliance.ethics_report import generate_ethics_report


CONSENT_FILE = "data/compliance/consent_requirements.txt"
RETENTION_FILE = "data/compliance/data_retention.txt"


print("=" * 90)
print("DAY 43 - ETHICS & COMPLIANCE REVIEW")
print("=" * 90)


# ------------------------------------------------------------------
# STEP 1 - CONSENT REQUIREMENTS
# ------------------------------------------------------------------

print("\n[STEP 1] CONSENT REQUIREMENTS")
print("-" * 90)

consent_result = check_consent_requirements(
    CONSENT_FILE
)

for key, value in consent_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 2 - FAIRNESS REVIEW
# ------------------------------------------------------------------

print("\n[STEP 2] FAIRNESS REVIEW")
print("-" * 90)

score_data = {
    "ATS Score": None,
    "Screening Score": None,
    "HR Interview Score": None,
    "Unified Score": None
}

fairness_result = review_fairness(
    score_data
)

for key, value in fairness_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 3 - DEMOGRAPHIC BIAS FILTER
# ------------------------------------------------------------------

print("\n[STEP 3] DEMOGRAPHIC BIAS FILTER")
print("-" * 90)

filtered_result = remove_demographic_signals(
    score_data
)

for key, value in filtered_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 4 - EXPLAINABILITY NOTES
# ------------------------------------------------------------------

print("\n[STEP 4] EXPLAINABILITY NOTES")
print("-" * 90)

explainability_result = generate_explainability_notes(
    filtered_result["Filtered Data"]
)

for key, value in explainability_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 5 - DATA RETENTION
# ------------------------------------------------------------------

print("\n[STEP 5] DATA RETENTION REVIEW")
print("-" * 90)

retention_result = review_data_retention(
    RETENTION_FILE
)

for key, value in retention_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 6 - COMPLIANCE CHECK
# ------------------------------------------------------------------

print("\n[STEP 6] COMPLIANCE CHECK")
print("-" * 90)

compliance_result = check_compliance(
    consent_result,
    fairness_result,
    filtered_result,
    explainability_result,
    retention_result
)

for key, value in compliance_result.items():
    print(f"{key:<30}: {value}")


# ------------------------------------------------------------------
# STEP 7 - FINAL ETHICS REPORT
# ------------------------------------------------------------------

print("\n[STEP 7] FINAL ETHICS REPORT")
print("-" * 90)

ethics_report = generate_ethics_report(
    consent_result,
    fairness_result,
    filtered_result,
    explainability_result,
    retention_result,
    compliance_result
)

print("Report Status                 : Generated")

print("\nReport Sections:")

for section in ethics_report["Ethics Review"]:
    print(f"- {section}")

print("\nCompliance Readiness:")

for key, value in compliance_result.items():
    if key != "Compliance Checks":
        print(f"{key:<30}: {value}")

print("\nCompliance Checks:")

for check_name, status in compliance_result[
    "Compliance Checks"
].items():

    result_text = "PASS" if status else "REVIEW"

    print(
        f"{check_name:<30}: {result_text}"
    )


print("\n" + "=" * 90)
print(" ETHICS & COMPLIANCE REVIEW COMPLETED")
print("=" * 90)