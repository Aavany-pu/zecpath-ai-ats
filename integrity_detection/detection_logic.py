def load_detection_rules(file_path):
    rules = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            signal, rule = line.split(":", 1)

            rules[signal.strip()] = rule.strip()

    return rules


def create_detection_logic(file_path, signals):
    rules = load_detection_rules(file_path)

    detection_logic = {}

    for signal in signals:
        if signal in rules:
            detection_logic[signal] = {
                "Signal": signal,
                "Detection Rule": rules[signal],
                "Threshold Flag": "Configuration Required",
                "Pattern Recognition": "Configuration Required"
            }

    if not detection_logic:
        return {
            "Status": "No Detection Logic Found",
            "Detection Logic": {}
        }

    return {
        "Status": "Detection Logic Created",
        "Detection Logic": detection_logic
    }