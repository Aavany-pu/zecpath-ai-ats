from unified_scoring.scoring_anomaly_correction import (
    correct_scoring_anomaly
)


def refine_score(
    ai_score,
    reference_score,
    tolerance
):

    correction = correct_scoring_anomaly(
        ai_score,
        reference_score,
        tolerance
    )

    refined_score = correction["Corrected Score"]

    return {
        "Original Score": correction["Original AI Score"],
        "Reference Score": correction["Reference Score"],
        "Difference": correction["Difference"],
        "Refined Score": refined_score
    }