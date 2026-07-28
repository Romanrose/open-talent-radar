from __future__ import annotations

import json
from pathlib import Path

from .models import Opportunity, Profile


def load_profile(path: str | Path) -> Profile:
    return Profile.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))


def load_opportunities(directory: str | Path) -> list[Opportunity]:
    files = sorted(Path(directory).glob("*.json"))
    if not files:
        raise FileNotFoundError(f"No opportunity JSON files found in {directory}")
    return [Opportunity.from_dict(json.loads(path.read_text(encoding="utf-8"))) for path in files]
