def extract_experience(resume_text):

    lines = resume_text.split("\n")

    experience_keywords = [
        "experience",
        "work experience",
        "professional experience",
        "employment history"
    ]

    stop_keywords = [
        "education",
        "skills",
        "projects",
        "certifications",
        "achievements",
        "languages",
        "interests",
        "contact"
    ]

    experience_section = False
    experience_details = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower() in experience_keywords:
            experience_section = True
            continue

        if experience_section:

            if line.lower() in stop_keywords:
                break

            experience_details.append(line)

    return 