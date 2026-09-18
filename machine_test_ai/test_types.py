def load_test_types(file_path):
    test_types = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            test_types.append(line)

    return test_types


def get_test_types(file_path):
    test_types = load_test_types(file_path)

    if not test_types:
        return {
            "Status": "No Machine Test Types Found",
            "Test Types": []
        }

    return {
        "Status": "Machine Test Types Loaded",
        "Test Types": test_types
    }