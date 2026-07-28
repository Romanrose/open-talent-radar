# Contributing to Open Talent Radar

## Principles

- Treat every opportunity record as a claim that needs a verifiable source.
- Link to an official page whenever possible.
- Mark programs as `verify` or `watch` when the next intake is not explicitly open.
- Keep personal data out of pull requests and issues.
- Prefer small, reviewable changes.

## Development

```bash
python -m unittest discover -s tests
python -m radar.cli report --output reports/latest.md
```

When adding a program, use one JSON file per opportunity and preserve the fields in the example record from the README.
