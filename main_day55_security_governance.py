from security_governance.audit_trail import generate_audit_trail

from security_governance.data_retention import (
    load_retention_configuration,
    evaluate_retention_policy
)

from security_governance.consent_management import (
    load_consent_configuration,
    evaluate_consent_policy
)

from security_governance.secure_storage import (
    load_storage_configuration,
    evaluate_secure_storage
)

from security_governance.access_control import (
    evaluate_access_request
)

from security_governance.security_framework import (
    build_security_framework
)

from security_governance.governance_report import (
    generate_governance_report
)


RETENTION_FILE = (
    "data/security_governance/"
    "retention_configuration.txt"
)

CONSENT_FILE = (
    "data/security_governance/"
    "consent_configuration.txt"
)

STORAGE_FILE = (
    "data/security_governance/"
    "storage_configuration.txt"
)


print("=" * 90)
print("- SECURITY & AI GOVERNANCE")
print("=" * 90)


# --------------------------------------------------------------------------
# STEP 1 - AUDIT TRAIL
# --------------------------------------------------------------------------

print("\nSTEP 1 - AUDIT TRAIL SYSTEM")
print("-" * 90)

audit_trail = generate_audit_trail(
    None,
    None
)

print(
    f"{'Status':<40}: "
    f"{audit_trail['Status']}"
)

print(
    f"{'Score Log':<40}: "
    f"{audit_trail['Score Log']['Log Type']}"
)

print(
    f"{'Decision Log':<40}: "
    f"{audit_trail['Decision Log']['Log Type']}"
)


# --------------------------------------------------------------------------
# STEP 2 - DATA RETENTION
# --------------------------------------------------------------------------

print("\nSTEP 2 - DATA RETENTION POLICY")
print("-" * 90)

retention_configuration = load_retention_configuration(
    RETENTION_FILE
)

retention_policy = evaluate_retention_policy(
    retention_configuration
)

print(
    f"{'Status':<40}: "
    f"{retention_policy['Status']}"
)


# --------------------------------------------------------------------------
# STEP 3 - CONSENT MANAGEMENT
# --------------------------------------------------------------------------

print("\nSTEP 3 - CONSENT-BASED DATA USAGE")
print("-" * 90)

consent_configuration = load_consent_configuration(
    CONSENT_FILE
)

consent_policy = evaluate_consent_policy(
    consent_configuration,
    False
)

print(
    f"{'Status':<40}: "
    f"{consent_policy['Status']}"
)

print(
    f"{'Processing Allowed':<40}: "
    f"{consent_policy['Consent Result']['Processing Allowed']}"
)


# --------------------------------------------------------------------------
# STEP 4 - SECURE STORAGE
# --------------------------------------------------------------------------

print("\nSTEP 4 - SECURE STORAGE")
print("-" * 90)

storage_configuration = load_storage_configuration(
    STORAGE_FILE
)

secure_storage = evaluate_secure_storage(
    storage_configuration
)

print(
    f"{'Status':<40}: "
    f"{secure_storage['Status']}"
)


# --------------------------------------------------------------------------
# STEP 5 - ACCESS CONTROL
# --------------------------------------------------------------------------

print("\nSTEP 5 - ACCESS CONTROL")
print("-" * 90)

access_control = evaluate_access_request(
    None,
    None,
    None
)

print(
    f"{'Status':<40}: "
    f"{access_control['Status']}"
)

print(
    f"{'Access Status':<40}: "
    f"{access_control['Access Result']['Status']}"
)


# --------------------------------------------------------------------------
# STEP 6 - SECURITY FRAMEWORK
# --------------------------------------------------------------------------

print("\nSTEP 6 - SECURITY FRAMEWORK")
print("-" * 90)

security_framework = build_security_framework(
    audit_trail,
    retention_policy,
    consent_policy,
    secure_storage,
    access_control
)

print(
    f"{'Status':<40}: "
    f"{security_framework['Framework Status']}"
)


# --------------------------------------------------------------------------
# STEP 7 - GOVERNANCE REPORT
# --------------------------------------------------------------------------

print("\nSTEP 7 - GOVERNANCE REPORT")
print("-" * 90)

governance_report = generate_governance_report(
    audit_trail,
    retention_policy,
    consent_policy,
    secure_storage,
    access_control,
    security_framework
)

print(
    f"{'Status':<40}: "
    f"{governance_report['Report Status']}"
)


# --------------------------------------------------------------------------
# FINAL SYSTEM STATUS
# --------------------------------------------------------------------------

print("\n" + "=" * 90)
print("DAY 55 SECURITY & AI GOVERNANCE PIPELINE COMPLETED")
print("=" * 90)

print("\nFINAL SYSTEM STATUS")
print("-" * 90)

print(
    f"{'Audit Trail':<40}: "
    f"{audit_trail['Status']}"
)

print(
    f"{'Data Retention':<40}: "
    f"{retention_policy['Status']}"
)

print(
    f"{'Consent Management':<40}: "
    f"{consent_policy['Status']}"
)

print(
    f"{'Secure Storage':<40}: "
    f"{secure_storage['Status']}"
)

print(
    f"{'Access Control':<40}: "
    f"{access_control['Status']}"
)

print(
    f"{'Security Framework':<40}: "
    f"{security_framework['Framework Status']}"
)

print(
    f"{'Governance Report':<40}: "
    f"{governance_report['Report Status']}"
)

print("\n" + "=" * 90)
print("COMPLETED SUCCESSFULLY")
print("=" * 90)