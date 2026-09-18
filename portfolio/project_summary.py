from pathlib import Path


def generate_project_summary(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Project Summary": {}
        }

    directories = []

    excluded = {
        "__pycache__",
        ".git",
        ".venv",
        "venv"
    }

    for item in sorted(project_root.iterdir()):
        if item.is_dir() and item.name not in excluded:
            directories.append(item.name)

    python_files = list(project_root.rglob("*.py"))

    summary = {
        "Project Name": project_root.name,
        "Project Location": str(project_root),
        "Project Directories": directories,
        "Python File Count": len(python_files)
    }

    return {
        "Status": "Project Summary Generated",
        "Project Summary": summary
    }