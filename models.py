"""models.py — ORM models for ATO Accelerator."""

from __future__ import annotations

import datetime as _dt
import json

from sqlalchemy import DateTime, ForeignKey, Integer, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class System(Base):
    """A federal information system undergoing the RMF process."""
    __tablename__ = "systems"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    system_owner: Mapped[str | None] = mapped_column(Text, nullable=True)
    tech_stack: Mapped[str | None] = mapped_column(Text, nullable=True)
    data_types: Mapped[str | None] = mapped_column(Text, nullable=True)

    # FIPS 199 categorization results
    impact_level: Mapped[str | None] = mapped_column(Text, nullable=True)   # Low/Moderate/High
    confidentiality: Mapped[str | None] = mapped_column(Text, nullable=True)
    integrity: Mapped[str | None] = mapped_column(Text, nullable=True)
    availability: Mapped[str | None] = mapped_column(Text, nullable=True)
    categorization_rationale: Mapped[str | None] = mapped_column(Text, nullable=True)

    created_at: Mapped[_dt.datetime] = mapped_column(DateTime, server_default=func.now())

    assessments: Mapped[list[ControlAssessment]] = relationship(
        "ControlAssessment", back_populates="system", cascade="all, delete-orphan"
    )

    @property
    def implemented_count(self) -> int:
        return sum(1 for a in self.assessments if a.status == "implemented")

    @property
    def planned_count(self) -> int:
        return sum(1 for a in self.assessments if a.status == "planned")

    @property
    def not_started_count(self) -> int:
        return sum(1 for a in self.assessments if a.status == "not_started")

    @property
    def not_applicable_count(self) -> int:
        return sum(1 for a in self.assessments if a.status == "not_applicable")

    @property
    def inherited_count(self) -> int:
        return sum(1 for a in self.assessments if a.status == "inherited")

    @property
    def total_controls(self) -> int:
        return len(self.assessments)

    @property
    def completion_pct(self) -> int:
        if not self.total_controls:
            return 0
        done = self.implemented_count + self.not_applicable_count + self.inherited_count
        return int(done / self.total_controls * 100)

    @property
    def ato_status(self) -> str:
        pct = self.completion_pct
        if pct >= 90:
            return "ATO Ready"
        if pct >= 60:
            return "In Progress"
        return "Early Stage"


class ControlAssessment(Base):
    """Tracks the implementation status of one NIST 800-53 control for a system."""
    __tablename__ = "control_assessments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    system_id: Mapped[int] = mapped_column(Integer, ForeignKey("systems.id"))
    control_id: Mapped[str] = mapped_column(Text)        # e.g. "AC-1"
    control_family: Mapped[str] = mapped_column(Text)    # e.g. "AC"
    status: Mapped[str] = mapped_column(Text, default="not_started")
    implementation_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    generated_narrative: Mapped[str | None] = mapped_column(Text, nullable=True)
    updated_at: Mapped[_dt.datetime | None] = mapped_column(DateTime, nullable=True)

    system: Mapped[System] = relationship("System", back_populates="assessments")

    @property
    def status_label(self) -> str:
        from config import CONTROL_STATUSES
        return CONTROL_STATUSES.get(self.status, self.status.replace("_", " ").title())

    @property
    def status_css(self) -> str:
        return {
            "implemented":    "status-implemented",
            "planned":        "status-planned",
            "not_applicable": "status-na",
            "inherited":      "status-inherited",
            "not_started":    "status-not-started",
        }.get(self.status, "status-not-started")
