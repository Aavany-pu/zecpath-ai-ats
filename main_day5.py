from parsers.resume_parser import read_pdf

file_path = "data/resumes/resume1_python_developer.pdf"

resume_text = read_pdf(file_path)

print("RESUME CONTENT")
print("-" * 50)

print(resume_text)