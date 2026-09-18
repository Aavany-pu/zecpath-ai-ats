from dynamic_followup.conversation_tracker import track_conversation


def build_decision_tree():

    conversation = track_conversation()

    decision_tree = []

    for item in conversation:

        difficulty = item["Difficulty Level"]
        status = item["Conversation Status"]

        if status == "Repeated":

            action = "Skip Question"

        elif difficulty == "Easy":

            action = "Ask Clarification"

        elif difficulty == "Medium":

            action = "Ask Deep Follow-up"

        else:

            action = "Ask Scenario-Based Question"

        decision_tree.append({

            "Question ID": item["Question ID"],

            "Question": item["Question"],

            "Difficulty Level": difficulty,

            "Conversation Status": status,

            "Decision": action,

            "Next Question": item["Adaptive Question"]

        })

    return decision_tree