def load_report_configuration(file_path):
    configuration = {}
    limitations = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            if key.startswith("Limitation"):
                limitations.append(value)
            else:
                configuration[key] = value

    configuration["Limitations"] = limitations

    return configuration


def generate_behavioral_report(framework_result, file_path):
    configuration = load_report_configuration(file_path)

    framework = framework_result.get("Framework", [])

    return {
        "Report Status": framework_result.get("Status", ""),
        "Analysis Type": configuration.get("Analysis Type", ""),
        "Candidate Score": configuration.get(
            "Candidate Score Status", ""
        ),
        "Hiring Decision": configuration.get(
            "Hiring Decision Status", ""
        ),
        "Signals Analyzed": len(framework),
        "Framework": framework,
        "Limitations": configuration.get(
            "Limitations", []
        )
    }