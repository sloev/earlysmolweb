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

Add or refresh an `article-data` JSON block only when the research supports a specific, tellable story rooted in that country. If it does not, omit the block; the country remains in Coverage and Research records. The website publishes only explicit article blocks and does not generate generic stories from research notes. Do not create separate HTML pages or manually edit the site template for country content.

The block contains `title`, `dek`, `lead`, `sections` (each with `heading` and `markdown`), `image` (sourced image metadata or `null`), and `sources`. Follow the complete example and rules in AGENTS.md and WORK_METHOD.md. Article prose must be readable, genuinely explanatory, and fully supported by the research record.

When adding an image, use a reusable source, verify its license, and include direct image URL, alt text, caption, creator, exact license, and source page URL. If none is verified, use `null`; the website will publish without an image rather than substituting generic scenery. Never invent image credits or claims.


## Editorial gate for public articles — supersedes older broad article guidance

Do not write an article just because a country research file exists. Do not turn a country timeline, infrastructure summary, list of leads, or evidence-gap note into a generic country story. Publish an article only when the research supports a specific, tellable episode rooted in that country: for example, a named person publishing a homepage, a newspaper or community launching an online service, a local provider and its users, a particular online community, or a recoverable early website. The article must tell what happened, who did it, when, where, how, and what the sources actually establish. It should read as continuous reported prose, not a wiki entry, catalogue, bullet-point chronology, or general overview.

If no such episode is established, omit the article-data block entirely. The country remains discoverable in Coverage and Research records. Do not use the article slot as a placeholder. Remove any existing article block that no longer meets this test. The website must not auto-generate an article from raw research notes.

Images are editorial evidence, not decoration. Search for and prefer (in order of relevance) portraits of named participants, original screenshots/captures of the actual site or service, contemporary publication/provider logos, newspaper mastheads, event or workplace photographs, and relevant archival documents. Do not use generic country landscapes, generic flags, or unrelated stock imagery. Never imply that a portrait depicts a named person unless its identity is established by the source. For every image, verify that the exact asset is reusable and provide its direct HTTPS URL, meaningful alt text, contextual caption, creator/rights holder, exact license/rights statement, and source page. Link credits to the source page. If no suitable, reusable and accurately identified image is found, set image to null and publish without an image; do not fabricate or substitute scenery.

A short story is better than a padded one. Aim for a focused narrative, normally 300–700 words when the evidence supports it, with 2–5 key sources. Every material claim must be traceable to the canonical research note and cited source. Preserve disputed dates, distinguish first-hand contemporary evidence from retrospective accounts, and do not claim a national first unless comparative evidence supports it. If the evidence supports only a candidate or probable story, say so plainly in the prose.
