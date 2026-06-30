import re


def extract_experience(resume_text):

    experience = 0

    patterns = [

        r"(\d+)\+?\s*years",

        r"(\d+)\+?\s*year",

        r"(\d+)\s*yrs",

        r"(\d+)\s*yr"

    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            resume_text,
            re.IGNORECASE
        )

        if match:

            experience = int(
                match.group(1)
            )

            break

    return experience