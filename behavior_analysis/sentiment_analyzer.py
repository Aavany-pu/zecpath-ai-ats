def analyze_sentiment(transcript):

    transcript = transcript.lower()

    positive = [

        "confident",

        "experienced",

        "success",

        "completed",

        "developed"

    ]

    negative = [

        "difficult",

        "problem",

        "failed",

        "unable"

    ]

    positive_count = 0

    negative_count = 0

    for word in positive:

        positive_count += transcript.count(
            word
        )

    for word in negative:

        negative_count += transcript.count(
            word
        )

    if positive_count > negative_count:

        sentiment = "Positive"

    elif negative_count > positive_count:

        sentiment = "Negative"

    else:

        sentiment = "Neutral"

    return {

        "positive_words":

        positive_count,

        "negative_words":

        negative_count,

        "sentiment":

        sentiment

    }