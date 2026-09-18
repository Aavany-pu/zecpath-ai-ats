def create_stakeholder_questions():
    questions = [
        {
            "Question": "What problem does Zecpath AI solve?",
            "Focus": "Problem Statement"
        },
        {
            "Question": "How does the AI solution support the recruitment process?",
            "Focus": "AI Solution"
        },
        {
            "Question": "What are the major components of the system?",
            "Focus": "System Architecture"
        },
        {
            "Question": "How does the hiring pipeline work?",
            "Focus": "Hiring Pipeline"
        },
        {
            "Question": "Which AI modules are included in the system?",
            "Focus": "AI Modules"
        },
        {
            "Question": "How does the system evaluate candidate information?",
            "Focus": "Evaluation"
        },
        {
            "Question": "What information is presented to recruiters?",
            "Focus": "Recruiter Output"
        },
        {
            "Question": "How can this system create business value?",
            "Focus": "Business Impact"
        },
        {
            "Question": "How would you improve the system in the future?",
            "Focus": "Future Improvements"
        },
        {
            "Question": "Can you explain the complete system workflow?",
            "Focus": "End-to-End Workflow"
        }
    ]

    return {
        "Status": "Stakeholder Q&A Prepared",
        "Questions": questions,
        "Total Questions": len(questions)
    }