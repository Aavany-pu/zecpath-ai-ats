from parsers.resume_parser import read_pdf
from parsers.experience_parser import extract_experience

resume_text = read_pdf("data/resumes/resume1_python_developer.pdf")

experience = extract_experience(resume_text)

print("Experience Details")
print("------------------")

for item in experience:
    print(item)