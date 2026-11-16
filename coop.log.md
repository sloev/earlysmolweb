# Cooperation log

Append-only coordination ledger. Read before claiming work; append updates rather than rewriting history.

## Protocol
- Claim: `[YYYY-MM-DD HH:MM UTC] CLAIM — Track A/B — place — scope — agent — branch/status`
- Update: `[YYYY-MM-DD HH:MM UTC] UPDATE — ...`
- Handoff: `[YYYY-MM-DD HH:MM UTC] HANDOFF — ... — evidence/links — confidence — next action`
- Keep claims narrow enough to avoid collisions. Track A (leads) and Track B (evidence/write-up) may work on the same place if their scopes are explicit.
- Use status labels: `claimed`, `in progress`, `blocked`, `handed off`, `complete`.

## Initial project setup — 2026-11-16
- [2026-11-16] SETUP — Repository was empty; initialized README, working method, country priority register, and this coordination ledger.
- [2026-11-16] PROTOCOL — Two simultaneous tracks established: **A / Leads** and **B / Evidence & write-up**. See `WORK_METHOD.md`.
- [2026-11-16] NEXT — First wave proposed: Greenland, Faroe Islands, Iceland, Denmark, Iran, Uruguay. Parallel comparative research: United States.
- [2026-11-16] NOTE — No historical candidates have yet been verified by this setup commit. All country work remains unclaimed until an agent appends a claim below.

## Active claims
- [2026-11-16] CLAIM — Track A — Uruguay — investigate Chasque's 1995 user-page hosting and find individual personal pages in early .uy/RAU archives — ChatGPT — in progress.
- [2026-11-16] CLAIM — Track A — Iran — discover pre-2001 personal-homepage leads and verify early-2001 weblog leads/territorial attribution — ChatGPT — in progress.

## Findings and handoffs
_None yet._

## Research updates — 2026-11-16
- [2026-11-16] UPDATE — Track A scouting — Greenland — found 1995 connectivity/ISP and local-institution leads (NSRC; Nordic library technology report); no personal homepage verified. See `research/greenland.md`.
- [2026-11-16] UPDATE — Track A scouting — Faroe Islands — found January 1995 university/research connectivity lead; no personal homepage verified. See `research/faroe-islands.md`.
- [2026-11-16] UPDATE — Track B context — Iceland — University of Iceland reports its institutional site went online November 1992; 1994 is its oldest surviving version; no personal page verified. Vefsafn offers open access to Icelandic web material from 1996 onward. See `research/iceland.md`.
- [2026-11-16] HANDOFF — Greenland/Faroe/Iceland — these are infrastructure and archival leads only, not earliest-personal-web findings. Next researcher should extract named individuals and personal URLs from NSRC records and Vefsafn/Internet Archive captures, then record evidence grades.

- [2026-11-16] PROJECT RULE — All 195 baseline countries are in scope from the outset, alongside separately tracked jurisdictions. `COUNTRIES.md` is a flexible priority heuristic, not a sequential queue: research multiple countries in parallel, follow strong leads anywhere, use diminishing returns rather than exhaustion as the stopping rule, and revisit countries as evidence emerges. See `WORK_METHOD.md`.

## Notice to all agents — global coverage and live instructions

**Effective immediately:** the 195-country baseline is a worldwide coverage commitment. The priority list is a flexible heuristic, not a sequential queue. Work across countries in parallel; do not wait to exhaust one country before researching another. Follow strong leads wherever they arise, use diminishing returns to decide when to shift effort, record gaps rather than declaring a country exhausted, and revisit countries when new evidence appears. Greenland, the Faroe Islands, and other separately tracked jurisdictions remain in scope as listed in `COUNTRIES.md`.

**Before starting or resuming any task, every agent must read this entire `coop.log.md` for current claims, updates, handoffs, and instructions, as well as `WORK_METHOD.md` and the relevant country file.** Check the log again before claiming work and before committing or handing off, so you do not duplicate active work or miss new directions. Treat this log as the live coordination channel; append material updates and handoffs here.

- [2026-11-16] UPDATE — Track A — Iran — identified candidate personal weblog leads for Salman Jariri (reported 7 Sep 2001) and Hossein Derakhshan (Sep 2001), plus contemporaneous 1995/1997 infrastructure directories for further extraction. Neither is yet verified as the earliest personal website associated with Iran; territorial attribution and archive captures remain open. See research/iran.md.

- [2026-11-16] UPDATE — Track A — Uruguay — identified a promising August 1995 Chasque lead: a study reports open public user-page uploads without institutional affiliation. Also found .uy/RAU 1990 institutional roots, a 1995 Peñarol fan site, and Montevideo Portal (Nov 1995) as context/link-discovery paths. No personal-page candidate verified yet. See research/uruguay.md.

- [2026-11-16] UPDATE — Track A — Uruguay — inspected the three contemporary NSRC records: Chasque node update (12 Jun 1995), RAU WWW launch announcement (4 Nov 1995; server went live 1 Nov), and Chasque/ITeM report (23 Apr 1996). Found a concrete individually attributed candidate, “Quinquenio” by designer Sebastián Mateos, on GeoCities; main page says online since Nov 1997, a subpage dated 29 Nov 1997, contact email at chasque.apc.org. Candidate only: creator's Uruguay residence and solo/personal authorship still need corroboration. See research/uruguay.md. Next: investigate creator identity, archived guestbook/links, and earlier Chasque-hosted personal pages.
- [2026-11-16] UPDATE — Track A — Iran — inspected full 13 Nov 1995 NSRC report. It lists institutional hosts/Gopher servers and reproduces Neda's announcement: individual accounts existed, but Internet service at that date was email and offline FTP/news/mailing lists, not direct web hosting. No personal homepage identified. Hostnames and Gopher servers are leads for extracting older personal directories, not evidence of personal sites. See research/iran.md.
