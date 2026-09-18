from unified_scoring.cross_round_scoring import calculate_cross_round_score
from unified_scoring.hiring_fit_calculator import calculate_hiring_fit
from unified_scoring.unified_candidate_score import create_unified_candidate_score


print()
print("=" * 90)
print("DAY 41 - UNIFIED SCORING ENGINE".center(90))
print("=" * 90)

candidate = input("Enter Candidate: ")

print()

ats_score = float(input("Enter ATS Score: "))

screening_score = float(input("Enter Screening Score: "))

hr_score = float(input("Enter HR Interview Score: "))

print()

ats_weight = float(input("Enter ATS Weight: "))

screening_weight = float(input("Enter Screening Weight: "))

hr_weight = float(input("Enter HR Weight: "))


unified_score = calculate_cross_round_score(

    ats_score,

    screening_score,

    hr_score,

    ats_weight,

    screening_weight,

    hr_weight

)


hiring_fit = calculate_hiring_fit(
    unified_score
)


candidate_score = create_unified_candidate_score(

    candidate,

    ats_score,

    screening_score,

    hr_score,

    unified_score,

    hiring_fit

)


print()
print("=" * 90)
print("UNIFIED CANDIDATE SCORE".center(90))
print("=" * 90)


for key, value in candidate_score.items():

    print(f"{key:<30}: {value}")


print("=" * 90)
print("DAY 41 COMPLETED SUCCESSFULLY".center(90))
print("=" * 90)