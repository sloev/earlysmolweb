# Working method

## Mission

Find, document, and preserve the earliest discoverable **personal expressions on the internet** associated with every country and separately tracked territory. The emphasis is on people making a corner of the network their own: personal homepages, hand-built sites, web diaries, personal blogs, homepages hosted by universities/ISPs, GeoCities-style pages, personal web rings, and early independent online publishing.

This is a historical research project, not a contest. "Earliest" is a working hypothesis that must be qualified by the surviving evidence. We do not equate the first surviving page with the first page ever made.

## Global coverage and priority heuristic

The commitment is worldwide coverage: **all 195 baseline countries are in scope**, alongside the separately tracked research jurisdictions listed in `COUNTRIES.md`. The priority register is a heuristic for allocating attention, not a country-by-country completion sequence.

- Work across multiple countries concurrently; do not wait to exhaust one country before opening or advancing others.
- Use priority to guide initial scouting, scarce researcher time, and where to dig more deeply—not to exclude, defer indefinitely, or rank the historical value of any place.
- Follow strong leads wherever they arise, including countries later in the list. New evidence can change priorities at any time.
- Use diminishing returns as a practical stopping rule: when a round of searches is producing few new leads, record the gaps and move effort elsewhere. Do not declare a country exhausted or complete merely because obvious sources have been checked.
- Keep every country's status visible (not started, scouting, active, evidence review, low-yield for now, revisited); low-yield is provisional, not closed.
- Revisit countries as new archives, local-language sources, contacts, tools, and cross-border leads become available.

The goal is a continuously improving worldwide map, not a sequential checklist.

## Two tracks, run simultaneously

### Track A — Leads

Purpose: discover candidates and routes into local histories.

- Search in local languages, scripts, transliterations, and historical terminology.
- Look beyond search engines: national libraries, university archives, ISP histories, computer clubs, BBS/FidoNet communities, newspapers, Usenet, mailing lists, web rings, alumni pages, and personal recollections.
- Search country-specific domains and hosting conventions, but do not assume a country-code domain proves the author's residence or nationality.
- Follow links outward from one confirmed page to its friends, guestbooks, rings, link lists, and reciprocal links.
- Record weak leads too, clearly labelled as leads. Never quietly promote a lead to a verified record.
- Seek local researchers and native-language sources, especially where the public web archive is sparse.

Deliverable: a lead record with a URL/name, country connection hypothesis, date clue, discovery route, source, confidence, and next action.

### Track B — Evidence, extraction, and write-up

Purpose: turn leads into durable, reviewable country records.

- Verify the page or its archived capture, author/owner, personal character, country connection, and date.
- Capture evidence before writing conclusions. Prefer primary evidence: dated source files, server/ISP records, contemporaneous directory listings, web-archive captures, personal statements, and contemporary press.
- Preserve exact URLs, archive URLs, access dates, timestamps, screenshots or WARC references where lawful and practical, and relevant quoted metadata.
- Distinguish a page's **creation**, **first known publication**, **first archive capture**, **last update**, and **date inferred from secondary evidence**.
- Record conflicting dates and uncertainty. Never silently choose the most convenient date.
- Produce a concise country narrative and a structured entry for each candidate.
- Re-check citations and links; flag dead links and explain how evidence survives.

Deliverable: a sourced country page and structured candidate records, with confidence and unresolved questions visible.

## Coordination protocol

1. Read this file and `coop.log.md` before starting.
2. Claim work in `coop.log.md` with a short timestamped entry: track, country/territory, exact task, status, and branch/PR if applicable.
3. Avoid overlapping country assignments. If a country is already active, coordinate in the log before duplicating work.
4. Use small, reviewable commits. Do not overwrite another agent's work; fetch the latest file and merge changes deliberately.
5. On completion, append findings, source links, confidence, open questions, and the next handoff to `coop.log.md`.
6. A lead is not a finding. Label every record `lead`, `candidate`, `probable`, or `verified`.
7. When in doubt, leave an explicit question rather than inventing a date, author, URL, or country attribution.

## Evidence standard

Use the following hierarchy as a guide, not a rigid formula:

