def create_system_architecture():
    architecture = [
        "Candidate Data",
        "Resume Processing",
        "ATS Scoring",
        "Candidate Screening",
        "HR Interview Evaluation",
        "Technical Skill Evaluation",
        "Decision & Recommendation",
        "Hiring Intelligence Report",
        "Recruiter-Facing Output"
    ]

    connections = [
        "Candidate Data -> Resume Processing",
        "Resume Processing -> ATS Scoring",
        "ATS Scoring -> Candidate Screening",
        "Candidate Screening -> HR Interview Evaluation",
        "HR Interview Evaluation -> Technical Skill Evaluation",
        "Technical Skill Evaluation -> Decision & Recommendation",
        "Decision & Recommendation -> Hiring Intelligence Report",
        "Hiring Intelligence Report -> Recruiter-Facing Output"
    ]

    return {
        "Status": "System Architecture Prepared",
        "Components": architecture,
        "Connections": connections
    }