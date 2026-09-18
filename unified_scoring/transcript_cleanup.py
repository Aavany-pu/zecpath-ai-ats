import re


def clean_transcript(transcript):

    cleaned = transcript.strip()

    cleaned = re.sub(
        r"\s+",
        " ",
        cleaned
    )

    cleaned = re.sub(
        r"[ \t]+([,.!?])",
        r"\1",
        cleaned
    )

    cleaned = re.sub(
        r"([,.!?]){2,}",
        r"\1",
        cleaned
    )

    return cleaned.strip()