- **A — Direct/primary:** original page with credible dated metadata; contemporaneous hosting records; a reliable archive capture; author/owner testimony corroborated by a surviving artifact.
- **B — Strong contemporary corroboration:** dated link directory, web ring, newspaper, university/ISP page, mailing-list post, or other contemporary source identifying the page/person.
- **C — Retrospective corroboration:** later interview, personal recollection, retrospective article, or modern database.
- **D — Discovery lead only:** search result, undated mention, copied link, unattributed screenshot, or unsupported claim.

A high-confidence "earliest known" claim normally needs at least one A source or multiple independent B sources. C and D sources are useful, but must not be presented as proof by themselves.

## What counts

Include personal expression made by an individual or a small personal project, including:
- personal homepages and self-authored sites;
- personal diaries, journals, weblogs, photo pages, fan pages, art pages, and experimental sites;
- personal pages hosted on university, employer, ISP, community, or free-hosting accounts;
- early personal publishing on local networks or services when it clearly connects to the public internet story.

Usually exclude:
- corporate, government, institutional, and commercial homepages unless they preserve a personal page or provide essential context;
- official artist/celebrity promotional sites with no meaningful personal authorship;
- forum profiles or social-network accounts alone, unless they represent a notable early form of personal publishing;
- pages merely hosted on a country's domain without a defensible connection to a person or community there.

Do not impose a narrow definition of "website": record precursors and adjacent forms, but label their medium accurately (BBS, Usenet, Gopher, FTP, personal page, web diary, etc.).

## Country and territory attribution

Country is a research facet, not a claim about identity. A page may be connected through the author's residence, local hosting, language/community, or explicit self-description. Record which connection applies and do not infer nationality from a domain suffix.

Use the 195-state baseline in `COUNTRIES.md`. Track Greenland and the Faroe Islands as separate research jurisdictions, as well as other territories when evidence warrants it. Denmark remains its own country entry. Where sovereignty or status is contested, record the chosen scope and explain it neutrally; do not erase local internet histories.

## Standard candidate record

Use this template in country files (one record per person/site):

```yaml
id: ISO-3166-1-alpha-2-or-territory-slug + local sequence
status: lead | candidate | probable | verified
person_or_project:
title:
url_original:
url_archived:
country_or_territory:
connection_basis: author-residence | local-hosting | language-community | self-described | other
medium: personal-homepage | diary | blog | art | community-page | bbs | usenet | gopher | other
date_claimed:
date_type: creation | first-publication | first-capture | last-updated | inferred
date_precision: exact | month | year | range | unknown
evidence:
  - source_url:
    source_type:
    observed_date:
    supports:
    grade: A | B | C | D
author_attribution:
language:
notes:
uncertainties:
researcher:
last_checked:
```

Do not fill unknown fields with guesses. Use `unknown` or leave them blank.

## Country write-up outline

1. **Internet context:** first public connectivity and local hosting context, with sources.
2. **Personal web ecology:** ISPs, universities, clubs, free hosts, directories, web rings, language/script issues.
3. **Earliest known personal expressions:** dated entries, ranked by strength of evidence rather than false certainty.
4. **Evidence and chronology:** what survives, what does not, and how dates were established.
5. **Gaps and next leads:** local archives, people, terms, institutions, and unresolved claims.
6. **Bibliography / evidence log:** source URLs, archive captures, access dates.

## Research habits and ethics

- Search in relevant local languages and scripts; preserve original titles and names alongside transliterations.
- Respect privacy. Prefer material intentionally published publicly; do not expose private contact details or sensitive personal information.
- Do not bypass access controls, paywalls, or archive restrictions. Respect robots, terms, copyright, and takedown requests.
- Quote only what is needed to substantiate a historical claim. Link to originals and archives rather than republishing entire sites.
- Keep a copy of research metadata and citations in the repository; large binary captures should live in an appropriate archive with stable identifiers, not be committed casually.
- Make negative findings precise: "no earlier example found in sources searched" rather than "none existed."

## First research wave

Begin with a distributed first wave across Greenland, the Faroe Islands, Iceland, Denmark, Iran, and Uruguay, while a parallel researcher/agent explores the United States as a comparative/control case. At the same time, keep scouting and accepting leads from every other country; do not serialize work or require one country to be exhausted before moving to another. Use `COUNTRIES.md` as a flexible heuristic and rebalance effort according to lead quality, documentation gaps, and diminishing returns. The list is a discovery strategy, not a ranking of cultural importance or technical sophistication.
