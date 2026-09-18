import os


def compile_reports(root_directory="."):
    report_files = []

    allowed_extensions = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
        ".json",
        ".csv"
    }

    excluded_directories = {
        "__pycache__",
        ".git",
        ".venv",
        "venv"
    }

    report_keywords = {
        "report",
        "review",
        "analysis",
        "validation",
        "benchmark",
        "performance",
        "feedback",
        "result"
    }

    for root, directories, files in os.walk(root_directory):
        directories[:] = [
            directory
            for directory in directories
            if directory not in excluded_directories
        ]

        for file in files:
            extension = os.path.splitext(file)[1].lower()
            filename = file.lower()

            if extension not in allowed_extensions:
                continue

            if any(
                keyword in filename
                for keyword in report_keywords
            ):
                relative_path = os.path.relpath(
                    os.path.join(root, file),
                    root_directory
                )

                report_files.append(relative_path)

    report_files.sort()

    return {
        "Status": (
            "Report Compilation Completed"
            if report_files
            else "No Report Files Found"
        ),
        "Report Files": report_files,
        "Total Reports": len(report_files)
    }