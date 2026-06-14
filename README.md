# ATO Accelerator

AI-powered NIST 800-53 / Risk Management Framework (RMF) compliance assistant for defense contractors — automates the most painful parts of getting an Authority to Operate (ATO).

Built for ISSOs, ISSMs, and defense contractors at Leidos, SAIC, Booz Allen Hamilton, and other primes who spend months on ATO documentation.

**Live demo:** https://ato-accelerator.onrender.com



---

## What It Does

Every DoD system needs an ATO before it can go live. Getting one requires:
1. **FIPS 199 Categorization** — determining if your system is Low, Moderate, or High impact
2. **Control Selection** — picking the right NIST 800-53 controls for your baseline (125–165+ controls)
3. **SSP Writing** — documenting how each control is implemented (the most time-consuming part)
4. **Gap Analysis / POA&M** — tracking what's missing before the Authorizing Official signs off

This tool automates steps 1, 3, and 4 with Claude AI.

---

## Features

| Feature | Description |
|---------|-------------|
| FIPS 199 Categorization | Describe your system → Claude assigns Low/Moderate/High impact for C, I, A |
| Control Baseline | Auto-loads the correct NIST 800-53 Rev 5 controls for your impact level |
| SSP Narrative Generator | Claude writes formal SSP implementation statements tailored to your system |
| Status Tracker | Mark each control Implemented / Planned / Inherited / N/A |
| ATO Report | Completion percentage, POA&M items, and readiness summary |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | FastAPI + Python 3.12 |
| AI | Claude Haiku (FIPS 199 categorization + SSP narrative generation) |
| Controls data | NIST SP 800-53 Rev 5 (150+ controls, all 20 families, embedded) |
| Database | SQLite + SQLAlchemy 2.0 |
| Frontend | Jinja2 templates + vanilla CSS |
| Deploy | Render (free tier) |

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/JaKPoT/ato-accelerator.git
cd ato-accelerator

# 2. Add your Anthropic API key
cp .env.example .env
# Edit .env and add ANTHROPIC_API_KEY=sk-ant-...

# 3. Run (Windows)
START_HERE.bat

# Or manually:
python -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\uvicorn main:app --reload
```

Open http://localhost:8000

---

## Demo

Load the pre-built demo at `/seed`. Shows the **AESIR Mission Planning System** — a fictional DoD web application:

- Moderate impact level (Confidentiality: Moderate, Integrity: Moderate, Availability: Moderate)
- 165 NIST 800-53 controls across all 20 families
- 88 implemented, 67 planned, 1 not started (CM-7 — the POA&M item)
- Pre-generated SSP narrative for AC-2 (Account Management)

Click any control to view its requirement, update its status, or generate a new SSP narrative with Claude.

---

## API Keys Required

| Key | Where to get it | Cost |
|-----|----------------|------|
| `ANTHROPIC_API_KEY` | console.anthropic.com | ~$0.01–0.03/narrative (Haiku model) |

---

## NIST 800-53 Coverage

| Baseline | Controls included |
|----------|------------------|
| Low | ~125 controls |
| Moderate | ~165 controls |
| High | ~175 controls |

All 20 control families: AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR

---

## Deployment (Render)

1. Push to GitHub
2. Connect repo at render.com → New Web Service
3. Set `ANTHROPIC_API_KEY` as an Environment Secret in the Render dashboard
4. Deploy — Render auto-detects `render.yaml`

---

## Tests

```bash
venv\Scripts\python.exe -m pytest tests/ -v
# 17 passed in 1.29s
```

Tests cover: control catalog integrity, baseline subset relationships, FIPS 199 categorization parsing, SSP narrative generation, error handling.

---

*DEMONSTRATION ONLY — always verify against official NIST SP 800-53 Rev 5 guidance before use in a real ATO package*
