import os


def load_existing_job_descriptions(job_description_folder):
    job_descriptions = []

    if not os.path.exists(job_description_folder):
        return {
            "Status": "Job Description Folder Not Found",
            "Job Description Count": 0,
            "Job Descriptions": []
        }

    for file_name in sorted(os.listdir(job_description_folder)):
        file_path = os.path.join(
            job_description_folder,
            file_name
        )

        if not os.path.isfile(file_path):
            continue

        if file_name.lower().endswith((".txt", ".pdf", ".docx")):
            job_descriptions.append({
                "File Name": file_name,
                "File Path": file_path
            })

    if not job_descriptions:
        return {
            "Status": "No Job Descriptions Found",
            "Job Description Count": 0,
            "Job Descriptions": []
        }

    return {
        "Status": "Existing Job Descriptions Loaded",
        "Job Description Count": len(job_descriptions),
        "Job Descriptions": job_descriptions
    }