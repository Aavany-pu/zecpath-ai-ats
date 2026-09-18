from cross_round_aggregation.ats_loader import get_ats_score
from cross_round_aggregation.screening_loader import get_screening_score
from cross_round_aggregation.hr_loader import get_hr_score
from cross_round_aggregation.score_normalizer import get_normalized_scores
from cross_round_aggregation.weight_loader import get_role_weights
from cross_round_aggregation.aggregation_engine import get_aggregated_score
from cross_round_aggregation.hiring_fit_calculator import get_hiring_fit
from cross_round_aggregation.transparency_report import (
    get_transparency_report
)
from cross_round_aggregation.unified_candidate_score import (
    get_unified_candidate_score
)


ATS_FILE = "data/structured_data/ats_score.json"
SCREENING_FILE = "data/screening_reports/final_report.json"
WEIGHTS_FILE = (
    "data/cross_round_aggregation/role_weights.txt"
)


def main():

    print("=" * 90)
    print("DAY 51 - CROSS-ROUND AGGREGATION ENGINE")
    print("=" * 90)

    # Load candidate ID from ATS output
    import json

    with open(
        ATS_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        ats_data = json.load(file)

    candidate_id = ats_data.get(
        "candidate_id",
        "Unknown"
    )

    # Load existing round scores
    ats_score = get_ats_score(
        ATS_FILE
    )

    screening_score = get_screening_score(
        SCREENING_FILE
    )

    hr_score = get_hr_score()

    scores = {
        "ATS": ats_score,
        "Screening": screening_score,
        "HR Interview": hr_score,
        "Technical Interview": None,
        "Machine Test": None
    }

    # Normalize available scores
    normalized_scores = get_normalized_scores(
        scores
    )

    # Load external role weights
    weights = get_role_weights(
        WEIGHTS_FILE
    )

    # Aggregate available scores
    final_score = get_aggregated_score(
        normalized_scores,
        weights
    )

    # Calculate hiring fit
    hiring_fit = get_hiring_fit(
        final_score
    )

    # Create transparent scoring report
    transparency = get_transparency_report(
        normalized_scores,
        weights,
        final_score
    )

    # Create unified candidate score object
    unified_score = get_unified_candidate_score(
        candidate_id,
        normalized_scores,
        weights,
        final_score,
        hiring_fit
    )

    print("\nCANDIDATE INFORMATION")
    print("-" * 90)
    print(f"{'Candidate ID':<30}: {candidate_id}")

    print("\nROUND SCORES")
    print("-" * 90)

    for round_name, score in normalized_scores.items():

        if score is None:
            display_score = "Not Available"
        else:
            display_score = score

        print(
            f"{round_name:<30}: {display_score}"
        )

    print("\nROLE WEIGHTS")
    print("-" * 90)

    for key, value in weights.items():

        print(
            f"{key:<30}: {value}"
        )

    print("\nFINAL RESULT")
    print("-" * 90)

    print(
        f"{'Aggregated Score':<30}: "
        f"{final_score}"
    )

    print(
        f"{'Hiring Fit Percentage':<30}: "
        f"{hiring_fit}%"
    )

    print("\nTRANSPARENCY")
    print("-" * 90)

    for item in transparency[
        "Scoring Details"
    ]:

        print(
            f"{item['Round']:<25} | "
            f"Score: {str(item['Score']):<10} | "
            f"Weight: {str(item['Weight']):<8} | "
            f"Status: {item['Status']}"
        )

    print("\nUNIFIED CANDIDATE SCORE")
    print("-" * 90)

    for key, value in unified_score.items():

        print(
            f"{key:<30}: {value}"
        )

    print("=" * 90)
    print("CROSS-ROUND AGGREGATION COMPLETED")
    print("=" * 90)


if __name__ == "__main__":
    main()