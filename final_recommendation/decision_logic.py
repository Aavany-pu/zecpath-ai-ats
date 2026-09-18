def load_decision_rules(file_path):
    rules = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            rules[key.strip()] = value.strip()

    return rules


def create_hybrid_logic(file_path):
    rules = load_decision_rules(file_path)

    return {
        "Status": "Hybrid Decision Logic Configured",
        "Score Evaluation": rules.get(
            "Score Evaluation", ""
        ),
        "Rule Evaluation": rules.get(
            "Rule Evaluation", ""
        ),
        "Decision Resolution": rules.get(
            "Decision Resolution", ""
        )
    }