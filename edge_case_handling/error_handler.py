from edge_case_handling.audio_checker import check_audio_quality
from edge_case_handling.language_detector import detect_language_mix
from edge_case_handling.missing_answer_handler import (
    check_missing_answers,
    retry_questions
)
from edge_case_handling.safety_fallback import (
    build_safety_report
)


def run_error_handling(

    transcript_path

):

    audio_result = check_audio_quality(

        transcript_path

    )

    language_result = detect_language_mix(

        transcript_path

    )

    missing_result = check_missing_answers(

        transcript_path

    )

    retry_list = retry_questions(

        missing_result

    )

    safety_report = build_safety_report(

        audio_result,

        language_result,

        missing_result

    )

    return {

        "audio_result": audio_result,

        "language_result": language_result,

        "missing_result": missing_result,

        "retry_questions": retry_list,

        "safety_report": safety_report

    }