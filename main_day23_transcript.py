import os

from parsers.resume_parser import read_pdf

from parsers.skill_extractor import (
    extract_skills
)

from parsers.experience_parser import (
    extract_experience
)

from transcripts.transcripts_schema import (
    create_transcript
)

from transcripts.screening_data_structure import (
    create_screening_data
)

from transcripts.metadata_standards import (
    create_metadata
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

        transcript = create_transcript(

            file,

            skills,

            experience
        )

        screening_data = create_screening_data(

            file,

            skills,

            experience
        )

        metadata = create_metadata(

            file,

            skills,

            experience
        )

        print("\n")
        print("=" * 60)

        print("VOICE TRANSCRIPT")

        print(transcript)

        print()

        print("AI SCREENING DATA")

        print(screening_data)

        print()

        print("METADATA")

        print(metadata)