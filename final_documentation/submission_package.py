from pathlib import Path


def create_submission_package(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Submission Package": {}
        }

    package = {
        "Codebase": [],
        "Documentation": [],
        "Reports": [],
        "AI Roadmap": [],
        "Portfolio": []
    }

    excluded = {
        "__pycache__",
        ".git",
        ".venv",
        "venv"
    }

    for file_path in project_root.rglob("*"):
        if not file_path.is_file():
            continue

        if any(part in excluded for part in file_path.parts):
            continue

        relative_path = file_path.relative_to(project_root)

        if file_path.suffix.lower() == ".py":
            package["Codebase"].append(str(relative_path))

        elif file_path.suffix.lower() in {".md", ".pdf", ".txt", ".docx"}:
            package["Documentation"].append(str(relative_path))

        if any(
            keyword in file_path.name.lower()
            for keyword in {
                "report",
                "review",
                "analysis",
                "validation",
                "benchmark",
                "performance",
                "feedback"
            }
        ):
            package["Reports"].append(str(relative_path))

        if any(
            keyword in file_path.name.lower()
            for keyword in {
                "roadmap",
                "future",
                "innovation",
                "scaling",
                "advanced_feature"
            }
        ):
            package["AI Roadmap"].append(str(relative_path))

        if "portfolio" in file_path.parts:
            package["Portfolio"].append(str(relative_path))

    for category in package:
        package[category] = sorted(set(package[category]))

    return {
        "Status": "Submission Package Compiled",
        "Submission Package": package
    }