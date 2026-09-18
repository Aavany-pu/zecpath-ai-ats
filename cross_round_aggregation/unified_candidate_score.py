def create_unified_candidate_score(
    candidate_id,
    scores,
    weights,
    final_score,
    hiring_fit
):

    return {
        "Candidate ID": candidate_id,
        "Round Scores": scores,
        "Role Weights": weights,
        "Aggregated Score": final_score,
        "Hiring Fit Percentage": hiring_fit
    }


def get_unified_candidate_score(
    candidate_id,
    scores,
    weights,
    final_score,
    hiring_fit
):

    return create_unified_candidate_score(
        candidate_id,
        scores,
        weights,
        final_score,
        hiring_fit
    )