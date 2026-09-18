from api_integration.ai_api_registry import get_ai_api_registry
from api_integration.integration_mapping import create_integration_mapping
from api_integration.api_schemas import get_api_schemas
from api_integration.processing_strategy import get_processing_strategy
from api_integration.error_retry_handler import handle_api_error
from api_integration.api_security import define_api_security
from api_integration.integration_report import generate_integration_report


print("=" * 90)
print("DAY 59 - API & INTEGRATION PLANNING TEST")
print("=" * 90)


# Step 1: API Registry
api_registry = get_ai_api_registry()

print("\n[1] AI API REGISTRY")
print("-" * 90)
print(f"Status{' ' * 25}: {api_registry['Status']}")

for api in api_registry["AI APIs"]:
    print(f"API{' ' * 30}: {api}")


# Step 2: Integration Mapping
integration_mapping = create_integration_mapping()

print("\n[2] BACKEND → AI → DATABASE")
print("-" * 90)
print(f"Status{' ' * 25}: {integration_mapping['Status']}")

for item in integration_mapping["Integration Flow"]:
    print(f"\nStage{' ' * 25}: {item['Stage']}")
    print(f"Backend{' ' * 23}: {item['Backend']}")
    print(f"AI Module{' ' * 21}: {item['AI Module']}")
    print(f"Database{' ' * 22}: {item['Database']}")


# Step 3: API Schemas
api_schemas = get_api_schemas()

print("\n[3] API SCHEMAS")
print("-" * 90)
print(f"Status{' ' * 25}: {api_schemas['Status']}")

for api_name, schema in api_schemas["Schemas"].items():
    print(f"\nAPI{' ' * 30}: {api_name}")
    print(f"Request{' ' * 23}: {schema['Request']}")
    print(f"Response{' ' * 22}: {schema['Response']}")


# Step 4: Processing Strategy
processing_strategy = get_processing_strategy()

print("\n[4] PROCESSING STRATEGY")
print("-" * 90)
print(f"Status{' ' * 25}: {processing_strategy['Status']}")

for process, details in processing_strategy["Processing Strategy"].items():
    print(f"\nProcess{' ' * 24}: {process}")
    print(f"Type{' ' * 27}: {details['Processing Type']}")
    print(f"Reason{' ' * 25}: {details['Reason']}")


# Step 5: Error Handling
error_handling = handle_api_error(None)

print("\n[5] ERROR HANDLING")
print("-" * 90)
print(f"Status{' ' * 25}: {error_handling['Status']}")
print(f"Retry Required{' ' * 17}: {error_handling['Retry Required']}")
print(f"Retry Count{' ' * 20}: {error_handling['Retry Count']}")


# Step 6: Security
security = define_api_security()

print("\n[6] API SECURITY")
print("-" * 90)
print(f"Status{' ' * 25}: {security['Status']}")

for key, value in security["Security Requirements"].items():
    print(f"{key:<30}: {value}")


# Step 7: Final Report
report = generate_integration_report(
    api_registry,
    integration_mapping,
    api_schemas,
    processing_strategy,
    error_handling,
    security
)

print("\n[7] FINAL INTEGRATION REPORT")
print("-" * 90)
print(f"Status{' ' * 25}: {report['Status']}")

print("\n" + "=" * 90)
print("API INTEGRATION TEST COMPLETED")
print("=" * 90)