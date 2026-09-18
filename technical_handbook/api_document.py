def create_api_document():
    api_documentation = [
        {
            "API": "Resume Parsing API",
            "Purpose": "Resume processing and candidate information extraction"
        },
        {
            "API": "ATS Scoring API",
            "Purpose": "Candidate resume evaluation against job requirements"
        },
        {
            "API": "Screening AI API",
            "Purpose": "Candidate screening evaluation"
        },
        {
            "API": "Interview AI API",
            "Purpose": "Interview processing and evaluation"
        },
        {
            "API": "Decision AI API",
            "Purpose": "Final candidate decision processing"
        }
    ]

    return {
        "Status": "API Documentation Created",
        "APIs": api_documentation
    }