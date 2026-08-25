from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass(frozen=True)
class Opportunity:
    slug: str
    name: str
    organization: str
    kind: str
    url: str
    status: str
    deadline: str | None = None
    mentorship: bool = False
    remote: bool = True
    reward: str = ""
    skills: list[str] = field(default_factory=list)
    interests: list[str] = field(default_factory=list)
    difficulty: str = "medium"
    summary: str = ""
    source: str = "community"
    eligibility: str = ""
    graduation_years: list[int] = field(default_factory=list)
    last_verified: str | None = None
    track: str = "open_source"
    employment_type: str = ""
    role_family: str = ""
    location: str = ""
    work_mode: str = ""
    seniority: str = ""

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Opportunity":
        required = {"slug", "name", "organization", "kind", "url", "status"}
        missing = required.difference(raw)
        if missing:
            raise ValueError(f"Opportunity is missing fields: {', '.join(sorted(missing))}")
        return cls(**raw)

    @property
    def parsed_deadline(self) -> date | None:
        if not self.deadline or self.deadline.lower() == "rolling":
            return None
        try:
            return date.fromisoformat(self.deadline)
        except ValueError:
            return None


@dataclass(frozen=True)
class Profile:
    name: str
    education: dict[str, Any]
    skills: dict[str, list[str]]
    interests: list[str]
    preferences: dict[str, Any]

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "Profile":
        return cls(
            name=raw.get("name", "Contributor"),
            education=raw.get("education", {}),
            skills=raw.get("skills", {}),
            interests=raw.get("interests", []),
            preferences=raw.get("preferences", {}),
        )

    @property
    def all_skills(self) -> dict[str, int]:
        weights = {"strong": 3, "familiar": 2, "learning": 1}
        return {
            skill.lower(): weights.get(level, 1)
            for level, skills in self.skills.items()
            for skill in skills
        }


@dataclass(frozen=True)
class Match:
    opportunity: Opportunity
    score: int
    skill_score: int
    interest_score: int
    fit_notes: list[str]
    gaps: list[str]
