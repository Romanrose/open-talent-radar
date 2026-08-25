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


def load_source_catalog(path: str | Path) -> list[dict]:
    """Load a reviewed official-source catalog without treating it as job data."""
    catalog = Path(path)
    files = [catalog] if catalog.is_file() else sorted(catalog.glob("*.json"))
    if not files:
        raise FileNotFoundError(f"No source catalog JSON files found in {path}")
    sources = []
    for file in files:
        payload = json.loads(file.read_text(encoding="utf-8"))
        sources.extend(payload.get("sources", []))
    if not sources:
        raise ValueError(f"No official sources found in {path}")
    return sources
