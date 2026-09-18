def load_signal_behavior_mapping(file_path):
    mapping = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            signal, insight = line.split(":", 1)

            mapping[signal.strip()] = insight.strip()

    return mapping


def map_behavioral_signals(file_path, signals):
    mapping = load_signal_behavior_mapping(file_path)

    mapped_results = {}

    for signal in signals:
        if signal in mapping:
            mapped_results[signal] = mapping[signal]

    if not mapped_results:
        return {
            "Status": "No Behavioral Mapping Found",
            "Mappings": {}
        }

    return {
        "Status": "Behavioral Signals Mapped",
        "Mappings": mapped_results
    }