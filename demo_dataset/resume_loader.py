import os


def load_existing_resumes(resume_folder):
    resumes = []

    if not os.path.exists(resume_folder):
        return {
            "Status": "Resume Folder Not Found",
            "Resume Count": 0,
            "Resumes": []
        }

    for file_name in sorted(os.listdir(resume_folder)):
        file_path = os.path.join(resume_folder, file_name)

        if not os.path.isfile(file_path):
            continue

        if file_name.lower().endswith(".pdf"):
            resumes.append({
                "File Name": file_name,
                "File Path": file_path
            })

    if not resumes:
        return {
            "Status": "No PDF Resumes Found",
            "Resume Count": 0,
            "Resumes": []
        }

    return {
        "Status": "Existing Resumes Loaded",
        "Resume Count": len(resumes),
        "Resumes": resumes
    }