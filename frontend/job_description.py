from pathlib import Path


SUPPORTED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".docx"
}


def find_job_descriptions(job_description_directory):
    job_description_directory = Path(job_description_directory)

    if not job_description_directory.exists():
        return {
            "Status": "Job Description Directory Not Found",
            "Job Descriptions": []
        }

    job_descriptions = []

    for file_path in sorted(job_description_directory.iterdir()):
        if (
            file_path.is_file()
            and file_path.suffix.lower() in SUPPORTED_EXTENSIONS
        ):
            job_descriptions.append(str(file_path))

    return {
        "Status": "Job Descriptions Found",
        "Job Descriptions": job_descriptions
    }