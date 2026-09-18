from dynamic_followup.response_analyzer import analyze_responses
from dynamic_followup.followup_triggers import generate_followup_triggers
from dynamic_followup.difficulty_adapter import adapt_question_difficulty
from dynamic_followup.conversation_tracker import track_conversation
from dynamic_followup.decision_tree import build_decision_tree
from dynamic_followup.adaptive_framework import build_adaptive_framework


print("\nDAY 34 - DYNAMIC FOLLOW-UP LOGIC\n")


print("=" * 70)
print("1. RESPONSE ANALYSIS")
print("=" * 70)

for item in analyze_responses():
    print("-" * 60)
    for key, value in item.items():
        print(f"{key:<25}: {value}")

print("-" * 60)


print("\n" + "=" * 70)
print("2. FOLLOW-UP TRIGGERS")
print("=" * 70)

for item in generate_followup_triggers():
    print("-" * 60)
    for key, value in item.items():
        print(f"{key:<25}: {value}")

print("-" * 60)


print("\n" + "=" * 70)
print("3. DIFFICULTY ADAPTATION")
print("=" * 70)

for item in adapt_question_difficulty():
    print("-" * 60)
    for key, value in item.items():
        print(f"{key:<25}: {value}")

print("-" * 60)


print("\n" + "=" * 70)
print("4. CONVERSATION TRACKING")
print("=" * 70)

for item in track_conversation():
    print("-" * 60)
    for key, value in item.items():
        print(f"{key:<25}: {value}")

print("-" * 60)


print("\n" + "=" * 70)
print("5. DECISION TREE")
print("=" * 70)

for item in build_decision_tree():
    print("-" * 60)
    for key, value in item.items():
        print(f"{key:<25}: {value}")

print("-" * 60)


print("\n" + "=" * 70)
print("6. ADAPTIVE QUESTIONING FRAMEWORK")
print("=" * 70)

framework = build_adaptive_framework()

for key, value in framework.items():
    print(f"\n{key}")
    print("-" * 50)
    print(value)


print("\n" + "=" * 70)
print("DAY 34 COMPLETED SUCCESSFULLY")
print("=" * 70)