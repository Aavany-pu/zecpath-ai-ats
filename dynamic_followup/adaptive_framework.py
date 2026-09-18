from dynamic_followup.response_analyzer import analyze_responses
from dynamic_followup.followup_triggers import generate_followup_triggers
from dynamic_followup.difficulty_adapter import adapt_question_difficulty
from dynamic_followup.conversation_tracker import track_conversation
from dynamic_followup.decision_tree import build_decision_tree


def build_adaptive_framework():

    framework = {

        "Response Analysis": analyze_responses(),

        "Follow-up Triggers": generate_followup_triggers(),

        "Difficulty Adaptation": adapt_question_difficulty(),

        "Conversation Tracking": track_conversation(),

        "Decision Tree": build_decision_tree()

    }

    return framework