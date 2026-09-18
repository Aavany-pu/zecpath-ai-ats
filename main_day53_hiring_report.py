from hiring_report.report_sections import get_report_sections
from hiring_report.input_loader import load_input_sources
from hiring_report.insight_combiner import combine_evaluation_insights
from hiring_report.strength_weakness import extract_strengths_and_weaknesses
from hiring_report.risk_indicators import extract_risk_indicators
from hiring_report.recommendation_loader import extract_final_recommendation
from hiring_report.hiring_report_generator import generate_hiring_report
from hiring_report.report_formatter import format_hiring_report
from hiring_report.report_exporter import export_hiring_report


SECTIONS_FILE = "data/hiring_report/report_sections.txt"
INPUT_SOURCES_FILE = "data/hiring_report/input_sources.txt"
OUTPUT_FILE = "data/hiring_report/hiring_intelligence_report.txt"


print("=" * 90)
print(" HIRING INTELLIGENCE REPORT GENERATOR")
print("=" * 90)


# --------------------------------------------------------------------------
# STEP 1 - LOAD REPORT SECTIONS
# --------------------------------------------------------------------------

print("\nSTEP 1 - REPORT SECTIONS")
print("-" * 90)

sections_result = get_report_sections(SECTIONS_FILE)

print(f"{'Status':<35}: {sections_result['Status']}")
print(f"{'Number of Sections':<35}: {len(sections_result['Sections'])}")

for index, section in enumerate(sections_result["Sections"], start=1):
    print(f"{index:<3} {section}")


# --------------------------------------------------------------------------
# STEP 2 - LOAD INPUT SOURCES
# --------------------------------------------------------------------------

print("\nSTEP 2 - INPUT SOURCES")
print("-" * 90)

sources_result = load_input_sources(INPUT_SOURCES_FILE)

print(f"{'Status':<35}: {sources_result['Status']}")

for source, path in sources_result["Sources"].items():
    print(f"{source:<35}: {path}")


# --------------------------------------------------------------------------
# STEP 3 - COMBINE EVALUATION INSIGHTS
# --------------------------------------------------------------------------

print("\nSTEP 3 - INSIGHT COMBINATION")
print("-" * 90)

combined_result = combine_evaluation_insights(
    None,
    None,
    None,
    None,
    None
)

evaluation_report = combined_result["Report"]

print(f"{'Status':<35}: {combined_result['Status']}")


# --------------------------------------------------------------------------
# STEP 4 - EXTRACT STRENGTHS AND WEAKNESSES
# --------------------------------------------------------------------------

print("\nSTEP 4 - STRENGTH AND WEAKNESS EXTRACTION")
print("-" * 90)

strength_weakness_result = extract_strengths_and_weaknesses(
    evaluation_report
)

print(
    f"{'Status':<35}: "
    f"{strength_weakness_result['Status']}"
)

print(
    f"{'Strengths Found':<35}: "
    f"{len(strength_weakness_result['Strengths'])}"
)

print(
    f"{'Weaknesses Found':<35}: "
    f"{len(strength_weakness_result['Weaknesses'])}"
)


# --------------------------------------------------------------------------
# STEP 5 - EXTRACT RISK INDICATORS
# --------------------------------------------------------------------------

print("\nSTEP 5 - RISK INDICATOR EXTRACTION")
print("-" * 90)

risk_result = extract_risk_indicators(
    evaluation_report
)

print(
    f"{'Status':<35}: "
    f"{risk_result['Status']}"
)

print(
    f"{'Risk Indicators Found':<35}: "
    f"{len(risk_result['Risk Indicators'])}"
)


# --------------------------------------------------------------------------
# STEP 6 - EXTRACT FINAL RECOMMENDATION
# --------------------------------------------------------------------------

print("\nSTEP 6 - FINAL RECOMMENDATION")
print("-" * 90)

recommendation_result = extract_final_recommendation(
    evaluation_report
)

print(
    f"{'Status':<35}: "
    f"{recommendation_result['Status']}"
)

print(
    f"{'Final Recommendation':<35}: "
    f"{recommendation_result['Final Recommendation']}"
)


# --------------------------------------------------------------------------
# STEP 7 - GENERATE HIRING REPORT
# --------------------------------------------------------------------------

print("\nSTEP 7 - HIRING REPORT GENERATION")
print("-" * 90)

hiring_report = generate_hiring_report(
    sections_result["Sections"],
    evaluation_report,
    strength_weakness_result,
    risk_result,
    recommendation_result
)

print(
    f"{'Status':<35}: "
    f"{hiring_report['Report Status']}"
)


# --------------------------------------------------------------------------
# STEP 8 - FORMAT REPORT
# --------------------------------------------------------------------------

print("\nSTEP 8 - REPORT FORMATTING")
print("-" * 90)

formatted_report = format_hiring_report(
    hiring_report
)

print(
    f"{'Status':<35}: Report Formatted"
)


# --------------------------------------------------------------------------
# STEP 9 - EXPORT REPORT
# --------------------------------------------------------------------------

print("\nSTEP 9 - REPORT EXPORT")
print("-" * 90)

export_result = export_hiring_report(
    formatted_report,
    OUTPUT_FILE
)

print(
    f"{'Status':<35}: "
    f"{export_result['Status']}"
)

print(
    f"{'Output File':<35}: "
    f"{export_result['Output File']}"
)


# --------------------------------------------------------------------------
# FINAL SYSTEM STATUS
# --------------------------------------------------------------------------

print("\n" + "=" * 90)
print("DAY 53 HIRING INTELLIGENCE REPORT PIPELINE COMPLETED")
print("=" * 90)

print("\nFINAL SYSTEM STATUS")
print("-" * 90)

print(
    f"{'Report Sections':<35}: "
    f"{len(hiring_report['Report Sections'])}"
)

print(
    f"{'Evaluation Insights':<35}: "
    f"{len(hiring_report['Evaluation Insights'])}"
)

print(
    f"{'Strengths':<35}: "
    f"{len(hiring_report['Strengths'])}"
)

print(
    f"{'Weaknesses':<35}: "
    f"{len(hiring_report['Weaknesses'])}"
)

print(
    f"{'Risk Indicators':<35}: "
    f"{len(hiring_report['Risk Indicators'])}"
)

print(
    f"{'Final Recommendation':<35}: "
    f"{hiring_report['Final Recommendation']}"
)

print(
    f"{'Export Status':<35}: "
    f"{export_result['Status']}"
)

print(
    f"{'Export File':<35}: "
    f"{export_result['Output File']}"
)

print("\n" + "=" * 90)
print("DAILY HIRING INTELLIGENCE REPORT PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 90)