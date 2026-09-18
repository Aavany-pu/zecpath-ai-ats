def run_interview_demo(transcript_path):
    with open(transcript_path, "r", encoding="utf-8") as file:
        transcript = file.read().strip()

    if not transcript:
        return {
            "Status": "No Interview Data",
            "Transcript": ""
        }

    return {
        "Status": "Interview Loaded",
        "Transcript": transcript
    }