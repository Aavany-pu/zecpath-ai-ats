from pathlib import Path


def generate_skills_summary(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Skills Summary": []
        }

    skills = []

    skill_sources = {
        "ats_engine": "ATS and resume scoring",
        "screening": "Candidate screening",
        "hr_scoring_engine": "HR interview evaluation",
        "technical": "Technical skill evaluation",
        "decision": "Decision and recommendation processing",
        "presentation": "AI system presentation preparation",
        "mock_demo": "Demo and stakeholder walkthrough",
        "feature_enhancements": "Feature enhancement and output refinement",
        "final_optimization": "Final optimization and validation",
        "technical_handbook": "Technical documentation"
    }

    existing_directories = {
        item.name.lower()
        for item in project_root.iterdir()
        if item.is_dir()
    }

    for directory, description in skill_sources.items():
        if directory.lower() in existing_directories:
            skills.append({
                "Area": directory,
                "Description": description
            })

    return {
        "Status": "Skills Summary Generated",
        "Skills Summary": skills
    }