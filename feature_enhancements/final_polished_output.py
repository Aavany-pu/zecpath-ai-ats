def create_final_output(
    enhancement_report,
    recruiter_output,
    api_output
):
    if enhancement_report is None:
        return {
            "Status": "Final Output Cannot Be Created",
            "Output": {}
        }

    if not isinstance(enhancement_report, dict):
        return {
            "Status": "Invalid Enhancement Report",
            "Output": {}
        }

    final_output = {
        "Enhancement Report": enhancement_report,
        "Recruiter Output": recruiter_output,
        "API Output": api_output
    }

    return {
        "Status": "Final Polished Output Created",
        "Output": final_output
    }