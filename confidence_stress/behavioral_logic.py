from confidence_stress.hesitation_detector import detect_hesitation
from confidence_stress.uncertainty_detector import detect_uncertainty
from confidence_stress.repetition_detector import detect_repetition
from confidence_stress.sentiment_analyzer import analyze_sentiment
from confidence_stress.contradiction_detector import detect_contradictions
from confidence_stress.stress_indicator import measure_stress
from confidence_stress.confidence_score import calculate_confidence_score


def build_behavioral_logic():

    hesitation = detect_hesitation()

    uncertainty = detect_uncertainty()

    repetition = detect_repetition()

    sentiment = analyze_sentiment()

    contradiction = detect_contradictions()

    stress = measure_stress()

    confidence = calculate_confidence_score()

    behavioral_report = []

    total_questions = len(confidence)

    for i in range(total_questions):

        behavioral_report.append({

            "Question ID": confidence[i]["Question ID"],

            "Question": confidence[i]["Question"],

            "Hesitation Level":
                hesitation[i]["Hesitation Level"],

            "Uncertainty Level":
                uncertainty[i]["Uncertainty Level"],

            "Repetition Level":
                repetition[i]["Repetition Level"],

            "Sentiment":
                sentiment[i]["Sentiment"],

            "Contradiction":
                contradiction[i]["Status"],

            "Stress Level":
                stress[i]["Stress Level"],

            "Confidence Score":
                confidence[i]["Confidence Score"],

            "Confidence Level":
                confidence[i]["Confidence Level"]

        })

    return behavioral_report