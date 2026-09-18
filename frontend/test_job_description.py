from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from frontend.job_description import find_job_descriptions


JOB_DESCRIPTION_DIRECTORY = PROJECT_ROOT / "data" / "job_descriptions"

result = find_job_descriptions(JOB_DESCRIPTION_DIRECTORY)

print("=" * 90)
print("FRONTEND - JOB DESCRIPTION INPUT")
print("=" * 90)

print(f"{'Status':<30}: {result['Status']}")
print(
    f"{'Job Descriptions Found':<30}: "
    f"{len(result['Job Descriptions'])}"
)

for job_description in result["Job Descriptions"]:
    print(f"  - {job_description}")

print("=" * 90)