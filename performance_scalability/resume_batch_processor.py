def process_resume_batch(resumes, batch_size):
    if not resumes:
        return {
            "Status": "No Resumes Available",
            "Processed Resumes": []
        }

    if batch_size <= 0:
        return {
            "Status": "Invalid Batch Size",
            "Processed Resumes": []
        }

    processed_resumes = []

    for start_index in range(0, len(resumes), batch_size):
        batch = resumes[start_index:start_index + batch_size]

        for resume in batch:
            processed_resumes.append(resume)

    return {
        "Status": "Resume Batch Processing Completed",
        "Total Resumes": len(resumes),
        "Batch Size": batch_size,
        "Processed Resumes": processed_resumes
    }