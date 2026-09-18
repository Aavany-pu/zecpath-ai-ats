from hr_interview_engine.interview_categories import build_interview_categories
from hr_interview_engine.role_based_question_generator import generate_role_information
from hr_interview_engine.interview_state import build_interview_state
from hr_interview_engine.conversation_phases import build_conversation_phases


def build_flow_design():

    flow = {

        "Interview Categories": build_interview_categories(),

        "Role Information": generate_role_information(),

        "Interview State": build_interview_state(),

        "Conversation Phases": build_conversation_phases()

    }

    return flow