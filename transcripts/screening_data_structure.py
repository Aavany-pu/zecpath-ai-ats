def create_screening_data(

    resume_file,

    skills,

    experience

):

    screening_data = {

        "candidate_data": {

            "resume":
            resume_file,

            "skills":
            skills,

            "experience":
            experience
        }
    }

    return screening_data