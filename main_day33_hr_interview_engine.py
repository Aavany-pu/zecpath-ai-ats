from hr_interview_engine.interview_categories import build_interview_categories
from hr_interview_engine.role_based_question_generator import generate_role_information
from hr_interview_engine.interview_state import build_interview_state
from hr_interview_engine.conversation_phases import build_conversation_phases
from hr_interview_engine.flow_design import build_flow_design


def print_heading(title):

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)


def display(data):

    if isinstance(data, dict):

        for key, value in data.items():

            print(f"\n{key}")

            print("-" * 60)

            print(value)

    elif isinstance(data, list):

        for item in data:

            print(item)

    else:

        print(data)


def main():

    print_heading("DAY 33 - HR INTERVIEW ENGINE DESIGN")


    categories = build_interview_categories()

    print_heading("1. HR INTERVIEW CATEGORIES")

    display(categories)


    role_information = generate_role_information()

    print_heading("2. ROLE BASED INFORMATION")

    display(role_information)


    interview_state = build_interview_state()

    print_heading("3. INTERVIEW STATE")

    display(interview_state)


    phases = build_conversation_phases()

    print_heading("4. CONVERSATION PHASES")

    display(phases)


    flow = build_flow_design()

    print_heading("5. INTERVIEW FLOW DESIGN")

    display(flow)


    print_heading("DAY 33 COMPLETED")


if __name__ == "__main__":

    main()