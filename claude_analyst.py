"""
claude_analyst.py — Claude-powered analysis for ATO Accelerator.

Two jobs:
  1. categorize_system()     — FIPS 199 impact level determination
  2. generate_ssp_narrative() — draft SSP control implementation statement
"""

from __future__ import annotations

import json
import re

import anthropic

from config import ANTHROPIC_API_KEY, CLAUDE_MAX_TOKENS, CLAUDE_MODEL


class AnalystError(Exception):
    pass


_client: anthropic.Anthropic | None = None


def _get_client() -> anthropic.Anthropic:
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    return _client


def _strip_fences(text: str) -> str:
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    return text.strip()


def categorize_system(
    name: str,
    description: str,
    data_types: str,
    tech_stack: str,
) -> dict:
    """
    Run FIPS 199 categorization via Claude.

    Returns:
      {
        "impact_level": "Low" | "Moderate" | "High",
        "confidentiality": "Low" | "Moderate" | "High",
        "integrity": "Low" | "Moderate" | "High",
        "availability": "Low" | "Moderate" | "High",
        "rationale": str
      }
    Raises AnalystError on failure.
    """
    prompt = f"""You are a federal cybersecurity expert specializing in NIST Risk Management Framework (RMF) and FIPS 199 security categorization.

Analyze the following federal information system and determine its FIPS 199 security categorization.

SYSTEM NAME: {name}
DESCRIPTION: {description}
DATA TYPES: {data_types}
TECH STACK: {tech_stack}

Apply FIPS 199 criteria:
- LOW: Adverse effect would be limited
- MODERATE: Adverse effect would be serious
- HIGH: Adverse effect would be severe or catastrophic

Evaluate Confidentiality, Integrity, and Availability separately.
The overall impact level = the HIGHEST of the three.

Return ONLY valid JSON (no markdown):
{{
  "impact_level": "Moderate",
  "confidentiality": "Moderate",
  "integrity": "Low",
  "availability": "Moderate",
  "rationale": "2-3 sentence explanation referencing the specific data types and operational context that drove each rating"
}}"""

    try:
        response = _get_client().messages.create(
            model=CLAUDE_MODEL,
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = response.content[0].text
        result = json.loads(_strip_fences(raw))
    except anthropic.APIError as exc:
        raise AnalystError(f"Claude API error: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise AnalystError(f"Claude returned invalid JSON: {exc}") from exc

    for field in ("impact_level", "confidentiality", "integrity", "availability", "rationale"):
        if field not in result:
            raise AnalystError(f"Claude response missing field: {field}")

    return result


def generate_ssp_narrative(
    system_name: str,
    system_description: str,
    control_id: str,
    control_title: str,
    control_description: str,
    implementation_notes: str = "",
) -> str:
    """
    Generate a draft SSP control implementation narrative.

    Returns plain text (2-4 paragraphs). Raises AnalystError on failure.
    """
    notes_section = f"\nAdditional context from the system owner: {implementation_notes}" if implementation_notes else ""

    prompt = f"""You are a federal ISSO (Information System Security Officer) writing a System Security Plan (SSP) for the RMF Authorization process.

Write a formal SSP implementation narrative for the control below. The narrative should describe HOW this specific system implements the control — be specific to the system, not generic.

SYSTEM: {system_name}
SYSTEM DESCRIPTION: {system_description}{notes_section}

CONTROL: {control_id} — {control_title}
CONTROL REQUIREMENT: {control_description}

Write 2-4 paragraphs in formal government technical writing style. Include:
1. How the control is implemented (specific mechanisms, tools, configurations)
2. Who is responsible for implementing and maintaining the control
3. Any relevant policies, procedures, or automated mechanisms in place
4. Evidence/artifacts that would demonstrate compliance

Do NOT use markdown formatting. Write in plain prose. Be specific to this system — do not write generic boilerplate."""

    try:
        response = _get_client().messages.create(
            model=CLAUDE_MODEL,
            max_tokens=CLAUDE_MAX_TOKENS,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text.strip()
    except anthropic.APIError as exc:
        raise AnalystError(f"Claude API error: {exc}") from exc
