def export_hiring_report(report_text, output_path):
    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:
        file.write(report_text)

    return {
        "Status": "Hiring Report Exported",
        "Output File": output_path
    }