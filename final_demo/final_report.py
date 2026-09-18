from pathlib import Path


def generate_final_report(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Final Report": {}
        }

    report_files = []

    report_extensions = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
        ".json",
        ".csv"
    }

    report_keywords = {
        "report",
        "review",
        "analysis",
        "validation",
        "feedback",
        "result"
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

        if file_path.suffix.lower() not in report_extensions:
            continue

        if any(
            keyword in file_path.name.lower()
            for keyword in report_keywords
        ):
            report_files.append(
                str(file_path.relative_to(project_root))
            )

    report_files = sorted(set(report_files))

    return {
        "Status": "Final Report Generated",
        "Final Report": {
            "Project": project_root.name,
            "Report Files": report_files,
            "Report Count": len(report_files)
        }
    }