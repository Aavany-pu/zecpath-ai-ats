def format_output(data):
    if data is None:
        return {
            "Status": "No Output Available",
            "Formatted Output": ""
        }

    if not isinstance(data, dict):
        return {
            "Status": "Invalid Output Data",
            "Formatted Output": ""
        }

    lines = []

    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            
            for item in value:
                lines.append(f"  - {item}")
        elif isinstance(value, dict):
            lines.append(f"{key}:")
            
            for sub_key, sub_value in value.items():
                lines.append(
                    f"  {sub_key:<25}: {sub_value}"
                )
        else:
            lines.append(
                f"{key:<30}: {value}"
            )

    return {
        "Status": "Output Formatted Successfully",
        "Formatted Output": "\n".join(lines)
    }