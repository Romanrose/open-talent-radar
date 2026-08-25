from __future__ import annotations

import argparse
from pathlib import Path

from .data import load_opportunities, load_profile, load_source_catalog
from .analysis import render_analysis
from .matcher import rank
from .reporter import render_report, write_report
from .sync import render_source_monitor, sync_source_records, sync_sources
from .templates import application_record, job_application_record, learning_plan, write_template

DEFAULT_PROFILE = "profile.example.json"
DEFAULT_OPPORTUNITIES = "opportunities"
DEFAULT_JOBS = "jobs"
DEFAULT_JOB_SOURCES = "job-sources"
DEFAULT_OSS_SOURCES = "oss-sources"


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


def _job_matches(args: argparse.Namespace):
    profile = load_profile(args.profile)
    jobs = load_opportunities(args.jobs)
    return profile, rank(profile, jobs)


def command_job_match(args: argparse.Namespace) -> int:
    _, matches = _job_matches(args)
    for item in matches:
        print(f"{item.score:>3}  {item.opportunity.slug:<28} {item.opportunity.name}")
    return 0


def command_job_report(args: argparse.Namespace) -> int:
    profile, matches = _job_matches(args)
    threshold = int(profile.preferences.get("career", {}).get("minimum_match_score", 50))
    path = write_report(
        args.output,
        render_report(profile, matches, title="Open Talent Job Radar Report", threshold=threshold, mode="job"),
    )
    print(f"Wrote {path}")
    return 0


def command_job_track(args: argparse.Namespace) -> int:
    _, matches = _job_matches(args)
    for item in matches:
        if item.opportunity.slug == args.slug:
            path = write_template(Path(args.output) / f"{item.opportunity.slug}.md", job_application_record(item))
            print(f"Wrote {path}")
            return 0
    raise SystemExit(f"Unknown job: {args.slug}")


def _sync_catalog(args: argparse.Namespace, label: str) -> int:
    raw_sources = load_source_catalog(args.sources)
    sources = [
        {
            "slug": f"{source['organization'].lower()}-{index}",
            "name": source["name"],
            "url": source["url"],
        }
        for index, source in enumerate(raw_sources, start=1)
    ]
    state = sync_source_records(sources, args.state, args.timeout)
    path = write_report(args.output, render_source_monitor(state))
    changed = sum(1 for record in state["sources"].values() if record["changed"])
    print(f"Checked {len(sources)} official {label} sources; {changed} content changes detected. Wrote {path}")
    return 0


def command_job_sync(args: argparse.Namespace) -> int:
    return _sync_catalog(args, "job")


def command_oss_sync(args: argparse.Namespace) -> int:
    return _sync_catalog(args, "open-source")


def command_analyze(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile)
    jobs = load_opportunities(args.jobs)
    opportunities = load_opportunities(args.opportunities)
    path = write_report(args.output, render_analysis(profile, jobs, opportunities))
    print(f"Wrote {path}")
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

    job_match_parser = subparsers.add_parser("job-match", help="Rank verified job and internship records.")
    job_match_parser.add_argument("--jobs", default=DEFAULT_JOBS, help="Directory containing job records.")
    job_match_parser.set_defaults(func=command_job_match)

    job_report_parser = subparsers.add_parser("job-report", help="Write a job and internship recommendation report.")
    job_report_parser.add_argument("--jobs", default=DEFAULT_JOBS, help="Directory containing job records.")
    job_report_parser.add_argument("--output", default="reports/jobs-latest.md")
    job_report_parser.set_defaults(func=command_job_report)

    job_track_parser = subparsers.add_parser("job-track", help="Create an interview and application record for one job.")
    job_track_parser.add_argument("--jobs", default=DEFAULT_JOBS, help="Directory containing job records.")
    job_track_parser.add_argument("slug")
    job_track_parser.add_argument("--output", default="applications/jobs")
    job_track_parser.set_defaults(func=command_job_track)

    job_sync_parser = subparsers.add_parser("job-sync", help="Monitor reviewed official career pages for changes.")
    job_sync_parser.add_argument("--sources", default=DEFAULT_JOB_SOURCES)
    job_sync_parser.add_argument("--state", default="data/job-source-state.json")
    job_sync_parser.add_argument("--output", default="reports/job-source-monitor.md")
    job_sync_parser.add_argument("--timeout", type=int, default=20)
    job_sync_parser.set_defaults(func=command_job_sync)

    oss_sync_parser = subparsers.add_parser("oss-sync", help="Monitor reviewed official open-source program pages for changes.")
    oss_sync_parser.add_argument("--sources", default=DEFAULT_OSS_SOURCES)
    oss_sync_parser.add_argument("--state", default="data/oss-source-state.json")
    oss_sync_parser.add_argument("--output", default="reports/oss-source-monitor.md")
    oss_sync_parser.add_argument("--timeout", type=int, default=20)
    oss_sync_parser.set_defaults(func=command_oss_sync)

    analysis_parser = subparsers.add_parser("analyze", help="Write an auditable combined job and open-source analysis.")
    analysis_parser.add_argument("--jobs", default=DEFAULT_JOBS)
    analysis_parser.add_argument("--output", default="reports/radar-analysis.md")
    analysis_parser.set_defaults(func=command_analyze)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
