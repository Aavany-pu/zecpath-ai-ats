from datetime import datetime


def create_decision_audit_log(
    candidate_reference,
    decision,
    score_information,
    risk_information
):
    audit_log = {
        "Timestamp": datetime.now().isoformat(),
        "Candidate Reference": candidate_reference,
        "Decision": decision,
        "Score Information": score_information,
        "Risk Information": risk_information
    }

    return {
        "Status": "Decision Audit Log Created",
        "Audit Log": audit_log
    }