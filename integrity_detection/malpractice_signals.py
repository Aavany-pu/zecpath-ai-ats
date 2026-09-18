def load_malpractice_signals(file_path):
    signals = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            signals.append(line)

    return signals


def get_malpractice_signals(file_path):
    signals = load_malpractice_signals(file_path)

    if not signals:
        return {
            "Status": "No Malpractice Signals Found",
            "Signals": []
        }

    return {
        "Status": "Malpractice Signals Loaded",
        "Signals": signals
    }