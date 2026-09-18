from presentation.presentation_structure import create_presentation_structure
from presentation.problem_statement import create_problem_statement
from presentation.ai_solution import create_ai_solution
from presentation.system_architecture import create_system_architecture
from presentation.demo_flow import create_demo_flow
from presentation.hiring_pipeline import create_hiring_pipeline
from presentation.ai_modules_diagram import create_ai_modules_diagram
from presentation.business_impact import create_business_impact
from presentation.demo_script import create_demo_script
from presentation.presentation_deck import create_presentation_deck


print("=" * 90)
print("- FINAL PRESENTATION TEST")
print("=" * 90)


# STEP 1
presentation = create_presentation_structure()

print()
print("STEP 1 - PRESENTATION STRUCTURE")
print("-" * 90)
print(f"{'Status':<30}: {presentation['Status']}")


# STEP 2
problem = create_problem_statement()

print()
print("STEP 2 - PROBLEM STATEMENT")
print("-" * 90)
print(f"{'Status':<30}: {problem['Status']}")


# STEP 3
solution = create_ai_solution()

print()
print("STEP 3 - AI SOLUTION")
print("-" * 90)
print(f"{'Status':<30}: {solution['Status']}")


# STEP 4
architecture = create_system_architecture()

print()
print("STEP 4 - SYSTEM ARCHITECTURE")
print("-" * 90)
print(f"{'Status':<30}: {architecture['Status']}")


# STEP 5
demo_flow = create_demo_flow()

print()
print("STEP 5 - DEMO FLOW")
print("-" * 90)
print(f"{'Status':<30}: {demo_flow['Status']}")


# STEP 6
hiring_pipeline = create_hiring_pipeline()

print()
print("STEP 6 - HIRING PIPELINE")
print("-" * 90)
print(f"{'Status':<30}: {hiring_pipeline['Status']}")


# STEP 7
ai_modules = create_ai_modules_diagram()

print()
print("STEP 7 - AI MODULES")
print("-" * 90)
print(f"{'Status':<30}: {ai_modules['Status']}")


# STEP 8
business_impact = create_business_impact()

print()
print("STEP 8 - BUSINESS IMPACT")
print("-" * 90)
print(f"{'Status':<30}: {business_impact['Status']}")


# STEP 9
demo_script = create_demo_script()

print()
print("STEP 9 - DEMO SCRIPT")
print("-" * 90)
print(f"{'Status':<30}: {demo_script['Status']}")


# STEP 10
deck = create_presentation_deck(
    presentation,
    problem,
    solution,
    architecture,
    demo_flow,
    hiring_pipeline,
    ai_modules,
    business_impact,
    demo_script
)

print()
print("STEP 10 - PRESENTATION DECK")
print("-" * 90)
print(f"{'Status':<30}: {deck['Status']}")
print(f"{'Total Slides':<30}: {deck['Total Slides']}")


# FINAL VALIDATION
print()
print("FINAL VALIDATION")
print("-" * 90)

results = [
    presentation,
    problem,
    solution,
    architecture,
    demo_flow,
    hiring_pipeline,
    ai_modules,
    business_impact,
    demo_script,
    deck
]

failed = [
    result
    for result in results
    if not result.get("Status")
]

if not failed:
    print(f"{'Validation Status':<30}: PASSED")
    print(f"{'Components Tested':<30}: {len(results)}")
else:
    print(f"{'Validation Status':<30}: FAILED")
    print(f"{'Failed Components':<30}: {len(failed)}")


print()
print("=" * 90)
print(" COMPLETED")
print("=" * 90)