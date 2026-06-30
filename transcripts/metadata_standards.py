def create_metadata(

    resume_file,

    skills,

    experience

):

    metadata = {

        "resume_file":
        resume_file,

        "skill_count":
        len(skills),

        "experience":
        experience
    }

    return metadata