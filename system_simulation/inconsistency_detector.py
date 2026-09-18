def detect_inconsistencies(ai_human_comparison):
    inconsistencies = []

    consistency_status = ai_human_comparison.get(
        "Consistency Status"
    )

    if consistency_status == "AI and Human Judgment Inconsistent":
        inconsistencies.append(
            "Difference detected between AI and human judgment"
        )

    if inconsistencies:
        status = "Inconsistencies Detected"
    else:
        status = "No Inconsistencies Detected"

    return {
        "Status": status,
        "Inconsistencies": inconsistencies
    }
    