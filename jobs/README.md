# Job records

This directory is independent from `opportunities/`. It contains only individually verified jobs or internships that can be matched to a personal profile.

## Workflow

```text
job-sources/ official source
        -> candidate noted in an issue or personal inbox
        -> human checks official JD, eligibility, location, and deadline
        -> jobs/<slug>.json (status: open)
        -> job-match / job-report / job-track
        -> applied, interviewing, offer, rejected, or closed
```

Do not add a company home page here as a job record. A record must represent one concrete role or a clearly scoped official campus program.

## Required fields

`slug`, `name`, `organization`, `kind`, `url`, `status`, `skills`, `interests`, and `last_verified`.

For job matching, also add `employment_type`, `role_family`, `location`, `work_mode`, and `seniority` whenever the official page supplies them. Use `status: "open"` only after checking the official page; otherwise keep the item outside this directory until it is verified.
