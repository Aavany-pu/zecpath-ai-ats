from confidence_stress.hesitation_detector import detect_hesitation
from confidence_stress.uncertainty_detector import detect_uncertainty
from confidence_stress.repetition_detector import detect_repetition
from confidence_stress.sentiment_analyzer import analyze_sentiment
from confidence_stress.contradiction_detector import detect_contradictions
from confidence_stress.stress_indicator import measure_stress


def calculate_confidence_score():

    hesitation = detect_hesitation()

    uncertainty = detect_uncertainty()

    repetition = detect_repetition()

    sentiment = analyze_sentiment()

    contradiction = detect_contradictions()

    stress = measure_stress()

    confidence_results = []

    total_questions = len(hesitation)

    for i in range(total_questions):

        score = 100

        score -= hesitation[i]["Hesitation Count"] * 5

        score -= uncertainty[i]["Uncertainty Count"] * 5

        score -= repetition[i]["Repetition Count"] * 4

        if sentiment[i]["Sentiment"] == "Negative":

            score -= 10

        if contradiction[i]["Status"] == "Contradiction Found":

            score -= 15

        score -= stress[i]["Stress Score"]

        if score < 0:

            score = 0

        if score > 100:

            score = 100

        if score >= 85:

            level = "Very High"

        elif score >= 70:

            level = "High"

        elif score >= 50:

            level = "Moderate"

        else:

            level = "Low"

        confidence_results.append({

            "Question ID": hesitation[i]["Question ID"],

            "Question": hesitation[i]["Question"],

            "Confidence Score": score,

            "Confidence Level": level

        })

    return confidence_results