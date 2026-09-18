from ai_observability.logging_system import create_observability_logs
from ai_observability.monitoring_metrics import calculate_monitoring_metrics
from ai_observability.alerting_rules import evaluate_alerts
from ai_observability.monitoring_dashboard import create_monitoring_dashboard
from ai_observability.decision_audit import create_decision_audit_log
from ai_observability.observability_plan import create_observability_plan


print("=" * 90)
print("DAY 61 - AI MONITORING & OBSERVABILITY")
print("=" * 90)


# ============================================================
# STEP 1 - LOGGING SYSTEM
# ============================================================

print("\n" + "=" * 90)
print("STEP 1 - LOGGING SYSTEM")
print("=" * 90)

logs_result = create_observability_logs()

print(f"{'Status':<30}: {logs_result['Status']}")

for log_type, log in logs_result["Logs"].items():
    print(f"\n{log_type}")
    print("-" * 90)

    for key, value in log.items():
        print(f"{key:<30}: {value}")


# ============================================================
# STEP 2 - MONITORING METRICS
# ============================================================

print("\n" + "=" * 90)
print("STEP 2 - MONITORING METRICS")
print("=" * 90)

metrics_result = calculate_monitoring_metrics(
    response_times=[],
    correct_results=0,
    total_results=0,
    failed_requests=0,
    total_requests=0
)

print(f"{'Status':<30}: {metrics_result['Status']}")

for metric, value in metrics_result["Metrics"].items():
    print(f"{metric:<30}: {value}")


# ============================================================
# STEP 3 - ALERTING RULES
# ============================================================

print("\n" + "=" * 90)
print("STEP 3 - ALERTING RULES")
print("=" * 90)

alert_configuration = {
    "Average Response Time": {
        "Limit": 2.0,
        "Condition": "greater_than"
    },
    "Accuracy": {
        "Limit": 80.0,
        "Condition": "less_than"
    },
    "Failure Rate": {
        "Limit": 10.0,
        "Condition": "greater_than"
    }
}

alert_result = evaluate_alerts(
    metrics_result["Metrics"],
    alert_configuration
)

print(f"{'Status':<30}: {alert_result['Status']}")

if alert_result["Alerts"]:
    for alert in alert_result["Alerts"]:
        print("\nAlert")
        print("-" * 90)

        for key, value in alert.items():
            print(f"{key:<30}: {value}")
else:
    print(f"{'Alerts':<30}: None")


# ============================================================
# STEP 4 - MONITORING DASHBOARD
# ============================================================

print("\n" + "=" * 90)
print("STEP 4 - MONITORING DASHBOARD")
print("=" * 90)

dashboard_result = create_monitoring_dashboard(
    candidate_processing_stats={},
    interview_success_rates={},
    system_metrics=metrics_result["Metrics"],
    alerts=alert_result["Alerts"]
)

print(f"{'Status':<30}: {dashboard_result['Status']}")

for section, data in dashboard_result["Dashboard"].items():
    print(f"\n{section}")
    print("-" * 90)
    print(data)


# ============================================================
# STEP 5 - DECISION AUDIT LOG
# ============================================================

print("\n" + "=" * 90)
print("STEP 5 - DECISION AUDIT LOG")
print("=" * 90)

audit_result = create_decision_audit_log(
    candidate_reference=None,
    decision=None,
    score_information=None,
    risk_information=None
)

print(f"{'Status':<30}: {audit_result['Status']}")

for key, value in audit_result["Audit Log"].items():
    print(f"{key:<30}: {value}")


# ============================================================
# STEP 6 - OBSERVABILITY PLAN
# ============================================================

print("\n" + "=" * 90)
print("STEP 6 - OBSERVABILITY PLAN")
print("=" * 90)

plan_result = create_observability_plan(
    logging_result=logs_result,
    metrics_result=metrics_result,
    alert_result=alert_result,
    dashboard_result=dashboard_result,
    audit_result=audit_result
)

print(f"{'Status':<30}: {plan_result['Status']}")

for section in plan_result["Observability Plan"]:
    print(f"{section:<30}: Integrated")


# ============================================================
# FINAL RESULT
# ============================================================

print("\n" + "=" * 90)
print("DAY 61 FINAL RESULT")
print("=" * 90)

print(f"{'Logging System':<35}: Completed")
print(f"{'Monitoring Metrics':<35}: Completed")
print(f"{'Alerting Rules':<35}: Completed")
print(f"{'Monitoring Dashboard':<35}: Completed")
print(f"{'Decision Audit Logs':<35}: Completed")
print(f"{'Observability Plan':<35}: Completed")

print("=" * 90)
print(" OBSERVABILITY TEST COMPLETED")
print("=" * 90)