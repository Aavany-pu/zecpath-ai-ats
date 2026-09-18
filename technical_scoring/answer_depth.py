def detect_answer_depth(answer):
    if not isinstance(answer, str):
        return {
            "Status": "Invalid Answer",
            "Answer Depth": "Unknown",
            "Word Count": 0
        }

    cleaned_answer = answer.strip()

    if not cleaned_answer:
        return {
            "Status": "Empty Answer",
            "Answer Depth": "No Answer",
            "Word Count": 0
        }

    words = cleaned_answer.split()
    word_count = len(words)

    sentences = [
        sentence.strip()
        for sentence in cleaned_answer.split(".")
        if sentence.strip()
    ]

    explanation_indicators = [
        "because",
        "therefore",
        "for example",
        "for instance",
        "however",
        "so that",
        "as a result"
    ]

    explanation_count = sum(
        1
        for indicator in explanation_indicators
        if indicator in cleaned_answer.lower()
    )

    if word_count < 20 and explanation_count == 0:
        depth = "Shallow"

    elif word_count >= 50 and explanation_count >= 1:
        depth = "Deep"

    else:
        depth = "Moderate"

    return {
        "Status": "Answer Analyzed",
        "Answer Depth": depth,
        "Word Count": word_count,
        "Sentence Count": len(sentences),
        "Explanation Indicators": explanation_count
    }