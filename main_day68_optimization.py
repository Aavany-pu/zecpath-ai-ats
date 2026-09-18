from final_optimization.bug_detector import detect_bugs
from final_optimization.edge_case_validator import validate_edge_cases
from final_optimization.module_validator import validate_modules
from final_optimization.output_consistency import check_output_consistency
from final_optimization.performance_tuner import measure_performance
from final_optimization.bug_fix_report import generate_bug_fix_report
from final_optimization.final_validation import validate_final_system
from final_optimization.release_readiness import check_release_readiness


print("=" * 90)
print(" - FINAL OPTIMIZATION & BUG FIXING")
print("=" * 90)


# ---------------------------------------------------------
# MODULE TEST DATA
# ---------------------------------------------------------

module_results = {
    "ATS": {"Status": "Validated"},
    "Screening": {"Status": "Validated"},
    "HR Interview": {"Status": "Validated"},
    "Technical Evaluation": {"Status": "Validated"},
    "Decision": {"Status": "Validated"}
}


# ---------------------------------------------------------
# STEP 1 - BUG DETECTION
# ---------------------------------------------------------

bug_result = detect_bugs(module_results)

print()
print("STEP 1 - BUG DETECTION")
print("-" * 90)
print(f"{'Status':<30}: {bug_result['Status']}")
print(f"{'Bug Count':<30}: {bug_result['Bug Count']}")


# ---------------------------------------------------------
# STEP 2 - EDGE CASE VALIDATION
# ---------------------------------------------------------

edge_case_result = validate_edge_cases([
    {},
    {"Status": "Valid"}
])

print()
print("STEP 2 - EDGE-CASE VALIDATION")
print("-" * 90)
print(f"{'Status':<30}: {edge_case_result['Status']}")
print(f"{'Issue Count':<30}: {edge_case_result['Issue Count']}")


# ---------------------------------------------------------
# STEP 3 - MODULE VALIDATION
# ---------------------------------------------------------

module_validation = validate_modules(
    module_results
)

print()
print("STEP 3 - MODULE VALIDATION")
print("-" * 90)
print(f"{'Status':<30}: {module_validation['Status']}")
print(
    f"{'Validated Modules':<30}: "
    f"{len(module_validation['Validated Modules'])}"
)
print(
    f"{'Failed Modules':<30}: "
    f"{len(module_validation['Failed Modules'])}"
)


# ---------------------------------------------------------
# STEP 4 - OUTPUT CONSISTENCY
# ---------------------------------------------------------

consistency_result = check_output_consistency(
    module_results
)

print()
print("STEP 4 - OUTPUT CONSISTENCY")
print("-" * 90)
print(f"{'Status':<30}: {consistency_result['Status']}")
print(f"{'Consistent':<30}: {consistency_result['Consistent']}")
print(
    f"{'Issue Count':<30}: "
    f"{len(consistency_result['Issues'])}"
)


# ---------------------------------------------------------
# STEP 5 - PERFORMANCE TUNING
# ---------------------------------------------------------

performance_result = measure_performance(
    validate_modules,
    module_results
)

print()
print("STEP 5 - PERFORMANCE TUNING")
print("-" * 90)
print(f"{'Status':<30}: {performance_result['Status']}")

if performance_result["Execution Time"] is not None:
    print(
        f"{'Execution Time':<30}: "
        f"{performance_result['Execution Time']:.6f} seconds"
    )


# ---------------------------------------------------------
# STEP 6 - BUG FIX REPORT
# ---------------------------------------------------------

bug_fix_report = generate_bug_fix_report(
    bug_result,
    edge_case_result,
    module_validation,
    consistency_result,
    performance_result
)

print()
print("STEP 6 - BUG FIX REPORT")
print("-" * 90)
print(f"{'Status':<30}: {bug_fix_report['Status']}")
print(
    f"{'Report Sections':<30}: "
    f"{len(bug_fix_report['Report'])}"
)


# ---------------------------------------------------------
# STEP 7 - FINAL SYSTEM VALIDATION
# ---------------------------------------------------------

final_validation = validate_final_system(
    bug_result,
    edge_case_result,
    module_validation,
    consistency_result,
    performance_result,
    bug_fix_report
)

print()
print("STEP 7 - FINAL SYSTEM VALIDATION")
print("-" * 90)
print(f"{'Status':<30}: {final_validation['Status']}")
print(
    f"{'Validated Components':<30}: "
    f"{final_validation['Validated Components']}"
)
print(
    f"{'Failed Components':<30}: "
    f"{len(final_validation['Failed Components'])}"
)


# ---------------------------------------------------------
# STEP 8 - RELEASE READINESS
# ---------------------------------------------------------

release_result = check_release_readiness(
    final_validation
)

print()
print("STEP 8 - RELEASE READINESS")
print("-" * 90)
print(f"{'Status':<30}: {release_result['Status']}")
print(f"{'Reason':<30}: {release_result['Reason']}")


# ---------------------------------------------------------
# FINAL TEST
# ---------------------------------------------------------

print()
print("FINAL DAY 68 VALIDATION")
print("-" * 90)

if release_result["Status"] == "Release Ready":

    print(f"{'Validation Status':<30}: PASSED")
    print(f"{'Optimization Steps':<30}: 8")
    print(f"{'Release Status':<30}: READY")

else:

    print(f"{'Validation Status':<30}: FAILED")
    print(f"{'Release Status':<30}: NOT READY")


print()
print("=" * 90)

if release_result["Status"] == "Release Ready":
    print("COMPLETED")
else:
    print(" TEST FAILED")

print("=" * 90)