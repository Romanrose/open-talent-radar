from __future__ import annotations

import argparse
from pathlib import Path

from .data import load_opportunities, load_profile
from .matcher import rank
from .reporter import render_report, write_report
from .sync import render_source_monitor, sync_sources
from .templates import application_record, learning_plan, write_template

DEFAULT_PROFILE = "profile.example.json"
DEFAULT_OPPORTUNITIES = "opportunities"


def _matches(args: argparse.Namespace):
    profile = load_profile(args.profile)
    opportunities = load_opportunities(args.opportunities)
    return profile, rank(profile, opportunities)


def command_match(args: argparse.Namespace) -> int:
    _, matches = _matches(args)
    for item in matches:
        print(f"{item.score:>3}  {item.opportunity.slug:<28} {item.opportunity.name}")
    return 0


def command_report(args: argparse.Namespace) -> int:
    profile, matches = _matches(args)
    report = render_report(profile, matches)
    path = write_report(args.output, report)
    print(f"Wrote {path}")
    return 0


def _find_match(args: argparse.Namespace):
    _, matches = _matches(args)
    for item in matches:
        if item.opportunity.slug == args.slug:
            return item
    raise SystemExit(f"Unknown opportunity: {args.slug}")


def command_learn(args: argparse.Namespace) -> int:
    item = _find_match(args)
    path = write_template(Path(args.output) / f"{item.opportunity.slug}.md", learning_plan(item.opportunity, item.gaps))
    print(f"Wrote {path}")
    return 0


def command_track(args: argparse.Namespace) -> int:
    item = _find_match(args)
    path = write_template(Path(args.output) / f"{item.opportunity.slug}.md", application_record(item))
    print(f"Wrote {path}")
    return 0


def command_sync(args: argparse.Namespace) -> int:
    opportunities = load_opportunities(args.opportunities)
    state = sync_sources(opportunities, args.state, args.timeout)
    path = write_report(args.output, render_source_monitor(state))
    changed = sum(1 for record in state["sources"].values() if record["changed"])
    print(f"Checked {len(opportunities)} official sources; {changed} content changes detected. Wrote {path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="oss-radar", description="Match open-source talent opportunities to a contributor profile.")
    parser.add_argument("--profile", default=DEFAULT_PROFILE)
    parser.add_argument("--opportunities", default=DEFAULT_OPPORTUNITIES)
    subparsers = parser.add_subparsers(dest="command", required=True)

    match_parser = subparsers.add_parser("match", help="Rank all tracked opportunities.")
    match_parser.set_defaults(func=command_match)

    report_parser = subparsers.add_parser("report", help="Write a Markdown recommendation report.")
    report_parser.add_argument("--output", default="reports/latest.md")
    report_parser.set_defaults(func=command_report)

    learn_parser = subparsers.add_parser("learn", help="Create a preparation checklist for one opportunity.")
    learn_parser.add_argument("slug")
    learn_parser.add_argument("--output", default="learning")
    learn_parser.set_defaults(func=command_learn)

    track_parser = subparsers.add_parser("track", help="Create an application record for one opportunity.")
    track_parser.add_argument("slug")
    track_parser.add_argument("--output", default="applications")
    track_parser.set_defaults(func=command_track)

    sync_parser = subparsers.add_parser("sync", help="Monitor official opportunity pages for changes requiring review.")
    sync_parser.add_argument("--state", default="data/source-state.json")
    sync_parser.add_argument("--output", default="reports/source-monitor.md")
    sync_parser.add_argument("--timeout", type=int, default=20)
    sync_parser.set_defaults(func=command_sync)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
