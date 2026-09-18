from ats_engine.ats_scoring import calculate_ats_score


def run_ats_evaluation(candidate_skills, required_skills):
    if candidate_skills is None:
        return {
            "Status": "Candidate Skills Missing",
            "ATS Result": {}
        }

    if required_skills is None:
        return {
            "Status": "Required Skills Missing",
            "ATS Result": {}
        }

    try:
        result = calculate_ats_score(
            candidate_skills,
            required_skills
        )

        return {
            "Status": "ATS Evaluation Completed",
            "ATS Result": result
        }

    except Exception as error:
        return {
            "Status": "ATS Evaluation Failed",
            "ATS Result": {},
            "Error": str(error)
        }