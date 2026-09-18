import re

def detect_language_mix(transcript_path):

    with open(transcript_path, "r", encoding="utf-8") as file:
        text = file.read()

    english_words = 0
    non_english_words = 0

    words = text.split()

    for word in words:

        # Remove punctuation
        word = re.sub(r"[^\w\u0D00-\u0D7F]", "", word)

        if word.lower() in ["question", "answer"]:
            continue

        # English words
        elif re.fullmatch(r"[A-Za-z0-9]+", word):
            english_words += 1

        # Malayalam Unicode block
        elif re.search(r"[\u0D00-\u0D7F]", word):
            non_english_words += 1

    if non_english_words > 0:
        language = "MIXED"
        mixed_language = True
    else:
        language = "ENGLISH"
        mixed_language = False

    return {
        "language": language,
        "mixed_language": mixed_language,
        "english_words": english_words,
        "non_english_words": non_english_words
    }