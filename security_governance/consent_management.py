def load_consent_configuration(file_path):
    configuration = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            configuration[key.strip()] = value.strip()

    return configuration


def verify_consent(consent_status):
    if consent_status is True:
        return {
            "Status": "Consent Verified",
            "Processing Allowed": True
        }

    return {
        "Status": "Consent Not Verified",
        "Processing Allowed": False
    }


def evaluate_consent_policy(configuration, consent_status):
    consent_result = verify_consent(consent_status)

    return {
        "Status": "Consent Policy Evaluated",
        "Configuration": configuration,
        "Consent Result": consent_result
    }