from answer_engine.intent_classifier import (
    classify_intent
)

from answer_engine.answer_understanding import (
    understand_answer
)

from answer_engine.semantic_formatter import (
    create_semantic_object
)

candidate_answers = [

    "I have 3 years of Python and SQL experience.",

    "My expected salary is 8 LPA.",

    "I can join immediately."
]

print("=" * 60)
print("DAY 25 - ANSWER INTENT & UNDERSTANDING")
print("=" * 60)

for answer in candidate_answers:

    intent = classify_intent(
        answer
    )

    extracted = understand_answer(
        answer
    )

    semantic = create_semantic_object(

        intent,

        extracted
    )

    print()
    print("Answer :", answer)
    print("Intent :", intent)
    print("Extracted :", extracted)
    print("Semantic Object :", semantic)