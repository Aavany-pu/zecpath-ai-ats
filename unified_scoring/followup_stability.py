def stabilize_followup_logic(
    answer,
    confidence_score,
    stress_score,
    previous_followup
):

    answer = answer.strip()

    if not answer:

        return {
            "Follow-up Required": True,
            "Reason": "Answer is empty",
            "Follow-up": previous_followup
        }


    if previous_followup == answer:

        return {
            "Follow-up Required": False,
            "Reason": "Repeated follow-up avoided",
            "Follow-up": ""
        }


    if confidence_score < 50:

        return {
            "Follow-up Required": True,
            "Reason": "Low confidence detected",
            "Follow-up": previous_followup
        }


    if stress_score > 70:

        return {
            "Follow-up Required": True,
            "Reason": "High stress detected",
            "Follow-up": previous_followup
        }


    return {
        "Follow-up Required": False,
        "Reason": "Response is stable",
        "Follow-up": ""
    }