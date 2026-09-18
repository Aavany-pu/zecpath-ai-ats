from behavioral_ai.signal_definitions import get_behavioral_signals
from behavioral_ai.measurable_indicators import get_measurable_indicators
from behavioral_ai.signal_mapper import map_behavioral_signals
from behavioral_ai.behavioral_scoring import (
    generate_behavioral_scoring_framework
)
from behavioral_ai.behavioral_framework import (
    build_behavioral_framework
)
from behavioral_ai.behavioral_report import (
    generate_behavioral_report
)


SIGNAL_FILE = "data/behavioral_ai/signal_configuration.txt"
INDICATOR_FILE = "data/behavioral_ai/measurable_indicators.txt"
MAPPING_FILE = "data/behavioral_ai/signal_behavior_mapping.txt"
SCORING_FILE = "data/behavioral_ai/behavioral_scoring_configuration.txt"
REPORT_CONFIG_FILE = "data/behavioral_ai/report_configuration.txt"


print("=" * 90)
print("DAY 48 - BEHAVIORAL AI RESEARCH & DESIGN")
print("=" * 90)


# STEP 1
print("\n[STEP 1] BEHAVIORAL SIGNAL DEFINITIONS")
print("-" * 90)

signal_result = get_behavioral_signals(SIGNAL_FILE)

for key, value in signal_result.items():
    if key != "Signals":
        print(f"{key:<35}: {value}")

print("\nObservable Signals:")

for index, signal in enumerate(
    signal_result["Signals"],
    start=1
):
    print(f"{index}. {signal}")


# STEP 2
print("\n[STEP 2] MEASURABLE BEHAVIORAL INDICATORS")
print("-" * 90)

indicator_result = get_measurable_indicators(
    INDICATOR_FILE
)

for key, value in indicator_result.items():
    if key != "Indicators":
        print(f"{key:<35}: {value}")

print("\nObservable Indicators:")

for index, (name, description) in enumerate(
    indicator_result["Indicators"].items(),
    start=1
):
    print(
        f"{index}. {name:<30}: "
        f"{description}"
    )


# STEP 3
print("\n[STEP 3] SIGNAL-TO-BEHAVIORAL INSIGHT MAPPING")
print("-" * 90)

mapping_result = map_behavioral_signals(
    MAPPING_FILE,
    signal_result["Signals"]
)

for key, value in mapping_result.items():
    if key != "Mappings":
        print(f"{key:<35}: {value}")

print("\nSignal → Observable Insight:")

for index, (signal, insight) in enumerate(
    mapping_result["Mappings"].items(),
    start=1
):
    print(
        f"{index}. {signal:<30}: "
        f"{insight}"
    )


# STEP 4
print("\n[STEP 4] NON-INVASIVE BEHAVIORAL SCORING")
print("-" * 90)

scoring_result = generate_behavioral_scoring_framework(
    SCORING_FILE,
    signal_result["Signals"]
)

for key, value in scoring_result.items():
    if key != "Framework":
        print(f"{key:<35}: {value}")

print("\nBehavioral Scoring Framework:")

for index, (indicator, details) in enumerate(
    scoring_result["Framework"].items(),
    start=1
):
    print(f"\n{index}. {indicator}")

    for key, value in details.items():
        print(
            f"   {key:<28}: "
            f"{value}"
        )


# STEP 5
print("\n[STEP 5] BEHAVIORAL ANALYSIS FRAMEWORK")
print("-" * 90)

framework_result = build_behavioral_framework(
    signal_result["Signals"],
    indicator_result["Indicators"],
    mapping_result["Mappings"],
    scoring_result["Framework"]
)

print(
    f"{'Status':<35}: "
    f"{framework_result['Status']}"
)

print("\nFramework Signals:")

for index, item in enumerate(
    framework_result["Framework"],
    start=1
):
    print(
        f"{index}. "
        f"{item['Signal']:<30}"
    )


# STEP 6
print("\n[STEP 6] BEHAVIORAL ANALYSIS REPORT")
print("-" * 90)

behavioral_report = generate_behavioral_report(
    framework_result,
    REPORT_CONFIG_FILE
)

for key, value in behavioral_report.items():
    if key not in ["Framework", "Limitations"]:
        print(
            f"{key:<35}: "
            f"{value}"
        )

print("\nLimitations:")

for index, limitation in enumerate(
    behavioral_report["Limitations"],
    start=1
):
    print(f"{index}. {limitation}")


# FINAL
print("\n" + "=" * 90)
print("BEHAVIORAL AI PIPELINE COMPLETED")
print("=" * 90)