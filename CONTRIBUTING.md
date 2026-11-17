# Contributing

Thank you for helping document early internet history worldwide.

## Before researching

1. Read WORK_METHOD.md and the latest coop.log.md.
2. Check the existing country file to avoid duplicating work.
3. Coordinate overlapping work in coop.log.md.
4. Work directly on main; this project currently uses a main-only collaboration policy.

## Evidence requirements

- Link sources next to the claims they support.
- Prefer primary evidence and contemporary sources.
- Record source type, observed/publication date, what it supports, and evidence grade where possible.
- Distinguish creation, first publication, first archive capture, last update, and inferred dates.
- Keep conflicting accounts and uncertainty visible.
- Label each item as a lead, candidate, probable, or verified finding.
- Never infer a person's nationality from a domain suffix or server location alone.

## Research files

Add or update one Markdown file per country or separately tracked jurisdiction in research/. Use a lowercase, hyphenated filename. Follow the country write-up outline and candidate record in WORK_METHOD.md.

Do not put private contact details or sensitive personal information in the repository. Respect copyright, archive restrictions, access controls, and takedown requests.

## Website

Do not edit docs/index.html by hand. It is generated from the research Markdown files by running scripts/build_site.py after installing the Python Markdown package. GitHub Actions runs the generator when research or generator inputs change on main, then commits the refreshed page to docs/index.html. GitHub Pages serves the main /docs folder.

## Commit style

Use concise messages that describe the research or documentation change. Keep source citations close to the claims they support.
