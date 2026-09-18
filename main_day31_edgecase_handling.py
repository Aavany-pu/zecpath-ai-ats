from edge_case_handling.error_handler import run_error_handling
from edge_case_handling.safety_fallback import get_fallback_response

transcript_path = "data/transcripts/interview_transcript.txt"

result = run_error_handling(transcript_path)



print("Audio Result")
print(result["audio_result"])

if result["audio_result"]["quality"] == "POOR":
    print("Fallback Response")
    print(get_fallback_response("poor_audio"))

print("\nLanguage Result")
print(result["language_result"])

if result["language_result"]["mixed_language"]:
    print("Fallback Response")
    print(get_fallback_response("language_mix"))

print("\nMissing Answer Result")
print(result["missing_result"])

if result["missing_result"]["retry_required"]:
    print("Fallback Response")
    print(get_fallback_response("missing_answer"))

print("\nRetry Questions")
for retry in result["retry_questions"]:
    print(retry)

print("\nSafety Report")
print(result["safety_report"])

if not result["safety_report"]["system_safe"]:
    print("\nOverall System Fallback")
    print(get_fallback_response("unknown"))

print("\nedgecase_handling.py executed successfully.")