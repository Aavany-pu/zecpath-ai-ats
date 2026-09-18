def load_consent_requirements(file_path):
    requirements = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line == "Consent Requirements":
                continue

            requirements.append(line)

    return requirements


def check_consent_requirements(file_path):
    requirements = load_consent_requirements(file_path)

    result = {
        "Consent Requirements Found": len(requirements),
        "Requirements": requirements,
        "Status": "Ready for Review"
    }

    return result