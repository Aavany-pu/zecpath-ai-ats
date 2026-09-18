from pathlib import Path


def find_resume_files(resume_directory):
    resume_directory = Path(resume_directory)

    if not resume_directory.exists():
        return {
            "Status": "Resume Directory Not Found",
            "Resume Files": []
        }

    resume_files = []

    for file_path in sorted(resume_directory.iterdir()):
        if file_path.is_file() and file_path.suffix.lower() == ".pdf":
            resume_files.append(str(file_path))

    return {
        "Status": "Resume Files Found",
        "Resume Files": resume_files
    }