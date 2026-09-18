def generate_machine_test_report(
    machine_test_framework,
    scoring_model
):
    return {
        "Report Status": machine_test_framework.get(
            "Framework Status",
            ""
        ),
        "Test Types": len(
            machine_test_framework.get(
                "Test Types",
                []
            )
        ),
        "Evaluation Metrics": len(
            machine_test_framework.get(
                "Evaluation Metrics",
                []
            )
        ),
        "Capture Components": len(
            machine_test_framework.get(
                "Input Output Capture",
                {}
            )
        ),
        "Time Scoring Components": len(
            machine_test_framework.get(
                "Time Based Scoring",
                {}
            )
        ),
        "Task Evaluation Status": machine_test_framework.get(
            "Task Evaluation",
            {}
        ).get(
            "Evaluation Status",
            ""
        ),
        "Scoring Status": scoring_model.get(
            "Scoring Status",
            ""
        )
    }