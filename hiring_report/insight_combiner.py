def combine_evaluation_insights(
    ats_summary,
    screening_results,
    hr_insights,
    technical_performance,
    behavioral_flags
):
    combined_report = {
        "ATS Summary": ats_summary,
        "Screening Results": screening_results,
        "HR Insights": hr_insights,
        "Technical Performance": technical_performance,
        "Behavioral Flags": behavioral_flags
    }

    return {
        "Status": "Evaluation Insights Combined",
        "Report": combined_report
    }