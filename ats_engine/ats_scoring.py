def extract_keywords(text):

    words = text.lower().split()

    keywords = []

    for word in words:

        word = word.strip(".,!?():;[]{}")

        if len(word) > 2:
            keywords.append(word)

    return list(set(keywords))


def calculate_ats_score(resume_text, jd_text):

    resume_keywords = extract_keywords(resume_text)

    jd_keywords = extract_keywords(jd_text)

    matched_keywords = []

    missing_keywords = []

    for keyword in jd_keywords:

        if keyword in resume_keywords:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    total_keywords = len(jd_keywords)

    if total_keywords == 0:
        score = 0
    else:
        score = (len(matched_keywords) / total_keywords) * 100

    return {
        "score": round(score, 2),
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "total_matches": len(matched_keywords)
    }