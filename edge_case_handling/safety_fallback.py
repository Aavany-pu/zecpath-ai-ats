def get_fallback_response(issue):

    issue = issue.lower()

    fallback_messages = {

        "poor_audio": "The audio quality is poor. Please speak clearly and try again.",

        "missing_answer": "No answer was detected. Could you please answer the question again?",

        "language_mix": "Multiple languages were detected. Please answer in one language if possible.",

        "background_noise": "Background noise was detected. Please move to a quieter place and continue.",

        "unknown": "I'm sorry, I couldn't understand your response. Let's continue with the next question."

    }

    return fallback_messages.get(

        issue,

        fallback_messages["unknown"]

    )


def build_safety_report(

        audio_result,

        language_result,

        missing_result

):

    report = {

        "audio_status": audio_result,

        "language_status": language_result,

        "missing_answer_status": missing_result,

        "system_safe": True

    }

    if (

        audio_result["quality"] == "POOR"

        or

        language_result["mixed_language"]

        or

        missing_result["retry_required"]

    ):

        report["system_safe"] = False

    return report