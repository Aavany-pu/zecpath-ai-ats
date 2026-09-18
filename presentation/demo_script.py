def create_demo_script():
    script = [
        {
            "Stage": "Introduction",
            "Action": "Introduce Zecpath AI and explain the recruitment problem."
        },
        {
            "Stage": "Problem",
            "Action": "Explain the challenges involved in processing and evaluating candidate information."
        },
        {
            "Stage": "AI Solution",
            "Action": "Explain how AI supports the recruitment workflow."
        },
        {
            "Stage": "Resume Processing",
            "Action": "Demonstrate candidate resume processing."
        },
        {
            "Stage": "ATS Scoring",
            "Action": "Show the ATS scoring output."
        },
        {
            "Stage": "Screening",
            "Action": "Show the candidate screening output."
        },
        {
            "Stage": "Interview Evaluation",
            "Action": "Demonstrate HR and technical evaluation outputs."
        },
        {
            "Stage": "Decision",
            "Action": "Show the decision and recommendation output."
        },
        {
            "Stage": "Hiring Intelligence",
            "Action": "Show the hiring intelligence report."
        },
        {
            "Stage": "Conclusion",
            "Action": "Summarize the system workflow and business impact."
        }
    ]

    return {
        "Status": "Demo Script Prepared",
        "Script": script,
        "Total Stages": len(script)
    }