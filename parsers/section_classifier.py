SECTION_HEADERS = {
    "skills": [
        "skills",
        "technical skills"
    ],

    "education": [
        "education"
    ],

    "experience": [
        "experience",
        "work experience"
    ],

    "projects": [
        "projects"
    ],

    "certifications": [
        "certifications"
    ]
}


def classify_sections(text):

    sections = {
        "skills": [],
        "education": [],
        "experience": [],
        "projects": [],
        "certifications": []
    }

    current_section = None

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if not line:

            continue

        lower_line = line.lower()

        found_header = False

        for section_name, headers in SECTION_HEADERS.items():

            if lower_line in headers:

                current_section = section_name

                found_header = True

                break

        if found_header:

            continue

        if current_section:

            sections[current_section].append(
                line
            )

    return sections