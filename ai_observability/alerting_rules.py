def evaluate_alerts(metrics, alert_configuration):
    alerts = []

    for metric_name, metric_value in metrics.items():
        if metric_value is None:
            continue

        configuration = alert_configuration.get(metric_name)

        if configuration is None:
            continue

        limit = configuration.get("Limit")
        condition = configuration.get("Condition")

        if limit is None or condition is None:
            continue

        if condition == "greater_than" and metric_value > limit:
            alerts.append({
                "Metric": metric_name,
                "Value": metric_value,
                "Limit": limit,
                "Alert": "Threshold Exceeded"
            })

        elif condition == "less_than" and metric_value < limit:
            alerts.append({
                "Metric": metric_name,
                "Value": metric_value,
                "Limit": limit,
                "Alert": "Below Minimum"
            })

    if alerts:
        status = "Alerts Triggered"
    else:
        status = "No Alerts Triggered"

    return {
        "Status": status,
        "Alerts": alerts
    }