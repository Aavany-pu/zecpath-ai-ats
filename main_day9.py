from parsers.skill_extractor import extract_skills
from parsers.skill_extractor import skill_confidence

resume_text = """
Python
SQL
Machine Learning
Excel
"""

skills = extract_skills(resume_text)

scores = skill_confidence(skills)

print("Extracted Skills")
print(skills)

print()

print("Confidence Scores")
print(scores)