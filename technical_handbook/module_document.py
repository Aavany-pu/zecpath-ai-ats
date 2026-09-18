def create_module_document():
    modules = [
        {
            "Module": "Resume Processing",
            "Purpose": "Handles resume input and candidate information extraction"
        },
        {
            "Module": "ATS Engine",
            "Purpose": "Processes candidate resume evaluation against job requirements"
        },
        {
            "Module": "Screening Engine",
            "Purpose": "Processes candidate screening evaluation"
        },
        {
            "Module": "HR Interview Engine",
            "Purpose": "Processes HR interview evaluation"
        },
        {
            "Module": "Technical Interview Engine",
            "Purpose": "Processes technical interview evaluation"
        },
        {
            "Module": "Behavioral AI",
            "Purpose": "Processes configured behavioral signals"
        },
        {
            "Module": "Integrity Detection",
            "Purpose": "Processes configured interview integrity signals"
        },
        {
            "Module": "Unified Scoring Engine",
            "Purpose": "Combines available evaluation results"
        },
        {
            "Module": "Final Recommendation AI",
            "Purpose": "Processes the final recommendation"
        },
        {
            "Module": "Hiring Intelligence Report",
            "Purpose": "Combines candidate evaluation information into a recruiter-facing report"
        },
        {
            "Module": "Security and Governance",
            "Purpose": "Provides security, audit, consent, storage, and access-control design"
        },
        {
            "Module": "AI Observability",
            "Purpose": "Provides logging and monitoring design for AI services"
        }
    ]

    return {
        "Status": "Module Documentation Created",
        "Modules": modules
    }