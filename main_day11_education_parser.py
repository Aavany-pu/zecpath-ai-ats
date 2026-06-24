from parsers.resume_parser import read_pdf
from parsers.education_parser import extract_education

resume_text = read_pdf(
    "data/resumes/resume1_python_developer.pdf"
)

education = extract_education(resume_text)

print("\nEDUCATION DETAILS")
print("-------------------------")

for item in education:
    print(item)