def clean_transcript(text):

    filler_words = [

        "um",

        "uh",

        "okay",

        "like"
    ]

    words = text.split()

    cleaned_words = []

    for word in words:

        if word.lower() not in filler_words:

            cleaned_words.append(
                word
            )

    return " ".join(
        cleaned_words
    )