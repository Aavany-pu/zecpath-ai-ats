from pathlib import Path

from final_documentation.codebase_compiler import compile_codebase
from final_documentation.documentation_compiler import compile_documentation
from final_documentation.report_compiler import compile_reports
from final_documentation.roadmap_compiler import compile_ai_roadmap
from final_documentation.submission_package import create_submission_package
from final_documentation.final_documentation_validator import (
    validate_final_documentation
)
from portfolio.internship_portfolio import generate_internship_portfolio


PROJECT_ROOT = Path(__file__).resolve().parent


print("=" * 90)
print(" - FINAL DOCUMENTATION SUBMISSION")
print("=" * 90)


print()
print("1. CODEBASE COMPILATION")
print("-" * 90)

codebase_result = compile_codebase(PROJECT_ROOT)

print(f"{'Status':<30}: {codebase_result['Status']}")
print(f"{'Python Files':<30}: {len(codebase_result.get('Files', []))}")


print()
print("2. DOCUMENTATION COMPILATION")
print("-" * 90)

documentation_result = compile_documentation(PROJECT_ROOT)

print(f"{'Status':<30}: {documentation_result['Status']}")
print(
    f"{'Documentation Files':<30}: "
    f"{len(documentation_result.get('Files', []))}"
)


print()
print("3. REPORT COMPILATION")
print("-" * 90)

report_result = compile_reports(PROJECT_ROOT)

print(f"{'Status':<30}: {report_result['Status']}")
print(f"{'Report Files':<30}: {len(report_result.get('Files', []))}")


print()
print("4. AI ROADMAP COMPILATION")
print("-" * 90)

roadmap_result = compile_ai_roadmap(PROJECT_ROOT)

print(f"{'Status':<30}: {roadmap_result['Status']}")
print(f"{'Roadmap Files':<30}: {len(roadmap_result.get('Files', []))}")


print()
print("5. INTERNSHIP PORTFOLIO")
print("-" * 90)

portfolio_result = generate_internship_portfolio(PROJECT_ROOT)

print(f"{'Status':<30}: {portfolio_result['Status']}")


print()
print("6. SUBMISSION PACKAGE")
print("-" * 90)

submission_result = create_submission_package(PROJECT_ROOT)

print(f"{'Status':<30}: {submission_result['Status']}")

package = submission_result.get("Submission Package", {})

for category, files in package.items():
    print(f"{category:<30}: {len(files)} files")


print()
print("7. FINAL DOCUMENTATION VALIDATION")
print("-" * 90)

validation_result = validate_final_documentation(PROJECT_ROOT)

print(f"{'Status':<30}: {validation_result['Status']}")
print(
    f"{'Required Items':<30}: "
    f"{validation_result['Required Items']}"
)
print(
    f"{'Existing Items':<30}: "
    f"{len(validation_result['Existing Items'])}"
)
print(
    f"{'Missing Items':<30}: "
    f"{len(validation_result['Missing Items'])}"
)


print()
print("=" * 90)

all_passed = (
    codebase_result["Status"] == "Codebase Compilation Completed"
    and documentation_result["Status"] == "Documentation Compilation Completed"
    and report_result["Status"] == "Report Compilation Completed"
    and roadmap_result["Status"] == "AI Roadmap Compilation Completed"
    and portfolio_result["Status"] == "Internship Portfolio Generated"
    and submission_result["Status"] == "Submission Package Compiled"
    and validation_result["Status"] == "Documentation Validation Passed"
)

if all_passed:
    print("VALIDATION STATUS             : PASSED")
    print("STATUS                 : COMPLETED")
else:
    print("VALIDATION STATUS             : FAILED")
    print("STATUS                 : REQUIRES REVIEW")

print("=" * 90)