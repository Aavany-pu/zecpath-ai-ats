import os


def load_existing_candidate_responses(response_folder):
    candidate_responses = []

    if not os.path.exists(response_folder):
        return {
            "Status": "Candidate Response Folder Not Found",
            "Response Count": 0,
            "Responses": []
        }

    for file_name in sorted(os.listdir(response_folder)):
        file_path = os.path.join(
            response_folder,
            file_name
        )

        if not os.path.isfile(file_path):
            continue

        if file_name.lower().endswith(
            (".txt", ".json", ".csv", ".pdf", ".docx")
        ):
            candidate_responses.append({
                "File Name": file_name,
                "File Path": file_path
            })

    if not candidate_responses:
        return {
            "Status": "No Candidate Responses Found",
            "Response Count": 0,
            "Responses": []
        }

    return {
        "Status": "Existing Candidate Responses Loaded",
        "Response Count": len(candidate_responses),
        "Responses": candidate_responses
    }