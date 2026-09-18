from pathlib import Path


def generate_achievements(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    if not project_root.exists():
        return {
            "Status": "Project Root Not Found",
            "Achievements": []
        }

    achievements = []

    day_modules = sorted(
        project_root.glob("main_day*.py"),
        key=lambda path: path.name
    )

    if day_modules:
        achievements.append(
            f"Implemented {len(day_modules)} day-based project modules."
        )

    required_directories = [
        "technical_handbook",
        "internal_review",
        "feature_enhancements",
        "presentation",
        "mock_demo",
        "final_optimization"
    ]

    for directory in required_directories:
        if (project_root / directory).exists():
            achievements.append(
                f"Completed project area: {directory}"
            )

    if (project_root / "README.md").exists():
        achievements.append(
            "Created project README documentation."
        )

    return {
        "Status": "Repository-Based Achievements Generated",
        "Achievements": achievements
    }