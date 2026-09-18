def get_api_schemas():
    schemas = {
        "Resume Parsing API": {
            "Request": {
                "resume_file": "string"
            },
            "Response": {
                "candidate_profile": "object",
                "status": "string"
            }
        },

        "ATS Scoring API": {
            "Request": {
                "candidate_profile": "object",
                "job_requirements": "object"
            },
            "Response": {
                "ats_result": "object",
                "status": "string"
            }
        },

        "Screening AI API": {
            "Request": {
                "candidate_profile": "object",
                "screening_input": "object"
            },
            "Response": {
                "screening_result": "object",
                "status": "string"
            }
        },

        "Interview AI API": {
            "Request": {
                "candidate_profile": "object",
                "interview_data": "object"
            },
            "Response": {
                "interview_result": "object",
                "status": "string"
            }
        },

        "Decision AI API": {
            "Request": {
                "candidate_evaluation": "object"
            },
            "Response": {
                "decision": "string",
                "confidence": "number",
                "status": "string"
            }
        }
    }

    return {
        "Status": "API Schemas Defined",
        "Schemas": schemas
    }