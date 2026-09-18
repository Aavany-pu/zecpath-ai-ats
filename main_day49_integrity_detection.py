from integrity_detection.malpractice_signals import (
    get_malpractice_signals
)

from integrity_detection.detection_logic import (
    create_detection_logic
)

from integrity_detection.warning_system import (
    create_warning_system
)

from integrity_detection.behavioral_integration import (
    integrate_behavioral_signals
)

from integrity_detection.integrity_framework import (
    build_integrity_framework
)

from integrity_detection.integrity_report import (
    generate_integrity_report
)


SIGNAL_FILE = (
    "data/integrity_detection/malpractice_signals.txt"
)

RULE_FILE = (
    "data/integrity_detection/detection_rules.txt"
)

WARNING_FILE = (
    "data/integrity_detection/warning_configuration.txt"
)

INTEGRATION_FILE = (
    "data/integrity_detection/behavioral_integration.txt"
)


print("=" * 90)
print("DAY 49 - MALPRACTICE & INTEGRITY DETECTION")
print("=" * 90)


# STEP 1
print("\n[STEP 1] MALPRACTICE SIGNAL DEFINITIONS")
print("-" * 90)

signal_result = get_malpractice_signals(
    SIGNAL_FILE
)

print(
    f"{'Status':<35}: "
    f"{signal_result['Status']}"
)

print("\nObservable Malpractice Signals:")

for index, signal in enumerate(
    signal_result["Signals"],
    start=1
):
    print(f"{index}. {signal}")


# STEP 2
print("\n[STEP 2] MALPRACTICE DETECTION LOGIC")
print("-" * 90)

detection_result = create_detection_logic(
    RULE_FILE,
    signal_result["Signals"]
)

print(
    f"{'Status':<35}: "
    f"{detection_result['Status']}"
)

print("\nDetection Logic:")

for index, (signal, details) in enumerate(
    detection_result["Detection Logic"].items(),
    start=1
):
    print(f"\n{index}. {signal}")

    for key, value in details.items():
        print(
            f"   {key:<28}: "
            f"{value}"
        )


# STEP 3
print("\n[STEP 3] WARNING & RISK FLAGGING SYSTEM")
print("-" * 90)

warning_result = create_warning_system(
    WARNING_FILE,
    detection_result["Detection Logic"]
)

print(
    f"{'Status':<35}: "
    f"{warning_result['Status']}"
)

print("\nWarning & Risk Configuration:")

for index, (signal, details) in enumerate(
    warning_result["Warning System"].items(),
    start=1
):
    print(f"\n{index}. {signal}")

    for key, value in details.items():
        print(
            f"   {key:<28}: "
            f"{value}"
        )


# STEP 4
print("\n[STEP 4] BEHAVIORAL SIGNAL INTEGRATION")
print("-" * 90)

integration_result = integrate_behavioral_signals(
    INTEGRATION_FILE,
    ["Day 48 Behavioral Signals"],
    signal_result["Signals"]
)

for key, value in integration_result.items():
    if key not in [
        "Behavioral Signals",
        "Integrity Signals"
    ]:
        print(
            f"{key:<35}: "
            f"{value}"
        )

print(
    f"{'Behavioral Signals':<35}: "
    f"{integration_result['Behavioral Signals']}"
)

print(
    f"{'Integrity Signals':<35}: "
    f"{integration_result['Integrity Signals']}"
)


# STEP 5
print("\n[STEP 5] INTEGRITY DETECTION FRAMEWORK")
print("-" * 90)

integrity_framework = build_integrity_framework(
    signal_result["Signals"],
    detection_result["Detection Logic"],
    warning_result["Warning System"],
    integration_result
)

print(
    f"{'Framework Status':<35}: "
    f"{integrity_framework['Framework Status']}"
)

print(
    f"{'Malpractice Signals':<35}: "
    f"{len(integrity_framework['Malpractice Signals'])}"
)

print(
    f"{'Detection Rules':<35}: "
    f"{len(integrity_framework['Detection Logic'])}"
)

print(
    f"{'Warning Rules':<35}: "
    f"{len(integrity_framework['Warning System'])}"
)

print(
    f"{'Behavioral Integration':<35}: "
    f"Configured"
)


# STEP 6
print("\n[STEP 6] MALPRACTICE DETECTION REPORT")
print("-" * 90)

integrity_report = generate_integrity_report(
    integrity_framework
)

for key, value in integrity_report.items():
    print(
        f"{key:<35}: "
        f"{value}"
    )


# FINAL
print("\n" + "=" * 90)
print("DAY 49 INTEGRITY DETECTION PIPELINE COMPLETED")
print("=" * 90)

print("\nFINAL SYSTEM STATUS")
print("-" * 90)

print(
    f"{'Malpractice Signals':<35}: "
    f"{integrity_report['Malpractice Signals']}"
)

print(
    f"{'Detection Rules':<35}: "
    f"{integrity_report['Detection Rules']}"
)

print(
    f"{'Warning Rules':<35}: "
    f"{integrity_report['Warning Rules']}"
)

print(
    f"{'Behavioral Integration':<35}: "
    f"{integrity_report['Behavioral Integration']}"
)

print(
    f"{'Detection Status':<35}: "
    f"{integrity_report['Detection Status']}"
)

print(
    f"{'Risk Status':<35}: "
    f"{integrity_report['Risk Status']}"
)

print("\n" + "=" * 90)
print("DAILY INTEGRITY DETECTION PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 90)