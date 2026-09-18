def recruiter_report(

    report

):

    recruiter_view = {

        "Skills":
        report["candidate_information"].get(
            "skills",
            []
        ),

        "Experience":
        report["candidate_information"].get(
            "experience",
            "Not Available"
        ),

        "Salary":
        report["candidate_information"].get(
            "salary",
            "Not Mentioned"
        ),

        "Availability":
        report["candidate_information"].get(
            "availability",
            "Unknown"
        ),

        "Screening Score":
        report["screening_score"],

        "Behavior":
        report["behavior_analysis"]

    }

    return recruiter_view