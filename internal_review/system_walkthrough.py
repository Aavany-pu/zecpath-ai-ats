def run_system_walkthrough(
    ats_result,
    screening_result,
    hr_result,
    technical_result,
    decision_result
):
    stages = {
        "ATS": ats_result,
        "Screening": screening_result,
        "HR": hr_result,
        "Technical": technical_result,
        "Decision": decision_result
    }

    completed_stages = []
    missing_stages = []

    for stage, result in stages.items():
        if result is not None:
            completed_stages.append(stage)
        else:
            missing_stages.append(stage)

    if missing_stages:
        status = "System Walkthrough Incomplete"
    else:
        status = "Full System Walkthrough Completed"

    return {
        "Status": status,
        "Completed Stages": completed_stages,
        "Missing Stages": missing_stages,
        "Pipeline": stages
    }