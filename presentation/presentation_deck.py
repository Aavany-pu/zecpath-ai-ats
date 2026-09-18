def create_presentation_deck(
    presentation_structure,
    problem_statement,
    ai_solution,
    architecture,
    demo_flow,
    hiring_pipeline,
    ai_modules,
    business_impact,
    demo_script
):
    slides = [
        {
            "Slide": 1,
            "Title": "Zecpath AI",
            "Content": "AI-Powered Recruitment System"
        },
        {
            "Slide": 2,
            "Title": problem_statement["Title"],
            "Content": problem_statement["Points"]
        },
        {
            "Slide": 3,
            "Title": ai_solution["Title"],
            "Content": ai_solution["Points"]
        },
        {
            "Slide": 4,
            "Title": "System Architecture",
            "Content": architecture["Components"]
        },
        {
            "Slide": 5,
            "Title": "Hiring Pipeline",
            "Content": hiring_pipeline["Pipeline"]
        },
        {
            "Slide": 6,
            "Title": "AI Modules",
            "Content": ai_modules["Modules"]
        },
        {
            "Slide": 7,
            "Title": "Demo Flow",
            "Content": demo_flow["Flow"]
        },
        {
            "Slide": 8,
            "Title": "Business Impact",
            "Content": business_impact["Impacts"]
        },
        {
            "Slide": 9,
            "Title": "System Walkthrough",
            "Content": demo_script["Script"]
        },
        {
            "Slide": 10,
            "Title": "Conclusion",
            "Content": "Zecpath AI recruitment workflow demonstration"
        }
    ]

    return {
        "Status": "Presentation Deck Structure Created",
        "Slides": slides,
        "Total Slides": len(slides)
    }