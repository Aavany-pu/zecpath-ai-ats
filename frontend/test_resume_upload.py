from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from frontend.resume_upload import find_resume_files


RESUME_DIRECTORY = PROJECT_ROOT / "data" / "resumes"

result = find_resume_files(RESUME_DIRECTORY)

print("=" * 90)
print("FRONTEND - RESUME INPUT")
print("=" * 90)

print(f"{'Status':<30}: {result['Status']}")
print(f"{'Resume Files Found':<30}: {len(result['Resume Files'])}")

for resume in result["Resume Files"]:
    print(f"  - {resume}")

print("=" * 90)