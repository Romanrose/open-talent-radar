from __future__ import annotations

from datetime import date

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
    if opportunity.status == "open":
        score += 5
        notes.append("Currently open")
    elif opportunity.status == "verify":
        score -= 5
        notes.append("Verify the intake status before applying")
    elif opportunity.status == "watch":
        score -= 10
        notes.append("Watch for the next intake")
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
