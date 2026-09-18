def simulate_hiring_journey(
    resume_input,
    ats_result,
    screening_result,
    hr_result,
    technical_result,
    final_decision
):
    return {
        "Status": "Full Hiring Journey Simulated",

        "Resume Upload": resume_input,

        "ATS Scoring": ats_result,

        "Screening": screening_result,

        "HR Interview": hr_result,

        "Technical Interview": technical_result,

        "Final Decision": final_decision
    }