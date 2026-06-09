"""
seed_data.py — Demo system for ATO Accelerator.

A fictional DoD mission planning web application at the Moderate baseline.
Represents a realistic mid-ATO-process snapshot: some controls implemented,
some planned, some not started.
"""

from __future__ import annotations

DEMO_SYSTEM = {
    "name": "AESIR Mission Planning System",
    "description": (
        "Web-based mission planning and tasking application used by operational "
        "units to coordinate air and ground missions. Processes sensitive mission "
        "data, personnel rosters, and operational schedules. Hosted on AWS GovCloud "
        "behind a CAC-authenticated gateway."
    ),
    "system_owner": "Maj. Sarah Chen, 412th Operations Group",
    "tech_stack": "Python/FastAPI backend, React frontend, PostgreSQL, AWS GovCloud (IL2), CAC/PKI authentication",
    "data_types": "CUI (Controlled Unclassified Information), mission schedules, personnel data, operational orders",
    "impact_level": "Moderate",
    "confidentiality": "Moderate",
    "integrity": "Moderate",
    "availability": "Moderate",
    "categorization_rationale": (
        "The system processes CUI and operational mission data. Unauthorized disclosure "
        "could compromise personnel safety and operational security (Confidentiality: Moderate). "
        "Integrity failures could result in incorrect mission tasking with potential safety "
        "consequences (Integrity: Moderate). The system supports time-sensitive operational "
        "planning; extended unavailability would seriously degrade mission capability "
        "(Availability: Moderate). Overall impact level: Moderate."
    ),
    # control_id → status
    "control_statuses": {
        # Implemented
        "AC-1": "implemented", "AC-2": "implemented", "AC-3": "implemented",
        "AC-7": "implemented", "AC-8": "implemented", "AC-17": "implemented",
        "AT-1": "implemented", "AT-2": "implemented", "AT-3": "implemented", "AT-4": "implemented",
        "AU-1": "implemented", "AU-2": "implemented", "AU-3": "implemented",
        "AU-4": "implemented", "AU-8": "implemented", "AU-9": "implemented",
        "CA-1": "implemented", "CA-6": "implemented",
        "CM-1": "implemented", "CM-2": "implemented", "CM-6": "implemented",
        "CM-8": "implemented", "CM-10": "implemented", "CM-11": "implemented",
        "CP-1": "implemented", "CP-9": "implemented",
        "IA-1": "implemented", "IA-2": "implemented", "IA-4": "implemented",
        "IA-5": "implemented", "IA-6": "implemented", "IA-7": "implemented",
        "IA-8": "implemented", "IA-11": "implemented",
        "IR-1": "implemented", "IR-4": "implemented", "IR-6": "implemented",
        "IR-8": "implemented",
        "MA-1": "implemented", "MA-2": "implemented", "MA-4": "implemented", "MA-5": "implemented",
        "MP-1": "implemented", "MP-2": "implemented", "MP-6": "implemented", "MP-7": "implemented",
        "PE-1": "implemented", "PE-2": "implemented", "PE-3": "implemented",
        "PE-6": "implemented", "PE-8": "implemented",
        "PL-1": "implemented", "PL-2": "implemented", "PL-4": "implemented",
        "PL-10": "implemented", "PL-11": "implemented",
        "PS-1": "implemented", "PS-2": "implemented", "PS-3": "implemented",
        "PS-4": "implemented", "PS-5": "implemented", "PS-6": "implemented",
        "PS-7": "implemented", "PS-8": "implemented",
        "RA-1": "implemented", "RA-2": "implemented", "RA-3": "implemented",
        "SA-1": "implemented", "SA-2": "implemented", "SA-3": "implemented",
        "SA-4": "implemented", "SA-5": "implemented",
        "SC-1": "implemented", "SC-5": "implemented", "SC-7": "implemented",
        "SC-12": "implemented", "SC-13": "implemented", "SC-39": "implemented",
        "SI-1": "implemented", "SI-2": "implemented", "SI-3": "implemented",
        "SI-4": "implemented", "SI-5": "implemented", "SI-12": "implemented",
        "SR-1": "implemented", "SR-2": "implemented", "SR-3": "implemented", "SR-5": "implemented",
        # Planned
        "AC-4": "planned", "AC-5": "planned", "AC-6": "planned",
        "AC-11": "planned", "AC-12": "planned",
        "AU-5": "planned", "AU-6": "planned", "AU-7": "planned", "AU-11": "planned", "AU-12": "planned",
        "CA-2": "planned", "CA-3": "planned", "CA-5": "planned", "CA-7": "planned", "CA-9": "planned",
        "CM-3": "planned", "CM-4": "planned", "CM-5": "planned", "CM-9": "planned",
        "CP-2": "planned", "CP-3": "planned", "CP-4": "planned",
        "IA-3": "planned", "IA-12": "planned",
        "IR-2": "planned", "IR-3": "planned", "IR-5": "planned", "IR-7": "planned",
        "MA-3": "planned", "MA-6": "planned",
        "MP-3": "planned", "MP-4": "planned", "MP-5": "planned",
        "PE-12": "planned", "PE-13": "planned", "PE-14": "planned",
        "PE-15": "planned", "PE-16": "planned",
        "PL-8": "planned",
        "RA-5": "planned", "RA-7": "planned", "RA-9": "planned",
        "SA-8": "planned", "SA-9": "planned", "SA-10": "planned", "SA-11": "planned",
        "SC-2": "planned", "SC-4": "planned", "SC-8": "planned", "SC-10": "planned",
        "SC-15": "planned", "SC-17": "planned", "SC-18": "planned", "SC-19": "planned",
        "SC-20": "planned", "SC-21": "planned", "SC-22": "planned", "SC-23": "planned",
        "SC-28": "planned",
        "SI-7": "planned", "SI-8": "planned", "SI-10": "planned",
        "SI-11": "planned", "SI-16": "planned",
        "SR-6": "planned", "SR-8": "planned", "SR-11": "planned",
        # Not applicable (cloud-hosted — physical controls inherited from AWS GovCloud)
        "CP-6": "inherited", "CP-7": "inherited", "CP-8": "inherited", "CP-10": "inherited",
        "AC-14": "not_applicable", "AC-18": "not_applicable", "AC-19": "not_applicable",
        "AC-20": "not_applicable", "AC-22": "not_applicable",
    },
    # Pre-generated SSP narrative for one control (AC-2) as demo
    "sample_narrative": {
        "control_id": "AC-2",
        "narrative": (
            "The AESIR Mission Planning System implements account management through a combination "
            "of CAC/PKI-based authentication enforced at the AWS GovCloud gateway and role-based "
            "access controls within the application tier. All user accounts are provisioned by the "
            "designated System Administrator (SA) upon receipt of a DD Form 2875 (System Authorization "
            "Access Request) signed by the user's commander and the Information System Security Officer "
            "(ISSO). Account types include standard user, supervisor, mission planner, and system "
            "administrator, each with defined access privileges documented in the System Security Plan.\n\n"
            "The SA conducts quarterly account reviews using automated reports generated by the "
            "application's audit module. Dormant accounts (inactive for 30 days) are automatically "
            "disabled pending review. Upon separation, PCS/TDY, or change of duty, the user's "
            "commander notifies the SA within 24 hours, and the SA disables the account within one "
            "business day per the Account Management SOP (AESIR-SOP-004). Shared or group accounts "
            "are prohibited except for specific service accounts, which require documented justification "
            "and ISSO approval.\n\n"
            "Evidence of compliance includes the account management audit logs retained for 36 months "
            "in AWS CloudWatch, the DD 2875 archive maintained by the SA, and quarterly account review "
            "reports signed by the ISSO and System Owner. The SA also maintains a current account roster "
            "reconciled against unit personnel rosters monthly."
        ),
    },
}
