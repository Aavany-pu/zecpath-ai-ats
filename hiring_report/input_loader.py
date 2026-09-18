def load_input_sources(file_path):
    sources = {}

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            source_name, source_path = line.split(":", 1)

            source_name = source_name.strip()
            source_path = source_path.strip()

            sources[source_name] = source_path

    if not sources:
        return {
            "Status": "No Input Sources Found",
            "Sources": {}
        }

    return {
        "Status": "Input Sources Loaded",
        "Sources": sources
    }