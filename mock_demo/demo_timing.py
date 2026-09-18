def create_demo_timing(demo_stages):
    if demo_stages is None:
        return {
            "Status": "No Demo Stages Available",
            "Timing Plan": []
        }

    if not isinstance(demo_stages, list):
        return {
            "Status": "Invalid Demo Stage Data",
            "Timing Plan": []
        }

    timing_plan = []

    for index, stage in enumerate(demo_stages, start=1):
        timing_plan.append({
            "Stage": index,
            "Name": str(stage).strip()
        })

    return {
        "Status": "Demo Timing Plan Prepared",
        "Timing Plan": timing_plan,
        "Total Stages": len(timing_plan)
    }