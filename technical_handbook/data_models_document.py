def create_data_models_document():
    data_models = [
        {
            "Model": "Candidate Profile",
            "Purpose": "Stores extracted candidate information"
        },
        {
            "Model": "ATS Evaluation",
            "Purpose": "Stores resume and job requirement evaluation results"
        },
        {
            "Model": "Screening Evaluation",
            "Purpose": "Stores candidate screening results"
        },
        {
            "Model": "Interview Evaluation",
            "Purpose": "Stores HR and technical interview results"
        },
        {
            "Model": "Behavioral Evaluation",
            "Purpose": "Stores configured behavioral analysis results"
        },
        {
            "Model": "Integrity Evaluation",
            "Purpose": "Stores configured integrity evaluation results"
        },
        {
            "Model": "Unified Evaluation",
            "Purpose": "Stores combined evaluation results"
        },
        {
            "Model": "Final Recommendation",
            "Purpose": "Stores the final recommendation output"
        },
        {
            "Model": "Hiring Intelligence Report",
            "Purpose": "Stores the consolidated candidate evaluation report"
        }
    ]

    return {
        "Status": "Data Models Documentation Created",
        "Data Models": data_models
    }