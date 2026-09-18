def create_recruiter_output(report):
    if report is None:
        return {
            "Status": "No Recruiter Report Available",
            "Recruiter Output": {}
        }

    if not isinstance(report, dict):
        return {
            "Status": "Invalid Recruiter Report",
            "Recruiter Output": {}
        }

    recruiter_output = {}

    for section, content in report.items():
        recruiter_output[str(section).strip()] = content

    return {
        "Status": "Recruiter-Facing Output Created",
        "Recruiter Output": recruiter_output
    }