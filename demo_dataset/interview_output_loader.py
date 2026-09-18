import os


def load_existing_interview_outputs(interview_folders):
    interview_outputs = {}

    for interview_type, folder_path in interview_folders.items():

        if not os.path.exists(folder_path):
            interview_outputs[interview_type] = {
                "Status": "Interview Output Folder Not Found",
                "Output Count": 0,
                "Outputs": []
            }
            continue

        outputs = []

        for file_name in sorted(os.listdir(folder_path)):
            file_path = os.path.join(
                folder_path,
                file_name
            )

            if not os.path.isfile(file_path):
                continue

            if file_name.lower().endswith(
                (".txt", ".json", ".csv")
            ):
                outputs.append({
                    "File Name": file_name,
                    "File Path": file_path
                })

        if outputs:
            status = "Existing Interview Outputs Loaded"
        else:
            status = "No Interview Outputs Found"

        interview_outputs[interview_type] = {
            "Status": status,
            "Output Count": len(outputs),
            "Outputs": outputs
        }

    return {
        "Status": "Interview Output Dataset Checked",
        "Interview Outputs": interview_outputs
    }