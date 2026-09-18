from machine_test_ai.test_types import get_test_types

from machine_test_ai.evaluation_metrics import (
    get_evaluation_metrics
)

from machine_test_ai.input_output_capture import (
    create_capture_framework
)

from machine_test_ai.time_scoring import (
    create_time_scoring_framework
)

from machine_test_ai.task_evaluator import (
    create_task_evaluation_framework
)

from machine_test_ai.machine_test_framework import (
    build_machine_test_framework
)

from machine_test_ai.scoring_model import (
    create_scoring_model
)

from machine_test_ai.machine_test_report import (
    generate_machine_test_report
)


TEST_TYPE_FILE = (
    "data/machine_test_ai/test_types.txt"
)

METRIC_FILE = (
    "data/machine_test_ai/evaluation_metrics.txt"
)

CAPTURE_FILE = (
    "data/machine_test_ai/capture_configuration.txt"
)

TIME_SCORING_FILE = (
    "data/machine_test_ai/time_scoring_configuration.txt"
)


print("=" * 90)
print("DAY 50 - MACHINE TEST AI DESIGN")
print("=" * 90)


# STEP 1
print("\n[STEP 1] MACHINE TEST TYPE DEFINITIONS")
print("-" * 90)

result = get_test_types(TEST_TYPE_FILE)

print(
    f"{'Status':<35}: "
    f"{result['Status']}"
)

print("\nMachine Test Types:")

for index, test_type in enumerate(
    result["Test Types"],
    start=1
):
    print(f"{index}. {test_type}")


# STEP 2
print("\n[STEP 2] MACHINE TEST EVALUATION METRICS")
print("-" * 90)

metric_result = get_evaluation_metrics(
    METRIC_FILE
)

print(
    f"{'Status':<35}: "
    f"{metric_result['Status']}"
)

print("\nEvaluation Metrics:")

for index, metric in enumerate(
    metric_result["Metrics"],
    start=1
):
    print(f"{index}. {metric}")


# STEP 3
print("\n[STEP 3] INPUT / OUTPUT CAPTURE")
print("-" * 90)

capture_result = create_capture_framework(
    CAPTURE_FILE
)

print(
    f"{'Status':<35}: "
    f"{capture_result['Status']}"
)

print("\nCapture Framework:")

for index, (item, description) in enumerate(
    capture_result["Capture Framework"].items(),
    start=1
):
    print(
        f"{index}. {item:<25}: "
        f"{description}"
    )


# STEP 4
print("\n[STEP 4] TIME-BASED SCORING LOGIC")
print("-" * 90)

time_result = create_time_scoring_framework(
    TIME_SCORING_FILE
)

print(
    f"{'Status':<35}: "
    f"{time_result['Status']}"
)

print("\nTime-Based Scoring Framework:")

for index, (item, description) in enumerate(
    time_result["Time Scoring Framework"].items(),
    start=1
):
    print(
        f"{index}. {item:<25}: "
        f"{description}"
    )


# STEP 5
print("\n[STEP 5] TASK EVALUATION LOGIC")
print("-" * 90)

task_evaluation = create_task_evaluation_framework(
    result["Test Types"],
    metric_result["Metrics"],
    capture_result["Capture Framework"],
    time_result["Time Scoring Framework"]
)

print(
    f"{'Evaluation Status':<35}: "
    f"{task_evaluation['Evaluation Status']}"
)

print(
    f"{'Test Types Available':<35}: "
    f"{len(task_evaluation['Test Types'])}"
)

print(
    f"{'Evaluation Metrics':<35}: "
    f"{len(task_evaluation['Evaluation Metrics'])}"
)

print(
    f"{'Capture Components':<35}: "
    f"{len(task_evaluation['Input Output Capture'])}"
)

print(
    f"{'Time Evaluation':<35}: "
    f"{len(task_evaluation['Time Based Evaluation'])}"
)


# STEP 6
print("\n[STEP 6] MACHINE TEST AI FRAMEWORK")
print("-" * 90)

machine_test_framework = build_machine_test_framework(
    result["Test Types"],
    metric_result["Metrics"],
    capture_result["Capture Framework"],
    time_result["Time Scoring Framework"],
    task_evaluation
)

print(
    f"{'Framework Status':<35}: "
    f"{machine_test_framework['Framework Status']}"
)

print(
    f"{'Machine Test Types':<35}: "
    f"{len(machine_test_framework['Test Types'])}"
)

print(
    f"{'Evaluation Metrics':<35}: "
    f"{len(machine_test_framework['Evaluation Metrics'])}"
)

print(
    f"{'Capture Components':<35}: "
    f"{len(machine_test_framework['Input Output Capture'])}"
)

print(
    f"{'Time Scoring Components':<35}: "
    f"{len(machine_test_framework['Time Based Scoring'])}"
)

print(
    f"{'Task Evaluation Status':<35}: "
    f"{task_evaluation['Evaluation Status']}"
)


# STEP 7
print("\n[STEP 7] MACHINE TEST SCORING MODEL")
print("-" * 90)

scoring_model = create_scoring_model(
    metric_result["Metrics"],
    task_evaluation,
    time_result["Time Scoring Framework"]
)

print(
    f"{'Scoring Status':<35}: "
    f"{scoring_model['Scoring Status']}"
)

print(
    f"{'Evaluation Metrics':<35}: "
    f"{len(scoring_model['Evaluation Metrics'])}"
)

print(
    f"{'Task Evaluation':<35}: "
    f"Configured"
)

print(
    f"{'Time-Based Evaluation':<35}: "
    f"Configured"
)

print("\nScoring Metrics:")

for index, metric in enumerate(
    scoring_model["Evaluation Metrics"],
    start=1
):
    print(f"{index}. {metric}")


# STEP 8
print("\n[STEP 8] FINAL MACHINE TEST AI REPORT")
print("-" * 90)

machine_test_report = generate_machine_test_report(
    machine_test_framework,
    scoring_model
)

for key, value in machine_test_report.items():
    print(
        f"{key:<35}: "
        f"{value}"
    )


# FINAL STATUS
print("\n" + "=" * 90)
print("DAY 50 MACHINE TEST AI DESIGN COMPLETED")
print("=" * 90)

print("\nFINAL SYSTEM STATUS")
print("-" * 90)

print(
    f"{'Machine Test Types':<35}: "
    f"{machine_test_report['Test Types']}"
)

print(
    f"{'Evaluation Metrics':<35}: "
    f"{machine_test_report['Evaluation Metrics']}"
)

print(
    f"{'Capture Components':<35}: "
    f"{machine_test_report['Capture Components']}"
)

print(
    f"{'Time Scoring Components':<35}: "
    f"{machine_test_report['Time Scoring Components']}"
)

print(
    f"{'Task Evaluation':<35}: "
    f"{machine_test_report['Task Evaluation Status']}"
)

print(
    f"{'Scoring':<35}: "
    f"{machine_test_report['Scoring Status']}"
)

print("\n" + "=" * 90)
print("MACHINE TEST AI DESIGN COMPLETED SUCCESSFULLY")
print("=" * 90)