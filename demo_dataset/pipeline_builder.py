def build_hiring_pipeline(
    resumes,
    job_descriptions,
    candidate_responses,
    ats_results,
    screening_outputs,
    interview_outputs
):
    pipeline = {
        "Resume Data": resumes,
        "Job Description Data": job_descriptions,
        "Candidate Response Data": candidate_responses,
        "ATS Results": ats_results,
        "Screening Outputs": screening_outputs,
        "Interview Outputs": interview_outputs
    }

    return {
        "Status": "Complete Hiring Pipeline Dataset Created",
        "Pipeline": pipeline
    }