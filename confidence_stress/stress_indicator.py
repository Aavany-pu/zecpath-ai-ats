from confidence_stress.hesitation_detector import detect_hesitation
from confidence_stress.uncertainty_detector import detect_uncertainty
from confidence_stress.repetition_detector import detect_repetition
from confidence_stress.sentiment_analyzer import analyze_sentiment


def measure_stress():

    hesitation = detect_hesitation()

    uncertainty = detect_uncertainty()

    repetition = detect_repetition()

    sentiment = analyze_sentiment()

    stress_results = []

    total_questions = len(hesitation)

    for i in range(total_questions):

        stress_score = 0

        stress_score += hesitation[i]["Hesitation Count"] * 2

        stress_score += uncertainty[i]["Uncertainty Count"] * 3

        stress_score += repetition[i]["Repetition Count"] * 2

        if sentiment[i]["Sentiment"] == "Negative":

            stress_score += 5

        if stress_score <= 3:

            stress_level = "Low"

        elif stress_score <= 8:

            stress_level = "Moderate"

        else:

            stress_level = "High"

        stress_results.append({

            "Question ID": hesitation[i]["Question ID"],

            "Question": hesitation[i]["Question"],

            "Stress Score": stress_score,

            "Stress Level": stress_level

        })

    return stress_results