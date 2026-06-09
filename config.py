"""config.py — ATO Accelerator configuration."""

from __future__ import annotations

import os
from dotenv import load_dotenv

load_dotenv()

# --- API ---
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL = "claude-haiku-4-5-20251001"
CLAUDE_MAX_TOKENS = 4000

# --- App ---
APP_TITLE = "ATO Accelerator"
APP_SUBTITLE = "NIST 800-53 / RMF Compliance Assistant"
DEMO_MODE = True
DEMO_BANNER = "DEMONSTRATION ONLY — SYNTHETIC DATA — NOT FOR OPERATIONAL USE"
DATABASE_URL = "sqlite:///./ato_accelerator.db"

# --- FIPS 199 impact levels ---
IMPACT_LEVELS = ["Low", "Moderate", "High"]

# --- Control implementation statuses ---
CONTROL_STATUSES = {
    "implemented":      "Implemented",
    "planned":          "Planned",
    "not_applicable":   "Not Applicable",
    "inherited":        "Inherited",
    "not_started":      "Not Started",
}

# --- NIST 800-53 control families ---
CONTROL_FAMILIES = {
    "AC": "Access Control",
    "AT": "Awareness and Training",
    "AU": "Audit and Accountability",
    "CA": "Assessment, Authorization, and Monitoring",
    "CM": "Configuration Management",
    "CP": "Contingency Planning",
    "IA": "Identification and Authentication",
    "IR": "Incident Response",
    "MA": "Maintenance",
    "MP": "Media Protection",
    "PE": "Physical and Environmental Protection",
    "PL": "Planning",
    "PM": "Program Management",
    "PS": "Personnel Security",
    "PT": "PII Processing and Transparency",
    "RA": "Risk Assessment",
    "SA": "System and Services Acquisition",
    "SC": "System and Communications Protection",
    "SI": "System and Information Integrity",
    "SR": "Supply Chain Risk Management",
}
