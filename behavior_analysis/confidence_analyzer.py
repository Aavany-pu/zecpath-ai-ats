def analyze_confidence(transcript):

    transcript = transcript.lower()

    hesitation_words = [

        "um",

        "uh",

        "maybe",

        "probably",

        "i think"

    ]

    hesitation_count = 0

    for word in hesitation_words:

        hesitation_count += transcript.count(
            word
        )

    total_words = len(
        transcript.split()
    )

    confidence_score = max(

        0,

        100 - (hesitation_count * 10)

    )

    return {

        "hesitations":

        hesitation_count,

        "word_count":

        total_words,

        "confidence_score":

        confidence_score

    }