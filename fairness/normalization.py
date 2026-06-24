from parsers.resume_parser import read_pdf

def normalize_resume(file_path):

    resume_text = read_pdf(file_path)

    lines = resume_text.split("\n")

    cleaned_lines = []

    for line in lines:

        line = line.strip()

        if line:

            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)