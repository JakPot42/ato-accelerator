"""
nist_controls.py — NIST SP 800-53 Rev 5 control catalog (curated subset).

Includes the most critical controls across all 20 families for Low, Moderate,
and High baselines. Source: NIST SP 800-53 Rev 5 (public domain).

Baseline codes: L = Low, M = Moderate, H = High
Each higher baseline includes all lower baseline controls.
"""

from __future__ import annotations

# Each control: id, family, title, baseline (lowest level where required), description
CONTROLS: list[dict] = [
    # =========================================================================
    # AC — Access Control
    # =========================================================================
    {"id": "AC-1",  "family": "AC", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate access control policy and procedures."},
    {"id": "AC-2",  "family": "AC", "title": "Account Management",                     "baseline": "L", "description": "Manage system accounts including establishing, activating, modifying, reviewing, disabling, and removing accounts."},
    {"id": "AC-3",  "family": "AC", "title": "Access Enforcement",                     "baseline": "L", "description": "Enforce approved authorizations for logical access to information and system resources."},
    {"id": "AC-4",  "family": "AC", "title": "Information Flow Enforcement",           "baseline": "M", "description": "Enforce approved authorizations for controlling the flow of information within the system and between connected systems."},
    {"id": "AC-5",  "family": "AC", "title": "Separation of Duties",                   "baseline": "M", "description": "Separate duties of individuals to reduce risk of malevolent activity without collusion."},
    {"id": "AC-6",  "family": "AC", "title": "Least Privilege",                        "baseline": "M", "description": "Employ the principle of least privilege, allowing only authorized accesses necessary to accomplish assigned tasks."},
    {"id": "AC-7",  "family": "AC", "title": "Unsuccessful Logon Attempts",            "baseline": "L", "description": "Enforce a limit of consecutive invalid logon attempts and lock the account for a specified time period."},
    {"id": "AC-8",  "family": "AC", "title": "System Use Notification",                "baseline": "L", "description": "Display an approved system use notification message before granting access."},
    {"id": "AC-11", "family": "AC", "title": "Device Lock",                            "baseline": "M", "description": "Prevent further access after a defined period of inactivity via session lock."},
    {"id": "AC-12", "family": "AC", "title": "Session Termination",                    "baseline": "M", "description": "Automatically terminate a session after a defined condition."},
    {"id": "AC-14", "family": "AC", "title": "Permitted Actions Without Identification","baseline": "L", "description": "Identify and document actions that can be performed without identification or authentication."},
    {"id": "AC-17", "family": "AC", "title": "Remote Access",                          "baseline": "L", "description": "Establish usage restrictions and implementation guidance for remote access and authorize remote access before allowing connections."},
    {"id": "AC-18", "family": "AC", "title": "Wireless Access",                        "baseline": "L", "description": "Establish usage restrictions and implementation guidance for wireless access and authorize wireless access before allowing connections."},
    {"id": "AC-19", "family": "AC", "title": "Access Control for Mobile Devices",      "baseline": "L", "description": "Establish usage restrictions and implementation guidance for mobile devices and authorize connection of mobile devices."},
    {"id": "AC-20", "family": "AC", "title": "Use of External Systems",                "baseline": "L", "description": "Establish terms and conditions for authorized individuals to access the system from external systems."},
    {"id": "AC-22", "family": "AC", "title": "Publicly Accessible Content",            "baseline": "L", "description": "Designate individuals authorized to post information on publicly accessible systems and review proposed content."},

    # =========================================================================
    # AT — Awareness and Training
    # =========================================================================
    {"id": "AT-1",  "family": "AT", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate security and privacy awareness and training policy."},
    {"id": "AT-2",  "family": "AT", "title": "Literacy Training and Awareness",        "baseline": "L", "description": "Provide security and privacy literacy training as part of initial and ongoing training."},
    {"id": "AT-3",  "family": "AT", "title": "Role-Based Training",                    "baseline": "L", "description": "Provide role-based security and privacy training to personnel with assigned security and privacy roles and responsibilities."},
    {"id": "AT-4",  "family": "AT", "title": "Training Records",                       "baseline": "L", "description": "Document and monitor information security and privacy training activities and retain training records."},

    # =========================================================================
    # AU — Audit and Accountability
    # =========================================================================
    {"id": "AU-1",  "family": "AU", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate audit and accountability policy and procedures."},
    {"id": "AU-2",  "family": "AU", "title": "Event Logging",                          "baseline": "L", "description": "Identify the types of events that the system is capable of logging in support of the audit function."},
    {"id": "AU-3",  "family": "AU", "title": "Content of Audit Records",               "baseline": "L", "description": "Ensure audit records contain information to establish what events occurred, the source, and the outcome."},
    {"id": "AU-4",  "family": "AU", "title": "Audit Log Storage Capacity",             "baseline": "L", "description": "Allocate audit log storage capacity to accommodate defined audit log retention requirements."},
    {"id": "AU-5",  "family": "AU", "title": "Response to Audit Logging Process Failures","baseline": "L", "description": "Alert personnel in the event of an audit logging process failure and take defined actions."},
    {"id": "AU-6",  "family": "AU", "title": "Audit Record Review, Analysis, and Reporting","baseline": "L", "description": "Review and analyze system audit records for indications of inappropriate activity and report findings."},
    {"id": "AU-7",  "family": "AU", "title": "Audit Record Reduction and Report Generation","baseline": "M", "description": "Provide audit record reduction and report generation to support on-demand review and after-the-fact analysis."},
    {"id": "AU-8",  "family": "AU", "title": "Time Stamps",                            "baseline": "L", "description": "Use internal system clocks to generate time stamps for audit records."},
    {"id": "AU-9",  "family": "AU", "title": "Protection of Audit Information",        "baseline": "L", "description": "Protect audit information and tools from unauthorized access, modification, and deletion."},
    {"id": "AU-11", "family": "AU", "title": "Audit Record Retention",                 "baseline": "L", "description": "Retain audit records for a defined time period to provide support for after-the-fact investigations."},
    {"id": "AU-12", "family": "AU", "title": "Audit Record Generation",                "baseline": "L", "description": "Provide audit record generation capability for the event types defined and allow designated personnel to select which events are audited."},

    # =========================================================================
    # CA — Assessment, Authorization, and Monitoring
    # =========================================================================
    {"id": "CA-1",  "family": "CA", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate assessment, authorization, and monitoring policy."},
    {"id": "CA-2",  "family": "CA", "title": "Control Assessments",                    "baseline": "L", "description": "Select and assess the controls in the system to determine if they are implemented correctly and producing the desired outcome."},
    {"id": "CA-3",  "family": "CA", "title": "Information Exchange",                   "baseline": "L", "description": "Approve and manage the exchange of information between the system and other systems using ISAs or MOUs."},
    {"id": "CA-5",  "family": "CA", "title": "Plan of Action and Milestones",          "baseline": "L", "description": "Develop a POA&M for the system to document planned remediation actions to correct weaknesses or deficiencies."},
    {"id": "CA-6",  "family": "CA", "title": "Authorization",                          "baseline": "L", "description": "Assign a senior official as the authorizing official (AO), ensure the AO authorizes the system before operation, and update the authorization."},
    {"id": "CA-7",  "family": "CA", "title": "Continuous Monitoring",                  "baseline": "L", "description": "Develop a continuous monitoring strategy and implement a program that includes ongoing assessments of control effectiveness."},
    {"id": "CA-8",  "family": "CA", "title": "Penetration Testing",                    "baseline": "H", "description": "Require penetration testing of the system at defined frequency and when significant changes occur."},
    {"id": "CA-9",  "family": "CA", "title": "Internal System Connections",            "baseline": "L", "description": "Authorize internal connections of system components and document interface characteristics and security requirements."},

    # =========================================================================
    # CM — Configuration Management
    # =========================================================================
    {"id": "CM-1",  "family": "CM", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate configuration management policy and procedures."},
    {"id": "CM-2",  "family": "CM", "title": "Baseline Configuration",                 "baseline": "L", "description": "Develop, document, and maintain a current baseline configuration of the system."},
    {"id": "CM-3",  "family": "CM", "title": "Configuration Change Control",           "baseline": "M", "description": "Determine the types of changes that are configuration-controlled and review and approve changes with security analysis."},
    {"id": "CM-4",  "family": "CM", "title": "Impact Analyses",                        "baseline": "M", "description": "Analyze changes to the system to determine potential security and privacy impacts prior to implementation."},
    {"id": "CM-5",  "family": "CM", "title": "Access Restrictions for Change",         "baseline": "M", "description": "Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system."},
    {"id": "CM-6",  "family": "CM", "title": "Configuration Settings",                 "baseline": "L", "description": "Establish and document configuration settings that reflect the most restrictive mode consistent with operational requirements."},
    {"id": "CM-7",  "family": "CM", "title": "Least Functionality",                    "baseline": "L", "description": "Configure the system to provide only essential capabilities, prohibiting or restricting the use of functions, ports, protocols, and services."},
    {"id": "CM-8",  "family": "CM", "title": "System Component Inventory",             "baseline": "L", "description": "Develop and document an inventory of system components that accurately reflects the current system."},
    {"id": "CM-9",  "family": "CM", "title": "Configuration Management Plan",          "baseline": "M", "description": "Develop, document, and implement a configuration management plan for the system."},
    {"id": "CM-10", "family": "CM", "title": "Software Usage Restrictions",            "baseline": "L", "description": "Use software and associated documentation in accordance with contract agreements and copyright laws."},
    {"id": "CM-11", "family": "CM", "title": "User-Installed Software",                "baseline": "L", "description": "Establish policies governing the installation of software by users and enforce software installation policies."},

    # =========================================================================
    # CP — Contingency Planning
    # =========================================================================
    {"id": "CP-1",  "family": "CP", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate contingency planning policy and procedures."},
    {"id": "CP-2",  "family": "CP", "title": "Contingency Plan",                       "baseline": "L", "description": "Develop a contingency plan for the system addressing contingency roles, responsibilities, assigned individuals, and activities."},
    {"id": "CP-3",  "family": "CP", "title": "Contingency Training",                   "baseline": "L", "description": "Provide contingency training to system users consistent with assigned roles and responsibilities."},
    {"id": "CP-4",  "family": "CP", "title": "Contingency Plan Testing",               "baseline": "L", "description": "Test the contingency plan to determine the effectiveness of the plan and the readiness to execute the plan."},
    {"id": "CP-6",  "family": "CP", "title": "Alternate Storage Site",                 "baseline": "M", "description": "Establish an alternate storage site and initiate necessary agreements to permit the transfer and storage of backup information."},
    {"id": "CP-7",  "family": "CP", "title": "Alternate Processing Site",              "baseline": "M", "description": "Establish an alternate processing site and initiate necessary agreements for processing capability in the event of primary site disruption."},
    {"id": "CP-8",  "family": "CP", "title": "Telecommunications Services",            "baseline": "M", "description": "Establish alternate telecommunications services to resume operations when primary telecommunications capabilities are unavailable."},
    {"id": "CP-9",  "family": "CP", "title": "System Backup",                          "baseline": "L", "description": "Conduct backups of user-level information, system-level information, and system documentation at defined frequencies."},
    {"id": "CP-10", "family": "CP", "title": "System Recovery and Reconstitution",     "baseline": "L", "description": "Provide for the recovery and reconstitution of the system to a known state within defined time periods after a disruption."},

    # =========================================================================
    # IA — Identification and Authentication
    # =========================================================================
    {"id": "IA-1",  "family": "IA", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate identification and authentication policy and procedures."},
    {"id": "IA-2",  "family": "IA", "title": "Identification and Authentication (Org. Users)","baseline": "L", "description": "Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users."},
    {"id": "IA-3",  "family": "IA", "title": "Device Identification and Authentication","baseline": "M", "description": "Uniquely identify and authenticate devices before establishing connections to the system."},
    {"id": "IA-4",  "family": "IA", "title": "Identifier Management",                  "baseline": "L", "description": "Manage system identifiers by receiving authorization, selecting identifiers, assigning identifiers to intended subjects, and preventing reuse."},
    {"id": "IA-5",  "family": "IA", "title": "Authenticator Management",               "baseline": "L", "description": "Manage system authenticators by verifying identity, establishing content, setting/changing defaults, protecting authenticators, and rotating."},
    {"id": "IA-6",  "family": "IA", "title": "Authentication Feedback",                "baseline": "L", "description": "Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation."},
    {"id": "IA-7",  "family": "IA", "title": "Cryptographic Module Authentication",   "baseline": "L", "description": "Implement mechanisms for authentication to a cryptographic module that meet applicable federal laws and standards."},
    {"id": "IA-8",  "family": "IA", "title": "Identification and Authentication (Non-Org. Users)","baseline": "L", "description": "Uniquely identify and authenticate non-organizational users and processes acting on their behalf."},
    {"id": "IA-11", "family": "IA", "title": "Re-Authentication",                      "baseline": "L", "description": "Require users to re-authenticate when defined circumstances or situations require re-authentication."},
    {"id": "IA-12", "family": "IA", "title": "Identity Proofing",                      "baseline": "M", "description": "Identity proof users that require accounts for logical access to systems based on appropriate assurance level requirements."},

    # =========================================================================
    # IR — Incident Response
    # =========================================================================
    {"id": "IR-1",  "family": "IR", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate incident response policy and procedures."},
    {"id": "IR-2",  "family": "IR", "title": "Incident Response Training",             "baseline": "L", "description": "Provide incident response training to system users consistent with assigned roles and responsibilities."},
    {"id": "IR-3",  "family": "IR", "title": "Incident Response Testing",              "baseline": "M", "description": "Test the incident response capability using defined tests to determine the effectiveness of the incident response capability."},
    {"id": "IR-4",  "family": "IR", "title": "Incident Handling",                      "baseline": "L", "description": "Implement an incident handling capability for incidents that includes preparation, detection, analysis, containment, eradication, and recovery."},
    {"id": "IR-5",  "family": "IR", "title": "Incident Monitoring",                    "baseline": "L", "description": "Track and document incidents using defined automated mechanisms."},
    {"id": "IR-6",  "family": "IR", "title": "Incident Reporting",                     "baseline": "L", "description": "Require personnel to report suspected incidents to the organizational incident response capability within defined time period."},
    {"id": "IR-7",  "family": "IR", "title": "Incident Response Assistance",           "baseline": "L", "description": "Provide an incident response support resource that offers advice and assistance to users of the system for handling incidents."},
    {"id": "IR-8",  "family": "IR", "title": "Incident Response Plan",                 "baseline": "L", "description": "Develop an incident response plan addressing roles/responsibilities, incident definition, procedures, reporting, and plan review."},

    # =========================================================================
    # MA — Maintenance
    # =========================================================================
    {"id": "MA-1",  "family": "MA", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate maintenance policy and procedures."},
    {"id": "MA-2",  "family": "MA", "title": "Controlled Maintenance",                 "baseline": "L", "description": "Schedule, document, and review records of maintenance and repairs on system components."},
    {"id": "MA-3",  "family": "MA", "title": "Maintenance Tools",                      "baseline": "M", "description": "Approve, control, and monitor the use of system maintenance tools."},
    {"id": "MA-4",  "family": "MA", "title": "Nonlocal Maintenance",                   "baseline": "L", "description": "Approve, monitor, and control nonlocal maintenance and diagnostic activities."},
    {"id": "MA-5",  "family": "MA", "title": "Maintenance Personnel",                  "baseline": "L", "description": "Establish a process for maintenance personnel authorization and maintain a list of authorized maintenance organizations or personnel."},
    {"id": "MA-6",  "family": "MA", "title": "Timely Maintenance",                     "baseline": "M", "description": "Obtain maintenance support and/or spare parts for defined system components within a defined time period of failure."},

    # =========================================================================
    # MP — Media Protection
    # =========================================================================
    {"id": "MP-1",  "family": "MP", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate media protection policy and procedures."},
    {"id": "MP-2",  "family": "MP", "title": "Media Access",                           "baseline": "L", "description": "Restrict access to digital and non-digital media containing information to authorized individuals."},
    {"id": "MP-3",  "family": "MP", "title": "Media Marking",                          "baseline": "M", "description": "Mark system media indicating distribution limitations, handling caveats, and applicable security markings."},
    {"id": "MP-4",  "family": "MP", "title": "Media Storage",                          "baseline": "M", "description": "Physically control and securely store digital and non-digital media within controlled areas."},
    {"id": "MP-5",  "family": "MP", "title": "Media Transport",                        "baseline": "M", "description": "Protect and control digital and non-digital media during transport outside controlled areas."},
    {"id": "MP-6",  "family": "MP", "title": "Media Sanitization",                     "baseline": "L", "description": "Sanitize system media prior to disposal, release out of organizational control, or release for reuse."},
    {"id": "MP-7",  "family": "MP", "title": "Media Use",                              "baseline": "L", "description": "Restrict or prohibit the use of defined types of system media on defined system components."},

    # =========================================================================
    # PE — Physical and Environmental Protection
    # =========================================================================
    {"id": "PE-1",  "family": "PE", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate physical and environmental protection policy and procedures."},
    {"id": "PE-2",  "family": "PE", "title": "Physical Access Authorizations",         "baseline": "L", "description": "Develop and maintain a list of individuals with authorized access to the facility containing the system."},
    {"id": "PE-3",  "family": "PE", "title": "Physical Access Control",                "baseline": "L", "description": "Enforce physical access authorizations and maintain audit logs of physical access."},
    {"id": "PE-6",  "family": "PE", "title": "Monitoring Physical Access",             "baseline": "L", "description": "Monitor physical access to the facility to detect and respond to physical security incidents."},
    {"id": "PE-8",  "family": "PE", "title": "Visitor Access Records",                 "baseline": "L", "description": "Maintain visitor access records to the facility containing the system for a defined period."},
    {"id": "PE-12", "family": "PE", "title": "Emergency Lighting",                     "baseline": "L", "description": "Employ and maintain automatic emergency lighting for the system that activates in the event of a power outage."},
    {"id": "PE-13", "family": "PE", "title": "Fire Protection",                        "baseline": "L", "description": "Employ and maintain fire suppression and detection devices/systems for the system."},
    {"id": "PE-14", "family": "PE", "title": "Environmental Controls",                 "baseline": "L", "description": "Maintain temperature and humidity levels within the facility where the system resides at defined acceptable levels."},
    {"id": "PE-15", "family": "PE", "title": "Water Damage Protection",                "baseline": "L", "description": "Protect the system from damage resulting from water leakage by providing master shutoff valves."},
    {"id": "PE-16", "family": "PE", "title": "Delivery and Removal",                   "baseline": "L", "description": "Authorize and control information system components entering and exiting the facility."},

    # =========================================================================
    # PL — Planning
    # =========================================================================
    {"id": "PL-1",  "family": "PL", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate planning policy and procedures."},
    {"id": "PL-2",  "family": "PL", "title": "System Security and Privacy Plans",      "baseline": "L", "description": "Develop SSP/PMP describing operational context, categorization, connections, controls, and implementation status."},
    {"id": "PL-4",  "family": "PL", "title": "Rules of Behavior",                      "baseline": "L", "description": "Establish and provide users with rules of behavior for the system before authorizing access."},
    {"id": "PL-8",  "family": "PL", "title": "Security and Privacy Architectures",     "baseline": "M", "description": "Develop security and privacy architectures for the system that describe requirements, approach, assumptions, and risk decisions."},
    {"id": "PL-10", "family": "PL", "title": "Baseline Selection",                     "baseline": "L", "description": "Select a control baseline for the system."},
    {"id": "PL-11", "family": "PL", "title": "Baseline Tailoring",                     "baseline": "L", "description": "Tailor the selected control baseline by applying specified tailoring actions."},

    # =========================================================================
    # PS — Personnel Security
    # =========================================================================
    {"id": "PS-1",  "family": "PS", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate personnel security policy and procedures."},
    {"id": "PS-2",  "family": "PS", "title": "Position Risk Designation",              "baseline": "L", "description": "Assign a risk designation to all organizational positions and establish screening criteria for positions."},
    {"id": "PS-3",  "family": "PS", "title": "Personnel Screening",                    "baseline": "L", "description": "Screen individuals prior to authorizing access to the system and re-screen individuals according to defined conditions."},
    {"id": "PS-4",  "family": "PS", "title": "Personnel Termination",                  "baseline": "L", "description": "Upon termination, disable system access, conduct exit interviews, retrieve authenticators, and notify security personnel."},
    {"id": "PS-5",  "family": "PS", "title": "Personnel Transfer",                     "baseline": "L", "description": "Review and confirm ongoing operational need for access authorizations when personnel are transferred."},
    {"id": "PS-6",  "family": "PS", "title": "Access Agreements",                      "baseline": "L", "description": "Establish and document access agreements for organizational systems, review and update agreements, and re-sign on transfer."},
    {"id": "PS-7",  "family": "PS", "title": "External Personnel Security",            "baseline": "L", "description": "Establish personnel security requirements including security roles and responsibilities for external providers."},
    {"id": "PS-8",  "family": "PS", "title": "Personnel Sanctions",                    "baseline": "L", "description": "Employ a formal sanctions process for individuals failing to comply with established information security and privacy policies."},

    # =========================================================================
    # RA — Risk Assessment
    # =========================================================================
    {"id": "RA-1",  "family": "RA", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate risk assessment policy and procedures."},
    {"id": "RA-2",  "family": "RA", "title": "Security Categorization",                "baseline": "L", "description": "Categorize the system and information it processes, stores, and transmits consistent with applicable laws and FIPS 199."},
    {"id": "RA-3",  "family": "RA", "title": "Risk Assessment",                        "baseline": "L", "description": "Conduct a risk assessment and document results including threats, vulnerabilities, likelihood, impact, and risk determination."},
    {"id": "RA-5",  "family": "RA", "title": "Vulnerability Monitoring and Scanning",  "baseline": "L", "description": "Monitor and scan for vulnerabilities in the system at defined frequencies and when new vulnerabilities are identified."},
    {"id": "RA-7",  "family": "RA", "title": "Risk Response",                          "baseline": "L", "description": "Respond to findings from security assessments, monitoring, and audits consistent with organizational risk tolerance."},
    {"id": "RA-9",  "family": "RA", "title": "Criticality Analysis",                   "baseline": "M", "description": "Identify critical system components and functions by performing a criticality analysis."},

    # =========================================================================
    # SA — System and Services Acquisition
    # =========================================================================
    {"id": "SA-1",  "family": "SA", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate system and services acquisition policy and procedures."},
    {"id": "SA-2",  "family": "SA", "title": "Allocation of Resources",                "baseline": "L", "description": "Determine, document, and allocate the resources required to protect the system as part of the organizational capital planning process."},
    {"id": "SA-3",  "family": "SA", "title": "System Development Life Cycle",          "baseline": "L", "description": "Acquire, develop, and manage the system using a system development life cycle incorporating security and privacy considerations."},
    {"id": "SA-4",  "family": "SA", "title": "Acquisition Process",                    "baseline": "L", "description": "Include security and privacy requirements in acquisition contracts for systems, system components, and system services."},
    {"id": "SA-5",  "family": "SA", "title": "System Documentation",                   "baseline": "L", "description": "Obtain or develop administrator documentation for the system describing secure configuration, installation, and operation."},
    {"id": "SA-8",  "family": "SA", "title": "Security and Privacy Engineering Principles","baseline": "M","description": "Apply security and privacy engineering principles in the specification, design, development, and modification of the system."},
    {"id": "SA-9",  "family": "SA", "title": "External System Services",               "baseline": "L", "description": "Require external providers to comply with organizational security and privacy requirements and monitor provider compliance."},
    {"id": "SA-10", "family": "SA", "title": "Developer Configuration Management",     "baseline": "M", "description": "Require developers to perform configuration management during development including tracking security flaws and remediation."},
    {"id": "SA-11", "family": "SA", "title": "Developer Testing and Evaluation",       "baseline": "M", "description": "Require developers to implement a security and privacy assessment plan and perform testing at defined stages."},

    # =========================================================================
    # SC — System and Communications Protection
    # =========================================================================
    {"id": "SC-1",  "family": "SC", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate system and communications protection policy and procedures."},
    {"id": "SC-2",  "family": "SC", "title": "Separation of System and User Functionality","baseline": "M","description": "Separate user functionality (including user interface services) from system management functionality."},
    {"id": "SC-4",  "family": "SC", "title": "Information in Shared System Resources", "baseline": "M", "description": "Prevent unauthorized and unintended information transfer via shared system resources."},
    {"id": "SC-5",  "family": "SC", "title": "Denial-of-Service Protection",           "baseline": "L", "description": "Protect against and limit the effects of denial-of-service events."},
    {"id": "SC-7",  "family": "SC", "title": "Boundary Protection",                    "baseline": "L", "description": "Monitor and control communications at the external boundary and at key internal boundaries of the system."},
    {"id": "SC-8",  "family": "SC", "title": "Transmission Confidentiality and Integrity","baseline": "M","description": "Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of information during transmission."},
    {"id": "SC-10", "family": "SC", "title": "Network Disconnect",                     "baseline": "M", "description": "Terminate the network connection associated with a communications session at the end of the session or after a defined period of inactivity."},
    {"id": "SC-12", "family": "SC", "title": "Cryptographic Key Establishment and Management","baseline": "L","description": "Establish and manage cryptographic keys when cryptography is employed within the system."},
    {"id": "SC-13", "family": "SC", "title": "Cryptographic Protection",               "baseline": "L", "description": "Implement the following types of cryptography for defined cryptographic uses: FIPS-validated or NSA-approved cryptography."},
    {"id": "SC-15", "family": "SC", "title": "Collaborative Computing Devices and Applications","baseline": "L","description": "Prohibit remote activation of collaborative computing devices and provide an explicit indication of use to present users."},
    {"id": "SC-17", "family": "SC", "title": "Public Key Infrastructure Certificates", "baseline": "M", "description": "Issue public key certificates under an appropriate certificate policy or obtain from an approved service provider."},
    {"id": "SC-18", "family": "SC", "title": "Mobile Code",                            "baseline": "M", "description": "Define acceptable and unacceptable mobile code and technologies, authorize use, and prevent use of unacceptable mobile code."},
    {"id": "SC-19", "family": "SC", "title": "Voice Over Internet Protocol",           "baseline": "M", "description": "Establish usage restrictions and implementation guidance for VoIP technologies and authorize use within the system."},
    {"id": "SC-20", "family": "SC", "title": "Secure Name/Address Resolution Service (Auth.)","baseline": "L","description": "Provide additional data origin authentication and integrity verification artifacts with authoritative name resolution data."},
    {"id": "SC-21", "family": "SC", "title": "Secure Name/Address Resolution Service (Recur.)","baseline": "L","description": "Request and perform data origin authentication and data integrity verification on DNS resolution responses."},
    {"id": "SC-22", "family": "SC", "title": "Architecture and Provisioning for Name/Address Resolution","baseline": "L","description": "Ensure the systems that collectively provide name/address resolution service are fault-tolerant and implement role separation."},
    {"id": "SC-23", "family": "SC", "title": "Session Authenticity",                   "baseline": "M", "description": "Protect the authenticity of communications sessions."},
    {"id": "SC-28", "family": "SC", "title": "Protection of Information at Rest",      "baseline": "M", "description": "Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of information at rest."},
    {"id": "SC-39", "family": "SC", "title": "Process Isolation",                      "baseline": "L", "description": "Maintain a separate execution domain for each executing process."},

    # =========================================================================
    # SI — System and Information Integrity
    # =========================================================================
    {"id": "SI-1",  "family": "SI", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate system and information integrity policy and procedures."},
    {"id": "SI-2",  "family": "SI", "title": "Flaw Remediation",                       "baseline": "L", "description": "Identify, report, and correct system flaws; test software/firmware updates before installation; install security-relevant updates."},
    {"id": "SI-3",  "family": "SI", "title": "Malicious Code Protection",              "baseline": "L", "description": "Implement malicious code protection at entry and exit points and system components to detect and eradicate malicious code."},
    {"id": "SI-4",  "family": "SI", "title": "System Monitoring",                      "baseline": "L", "description": "Monitor the system to detect attacks and indicators of potential attacks, and unauthorized connections."},
    {"id": "SI-5",  "family": "SI", "title": "Security Alerts, Advisories, and Directives","baseline": "L","description": "Receive security alerts, advisories, and directives from defined external organizations and disseminate to defined personnel."},
    {"id": "SI-6",  "family": "SI", "title": "Security and Privacy Function Verification","baseline": "H","description": "Verify the correct operation of defined security and privacy functions and notify defined personnel of failed verification."},
    {"id": "SI-7",  "family": "SI", "title": "Software, Firmware, and Information Integrity","baseline": "M","description": "Employ integrity verification tools to detect unauthorized changes to software, firmware, and information."},
    {"id": "SI-8",  "family": "SI", "title": "Spam Protection",                        "baseline": "M", "description": "Employ spam protection mechanisms at system entry and exit points to detect and act on unsolicited messages."},
    {"id": "SI-10", "family": "SI", "title": "Information Input Validation",           "baseline": "M", "description": "Check the validity of information inputs to the system."},
    {"id": "SI-11", "family": "SI", "title": "Error Handling",                         "baseline": "M", "description": "Generate error messages that provide information necessary for corrective actions without revealing information that could be exploited."},
    {"id": "SI-12", "family": "SI", "title": "Information Management and Retention",   "baseline": "L", "description": "Manage and retain information within the system and information output consistent with applicable laws and organizational policies."},
    {"id": "SI-16", "family": "SI", "title": "Memory Protection",                      "baseline": "M", "description": "Implement the following controls to protect the system memory from unauthorized code execution: data execution prevention, address space layout randomization."},

    # =========================================================================
    # SR — Supply Chain Risk Management
    # =========================================================================
    {"id": "SR-1",  "family": "SR", "title": "Policy and Procedures",                  "baseline": "L", "description": "Develop, document, and disseminate supply chain risk management policy and procedures."},
    {"id": "SR-2",  "family": "SR", "title": "Supply Chain Risk Management Plan",      "baseline": "L", "description": "Develop a plan for managing supply chain risks associated with the research and development, design, manufacturing, and acquisition of systems."},
    {"id": "SR-3",  "family": "SR", "title": "Supply Chain Controls and Processes",    "baseline": "L", "description": "Establish a process or processes to identify and address weaknesses or deficiencies in the supply chain elements."},
    {"id": "SR-5",  "family": "SR", "title": "Acquisition Strategies, Tools, and Methods","baseline": "L","description": "Employ acquisition strategies, contract tools, and procurement methods to protect against, identify, and mitigate supply chain risks."},
    {"id": "SR-6",  "family": "SR", "title": "Supplier Assessments and Reviews",       "baseline": "M", "description": "Assess and review the supply chain-related risks associated with suppliers or contractors and the system, system component, or service they provide."},
    {"id": "SR-8",  "family": "SR", "title": "Notification Agreements",                "baseline": "M", "description": "Establish agreements and procedures with entities involved in the supply chain for the system to notify the organization of any compromises."},
    {"id": "SR-10", "family": "SR", "title": "Inspection of Systems or Components",    "baseline": "H", "description": "Inspect the system or system components using defined inspection techniques to detect tampering."},
    {"id": "SR-11", "family": "SR", "title": "Component Authenticity",                 "baseline": "M", "description": "Develop and implement anti-counterfeit policy and procedures for detecting and preventing counterfeit components."},
]

# Build a lookup dict: control_id → control dict
CONTROL_LOOKUP: dict[str, dict] = {c["id"]: c for c in CONTROLS}

# Baseline sets — each level includes all lower levels
_LOW_IDS    = {c["id"] for c in CONTROLS if c["baseline"] in ("L",)}
_MOD_IDS    = {c["id"] for c in CONTROLS if c["baseline"] in ("L", "M")}
_HIGH_IDS   = {c["id"] for c in CONTROLS}   # all controls

BASELINE_CONTROLS: dict[str, list[dict]] = {
    "Low":      [c for c in CONTROLS if c["id"] in _LOW_IDS],
    "Moderate": [c for c in CONTROLS if c["id"] in _MOD_IDS],
    "High":     list(CONTROLS),
}


def get_controls_for_level(impact_level: str) -> list[dict]:
    return BASELINE_CONTROLS.get(impact_level, BASELINE_CONTROLS["Low"])


def get_control(control_id: str) -> dict | None:
    return CONTROL_LOOKUP.get(control_id)


def families_summary(controls: list[dict]) -> dict[str, int]:
    """Return {family_code: count} for a list of controls."""
    result: dict[str, int] = {}
    for c in controls:
        result[c["family"]] = result.get(c["family"], 0) + 1
    return dict(sorted(result.items()))
