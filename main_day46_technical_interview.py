from technical_interview.interview_structure import (
    create_interview_structure
)

from technical_interview.experience_logic import (
    determine_experience_level
)

from technical_interview.role_skill_mapper import (
    map_role_to_skills
)

from technical_interview.difficulty_progression import (
    get_difficulty_progression
)

from technical_interview.interview_states import (
    load_interview_flow
)

from technical_interview.interview_flow import (
    create_technical_interview_blueprint
)


ROLE_FILE = (
    "data/technical_interview/"
    "role_skill_domains.txt"
)

DIFFICULTY_FILE = (
    "data/technical_interview/"
    "difficulty_progression.txt"
)

FLOW_FILE = (
    "data/technical_interview/"
    "interview_flow.txt"
)


print("=" * 90)
print("DAY 46 - TECHNICAL INTERVIEW SYSTEM DESIGN")
print("=" * 90)


# ================================================================
# STEP 1 - INTERVIEW STRUCTURE
# ================================================================

print("\n[STEP 1] TECHNICAL INTERVIEW STRUCTURE")
print("-" * 90)

structure = create_interview_structure()

for index, stage in enumerate(
    structure,
    start=1
):
    print(f"{index}. {stage}")


# ================================================================
# STEP 2 - EXPERIENCE LOGIC
# ================================================================

print("\n[STEP 2] EXPERIENCE-BASED LOGIC")
print("-" * 90)

experience_input = input(
    "Enter candidate experience in years: "
)

try:
    years_of_experience = float(
        experience_input
    )

    experience_result = determine_experience_level(
        years_of_experience
    )

except ValueError:
    experience_result = {
        "Status": "Invalid Experience",
        "Experience Level": None,
        "Difficulty": None
    }

for key, value in experience_result.items():
    print(f"{key:<35}: {value}")


# ================================================================
# STEP 3 - ROLE TO SKILL MAPPING
# ================================================================

print("\n[STEP 3] ROLE TO SKILL DOMAIN MAPPING")
print("-" * 90)

candidate_role = input(
    "Enter technical job role: "
)

role_result = map_role_to_skills(
    ROLE_FILE,
    candidate_role
)

for key, value in role_result.items():
    print(f"{key:<35}: {value}")

if role_result["Skill Domains"]:

    print("\nSkill Domains:")

    for index, skill in enumerate(
        role_result["Skill Domains"],
        start=1
    ):
        print(f"{index}. {skill}")


# ================================================================
# STEP 4 - DIFFICULTY PROGRESSION
# ================================================================

print("\n[STEP 4] QUESTION DIFFICULTY PROGRESSION")
print("-" * 90)

difficulty = experience_result["Difficulty"]

if difficulty:

    progression_result = get_difficulty_progression(
        DIFFICULTY_FILE,
        difficulty
    )

else:

    progression_result = {
        "Status": "Difficulty Not Available",
        "Difficulty": None,
        "Progression": []
    }

for key, value in progression_result.items():

    if key != "Progression":
        print(f"{key:<35}: {value}")

print("\nQuestion Progression:")

if progression_result["Progression"]:

    for index, stage in enumerate(
        progression_result["Progression"],
        start=1
    ):
        print(f"{index}. {stage}")

else:
    print("No progression available.")


# ================================================================
# STEP 5 - INTERVIEW FLOW
# ================================================================

print("\n[STEP 5] INTERVIEW FLOW STATES & TRANSITIONS")
print("-" * 90)

flow = load_interview_flow(
    FLOW_FILE
)

for current_state, next_state in flow.items():

    print(
        f"{current_state:<20} -> {next_state}"
    )


# ================================================================
# STEP 6 - BLUEPRINT
# ================================================================

print("\n[STEP 6] TECHNICAL INTERVIEW AI BLUEPRINT")
print("-" * 90)

blueprint = create_technical_interview_blueprint(
    structure,
    experience_result,
    role_result,
    progression_result,
    flow
)

print(
    f"{'Blueprint Status':<35}: Generated"
)

print("\nInterview Structure:")

for index, stage in enumerate(
    blueprint["Interview Structure"],
    start=1
):
    print(f"{index}. {stage}")

print("\nExperience Configuration:")

for key, value in blueprint[
    "Experience Level"
].items():

    print(
        f"{key:<35}: {value}"
    )

print("\nRole & Skill Configuration:")

for key, value in blueprint[
    "Role Mapping"
].items():

    print(
        f"{key:<35}: {value}"
    )

print("\nQuestion Progression:")

for index, stage in enumerate(
    blueprint[
        "Question Progression"
    ]["Progression"],
    start=1
):
    print(f"{index}. {stage}")

print("\nInterview Flow:")

for current_state, next_state in blueprint[
    "Interview Flow"de

].items():

    print(
        f"{current_state:<20} -> {next_state}"
    )


# ================================================================
# FINAL STATUS
# ================================================================

print("\n" + "=" * 90)
print(" - TECHNICAL INTERVIEW SYSTEM DESIGN COMPLETED")
print("=" * 90)