def load_role_weights(file_path):

    weights = {}

    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        for line in file:

            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(
                ":",
                1
            )

            key = key.strip()
            value = value.strip()

            if key == "Role":
                weights[key] = value
            else:
                weights[key] = float(value)

    return weights


def get_role_weights(file_path):

    return load_role_weights(
        file_path
    )