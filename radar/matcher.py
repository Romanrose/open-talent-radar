from __future__ import annotations

from datetime import date
import re

from .models import Match, Opportunity, Profile


ALIASES = {
    "pytorch": "deep learning",
    "tensorflow": "deep learning",
    "hugging face": "llm",
    "large language models": "llm",
    "retrieval augmented generation": "rag",
    "containers": "docker",
}


def _canonical(item: str) -> str:
    normalised = item.strip().lower()
    return ALIASES.get(normalised, normalised)


def _normalise(items: list[str]) -> set[str]:
    return {_canonical(item) for item in items if item.strip()}


def _location_rank(location: str, preferences: list[str]) -> int | None:
    """Return the best preference rank for a possibly multi-city job location."""
    places = {_canonical(part) for part in re.split(r"[/,，、;；]", location) if part.strip()}
    for index, preferred in enumerate(preferences):
        if _canonical(preferred) in places:
            return index
    return None


def match(profile: Profile, opportunity: Opportunity, today: date | None = None) -> Match:
    today = today or date.today()
    profile_skills = {_canonical(skill): weight for skill, weight in profile.all_skills.items()}
    required_skills = _normalise(opportunity.skills)
    matched = required_skills.intersection(profile_skills)
    gaps = sorted(skill for skill in required_skills if skill not in profile_skills)

    if required_skills:
        weighted_match = sum(profile_skills[skill] for skill in matched)
        possible = len(required_skills) * 3
        skill_score = round(55 * weighted_match / possible)
    else:
        skill_score = 25

    shared_interests = _normalise(profile.interests).intersection(_normalise(opportunity.interests))
    interest_score = min(20, len(shared_interests) * 7)
    score = skill_score + interest_score
    notes: list[str] = []

    if opportunity.mentorship and profile.preferences.get("mentorship", True):
        score += 12
        notes.append("Includes named mentor or maintainer guidance")
    if opportunity.remote and profile.preferences.get("remote", True):
        score += 5
        notes.append("Remote-friendly contribution path")
    career = profile.preferences.get("career", {})
    if opportunity.track == "job":
        preferred_types = _normalise(career.get("employment_types", []))
        preferred_roles = _normalise(career.get("role_families", []))
        preferred_locations = career.get("locations", [])
        if opportunity.employment_type and _canonical(opportunity.employment_type) in preferred_types:
            score += 6
            notes.append(f"Preferred employment type: {opportunity.employment_type}")
        if opportunity.role_family and _canonical(opportunity.role_family) in preferred_roles:
            score += 8
            notes.append(f"Preferred role family: {opportunity.role_family}")
        location_rank = _location_rank(opportunity.location, preferred_locations) if opportunity.location else None
        if location_rank is not None:
            location_bonus = max(3, 12 - location_rank * 2)
            score += location_bonus
            notes.append(f"Location priority #{location_rank + 1}: {preferred_locations[location_rank]}")
    if opportunity.status == "open":
        score += 5
        notes.append("Currently open")
    elif opportunity.status == "verify":
        score -= 5
        notes.append("Verify the intake status before applying")
    elif opportunity.status == "watch":
        score -= 10
        notes.append("Watch for the next intake")
    graduation_year = profile.education.get("graduation_year")
    if opportunity.graduation_years and graduation_year not in opportunity.graduation_years:
        score -= 35
        notes.append(f"Expected graduation year {graduation_year} is not listed as eligible")
    if opportunity.parsed_deadline:
        days = (opportunity.parsed_deadline - today).days
        if 0 <= days <= 14:
            score += 4
            notes.append(f"Deadline in {days} days")
        elif days < 0:
            score -= 30
            notes.append("Deadline has passed")
    if shared_interests:
        notes.append(f"Aligned interests: {', '.join(sorted(shared_interests))}")
    if matched:
        notes.append(f"Matched skills: {', '.join(sorted(matched))}")

    return Match(
        opportunity=opportunity,
        score=max(0, min(100, score)),
        skill_score=skill_score,
        interest_score=interest_score,
        fit_notes=notes,
        gaps=gaps,
    )


def rank(profile: Profile, opportunities: list[Opportunity], today: date | None = None) -> list[Match]:
    return sorted((match(profile, item, today) for item in opportunities), key=lambda item: item.score, reverse=True)
