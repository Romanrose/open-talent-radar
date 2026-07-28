from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from .models import Opportunity


def _read_state(path: Path) -> dict:
    if not path.exists():
        return {"version": 1, "sources": {}}
    return json.loads(path.read_text(encoding="utf-8"))


def sync_sources(opportunities: list[Opportunity], state_path: str | Path, timeout: int = 20) -> dict:
    """Check official URLs and record content-level change signals.

    This intentionally does not turn arbitrary page text into opportunities. New
    records remain reviewable pull requests; the monitor only tells maintainers
    which official pages changed and therefore need review.
    """
    destination = Path(state_path)
    previous = _read_state(destination)
    previous_sources = previous.get("sources", {})
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    current: dict[str, dict] = {}

    for opportunity in opportunities:
        old = previous_sources.get(opportunity.slug, {})
        record = {
            "name": opportunity.name,
            "url": opportunity.url,
            "checked_at": now,
            "changed": False,
        }
        try:
            request = Request(opportunity.url, headers={"User-Agent": "OpenTalentRadar/0.1 (+https://github.com/Romanrose/open-talent-radar)"})
            with urlopen(request, timeout=timeout) as response:
                body = response.read(1_000_000)
                record["http_status"] = response.status
                record["content_hash"] = hashlib.sha256(body).hexdigest()
            record["changed"] = bool(old.get("content_hash") and old.get("content_hash") != record["content_hash"])
        except (URLError, OSError, ValueError) as error:
            record["error"] = str(error)
            record["http_status"] = None
        current[opportunity.slug] = record

    state = {"version": 1, "updated_at": now, "sources": current}
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return state


def render_source_monitor(state: dict) -> str:
    rows = [
        "# Official source monitor",
        "",
        f"Last checked: {state['updated_at']}",
        "",
        "| Source | HTTP | Changed | Review note |",
        "| --- | ---: | :---: | --- |",
    ]
    for record in state["sources"].values():
        note = record.get("error", "Review the official page if content changed.")
        rows.append(f"| [{record['name']}]({record['url']}) | {record.get('http_status', '—')} | {'Yes' if record['changed'] else 'No'} | {note} |")
    rows += [
        "",
        "This monitor only detects page-level changes. It never creates or edits opportunity records without a human review.",
    ]
    return "\n".join(rows) + "\n"
