from pathlib import Path

from portfolio.project_summary import generate_project_summary
from portfolio.skills_summary import generate_skills_summary
from portfolio.achievements import generate_achievements


def generate_internship_portfolio(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_summary = generate_project_summary(project_root)
    skills_summary = generate_skills_summary(project_root)
    achievements = generate_achievements(project_root)

    return {
        "Status": "Internship Portfolio Generated",
        "Project Summary": project_summary,
        "Skills Summary": skills_summary,
        "Achievements": achievements
    }