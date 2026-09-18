def generate_followup(answer):

    answer = answer.lower()

    if "python" in answer:

        return "Can you describe one Python project you worked on?"

    elif "sql" in answer:

        return "Can you explain how you used SQL in your previous work?"

    elif "machine learning" in answer:

        return "Which machine learning algorithms have you implemented?"

    elif "django" in answer:

        return "Can you explain your Django project?"

    else:

        return None