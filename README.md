# Open Talent Radar

> Discover open-source mentorship opportunities, match them to your profile, and turn a promising program into a sustained contribution plan.

Open Talent Radar is a GitHub-native, privacy-friendly command-line tool for students and early-career developers. It keeps opportunities, your profile, learning plans, and application records in version-controlled files—no website, account, or database required.

## What it does

- Tracks open-source internships, mentorships, contribution programs, and competitions in simple JSON files.
- Ranks each opportunity against your skills, interests, preferences, deadline, and mentor availability.
- Generates a Markdown radar report that is easy to review in GitHub.
- Creates a focused learning checklist and an application record for any opportunity.
- Adds a dedicated job radar for verified internships and campus roles, with role, location, graduation-year, and interview-preparation tracking.
- Refreshes the committed report on a weekly GitHub Actions schedule.
- Monitors official program pages for change signals, while keeping every catalog update human-reviewed.

## Quick start

```bash
git clone https://github.com/<your-account>/open-talent-radar.git
cd open-talent-radar
cp profile.example.json profile.json

# Optional: use a virtual environment if you want the oss-radar command.
python -m venv .venv
source .venv/bin/activate
pip install .

# Edit profile.json with your own background, then run:
oss-radar --profile profile.json match
oss-radar --profile profile.json report
oss-radar --profile profile.json learn mindspore-internship
oss-radar --profile profile.json track casbin-talent
oss-radar sync
oss-radar job-match
oss-radar job-report
oss-radar job-track bytedance-seed-internship
oss-radar job-sync
oss-radar oss-sync
```

You can always replace `oss-radar` with `python -m radar.cli` when you do not want to install the package.

`oss-radar sync` stores a content-hash snapshot of official source pages in `data/source-state.json` and writes `reports/source-monitor.md`. It detects pages that need a human review; it deliberately does **not** scrape arbitrary page text into unverified opportunities.

The generated files live in `reports/`, `learning/`, and `applications/`. Commit them or turn their action items into GitHub Issues.

For a project-driven Chinese learning path covering AI sandboxing, memory/performance work, LLM infrastructure, MindSpore, and Casbin/Casibase, see [AI Systems 学习目录](learning/ai-systems/).

## Example output

```text
 86  casbin-talent                Casbin Talent 2026
 83  mindspore-internship         MindSpore Open Source Internship
 78  ospp                         Open Source Promotion Plan
```

## Repository layout

```text
opportunities/     Curated opportunity records, one JSON file per program
radar/             Matching engine, report generator, and CLI
reports/           Generated recommendation reports
learning/          Generated preparation checklists
applications/      Generated application and contribution records
.github/           Weekly report workflow and contribution issue forms
```

## Opportunity data model

Every file under `opportunities/` is intentionally small and reviewable:

```json
{
  "slug": "community-program",
  "name": "Community Program",
  "organization": "Community",
  "kind": "open_source_mentorship",
  "url": "https://example.org",
  "status": "open",
  "deadline": "2026-08-31",
  "mentorship": true,
  "remote": true,
  "skills": ["Python", "Git"],
  "interests": ["Open Source"],
  "summary": "Short, factual description.",
  "source": "official"
}
```

Use `open`, `watch`, or `verify` for `status` so a report does not silently treat an unverified or cyclical program as actively accepting applications.

## Job radar

Job records live in the independent `jobs/` directory. The open-source radar reads only `opportunities/`; the job radar reads only `jobs/`. The official discovery sources are separately maintained in `job-sources/`, so a company career page never becomes a falsely specific job record. A verified job record can include `employment_type`, `role_family`, `location`, `work_mode`, and `seniority`.

Use `oss-radar job-match` for a ranked list, `oss-radar job-report` for `reports/jobs-latest.md`, and `oss-radar job-track <slug>` for a resume/interview checklist. Add only official career pages or job posts and retain `last_verified`; recruitment status changes quickly.

`oss-radar job-sync` checks the separate, human-reviewed `job-sources/official-china.json` catalog once and reports page-level changes. It is intentionally a review signal, not a scraping or auto-application tool.

`oss-radar oss-sync` applies the same review gate to `oss-sources/`, where long-running mentorship programs, domestic foundations, and project communities are kept separate from individual opportunity records.

## Scoring is explainable

The score combines skill overlap, interest overlap, mentor availability, remote preference, current status, and time-sensitive deadlines. It is deliberately rules-based in v0.1: contributors can inspect and adjust the weights in `radar/matcher.py` without needing an API key or opaque model call.

## Adding a source

1. Open an **Add an opportunity** issue or add a JSON file under `opportunities/`.
2. Prefer official program pages and include only verifiable claims.
3. Run `python -m unittest discover -s tests` and regenerate `reports/latest.md`.
4. Open a pull request with the source link and the program’s last verified date in the description.

The weekly workflow runs both the source monitor and the example report. It commits source-state changes and the monitor report so maintainers can review the exact pages that changed.

## Roadmap

- [x] Profile-driven ranking and Markdown reports
- [x] Learning and application templates
- [x] Weekly GitHub Actions report refresh
- [ ] Source adapters with change detection for official pages and GitHub Issues
- [ ] Optional local/remote LLM analysis for project-task fit
- [ ] GitHub Issue synchronization and deadline alerts
- [ ] Community-maintained program catalog and review policy

## Contributing

Contributions are welcome, especially verified opportunity records, source adapters, scoring improvements, and localization. Please avoid submitting private mentor contact details or scraping sources that prohibit automated access.

## License

[MIT](LICENSE)
