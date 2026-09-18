from unified_scoring.anomaly_detector import detect_scoring_anomaly
from unified_scoring.followup_stability import stabilize_followup_logic
from unified_scoring.scoring_anomaly_correction import correct_scoring_anomaly
from unified_scoring.transcript_cleanup import clean_transcript
from unified_scoring.refined_scoring_engine import refine_score


print()
print("=" * 90)
print("DAY 42 - OPTIMIZATION & STABILITY".center(90))
print("=" * 90)


# --------------------------------------------------
# TRANSCRIPT CLEANUP
# --------------------------------------------------

transcript = input("Enter Transcript: ")

cleaned_transcript = clean_transcript(
    transcript
)


# --------------------------------------------------
# SCORE INPUTS
# --------------------------------------------------

ai_score = float(
    input("Enter AI Score: ")
)

reference_score = float(
    input("Enter Reference Score: ")
)

tolerance = float(
    input("Enter Allowed Tolerance: ")
)

confidence_score = float(
    input("Enter Confidence Score: ")
)

stress_score = float(
    input("Enter Stress Score: ")
)

previous_followup = input(
    "Enter Previous Follow-up: "
)


# --------------------------------------------------
# SCORING ANOMALY DETECTION
# --------------------------------------------------

anomaly = detect_scoring_anomaly(
    ai_score,
    reference_score,
    tolerance
)


# --------------------------------------------------
# SCORING CORRECTION
# --------------------------------------------------

correction = correct_scoring_anomaly(
    ai_score,
    reference_score,
    tolerance
)


# --------------------------------------------------
# REFINED SCORE
# --------------------------------------------------

refined = refine_score(
    ai_score,
    reference_score,
    tolerance
)


# --------------------------------------------------
# FOLLOW-UP STABILITY
# --------------------------------------------------

followup = stabilize_followup_logic(
    cleaned_transcript,
    confidence_score,
    stress_score,
    previous_followup
)


# --------------------------------------------------
# FINAL OUTPUT
# --------------------------------------------------

print()
print("=" * 90)
print("OPTIMIZED HR INTERVIEW RESULT".center(90))
print("=" * 90)


print(f"{'Cleaned Transcript':<30}: {cleaned_transcript}")

print("-" * 90)

for key, value in anomaly.items():

    print(f"{key:<30}: {value}")

print("-" * 90)

for key, value in correction.items():

    print(f"{key:<30}: {value}")

print("-" * 90)

for key, value in refined.items():

    print(f"{key:<30}: {value}")

print("-" * 90)

for key, value in followup.items():

    print(f"{key:<30}: {value}")

print("=" * 90)

print(
    "DAY 42 COMPLETED SUCCESSFULLY".center(90)
)

print("=" * 90)