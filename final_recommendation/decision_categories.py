def load_decision_categories(file_path):
    categories = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            categories.append(line)

    return categories


def get_decision_categories(file_path):
    categories = load_decision_categories(file_path)

    if not categories:
        return {
            "Status": "No Decision Categories Found",
            "Categories": []
        }

    return {
        "Status": "Decision Categories Loaded",
        "Categories": categories
    }