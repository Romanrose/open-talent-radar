from __future__ import annotations

from datetime import date
from pathlib import Path

from .models import Match, Profile


def render_report(profile: Profile, matches: list[Match], generated_on: date | None = None) -> str:
    generated_on = generated_on or date.today()
    threshold = int(profile.preferences.get("minimum_match_score", 60))
    recommended = [item for item in matches if item.score >= threshold]
    lines = [
        "# Open Talent Radar Report",
        "",
        f"Generated for **{profile.name}** on {generated_on.isoformat()}.",
        "",
        "## Recommended opportunities",
        "",
        "| Score | Opportunity | Mentor | Status | Deadline | Why it fits |",
        "| ---: | --- | :---: | --- | --- | --- |",
    ]
    for item in recommended:
        op = item.opportunity
        why = "; ".join(item.fit_notes[:2]) or "Profile-compatible opportunity"
        lines.append(
            f"| {item.score} | [{op.name}]({op.url}) | {'Yes' if op.mentorship else 'No'} | {op.status} | {op.deadline or '—'} | {why} |"
        )

    lines += ["", "## Skill gaps to close", ""]
    for item in recommended:
        if item.gaps:
            lines.append(f"- **{item.opportunity.name}**: {', '.join(item.gaps)}")
    if not any(item.gaps for item in recommended):
        lines.append("- No critical gaps found in the current recommendations.")

    lines += ["", "## Next actions", ""]
    for item in recommended[:3]:
        lines.extend([
            f"### {item.opportunity.name}",
            f"- [ ] Read the [official opportunity page]({item.opportunity.url}).",
            "- [ ] Choose a task and write a short technical plan.",
            "- [ ] Open `oss-radar learn " + item.opportunity.slug + "` to generate a focused preparation checklist.",
            "- [ ] Open `oss-radar track " + item.opportunity.slug + "` to create an application record.",
            "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def write_report(path: str | Path, report: str) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(report, encoding="utf-8")
    return destination
