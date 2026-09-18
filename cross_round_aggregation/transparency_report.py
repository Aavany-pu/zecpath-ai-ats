def generate_transparency_report(
    scores,
    weights,
    final_score
):

    report = []

    for round_name, score in scores.items():

        weight = weights.get(round_name)

        if score is None:
            contribution = None
            status = "Score Not Available"

        elif weight is None:
            contribution = None
            status = "Weight Not Available"

        else:
            contribution = round(
                score * weight,
                2
            )
            status = "Included"

        report.append({
            "Round": round_name,
            "Score": score,
            "Weight": weight,
            "Weighted Contribution": contribution,
            "Status": status
        })

    return {
        "Final Aggregated Score": final_score,
        "Scoring Details": report
    }


def get_transparency_report(
    scores,
    weights,
    final_score
):

    return generate_transparency_report(
        scores,
        weights,
        final_score
    )