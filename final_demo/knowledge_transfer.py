from pathlib import Path


def generate_knowledge_transfer(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Knowledge Transfer": {}
        }

    system_areas = []

    for item in sorted(project_root.iterdir()):
        if item.is_dir() and item.name != "__pycache__":
            system_areas.append(item.name)

    return {
        "Status": "Knowledge Transfer Summary Generated",
        "Knowledge Transfer": {
            "System": project_root.name,
            "System Areas": system_areas,
            "Code Walkthrough": "Project modules can be reviewed from the repository",
            "System Explanation": "System workflow can be explained from the implemented modules"
        }
    }