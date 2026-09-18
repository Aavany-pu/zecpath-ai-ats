from hr_simulation.test_report import generate_test_report


def generate_simulation_summary():

    report = generate_test_report()

    summary = []

    total_sessions = len(report)

    if total_sessions == 0:

        return summary

    total_ai_score = 0

    total_manual_score = 0

    total_accuracy = 0

    consistent = 0

    minor_difference = 0

    major_difference = 0

    for item in report:

        total_ai_score += item["AI Score"]

        total_manual_score += item["Manual Score"]

        total_accuracy += item["Accuracy"]

        if item["Consistency"] == "Consistent":

            consistent += 1

        elif item["Consistency"] == "Minor Difference":

            minor_difference += 1

        else:

            major_difference += 1

    average_ai = round(total_ai_score / total_sessions, 2)

    average_manual = round(total_manual_score / total_sessions, 2)

    average_accuracy = round(total_accuracy / total_sessions, 2)

    summary.append({

        "Total Interview Sessions": total_sessions,

        "Average AI Score": average_ai,

        "Average Manual Score": average_manual,

        "Average Accuracy (%)": average_accuracy,

        "Consistent Results": consistent,

        "Minor Differences": minor_difference,

        "Major Differences": major_difference

    })

    return summary