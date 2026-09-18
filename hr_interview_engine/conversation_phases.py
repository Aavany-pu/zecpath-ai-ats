from hr_interview_engine.interview_state import build_interview_state


def build_conversation_phases():

    interview_state = build_interview_state()

    phases = {

        "Introduction": [],

        "Core HR Questions": [],

        "Role-Based Evaluation": [],

        "Closing": []

    }

    total_questions = len(interview_state)

    for interview in interview_state:

        question_id = interview["Question ID"]

        if question_id == 1:

            phases["Introduction"].append(interview)

        elif question_id < total_questions:

            phases["Core HR Questions"].append(interview)

        else:

            phases["Closing"].append(interview)

    return phases