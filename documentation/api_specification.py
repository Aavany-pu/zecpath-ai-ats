def load_api_endpoints(file_path):
    endpoints = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line == "API Endpoints":
                continue

            endpoints.append(line)

    return endpoints


def generate_api_specification(file_path):
    endpoints = load_api_endpoints(file_path)

    specification = {
        "Title": "HR Interview AI - API Specification",
        "Endpoint Count": len(
            [
                item for item in endpoints
                if item.startswith(("GET ", "POST ", "PUT ", "DELETE "))
            ]
        ),
        "Endpoints": endpoints
    }

    return specification