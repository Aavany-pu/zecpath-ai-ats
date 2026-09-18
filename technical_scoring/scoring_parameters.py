def load_scoring_parameters(file_path):
    parameters = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parameters.append(line)

    return parameters


def get_scoring_parameters(file_path):
    parameters = load_scoring_parameters(file_path)

    if not parameters:
        return {
            "Status": "No Scoring Parameters Found",
            "Parameters": []
        }

    return {
        "Status": "Scoring Parameters Loaded",
        "Parameters": parameters
    }