def load_interview_flow(file_path):
    transitions = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            current_state, next_state = line.split(":", 1)

            transitions[current_state.strip()] = (
                next_state.strip()
            )

    return transitions


def get_next_state(file_path, current_state):
    transitions = load_interview_flow(file_path)

    if current_state not in transitions:
        return {
            "Status": "State Not Found",
            "Current State": current_state,
            "Next State": None
        }

    return {
        "Status": "Transition Found",
        "Current State": current_state,
        "Next State": transitions[current_state]
    }