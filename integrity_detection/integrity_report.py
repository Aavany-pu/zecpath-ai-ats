def generate_integrity_report(framework):
    signals = framework.get(
        "Malpractice Signals",
        []
    )

    detection_logic = framework.get(
        "Detection Logic",
        {}
    )

    warning_system = framework.get(
        "Warning System",
        {}
    )

    behavioral_integration = framework.get(
        "Behavioral Integration",
        {}
    )

    return {
        "Report Status": framework.get(
            "Framework Status",
            ""
        ),
        "Malpractice Signals": len(signals),
        "Detection Rules": len(detection_logic),
        "Warning Rules": len(warning_system),
        "Behavioral Integration": (
            "Configured"
            if behavioral_integration
            else "Not Configured"
        ),
        "Detection Status": "Requires Observation Data",
        "Risk Status": "Requires Detection Evidence"
    }