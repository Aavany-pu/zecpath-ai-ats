import os

from parsers.resume_parser import read_pdf

from parsers.skill_extractor import (
    extract_skills
)

from parsers.experience_parser import (
    extract_experience
)

from speech_processing.transcript_cleaner import (
    clean_transcript
)

from speech_processing.transcript_normalizer import (
    normalize_transcript
)

from speech_processing.stt_accuracy import (
    calculate_accuracy
)

resume_folder = "data/resumes"

for file in os.listdir(
    resume_folder
):

    if file.endswith(".pdf"):

        path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            path
        )

        skills = extract_skills(
            resume_text
        )

        experience = extract_experience(
            resume_text
        )

        transcript_text = (

            " ".join(skills)

            +

            " experience "

            +

            str(experience)
        )

        cleaned_text = clean_transcript(
            transcript_text
        )

        normalized_text = normalize_transcript(
            cleaned_text
        )

        accuracy = calculate_accuracy(

            transcript_text,

            normalized_text
        )

        print("\n")
        print("=" * 60)

        print(
            "Resume :",
            file
        )

        print()

        print(
            "Clean Transcript :"
        )

        print(
            cleaned_text
        )

        print()

        print(
            "Normalized Transcript :"
        )

        print(
            normalized_text
        )

        print()

        print(
            "STT Accuracy :",
            accuracy,
            "%"
        )
        output_folder = "speech_processing"

output_file = os.path.join(
    output_folder,
    "transcript_output.txt"
)

with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    file.write(
        normalized_text
    )