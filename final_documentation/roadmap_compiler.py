import os


def compile_ai_roadmap(root_directory="."):
    roadmap_files = []

    allowed_extensions = {
        ".pdf",
        ".docx",
        ".txt",
        ".md",
        ".py",
        ".json"
    }

    excluded_directories = {
        "__pycache__",
        ".git",
        ".venv",
        "venv"
    }

    roadmap_keywords = {
        "roadmap",
        "future",
        "innovation",
        "scaling",
        "advanced_feature"
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
                for keyword in roadmap_keywords
            ):
                relative_path = os.path.relpath(
                    os.path.join(root, file),
                    root_directory
                )

                roadmap_files.append(relative_path)

    roadmap_files.sort()

    return {
        "Status": (
            "AI Roadmap Compilation Completed"
            if roadmap_files
            else "No AI Roadmap Files Found"
        ),
        "Roadmap Files": roadmap_files,
        "Total Roadmap Files": len(roadmap_files)
    }