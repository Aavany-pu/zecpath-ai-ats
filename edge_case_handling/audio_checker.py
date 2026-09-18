import os


def check_audio_quality(transcript_path):

    result = {

        "audio_available": False,

        "quality": "UNKNOWN",

        "reason": ""

    }

    if not os.path.exists(transcript_path):

        result["reason"] = "Transcript file not found."

        return result

    with open(

        transcript_path,

        "r",

        encoding="utf-8"

    ) as file:

        transcript = file.read().strip()

    if transcript == "":

        result["reason"] = "Transcript is empty."

        return result

    result["audio_available"] = True

    word_count = len(transcript.split())

    if word_count < 20:

        result["quality"] = "POOR"

    elif word_count < 100:

        result["quality"] = "AVERAGE"

    else:

        result["quality"] = "GOOD"

    return result