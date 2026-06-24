from parsers.resume_parser import read_pdf
from matching.semantic_matcher import semantic_match

resume_text = read_pdf(
    "data/resumes/resume1_python_developer.pdf"
)

with open(
    "data/job_descriptions/jd1.txt",
    "r",
    encoding="utf-8"
) as file:
    jd_text = file.read()

result = semantic_match(
    resume_text,
    jd_text
)

print("Semantic Match Score:", result["score"], "%")

print("\nMatched Keywords:")
for keyword in result["matched_keywords"]:
    print(keyword)

print("\nTotal Matches:", result["total_matches"])