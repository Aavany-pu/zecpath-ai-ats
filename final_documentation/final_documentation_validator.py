from pathlib import Path


def validate_final_documentation(project_root=None):
    if project_root is None:
        project_root = Path(__file__).resolve().parent.parent

    project_root = Path(project_root)

    required_items = [
        "README.md",
        "portfolio",
        "final_documentation",
        "technical_handbook",
        "presentation",
        "mock_demo",
        "feature_enhancements",
        "final_optimization"
    ]

    missing_items = []
    existing_items = []

    for item in required_items:
        item_path = project_root / item

        if item_path.exists():
            existing_items.append(item)
        else:
            missing_items.append(item)

    if missing_items:
        status = "Documentation Validation Failed"
    else:
        status = "Documentation Validation Passed"

    return {
        "Status": status,
        "Required Items": len(required_items),
        "Existing Items": existing_items,
        "Missing Items": missing_items
    }