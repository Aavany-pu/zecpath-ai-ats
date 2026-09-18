from interview_summary.summary_template import generate_summary_template


def simulate_interview_sessions():

    summary = generate_summary_template()

    sessions = []

    for item in summary:

        sessions.append({

            "Session ID": item["Question ID"],

            "Question": item["Question"],

            "Interview Status": "Completed"

        })

    return sessions