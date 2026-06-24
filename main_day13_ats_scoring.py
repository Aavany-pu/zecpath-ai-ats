from parsers.resume_parser import read_pdf
from ats_engine.ats_scoring import calculate_ats_score

resume_text = read_pdf(
    "data/resumes/resume1_python_developer.pdf"
)

with open(
    "data/job_descriptions/jd1.txt",
    "r",
    encoding="utf-8"
) as file:

    jd_text = file.read()

result = calculate_ats_score(
    resume_text,
    jd_text
)

print("ATS SCORE")
print("---------")
print(result["score"], "%")

print("\nMATCHED KEYWORDS")
print("----------------")

for keyword in result["matched_keywords"]:
    print(keyword)

print("\nMISSING KEYWORDS")
print("----------------")

for keyword in result["missing_keywords"]:
    print(keyword)

print("\nTOTAL MATCHES")
print("-------------")
print(result["total_matches"])