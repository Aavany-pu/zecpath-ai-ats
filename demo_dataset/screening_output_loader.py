import os


def load_existing_screening_outputs(screening_folder):
    screening_outputs = []

    if not os.path.exists(screening_folder):
        return {
            "Status": "Screening Output Folder Not Found",
            "Output Count": 0,
            "Outputs": []
        }

    for file_name in sorted(os.listdir(screening_folder)):
        file_path = os.path.join(
            screening_folder,
            file_name
        )

        if not os.path.isfile(file_path):
            continue

        if file_name.lower().endswith(
            (".txt", ".json", ".csv")
        ):
            screening_outputs.append({
                "File Name": file_name,
                "File Path": file_path
            })

    if not screening_outputs:
        return {
            "Status": "No Screening Outputs Found",
            "Output Count": 0,
            "Outputs": []
        }

    return {
        "Status": "Existing Screening Outputs Loaded",
        "Output Count": len(screening_outputs),
        "Outputs": screening_outputs
    }