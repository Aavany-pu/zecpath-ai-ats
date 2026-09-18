import os


def compile_documentation(root_directory="."):
    documentation_files = []

    allowed_extensions = {
        ".md",
        ".pdf",
        ".txt",
        ".docx"
    }

    excluded_directories = {
        "__pycache__",
        ".git",
        ".venv",
        "venv"
    }

    for root, directories, files in os.walk(root_directory):
        directories[:] = [
            directory
            for directory in directories
            if directory not in excluded_directories
        ]

        for file in files:
            extension = os.path.splitext(file)[1].lower()

            if extension in allowed_extensions:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(
                    full_path,
                    root_directory
                )

                documentation_files.append(relative_path)

    documentation_files.sort()

    return {
        "Status": (
            "Documentation Compilation Completed"
            if documentation_files
            else "No Documentation Files Found"
        ),
        "Documentation Files": documentation_files,
        "Total Documentation Files": len(documentation_files)
    }