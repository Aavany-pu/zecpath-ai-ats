def create_internal_review_report(
    walkthrough_result,
    accuracy_result,
    ux_result,
    performance_result,
    reviewer_result,
    improvement_result,
    action_result
):
    report = {
        "System Walkthrough": walkthrough_result,
        "Accuracy Review": accuracy_result,
        "UX Review": ux_result,
        "Performance Review": performance_result,
        "Reviewer Feedback": reviewer_result,
        "Prioritized Improvements": improvement_result,
        "Action Plan": action_result
    }

    return {
        "Status": "Internal Review Report Created",
        "Report": report
    }