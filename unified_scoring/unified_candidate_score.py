def create_unified_candidate_score(
    candidate,
    ats_score,
    screening_score,
    hr_score,
    unified_score,
    hiring_fit
):

    candidate_score = {

        "Candidate": candidate,

        "ATS Score": ats_score,

        "Screening Score": screening_score,

        "HR Interview Score": hr_score,

        "Unified Score": unified_score,

        "Hiring Fit (%)": hiring_fit

    }

    return candidate_score