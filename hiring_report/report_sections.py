def load_report_sections(file_path):
    sections = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            sections.append(line)

    return sections


def get_report_sections(file_path):
    sections = load_report_sections(file_path)

    if not sections:
        return {
            "Status": "No Report Sections Found",
            "Sections": []
        }

    return {
        "Status": "Report Sections Loaded",
        "Sections": sections
    }