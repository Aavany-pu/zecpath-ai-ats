def create_developer_onboarding_guide():
    onboarding_steps = [
        "Understand the Zecpath AI system architecture",
        "Review the project folder and module structure",
        "Review the API integration design",
        "Understand the scoring and evaluation modules",
        "Review the data models and system workflows",
        "Set up the development environment",
        "Run and verify the existing system modules",
        "Review logging, monitoring, security, and governance components",
        "Follow the documented development and deployment process"
    ]

    developer_guidelines = [
        "Understand existing module dependencies before making changes",
        "Keep module inputs and outputs consistent",
        "Validate changes using the available test workflows",
        "Maintain clear technical documentation",
        "Review errors and logs when debugging",
        "Follow the project's security and governance practices"
    ]

    return {
        "Status": "Developer Onboarding Guide Created",
        "Onboarding Steps": onboarding_steps,
        "Developer Guidelines": developer_guidelines
    }