def load_role_skill_domains(file_path):
    role_domains = {}

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:
            line = line.strip()

            if not line or ":" not in line:
                continue

            role, skills = line.split(":", 1)

            role = role.strip()

            skill_list = [
                skill.strip()
                for skill in skills.split(",")
                if skill.strip()
            ]

            role_domains[role] = skill_list

    return role_domains


def map_role_to_skills(file_path, role):
    role_domains = load_role_skill_domains(file_path)

    matched_role = None

    for available_role in role_domains:
        if available_role.lower() == role.strip().lower():
            matched_role = available_role
            break

    if matched_role is None:
        return {
            "Status": "Role Not Found",
            "Role": role,
            "Skill Domains": []
        }

    return {
        "Status": "Role Mapped",
        "Role": matched_role,
        "Skill Domains": role_domains[matched_role]
    }