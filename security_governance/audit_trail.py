def create_audit_log(log_type, event_data):
    return {
        "Log Type": log_type,
        "Event Data": event_data
    }


def create_score_log(score_data):
    return create_audit_log(
        "Score Log",
        score_data
    )


def create_decision_log(decision_data):
    return create_audit_log(
        "Decision Log",
        decision_data
    )


def generate_audit_trail(score_data, decision_data):
    score_log = create_score_log(score_data)
    decision_log = create_decision_log(decision_data)

    return {
        "Status": "Audit Trail Generated",
        "Score Log": score_log,
        "Decision Log": decision_log
    }