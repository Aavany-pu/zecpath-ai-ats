from system_finalization.system_summary import build_system_summary
from system_finalization.api_documentation import generate_api_documentation
from system_finalization.demo_runner import run_demo
from system_finalization.evaluation_report import generate_evaluation_report


def print_heading(title):

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)


def display(data):

    if isinstance(data, dict):

        for key, value in data.items():

            print(f"\n{key}")

            print("-" * 60)

            print(value)

    elif isinstance(data, list):

        for item in data:

            print(item)

    else:

        print(data)


def main():

    print_heading("ZECPATH AI SCREENING SYSTEM")

    system_summary = build_system_summary()

    print_heading("1. COMPLETE AI SCREENING SYSTEM")

    display(system_summary)


    api_documentation = generate_api_documentation()

    print_heading("2. API DESIGN")

    display(api_documentation)


    demo = run_demo()

    print_heading("3. END TO END AI SCREENING DEMO")

    display(demo)


    evaluation = generate_evaluation_report()

    print_heading("4. SCREENING AI EVALUATION REPORT")

    display(evaluation)


    print_heading("SYSTEM FINALIZATION COMPLETED")


if __name__ == "__main__":

    main()