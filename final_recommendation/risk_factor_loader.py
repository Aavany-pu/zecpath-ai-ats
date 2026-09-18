def load_risk_factors(file_path):
    risk_factors = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            risk_factors[key.strip()] = value.strip()

    return risk_factors


def create_risk_factor_framework(file_path):
    risk_factors = load_risk_factors(file_path)

    return {
        "Status": "Risk Factor Framework Configured",
        "Behavior Risk Source": risk_factors.get(
            "Behavior Risk Source",
            ""
        ),
        "Integrity Risk Source": risk_factors.get(
            "Integrity Risk Source",
            ""
        ),
        "Behavior Risk Status": risk_factors.get(
            "Behavior Risk Status",
            ""
        ),
        "Integrity Risk Status": risk_factors.get(
            "Integrity Risk Status",
            ""
        ),
        "Risk Evaluation": risk_factors.get(
            "Risk Evaluation",
            ""
        )
    }