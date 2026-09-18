def create_technical_interview_blueprint(
    structure,
    experience_result,
    role_result,
    progression_result,
    flow
):
    return {
        "Interview Structure": structure,
        "Experience Level": experience_result,
        "Role Mapping": role_result,
        "Question Progression": progression_result,
        "Interview Flow": flow
    }