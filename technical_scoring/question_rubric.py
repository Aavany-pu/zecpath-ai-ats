def load_question_rubrics(file_path):
    rubrics = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            question_type, parameters = line.split(":", 1)

            parameter_list = [
                parameter.strip()
                for parameter in parameters.split(",")
                if parameter.strip()
            ]

            rubrics[question_type.strip()] = parameter_list

    return rubrics


def get_question_rubric(file_path, question_type):
    rubrics = load_question_rubrics(file_path)

    for available_type in rubrics:
        if available_type.lower() == question_type.strip().lower():
            return {
                "Status": "Rubric Found",
                "Question Type": available_type,
                "Parameters": rubrics[available_type]
            }

    return {
        "Status": "Rubric Not Found",
        "Question Type": question_type,
        "Parameters": []
    }