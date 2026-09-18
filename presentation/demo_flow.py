def create_demo_flow():
    flow = [
        "Start the Zecpath AI system",
        "Provide candidate resume data",
        "Process candidate information",
        "Generate ATS scoring output",
        "Perform candidate screening",
        "Evaluate HR interview information",
        "Evaluate technical skill information",
        "Generate decision and recommendation output",
        "Generate hiring intelligence report",
        "Display recruiter-facing output"
    ]

    return {
        "Status": "Demo Flow Prepared",
        "Flow": flow,
        "Total Steps": len(flow)
    }