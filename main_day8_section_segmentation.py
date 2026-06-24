import os

from parsers.resume_parser import read_pdf

from parsers.section_classifier import (
    classify_sections
)

resume_folder = "data/resumes"

for file in os.listdir(
    resume_folder
):

    if file.endswith(".pdf"):

        file_path = os.path.join(
            resume_folder,
            file
        )

        resume_text = read_pdf(
            file_path
        )

        sections = classify_sections(
            resume_text
        )

        print("\n")
        print("=" * 60)

        print("RESUME :", file)

        print("\nSKILLS")

        print(
            sections["skills"]
        )

        print("\nEDUCATION")

        print(
            sections["education"]
        )

        print("\nEXPERIENCE")

        print(
            sections["experience"]
        )

        print("\nPROJECTS")

        print(
            sections["projects"]
        )

        print("\nCERTIFICATIONS")

        print(
            sections["certifications"]
        )

        print("=" * 60)