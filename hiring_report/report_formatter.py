def format_hiring_report(hiring_report):
    lines = []

    lines.append("=" * 90)
    lines.append("HIRING INTELLIGENCE REPORT")
    lines.append("=" * 90)

    lines.append("\nREPORT STATUS")
    lines.append("-" * 90)
    lines.append(
        f"{'Status':<35}: "
        f"{hiring_report.get('Report Status', '')}"
    )

    lines.append("\nEVALUATION INSIGHTS")
    lines.append("-" * 90)

    evaluation_insights = hiring_report.get(
        "Evaluation Insights",
        {}
    )

    for section, content in evaluation_insights.items():
        lines.append(f"\n{section}")

        if isinstance(content, dict):
            for key, value in content.items():
                lines.append(
                    f"  {key:<32}: {value}"
                )
        else:
            lines.append(
                f"  {'Result':<32}: {content}"
            )

    lines.append("\nSTRENGTHS")
    lines.append("-" * 90)

    for index, strength in enumerate(
        hiring_report.get("Strengths", []),
        start=1
    ):
        lines.append(
            f"{index}. {strength}"
        )

    lines.append("\nWEAKNESSES")
    lines.append("-" * 90)

    for index, weakness in enumerate(
        hiring_report.get("Weaknesses", []),
        start=1
    ):
        lines.append(
            f"{index}. {weakness}"
        )

    lines.append("\nRISK INDICATORS")
    lines.append("-" * 90)

    for index, risk in enumerate(
        hiring_report.get("Risk Indicators", []),
        start=1
    ):
        lines.append(
            f"{index}. {risk}"
        )

    lines.append("\nFINAL RECOMMENDATION")
    lines.append("-" * 90)

    lines.append(
        f"{'Recommendation':<35}: "
        f"{hiring_report.get('Final Recommendation')}"
    )

    lines.append("\n" + "=" * 90)

    return "\n".join(lines)