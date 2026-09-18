def create_monitoring_dashboard(
    candidate_processing_stats,
    interview_success_rates,
    system_metrics,
    alerts
):
    dashboard = {
        "Candidate Processing Stats": candidate_processing_stats,
        "Interview Success Rates": interview_success_rates,
        "System Metrics": system_metrics,
        "Active Alerts": alerts
    }

    return {
        "Status": "Monitoring Dashboard Structure Created",
        "Dashboard": dashboard
    }