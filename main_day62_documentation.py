from technical_handbook.documentation_structure import (
    get_documentation_structure
)

from technical_handbook.architecture_document import (
    create_architecture_document
)

from technical_handbook.api_document import (
    create_api_document
)

from technical_handbook.scoring_logic_document import (
    create_scoring_logic_document
)

from technical_handbook.data_models_document import (
    create_data_models_document
)

from technical_handbook.module_document import (
    create_module_document
)

from technical_handbook.workflow_document import (
    create_workflow_document,
    create_workflow_diagram
)

from technical_handbook.setup_deployment_document import (
    create_setup_deployment_document
)

from technical_handbook.developer_onboarding import (
    create_developer_onboarding_guide
)

from technical_handbook.technical_handbook import (
    create_technical_handbook
)


print("=" * 90)
print("- ZECpath AI TECHNICAL HANDBOOK")
print("=" * 90)


# STEP 1
structure_result = get_documentation_structure()


# STEP 2
architecture_result = create_architecture_document()


# STEP 3
api_result = create_api_document()


# STEP 4
scoring_result = create_scoring_logic_document()


# STEP 5
data_model_result = create_data_models_document()


# STEP 6
module_result = create_module_document()


# STEP 7
workflow_result = create_workflow_document()

workflow_diagram = create_workflow_diagram(
    workflow_result["Workflow"]
)


# STEP 8
setup_result = create_setup_deployment_document()


# STEP 9
onboarding_result = create_developer_onboarding_guide()


# STEP 10
handbook_result = create_technical_handbook(
    structure_result,
    architecture_result,
    api_result,
    scoring_result,
    data_model_result,
    module_result,
    workflow_result,
    setup_result,
    onboarding_result
)


print()
print("DOCUMENTATION VALIDATION")
print("-" * 90)

checks = {
    "Documentation Structure": structure_result,
    "System Architecture": architecture_result,
    "API Documentation": api_result,
    "Scoring Logic": scoring_result,
    "Data Models": data_model_result,
    "Module Documentation": module_result,
    "System Workflow": workflow_result,
    "Setup and Deployment": setup_result,
    "Developer Onboarding": onboarding_result,
    "Technical Handbook": handbook_result
}

passed = 0
failed = 0

for name, result in checks.items():

    if result and result.get("Status"):
        print(f"{name:<30}: PASS")
        passed += 1
    else:
        print(f"{name:<30}: FAIL")
        failed += 1


print()
print("WORKFLOW DIAGRAM")
print("-" * 90)
print(workflow_diagram)

print()
print("FINAL HANDBOOK STATUS")
print("-" * 90)

print(f"{'Passed Checks':<30}: {passed}")
print(f"{'Failed Checks':<30}: {failed}")

if failed == 0:
    print(f"{'Overall Status':<30}: COMPLETED")
else:
    print(f"{'Overall Status':<30}: REVIEW REQUIRED")

print("=" * 90)