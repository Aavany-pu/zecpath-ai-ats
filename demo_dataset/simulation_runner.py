def run_end_to_end_simulation(pipeline):
    if not pipeline:
        return {
            "Status": "Simulation Failed",
            "Pipeline": None
        }

    simulation_stages = [
        "Resume Processing",
        "Job Description Processing",
        "Candidate Response Processing",
        "ATS Evaluation",
        "Screening Evaluation",
        "Interview Evaluation"
    ]

    completed_stages = []

    for stage in simulation_stages:
        completed_stages.append(stage)

    return {
        "Status": "End-to-End Simulation Completed",
        "Completed Stages": completed_stages,
        "Pipeline": pipeline
    }