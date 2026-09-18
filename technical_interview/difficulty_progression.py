def load_difficulty_progression(file_path):
    progression = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            difficulty, stages = line.split(":", 1)

            difficulty = difficulty.strip()

            stage_list = [
                stage.strip()
                for stage in stages.split(",")
                if stage.strip()
            ]

            progression[difficulty] = stage_list

    return progression


def get_difficulty_progression(file_path, difficulty):
    progression = load_difficulty_progression(file_path)

    matched_difficulty = None

    for available_difficulty in progression:
        if (
            available_difficulty.lower()
            == difficulty.strip().lower()
        ):
            matched_difficulty = available_difficulty
            break

    if matched_difficulty is None:
        return {
            "Status": "Difficulty Not Found",
            "Difficulty": difficulty,
            "Progression": []
        }

    return {
        "Status": "Progression Found",
        "Difficulty": matched_difficulty,
        "Progression": progression[matched_difficulty]
    }