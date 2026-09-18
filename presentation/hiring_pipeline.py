def create_hiring_pipeline():
    pipeline = [
        "Candidate Resume",
        "Resume Processing",
        "ATS Scoring",
        "Candidate Screening",
        "HR Interview",
        "Technical Evaluation",
        "Decision & Recommendation",
        "Hiring Intelligence Report",
        "Recruiter Output"
    ]

    return {
        "Status": "Hiring Pipeline Prepared",
        "Pipeline": pipeline,
        "Total Stages": len(pipeline)
    }