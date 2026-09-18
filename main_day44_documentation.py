from documentation.architecture_document import (
    generate_architecture_document
)
from documentation.api_specification import (
    generate_api_specification
)
from documentation.scoring_documentation import (
    generate_scoring_documentation
)
from documentation.data_format_documentation import (
    generate_data_format_documentation
)
from documentation.integration_guide import (
    generate_integration_guide
)
from documentation.troubleshooting import (
    generate_troubleshooting_documentation
)
from documentation.developer_handbook import (
    generate_developer_handbook
)


API_FILE = "data/documentation/api_endpoints.txt"


print("=" * 90)
print("DAY 44 - DOCUMENTATION & API SPECIFICATION")
print("=" * 90)


# ------------------------------------------------------------------
# STEP 1 - ARCHITECTURE
# ------------------------------------------------------------------

print("\n[STEP 1] ARCHITECTURE DOCUMENTATION")
print("-" * 90)

components = [
    "Candidate Data",
    "ATS Evaluation",
    "Screening Evaluation",
    "HR Interview",
    "Follow-Up Logic",
    "Communication Evaluation",
    "Unified Scoring",
    "Ethics & Compliance"
]

architecture = generate_architecture_document(
    components
)

print(f"{'Title':<30}: {architecture['Title']}")
print(f"{'Purpose':<30}: {architecture['Purpose']}")

print("\nArchitecture Components:")

for index, component in enumerate(
    architecture["Components"],
    start=1
):
    print(f"{index}. {component}")


# ------------------------------------------------------------------
# STEP 2 - API SPECIFICATION
# ------------------------------------------------------------------

print("\n[STEP 2] API SPECIFICATION")
print("-" * 90)

api_specification = generate_api_specification(
    API_FILE
)

for key, value in api_specification.items():
    if key != "Endpoints":
        print(f"{key:<30}: {value}")

print("\nAPI Endpoints:")

for index, endpoint in enumerate(
    api_specification["Endpoints"],
    start=1
):
    print(f"{index}. {endpoint}")


# ------------------------------------------------------------------
# STEP 3 - SCORING LOGIC
# ------------------------------------------------------------------

print("\n[STEP 3] SCORING LOGIC DOCUMENTATION")
print("-" * 90)

scoring_modules = [
    "ATS Scoring",
    "Screening Scoring",
    "HR Interview Scoring",
    "Communication Evaluation",
    "Unified Candidate Scoring"
]

scoring_document = generate_scoring_documentation(
    scoring_modules
)

for key, value in scoring_document.items():
    if key != "Scoring Modules":
        print(f"{key:<30}: {value}")

print("\nScoring Modules:")

for index, module in enumerate(
    scoring_document["Scoring Modules"],
    start=1
):
    print(f"{index}. {module}")


# ------------------------------------------------------------------
# STEP 4 - DATA FORMATS
# ------------------------------------------------------------------

print("\n[STEP 4] DATA FORMAT DOCUMENTATION")
print("-" * 90)

data_formats = [
    "Candidate Profile Data",
    "Resume / CV Data",
    "Interview Transcript Data",
    "Screening Report Data",
    "HR Interview Score Data",
    "Communication Evaluation Data",
    "Unified Candidate Score Data",
    "Ethics & Compliance Report Data"
]

data_format_document = generate_data_format_documentation(
    data_formats
)

for key, value in data_format_document.items():
    if key != "Data Formats":
        print(f"{key:<30}: {value}")

print("\nData Formats:")

for index, data_format in enumerate(
    data_format_document["Data Formats"],
    start=1
):
    print(f"{index}. {data_format}")


# ------------------------------------------------------------------
# STEP 5 - INTEGRATION GUIDE
# ------------------------------------------------------------------

print("\n[STEP 5] DEVELOPER INTEGRATION GUIDE")
print("-" * 90)

integration_steps = [
    "Prepare the HR AI project environment.",
    "Provide the required candidate and interview data.",
    "Run the ATS and screening evaluation stages.",
    "Start the HR interview processing stage.",
    "Process interview responses and follow-up logic.",
    "Run communication evaluation.",
    "Generate the unified candidate score.",
    "Run ethics and compliance checks.",
    "Retrieve the final candidate evaluation results."
]

integration_guide = generate_integration_guide(
    integration_steps
)

print(f"{'Title':<30}: {integration_guide['Title']}")
print(f"{'Purpose':<30}: {integration_guide['Purpose']}")

print("\nIntegration Steps:")

for index, step in enumerate(
    integration_guide["Integration Steps"],
    start=1
):
    print(f"{index}. {step}")


# ------------------------------------------------------------------
# STEP 6 - TROUBLESHOOTING
# ------------------------------------------------------------------

print("\n[STEP 6] TROUBLESHOOTING DOCUMENTATION")
print("-" * 90)

troubleshooting_issues = [
    {
        "Issue": "Module Import Error",
        "Check": "Verify the module name, file name, and project path."
    },
    {
        "Issue": "Input File Not Found",
        "Check": "Verify that the required input file exists at the expected path."
    },
    {
        "Issue": "Invalid Data Format",
        "Check": "Verify that the input structure matches the expected data format."
    },
    {
        "Issue": "Missing Evaluation Result",
        "Check": "Verify that the previous processing stage completed successfully."
    },
    {
        "Issue": "Unexpected Scoring Result",
        "Check": "Review the scoring-stage outputs and configuration used by the system."
    }
]

troubleshooting_document = (
    generate_troubleshooting_documentation(
        troubleshooting_issues
    )
)

print(f"{'Title':<30}: {troubleshooting_document['Title']}")
print(f"{'Purpose':<30}: {troubleshooting_document['Purpose']}")

print("\nTroubleshooting Issues:")

for index, issue in enumerate(
    troubleshooting_document["Troubleshooting Issues"],
    start=1
):
    print(f"{index}. {issue['Issue']}")
    print(f"   Check: {issue['Check']}")


# ------------------------------------------------------------------
# STEP 7 - DEVELOPER HANDBOOK
# ------------------------------------------------------------------

print("\n[STEP 7] DEVELOPER HANDBOOK")
print("-" * 90)

handbook_sections = [
    "System Architecture",
    "API Specification",
    "Scoring Logic",
    "Data Formats",
    "Developer Integration",
    "Troubleshooting",
    "System Maintenance"
]

developer_handbook = generate_developer_handbook(
    handbook_sections
)

print(f"{'Title':<30}: {developer_handbook['Title']}")
print(f"{'Purpose':<30}: {developer_handbook['Purpose']}")

print("\nHandbook Sections:")

for index, section in enumerate(
    developer_handbook["Sections"],
    start=1
):
    print(f"{index}. {section}")


# ------------------------------------------------------------------
# FINAL
# ------------------------------------------------------------------

print("\n" + "=" * 90)

print("=" * 90)


print("\n" + "=" * 90)