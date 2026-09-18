def improve_report_clarity(report):
    if report is None:
        return {
            "Status": "No Report Available",
            "Report": {}
        }

    if not isinstance(report, dict):
        return {
            "Status": "Invalid Report Data",
            "Report": {}
        }

    sections = {}

    for key, value in report.items():
        section_name = str(key).strip()

        if isinstance(value, dict):
            sections[section_name] = {
                str(sub_key).strip(): sub_value
                for sub_key, sub_value in value.items()
            }

        else:
            sections[section_name] = value

    return {
        "Status": "Report Clarity Improved",
        "Report": sections
    }