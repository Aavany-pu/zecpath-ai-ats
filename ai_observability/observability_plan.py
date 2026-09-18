def create_observability_plan(
    logging_result,
    metrics_result,
    alert_result,
    dashboard_result,
    audit_result
):
    plan = {
        "Logging": logging_result,
        "Monitoring Metrics": metrics_result,
        "Alerting": alert_result,
        "Dashboard": dashboard_result,
        "Decision Audit": audit_result
    }

    return {
        "Status": "AI Observability Plan Created",
        "Observability Plan": plan
    }