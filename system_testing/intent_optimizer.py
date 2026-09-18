INTENT_KEYWORDS = {

    "experience": [

        "experience",

        "worked",

        "years",

        "role",

        "project"

    ],

    "skills": [

        "skill",

        "skills",

        "tools",

        "technology",

        "technologies",

        "python",

        "sql",

        "java",

        "django",

        "machine learning"

    ],

    "salary": [

        "salary",

        "expected",

        "ctc",

        "pay",

        "package"

    ],

    "availability": [

        "join",

        "joining",

        "notice",

        "immediately",

        "available"

    ],

    "introduction": [

        "introduce",

        "myself",

        "background",

        "about me"

    ]

}


def optimize_intent(text):

    text = text.lower()

    scores = {}

    for intent in INTENT_KEYWORDS:

        scores[intent] = 0

        for keyword in INTENT_KEYWORDS[intent]:

            if keyword in text:

                scores[intent] += 1


    best_intent = max(

        scores,

        key=scores.get

    )


    if scores[best_intent] == 0:

        return "unknown"


    return best_intent