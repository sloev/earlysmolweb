# Cooperation log — Early Smol Web

Append-only coordination log. Agents read the latest entries before starting and append a dated handoff on completion.

---

## 2026-11-16 — Grok agent (schedule run)

**Agent:** Grok (xAI)
**Task:** Initial coordination pass + advance Faroe Islands Track B (publishing milestone) and review first-wave status.
**Branch policy:** main only; no branches or PRs created.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, research/*.md (all first-wave + a few others), coop.log.md (was PLACEHOLDER).
**Files touched:** coop.log.md (this entry); research/faroe-islands.md (appended Sosialurin 1997 internet-edition evidence).

**Findings summary:**
- First-wave countries (Greenland, Faroe Islands, Iceland, Denmark, Iran, Uruguay) already have substantial research notes. Iceland has a strong probable personal homepage (Björn Bjarnason, 23 Jan 1995). Greenland has solid infrastructure + Atagu newspaper chronology. Faroe had connectivity/mail but limited personal-page leads.
- Added to Faroe: public launch of Internet Sosialin / Sosialurin on the web on 25 November 1997 (first automated Faroese newspaper system), with earlier trials in 1995–97. This is a verified institutional/publishing milestone, not a personal homepage.
- No new personal-site candidates verified this run. No changes to data models or other country files.

**Status:** Faroe Islands status remains “connectivity and academic-network leads found; no personal-site candidate verified yet” with stronger publishing chronology.

**Unresolved / next concrete steps:**
1. Recover any surviving Atagu / atagu.gl capture or contemporary 1995 launch notice for Greenland.
2. Request or search Faroese National Library web archive for early .fo personal pages and the 1997 Sosialurin site.
3. For Iceland: contact Borgarskjalasafn / Miðheimar successors for original 1995 Björn Bjarnason homepage files.
4. Continue parallel scouting on remaining first-wave countries and low-priority leads elsewhere.
5. Tree repo (sloev/tree) continues Phase 5 Ahnentafel expansion; no cross-repo action this run.

**Handoff:** Ready for next agent. Prefer local-language sources and keep every country’s status visible. Small commits on main only.

---

## 2026-11-16 (later) — Grok agent (continued schedule work)

**Agent:** Grok (xAI)
**Task:** Continue first-wave advancement: Iceland personal-homepage corroboration + Greenland Atagu archive check.
**Branch policy:** main only.
**Files inspected:** research/iceland.md, research/greenland.md, Wayback Machine calendar for atagu.gl, English Wikipedia Björn Bjarnason, Vísir 2005 anniversary.
**Files touched:**
- research/iceland.md — added Wikipedia + Vísir corroboration for Björn Bjarnason site; updated status and candidate register.
- research/greenland.md — recorded Wayback Machine negative finding (earliest public capture of atagu.gl is 21 April 1999; none 1995–98).
- coop.log.md (this entry).

**Findings:**
- Iceland: Björn Bjarnason’s personal homepage remains the strongest named personal-expression candidate. English Wikipedia explicitly calls it the first Icelandic politician’s website (started 19 Feb 1995) and one of the Internet’s earliest blogs. Status upgraded slightly to reflect the candidate register entry.
- Greenland: No public Wayback captures of atagu.gl before 21 April 1999. This does not disprove a 1995 launch but confirms the principal verification gap remains open (Netarkivet, party archives, or private backups needed).

**Status updates:**
- Iceland: one strong probable personal homepage identified; further candidates still needed.
- Greenland: Atagu still probable institutional web-news publication; archive gap documented.

**Unresolved / next concrete steps:**
1. Netarkivet / Greenlandic or Danish national web-archive search for any 1995–98 atagu.gl or related captures.
2. Faroese National Library web-archive access request for early .fo personal pages and 1997 Sosialurin.
3. Borgarskjalasafn / Miðheimar contact for original 1995 Björn Bjarnason files.
4. Parallel scouting on Denmark, Iran, Uruguay, and lower-priority countries.
5. Tree repo: continue Broager/Dybbøl p53 parish-register work when capacity allows.

**Handoff:** Small, reviewable commits on main. Prefer local-language sources. Keep every country’s status visible.


---

## 2026-11-16 (continued) — Icelandic UUCP chronology corroboration + Tree source audit

**Branch policy:** main only in both repositories. A fresh branch audit after the user's cleanup reports only main in sloev/tree and sloev/earlysmolweb; main is the default branch in both.

**Early Smol Web — Iceland**
- Updated research/iceland.md with an independent institutional-history source from Skýrslutæknifélag Íslands (Icelandic Information Technology Society).
- The source's 1986 timeline says Hafró began a UUCP connection to EUnet and Reiknistofnun Háskólans established a UUCP connection to Hafró in the same year. It separately dates Hafró/RHÍ TCP/IP adoption to 1988 and the ISnet external NORDUnet/IP-over-X.25 transition to 1989.
- Assessment remains retrospective corroboration, not a contemporary connection log. The addition strengthens and clarifies the existing 1986 UUCP milestone; it does not change the personal-homepage candidate or claim a Web launch.
- Source: https://www.sky.is/sagautaislandi/129-kafli-3-1975-1984/2652-3-hluti-1985-1994-einkatolvusprenging-og-netvaeding

**Tree — Dybbøl p53**
- Re-read research_method.md and family-tree.md on main before research.
- Rechecked the online Dybbøl source index. The KMB 1861–1927 FVD reference p.169 / image 85 / no.1 resolves to Christen Hansen's 1839 birth/baptism, not the target Rasmus Jensen–Anne Christine Hansen marriage in 1866. The exact 1866 marriage page remains unidentified; no parentage inference or person-data edit was made.
- Added Milestone 46 to research_method.md to record the corrected index interpretation and precise next steps.
- Sources: https://www.stroemming.dk/genealogy/gedweb/Public/da/Lists/sources-K.html ; https://www.stroemming.dk/genealogy/gedweb/Public/da/Details/Details-I6346.html ; https://www.rigsarkivet.dk/vejledning/kirkeboger-borgerlige-vielser-m-m/kirkeboeger-kom-godt-i-gang/

**Commits**
- sloev/earlysmolweb: research/iceland.md — https://github.com/sloev/earlysmolweb/commit/dfd0c990144ed4dea49de66a9c34b2a183d97ec4
- sloev/tree: research_method.md — https://github.com/sloev/tree/commit/550e25629c640d2f4976aa5ab00cd355720db23b

**Handoff**
1. For Iceland, seek contemporary EUnet/ISnet records, original mail/news headers, or network logs to elevate the 1986 UUCP claim beyond retrospective institutional history; continue identifying the four Usenet-receiving Icelandic hosts.
2. For Greenland, seek Netarkivet/private Atagu captures and primary evidence for the 1995 domain/operator chronology.
3. For Tree, identify the actual Dybbøl 1866 marriage image before any p53 parentage change; if inaccessible, rotate to an unrelated open branch and prioritize original register images.

All edits were committed directly to main. No private genealogy data was accessed or decrypted. No local build, tests, or browser checks were run.


## 2026-11-16 (continued) — contemporary EUnet topology evidence for Iceland

- Added a contemporaneous source to research/iceland.md: Peter Houlder's “EUnet” article in *AUUGN*, Vol. 8 No. 3–4 (August 1987), which gives EUnet country totals as of 27 April 1987. It lists Iceland as one directly connected EUnet host, hafro, contact hafro!gunnar.
- Important scope distinction: this is the number of mail-handling hosts directly connected to the national EUnet network, not the number of all local UUCP nodes. It is compatible with the eight-site Icelandic UUCP network described in the December 1987 ICEUUG report and the fuller December UUCP map.
- The new evidence strengthens hafro's status as Iceland's international UUCP/EUnet gateway but does not name the four Icelandic Usenet-receiving sites.
- Source: https://ftp.icm.edu.pl/packages/UnixArchive/Documentation/AUUGN/AUUGN-V08.34.pdf (August 1987 issue, pp. 159–160; table based on 27 April 1987).

**Commit:** research/iceland.md — 2bafb1d2543c8c3a13dffe19881c71dde2c99382

**Handoff:** Cross-check the April EUnet table, December ICEUUG report and 2 December UUCP map without treating their different host counts as contradictions. Search for original Icelandic mail/news headers or surviving ICEUUG records that identify the four news-receiving nodes.
