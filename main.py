"""main.py — ATO Accelerator FastAPI application."""

from __future__ import annotations

import datetime as _dt
import os

from fastapi import Depends, FastAPI, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from claude_analyst import AnalystError, categorize_system, generate_ssp_narrative
from config import APP_SUBTITLE, APP_TITLE, CONTROL_FAMILIES, CONTROL_STATUSES, DEMO_BANNER, DEMO_MODE
from database import get_db, init_db
from models import ControlAssessment, System
from nist_controls import CONTROL_LOOKUP, get_control, get_controls_for_level

app = FastAPI(title=APP_TITLE)

os.makedirs("static/css", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
def startup():
    init_db()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ctx(extra: dict | None = None) -> dict:
    base = {
        "app_title": APP_TITLE,
        "app_subtitle": APP_SUBTITLE,
        "demo_mode": DEMO_MODE,
        "demo_banner": DEMO_BANNER,
        "control_families": CONTROL_FAMILIES,
        "control_statuses": CONTROL_STATUSES,
    }
    if extra:
        base.update(extra)
    return base


def _build_assessments(db: Session, system: System) -> None:
    """Create ControlAssessment rows for every control in the system's baseline."""
    controls = get_controls_for_level(system.impact_level or "Low")
    existing = {a.control_id for a in system.assessments}
    for ctrl in controls:
        if ctrl["id"] not in existing:
            db.add(ControlAssessment(
                system_id=system.id,
                control_id=ctrl["id"],
                control_family=ctrl["family"],
                status="not_started",
            ))


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def index(request: Request, db: Session = Depends(get_db)):
    systems = db.query(System).order_by(System.created_at.desc()).all()
    return templates.TemplateResponse(request, "index.html", _ctx({"systems": systems}))


@app.get("/systems/new", response_class=HTMLResponse)
def new_system_form(request: Request):
    return templates.TemplateResponse(request, "new_system.html", _ctx())


@app.post("/systems/new")
def create_system(
    request: Request,
    db: Session = Depends(get_db),
    name: str = Form(...),
    description: str = Form(default=""),
    system_owner: str = Form(default=""),
    tech_stack: str = Form(default=""),
    data_types: str = Form(default=""),
):
    system = System(
        name=name,
        description=description,
        system_owner=system_owner,
        tech_stack=tech_stack,
        data_types=data_types,
    )
    db.add(system)
    db.commit()
    db.refresh(system)
    return RedirectResponse(f"/systems/{system.id}/categorize", status_code=303)


@app.get("/systems/{system_id}/categorize", response_class=HTMLResponse)
def categorize_form(request: Request, system_id: int, db: Session = Depends(get_db)):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")
    return templates.TemplateResponse(request, "categorize.html", _ctx({"system": system}))


@app.post("/systems/{system_id}/categorize")
def run_categorize(
    request: Request,
    system_id: int,
    db: Session = Depends(get_db),
):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    try:
        result = categorize_system(
            name=system.name,
            description=system.description or "",
            data_types=system.data_types or "",
            tech_stack=system.tech_stack or "",
        )
    except AnalystError as exc:
        return templates.TemplateResponse(
            request, "categorize.html",
            _ctx({"system": system, "error": str(exc)}),
            status_code=500,
        )

    system.impact_level = result["impact_level"]
    system.confidentiality = result["confidentiality"]
    system.integrity = result["integrity"]
    system.availability = result["availability"]
    system.categorization_rationale = result["rationale"]
    db.commit()

    _build_assessments(db, system)
    db.commit()

    return RedirectResponse(f"/systems/{system_id}", status_code=303)


@app.get("/systems/{system_id}", response_class=HTMLResponse)
def system_detail(request: Request, system_id: int, db: Session = Depends(get_db)):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    # Group assessments by family
    family_groups: dict[str, list[ControlAssessment]] = {}
    for a in sorted(system.assessments, key=lambda x: x.control_id):
        family_groups.setdefault(a.control_family, []).append(a)

    # Attach control metadata to each assessment for display
    assessments_with_meta = []
    for a in sorted(system.assessments, key=lambda x: x.control_id):
        ctrl = get_control(a.control_id)
        assessments_with_meta.append((a, ctrl))

    return templates.TemplateResponse(request, "system_detail.html", _ctx({
        "system": system,
        "family_groups": family_groups,
        "assessments_with_meta": assessments_with_meta,
        "control_lookup": CONTROL_LOOKUP,
    }))


@app.get("/systems/{system_id}/controls/{control_id}", response_class=HTMLResponse)
def control_detail(
    request: Request,
    system_id: int,
    control_id: str,
    db: Session = Depends(get_db),
):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    assessment = db.query(ControlAssessment).filter_by(
        system_id=system_id, control_id=control_id
    ).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Control not found for this system")

    ctrl = get_control(control_id)
    return templates.TemplateResponse(request, "control_detail.html", _ctx({
        "system": system,
        "assessment": assessment,
        "ctrl": ctrl,
    }))


@app.post("/systems/{system_id}/controls/{control_id}/status")
def update_status(
    system_id: int,
    control_id: str,
    db: Session = Depends(get_db),
    status: str = Form(...),
    implementation_notes: str = Form(default=""),
):
    assessment = db.query(ControlAssessment).filter_by(
        system_id=system_id, control_id=control_id
    ).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")

    assessment.status = status
    assessment.implementation_notes = implementation_notes
    assessment.updated_at = _dt.datetime.utcnow()
    db.commit()
    return RedirectResponse(f"/systems/{system_id}/controls/{control_id}", status_code=303)


@app.post("/systems/{system_id}/controls/{control_id}/generate")
def generate_narrative(
    request: Request,
    system_id: int,
    control_id: str,
    db: Session = Depends(get_db),
    implementation_notes: str = Form(default=""),
):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    assessment = db.query(ControlAssessment).filter_by(
        system_id=system_id, control_id=control_id
    ).first()
    if not assessment:
        raise HTTPException(status_code=404, detail="Assessment not found")

    ctrl = get_control(control_id)
    if not ctrl:
        raise HTTPException(status_code=404, detail="Control definition not found")

    try:
        narrative = generate_ssp_narrative(
            system_name=system.name,
            system_description=system.description or "",
            control_id=control_id,
            control_title=ctrl["title"],
            control_description=ctrl["description"],
            implementation_notes=implementation_notes,
        )
    except AnalystError as exc:
        ctrl_obj = get_control(control_id)
        return templates.TemplateResponse(
            request, "control_detail.html",
            _ctx({"system": system, "assessment": assessment,
                  "ctrl": ctrl_obj, "error": str(exc)}),
            status_code=500,
        )

    assessment.generated_narrative = narrative
    if implementation_notes:
        assessment.implementation_notes = implementation_notes
    assessment.updated_at = _dt.datetime.utcnow()
    db.commit()
    return RedirectResponse(f"/systems/{system_id}/controls/{control_id}", status_code=303)


@app.get("/systems/{system_id}/report", response_class=HTMLResponse)
def ato_report(request: Request, system_id: int, db: Session = Depends(get_db)):
    system = db.get(System, system_id)
    if not system:
        raise HTTPException(status_code=404, detail="System not found")

    gaps = [a for a in system.assessments if a.status in ("not_started", "planned")]
    implemented = [a for a in system.assessments if a.status == "implemented"]
    inherited = [a for a in system.assessments if a.status == "inherited"]
    na = [a for a in system.assessments if a.status == "not_applicable"]

    # Build POA&M — just the not_started controls
    poam = sorted(
        [a for a in system.assessments if a.status == "not_started"],
        key=lambda x: x.control_id,
    )

    return templates.TemplateResponse(request, "report.html", _ctx({
        "system": system,
        "gaps": gaps,
        "implemented": implemented,
        "inherited": inherited,
        "na": na,
        "poam": poam,
        "control_lookup": CONTROL_LOOKUP,
    }))


@app.post("/seed")
def seed(db: Session = Depends(get_db)):
    from seed_data import DEMO_SYSTEM

    existing = db.query(System).filter_by(name=DEMO_SYSTEM["name"]).first()
    if existing:
        return RedirectResponse(f"/systems/{existing.id}", status_code=303)

    system = System(
        name=DEMO_SYSTEM["name"],
        description=DEMO_SYSTEM["description"],
        system_owner=DEMO_SYSTEM["system_owner"],
        tech_stack=DEMO_SYSTEM["tech_stack"],
        data_types=DEMO_SYSTEM["data_types"],
        impact_level=DEMO_SYSTEM["impact_level"],
        confidentiality=DEMO_SYSTEM["confidentiality"],
        integrity=DEMO_SYSTEM["integrity"],
        availability=DEMO_SYSTEM["availability"],
        categorization_rationale=DEMO_SYSTEM["categorization_rationale"],
    )
    db.add(system)
    db.flush()

    # Build all control assessments for Moderate baseline
    controls = get_controls_for_level("Moderate")
    statuses = DEMO_SYSTEM["control_statuses"]
    sample = DEMO_SYSTEM["sample_narrative"]

    for ctrl in controls:
        status = statuses.get(ctrl["id"], "not_started")
        narrative = sample["narrative"] if ctrl["id"] == sample["control_id"] else None
        db.add(ControlAssessment(
            system_id=system.id,
            control_id=ctrl["id"],
            control_family=ctrl["family"],
            status=status,
            generated_narrative=narrative,
        ))

    db.commit()
    return RedirectResponse(f"/systems/{system.id}", status_code=303)
