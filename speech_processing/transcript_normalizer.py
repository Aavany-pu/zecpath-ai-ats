def normalize_transcript(text):

    text = text.lower()

    text = text.strip()

    text = text.replace(
        "  ",
        " "
    )

    return text