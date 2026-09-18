def load_retention_policy(file_path):
    policy = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line == "Data Retention Policy":
                continue

            policy.append(line)

    return policy


def review_data_retention(file_path):
    policy = load_retention_policy(file_path)

    review_required = []

    for item in policy:
        if "Review Required" in item:
            review_required.append(item)

    if review_required:
        status = "Compliance Review Required"
    else:
        status = "Retention Policy Available"

    return {
        "Status": status,
        "Policy Items": policy,
        "Review Required Items": review_required
    }