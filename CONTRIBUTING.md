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

Do not edit docs/index.html by hand. It is the public research atlas interface and reads the latest research Markdown files directly from the public main branch when visitors open the page. Add and update canonical findings in research/; the website reflects those changes automatically on the next page load. GitHub Pages serves main /docs.

## Commit style

Use concise messages that describe the research or documentation change. Keep source citations close to the claims they support.


## Public article data

Every new or materially updated country research file must include or refresh one `article-data` JSON block inside an HTML comment near the top of the Markdown file. This is how the website generates its country article; do not create separate HTML pages or manually edit the site template for country content.

The block contains `title`, `dek`, `lead`, `sections` (each with `heading` and `markdown`), `image` (sourced image metadata or `null`), and `sources`. Follow the complete example and rules in AGENTS.md and WORK_METHOD.md. Article prose must be readable, genuinely explanatory, and fully supported by the research record.

When adding an image, use a reusable source, verify its license, and include direct image URL, alt text, caption, creator, exact license, and source page URL. If none is verified, use `null`; the website may provide an attributed Wikimedia Commons fallback. Never invent image credits or claims.
