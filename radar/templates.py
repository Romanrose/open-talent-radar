from __future__ import annotations

from pathlib import Path

from .models import Match, Opportunity


def _safe_path(directory: str | Path, slug: str) -> Path:
    return Path(directory) / f"{slug}.md"


def learning_plan(opportunity: Opportunity, gaps: list[str]) -> str:
    gap_lines = "\n".join(f"- [ ] Learn or demonstrate: **{gap}**" for gap in gaps) or "- [ ] Review the contribution guide and task list."
    return f"""# Preparation plan: {opportunity.name}

Official page: {opportunity.url}

## Outcome

Be ready to propose and deliver a small, reviewable contribution to {opportunity.organization}.

## Skill gaps

{gap_lines}

## Contribution checklist

- [ ] Read the contributing guide and code of conduct.
- [ ] Set up the project locally and run its tests.
- [ ] Read three merged pull requests close to the target task.
- [ ] Complete one starter issue or documentation improvement.
- [ ] Draft a one-page implementation plan.
- [ ] Ask the mentor or maintainer for feedback.
"""


def application_record(match: Match) -> str:
    op = match.opportunity
    gap_lines = "\n".join(f"- [ ] {gap}" for gap in match.gaps) or "- [ ] No critical skill gap identified."
    return f"""# Application: {op.name}

- Organization: {op.organization}
- Official page: {op.url}
- Match score: {match.score}/100
- Mentor path: {'Yes' if op.mentorship else 'Confirm with the community'}
- Deadline: {op.deadline or 'Not listed'}

## Status

- [ ] Researched
- [ ] Contacted mentor or maintainer
- [ ] Prepared technical plan
- [ ] Submitted
- [ ] Accepted / completed

## Evidence

- Resume:
- Relevant repositories:
- Issues / pull requests:
- Contact notes:

## Gaps to close

{gap_lines}

## Project proposal notes

Describe the task, expected implementation, milestones, risks, and the value to the community.
"""


def job_application_record(match: Match) -> str:
    op = match.opportunity
    gap_lines = "\n".join(f"- [ ] {gap}" for gap in match.gaps) or "- [ ] No critical skill gap identified."
    return f"""# Job application: {op.name}

- Organization: {op.organization}
- Official page: {op.url}
- Role family: {op.role_family or 'Confirm'}
- Employment type: {op.employment_type or 'Confirm'}
- Location / mode: {op.location or 'Confirm'} / {op.work_mode or 'Confirm'}
- Match score: {match.score}/100
- Deadline: {op.deadline or 'Not listed'}

## Application status

- [ ] Official details verified
- [ ] Resume tailored
- [ ] Project evidence selected
- [ ] Applied
- [ ] Written assessment / interview scheduled
- [ ] Completed / offer outcome recorded

## Interview evidence

- Resume version:
- Most relevant project:
- System design / coding topics:
- Questions to ask the team:

## Skill gaps to close

{gap_lines}
"""


def write_template(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path
