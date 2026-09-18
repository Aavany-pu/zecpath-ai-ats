def generate_handover_summary(
    demo_result,
    scoring_result,
    recommendation_result,
    architecture_result,
    scoring_logic_result,
    feedback_result,
    improvement_result,
    knowledge_transfer_result,
    final_report_result
):
    results = {
        "Final Demo": demo_result,
        "Scoring Breakdown": scoring_result,
        "Hiring Recommendation": recommendation_result,
        "Architecture": architecture_result,
        "Scoring Logic": scoring_logic_result,
        "Evaluation Discussion": feedback_result,
        "Final Improvements": improvement_result,
        "Knowledge Transfer": knowledge_transfer_result,
        "Final Report": final_report_result
    }

    completed_sections = 0

    for result in results.values():
        if isinstance(result, dict):
            status = result.get("Status")

            if status and not status.startswith("Invalid"):
                completed_sections += 1

    return {
        "Status": "Final Handover Ready",
        "System": "Zecpath AI",
        "Completed Sections": completed_sections,
        "Total Sections": len(results),
        "Handover Sections": results
    }