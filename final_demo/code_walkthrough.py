from pathlib import Path


def generate_code_walkthrough(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Walkthrough": []
        }

    walkthrough = []

    important_areas = [
        "frontend",
        "ats_engine",
        "screening",
        "hr_scoring_engine",
        "final_demo",
        "technical_handbook",
        "final_optimization"
    ]

    for area in important_areas:
        area_path = project_root / area

        if area_path.exists():
            python_files = list(area_path.rglob("*.py"))

            walkthrough.append({
                "Module": area,
                "Python Files": len(python_files),
                "Location": str(area_path)
            })

    return {
        "Status": "Code Walkthrough Generated",
        "Walkthrough": walkthrough
    }