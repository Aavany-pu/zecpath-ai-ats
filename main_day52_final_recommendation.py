from final_recommendation.decision_categories import (
    get_decision_categories
)

from final_recommendation.decision_logic import (
    create_hybrid_logic
)

from final_recommendation.confidence_calculator import (
    create_confidence_framework
)

from final_recommendation.risk_factor_loader import (
    create_risk_factor_framework
)

from final_recommendation.explainable_decision import (
    create_explainable_decision
)

from final_recommendation.decision_engine import (
    create_decision_engine
)

from final_recommendation.recommendation_report import (
    create_recommendation_output
)


CATEGORY_FILE = (
    "data/final_recommendation/"
    "decision_categories.txt"
)

RULE_FILE = (
    "data/final_recommendation/"
    "decision_rules.txt"
)

CONFIDENCE_FILE = (
    "data/final_recommendation/"
    "confidence_configuration.txt"
)

RISK_FILE = (
    "data/final_recommendation/"
    "risk_factors.txt"
)


print("=" * 90)
print("DAY 52 - FINAL RECOMMENDATION AI")
print("=" * 90)


# STEP 1
print("\n[STEP 1] DECISION CATEGORY DEFINITIONS")
print("-" * 90)

category_result = get_decision_categories(
    CATEGORY_FILE
)

print(
    f"{'Status':<35}: "
    f"{category_result['Status']}"
)

print("\nDecision Categories:")

for index, category in enumerate(
    category_result["Categories"],
    start=1
):
    print(f"{index}. {category}")


# STEP 2
print("\n[STEP 2] RULE + SCORE HYBRID LOGIC")
print("-" * 90)

hybrid_result = create_hybrid_logic(
    RULE_FILE
)

for key, value in hybrid_result.items():
    print(
        f"{key:<35}: "
        f"{value}"
    )


# STEP 3
print("\n[STEP 3] DECISION CONFIDENCE FRAMEWORK")
print("-" * 90)

confidence_result = create_confidence_framework(
    CONFIDENCE_FILE
)

for key, value in confidence_result.items():
    print(
        f"{key:<35}: "
        f"{value}"
    )


# STEP 4
print("\n[STEP 4] BEHAVIOR & INTEGRITY RISK FACTORS")
print("-" * 90)

risk_result = create_risk_factor_framework(
    RISK_FILE
)

for key, value in risk_result.items():
    print(
        f"{key:<35}: "
        f"{value}"
    )


# STEP 5
print("\n[STEP 5] EXPLAINABLE DECISION OUTPUT")
print("-" * 90)

explanation_result = create_explainable_decision(
    "Requires Decision Evidence",
    "Requires Evaluation Evidence",
    confidence_result,
    risk_result
)

print(
    f"{'Decision':<35}: "
    f"{explanation_result['Decision']}"
)

print(
    f"{'Explanation Status':<35}: "
    f"{explanation_result['Explanation Status']}"
)


# STEP 6
print("\n[STEP 6] FINAL DECISION AI ENGINE")
print("-" * 90)

decision_engine = create_decision_engine(
    category_result["Categories"],
    hybrid_result,
    confidence_result,
    risk_result
)

print(
    f"{'Status':<35}: "
    f"{decision_engine['Status']}"
)

print(
    f"{'Decision Categories':<35}: "
    f"{len(decision_engine['Decision Categories'])}"
)

print(
    f"{'Decision Logic':<35}: "
    f"Configured"
)

print(
    f"{'Confidence Framework':<35}: "
    f"Configured"
)

print(
    f"{'Risk Framework':<35}: "
    f"Configured"
)

print(
    f"{'Decision Status':<35}: "
    f"{decision_engine['Decision Status']}"
)


# STEP 7
print("\n[STEP 7] FINAL CANDIDATE DECISION OUTPUT")
print("-" * 90)

recommendation_output = create_recommendation_output(
    decision_engine["Decision Status"],
    confidence_result,
    risk_result,
    explanation_result
)

print(
    f"{'Output Status':<35}: "
    f"{recommendation_output['Output Status']}"
)

print(
    f"{'Decision':<35}: "
    f"{recommendation_output['Decision']}"
)


# FINAL
print("\n" + "=" * 90)
print("DAY 52 FINAL RECOMMENDATION PIPELINE COMPLETED")
print("=" * 90)

print("\nFINAL SYSTEM STATUS")
print("-" * 90)

print(
    f"{'Decision Categories':<35}: "
    f"{len(category_result['Categories'])}"
)

print(
    f"{'Hybrid Logic':<35}: "
    f"Configured"
)

print(
    f"{'Confidence Framework':<35}: "
    f"Configured"
)

print(
    f"{'Risk Framework':<35}: "
    f"Configured"
)

print(
    f"{'Explainable Output':<35}: "
    f"Configured"
)

print(
    f"{'Decision Engine':<35}: "
    f"{decision_engine['Status']}"
)

print(
    f"{'Decision Status':<35}: "
    f"{recommendation_output['Decision']}"
)

print("\n" + "=" * 90)
print("COMPLETED SUCCESSFULLY")
print("=" * 90)