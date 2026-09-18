def create_workflow_document():
    workflow = [
        "Candidate Resume Upload",
        "Resume Parsing",
        "ATS Evaluation",
        "Candidate Screening",
        "HR Interview",
        "Technical Interview",
        "Behavioral Analysis",
        "Integrity Detection",
        "Unified Evaluation",
        "Final Recommendation",
        "Hiring Intelligence Report"
    ]

    return {
        "Status": "Hiring Workflow Documentation Created",
        "Workflow": workflow
    }


def create_workflow_diagram(workflow):
    if not workflow:
        return "No Workflow Available"

    diagram = workflow[0]

    for step in workflow[1:]:
        diagram += f" -> {step}"

    return diagram