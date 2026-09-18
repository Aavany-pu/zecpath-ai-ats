from conversation_flow.conversation_state import ConversationState
from conversation_flow.decision_tree import decide_next_action
from conversation_flow.fallback_handler import fallback_question
from conversation_flow.followup_trigger import generate_followup
from conversation_flow.retry_handler import retry_message
from conversation_flow.repeated_answer import is_repeated

import json

# Read questions generated in Day 22
with open(
    "data/interview_questions/candidate_questions.json",
    "r",
    encoding="utf-8"
) as file:

    questions = json.load(file)


state = ConversationState()

previous_answer = ""


print("=" * 60)
print("DAY 29 - AI CONVERSATION FLOW DESIGN")
print("=" * 60)


for question in questions:

    print()

    print("AI :", question["question"])

    answer = input("Candidate : ")

    if is_repeated(previous_answer, answer):

        print()

        print("AI : It looks like you repeated the same answer.")

        print("AI : Could you explain in more detail?")

        continue

    previous_answer = answer

    action = decide_next_action(answer)

    if action == "SILENCE":

        state.retry()

        message = retry_message(
            state.retry_count
        )

        if message:

            print()

            print("AI :", message)

        continue


    elif action == "CONFUSION":

        print()

        print("AI :", fallback_question())

        continue


    elif action == "SHORT":

        followup = generate_followup(answer)

        if followup:

            print()

            print("AI :", followup)

        else:

            print()

            print("AI : Could you explain a little more?")

    else:

        followup = generate_followup(answer)

        if followup:

            print()

            print("AI :", followup)

    state.next_question()


state.end()

print()

print("=" * 60)

print("Conversation Finished Successfully")

print("Conversation Status :", state.status)

print("=" * 60)