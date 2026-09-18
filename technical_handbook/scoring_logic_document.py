def create_scoring_logic_document():
    scoring_modules = [
        {
            "Module": "ATS Scoring",
            "Purpose": "Evaluate candidate resumes against job requirements"
        },
        {
            "Module": "Screening Scoring",
            "Purpose": "Evaluate candidate screening responses"
        },
        {
            "Module": "HR Scoring",
            "Purpose": "Evaluate HR interview performance"
        },
        {
            "Module": "Technical Skill Scoring",
            "Purpose": "Evaluate technical interview performance"
        },
        {
            "Module": "Behavioral Scoring",
            "Purpose": "Evaluate configured behavioral signals"
        },
        {
            "Module": "Integrity Evaluation",
            "Purpose": "Evaluate configured interview integrity signals"
        },
        {
            "Module": "Unified Scoring",
            "Purpose": "Combine available evaluation results"
        },
        {
            "Module": "Final Recommendation",
            "Purpose": "Generate the configured final hiring recommendation"
        }
    ]

    return {
        "Status": "Scoring Logic Documentation Created",
        "Scoring Modules": scoring_modules
    }