def check_demo_readiness(
    mock_demo,
    stakeholder_questions,
    feedback_report,
    improved_presentation
):
    checks = {
        "Mock Demo Structure": mock_demo,
        "Stakeholder Q&A": stakeholder_questions,
        "Feedback Report": feedback_report,
        "Improved Presentation": improved_presentation
    }

    missing_components = []

    for component, result in checks.items():
        if result is None:
            missing_components.append(component)
        elif not isinstance(result, dict):
            missing_components.append(component)

    if missing_components:
        return {
            "Status": "Demo Not Ready",
            "Missing Components": missing_components
        }

    return {
        "Status": "Final Demo Readiness Confirmed",
        "Missing Components": []
    }