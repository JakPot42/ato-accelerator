"""Tests for nist_controls.py and claude_analyst.py — no real API calls."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from nist_controls import (
    CONTROLS,
    get_control,
    get_controls_for_level,
    families_summary,
)
from claude_analyst import categorize_system, generate_ssp_narrative, AnalystError


# ---------------------------------------------------------------------------
# nist_controls
# ---------------------------------------------------------------------------

class TestNistControls:
    def test_controls_list_not_empty(self):
        assert len(CONTROLS) > 50

    def test_all_controls_have_required_fields(self):
        for c in CONTROLS:
            assert "id" in c, f"Missing id in {c}"
            assert "family" in c
            assert "title" in c
            assert "baseline" in c
            assert "description" in c

    def test_baseline_values_are_valid(self):
        valid = {"L", "M", "H"}
        for c in CONTROLS:
            assert c["baseline"] in valid, f"{c['id']} has invalid baseline {c['baseline']}"

    def test_low_baseline_is_subset_of_moderate(self):
        low = {c["id"] for c in get_controls_for_level("Low")}
        mod = {c["id"] for c in get_controls_for_level("Moderate")}
        assert low.issubset(mod)

    def test_moderate_baseline_is_subset_of_high(self):
        mod = {c["id"] for c in get_controls_for_level("Moderate")}
        high = {c["id"] for c in get_controls_for_level("High")}
        assert mod.issubset(high)

    def test_low_has_fewer_controls_than_moderate(self):
        assert len(get_controls_for_level("Low")) < len(get_controls_for_level("Moderate"))

    def test_get_control_returns_correct_entry(self):
        ac2 = get_control("AC-2")
        assert ac2 is not None
        assert ac2["title"] == "Account Management"
        assert ac2["family"] == "AC"

    def test_get_control_returns_none_for_unknown(self):
        assert get_control("ZZ-99") is None

    def test_families_summary_counts_correctly(self):
        low_controls = get_controls_for_level("Low")
        summary = families_summary(low_controls)
        assert "AC" in summary
        assert "IA" in summary
        assert all(isinstance(v, int) and v > 0 for v in summary.values())

    def test_ac1_in_all_baselines(self):
        for level in ("Low", "Moderate", "High"):
            ids = {c["id"] for c in get_controls_for_level(level)}
            assert "AC-1" in ids, f"AC-1 missing from {level} baseline"

    def test_high_only_control_not_in_low(self):
        high_only = {c["id"] for c in CONTROLS if c["baseline"] == "H"}
        low_ids = {c["id"] for c in get_controls_for_level("Low")}
        assert high_only.isdisjoint(low_ids)


# ---------------------------------------------------------------------------
# claude_analyst — categorize_system
# ---------------------------------------------------------------------------

class TestCategorizeSystem:
    def _mock_response(self, payload: dict) -> MagicMock:
        msg = MagicMock()
        msg.content = [MagicMock(text=json.dumps(payload))]
        return msg

    @patch("claude_analyst._get_client")
    def test_returns_correct_keys(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.messages.create.return_value = self._mock_response({
            "impact_level": "Moderate",
            "confidentiality": "Moderate",
            "integrity": "Low",
            "availability": "Moderate",
            "rationale": "Test rationale.",
        })
        result = categorize_system("TestSys", "A test system", "CUI", "Python/FastAPI")
        assert result["impact_level"] == "Moderate"
        assert result["confidentiality"] == "Moderate"
        assert "rationale" in result

    @patch("claude_analyst._get_client")
    def test_raises_on_invalid_json(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="not json at all")]
        )
        with pytest.raises(AnalystError, match="invalid JSON"):
            categorize_system("TestSys", "desc", "data", "stack")

    @patch("claude_analyst._get_client")
    def test_raises_on_missing_field(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.messages.create.return_value = self._mock_response({
            "impact_level": "Low",
            # missing confidentiality, integrity, availability, rationale
        })
        with pytest.raises(AnalystError, match="missing field"):
            categorize_system("TestSys", "desc", "data", "stack")

    @patch("claude_analyst._get_client")
    def test_strips_markdown_fences(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        payload = {
            "impact_level": "Low", "confidentiality": "Low",
            "integrity": "Low", "availability": "Low", "rationale": "r"
        }
        mock_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text=f"```json\n{json.dumps(payload)}\n```")]
        )
        result = categorize_system("s", "d", "dt", "ts")
        assert result["impact_level"] == "Low"


# ---------------------------------------------------------------------------
# claude_analyst — generate_ssp_narrative
# ---------------------------------------------------------------------------

class TestGenerateSspNarrative:
    @patch("claude_analyst._get_client")
    def test_returns_string(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.messages.create.return_value = MagicMock(
            content=[MagicMock(text="The system implements AC-1 by...")]
        )
        result = generate_ssp_narrative(
            "TestSys", "A test system", "AC-1",
            "Policy and Procedures", "Develop access control policy.",
        )
        assert isinstance(result, str)
        assert len(result) > 0

    @patch("claude_analyst._get_client")
    def test_raises_on_api_error(self, mock_get_client):
        import anthropic
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.messages.create.side_effect = anthropic.APIError(
            message="API error", request=MagicMock(), body=None
        )
        with pytest.raises(AnalystError):
            generate_ssp_narrative("s", "d", "AC-1", "t", "desc")
