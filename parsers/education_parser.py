def extract_education(resume_text):

    education_keywords = [
        "education",
        "academic qualification",
        "qualification",
        "educational qualification"
    ]

    stop_keywords = [
        "skills",
        "technical skills",
        "projects",
        "experience",
        "work experience",
        "certifications",
        "achievements",
        "languages",
        "interests",
        "contact"
    ]

    lines = resume_text.split("\n")

    education_section = False
    education_details = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        lower_line = line.lower()

        if any(keyword in lower_line for keyword in education_keywords):
            education_section = True
            continue

        if education_section:

            if any(keyword in lower_line for keyword in stop_keywords):
                break

            education_details.append(line)

    return education_details