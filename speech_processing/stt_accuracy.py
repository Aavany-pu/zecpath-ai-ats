def calculate_accuracy(

    original_text,

    processed_text

):

    original_words = len(
        original_text.split()
    )

    processed_words = len(
        processed_text.split()
    )

    if original_words == 0:

        return 0

    accuracy = (

        processed_words
        /
        original_words

    ) * 100

    return round(
        accuracy,
        2
    )