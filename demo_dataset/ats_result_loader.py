import os


def load_existing_ats_results(ats_folder):
    ats_results = []

    if not os.path.exists(ats_folder):
        return {
            "Status": "ATS Results Folder Not Found",
            "Result Count": 0,
            "Results": []
        }

    for file_name in sorted(os.listdir(ats_folder)):
        file_path = os.path.join(
            ats_folder,
            file_name
        )

        if not os.path.isfile(file_path):
            continue

        if file_name.lower().endswith(
            (".txt", ".json", ".csv")
        ):
            ats_results.append({
                "File Name": file_name,
                "File Path": file_path
            })

    if not ats_results:
        return {
            "Status": "No ATS Results Found",
            "Result Count": 0,
            "Results": []
        }

    return {
        "Status": "Existing ATS Results Loaded",
        "Result Count": len(ats_results),
        "Results": ats_results
    }