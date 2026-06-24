def calculate_metrics(results):

    total = len(results)

    passed = 0

    for result in results:

        if result["score"] >= 30:

            passed += 1

    accuracy = (
        passed / total
    ) * 100

    return {
        "total_resumes": total,
        "passed_resumes": passed,
        "accuracy": round(
            accuracy,
            2
        )
    }