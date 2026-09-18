import os


def compile_codebase(root_directory="."):
    python_files = []

    for root, directories, files in os.walk(root_directory):
        directories[:] = [
            directory
            for directory in directories
            if directory not in {
                "__pycache__",
                ".git",
                ".venv",
                "venv"
            }
        ]

        for file in files:
            if file.endswith(".py"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(
                    full_path,
                    root_directory
                )

                python_files.append(relative_path)

    python_files.sort()

    return {
        "Status": (
            "Codebase Compilation Completed"
            if python_files
            else "No Python Files Found"
        ),
        "Python Files": python_files,
        "Total Python Files": len(python_files)
    }