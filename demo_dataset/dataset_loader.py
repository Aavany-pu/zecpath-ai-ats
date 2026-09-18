import os


def load_demo_dataset(base_path):
    dataset = {}

    folders = [
        "resumes",
        "job_descriptions",
        "candidate_responses",
        "ats_results",
        "screening_outputs",
        "interview_responses"
    ]

    for folder in folders:
        folder_path = os.path.join(base_path, folder)

        if not os.path.exists(folder_path):
            dataset[folder] = {
                "Status": "Folder Not Found",
                "Files": []
            }
            continue

        files = []

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                files.append(file_name)

        dataset[folder] = {
            "Status": "Loaded",
            "Files": files
        }

    return {
        "Status": "Demo Dataset Loaded",
        "Dataset": dataset
    }