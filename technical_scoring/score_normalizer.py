def load_normalization_factors(file_path):
    factors = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            difficulty, factor = line.split(":", 1)

            try:
                factors[difficulty.strip()] = float(
                    factor.strip()
                )
            except ValueError:
                continue

    return factors


def normalize_score(
    score,
    difficulty,
    file_path
):
    factors = load_normalization_factors(
        file_path
    )

    matched_difficulty = None

    for available_difficulty in factors:
        if (
            available_difficulty.lower()
            == difficulty.strip().lower()
        ):
            matched_difficulty = available_difficulty
            break

    if matched_difficulty is None:
        return {
            "Status": "Normalization Factor Not Found",
            "Difficulty": difficulty,
            "Original Score": score,
            "Normalized Score": None
        }

    factor = factors[matched_difficulty]

    normalized_score = score * factor

    return {
        "Status": "Score Normalized",
        "Difficulty": matched_difficulty,
        "Original Score": score,
        "Normalization Factor": factor,
        "Normalized Score": round(
            normalized_score,
            2
        )
    }