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


## 2026-11-16 — correction to Dybbøl page-169 interpretation

A follow-up check of the 1976 archival inventory corrected the previous Tree handoff's description of the Dybbøl page reference:

- The inventory *Nordslesvigske præstearkiver V: Sønderborg provsti* (Landsarkivet for de Sønderjyske Landsdele, Åbenrå, 1976) lists Dybbøl Ab 4 (1861–1927) as containing marriages from 1861 to 1906 (PDF text lines 769–773).
- Therefore the KMB 1861–1927 FVD p.169 / image 85 / no.1 citation attached to Christen Hansen's profile is in the marriage section, not a birth entry. It is likely a marriage relevant to Christen's family evidence; do not call it a baptism or confuse it with p53's reported 1866 marriage.
- The exact 18 September 1866 marriage page for Rasmus Jensen and Anne Christine Hansen is still not located. The correct volume is now firmly identified as Dybbøl Ab 4, 1861–1927; page/image identification and transcription remain open.
- Corrected Tree research_method.md in commit https://github.com/sloev/tree/commit/b2c2f72e40f5b95018ee00532192c8f5d66fcb21.

**Archival inventory:** https://slaegtsbibliotek.dk/2024/941454.pdf (Dybbøl Ab 4, pp. 13–15 / PDF text lines 769–773).

---

## 2026-11-16 (continued) — Grok agent: Denmark advancement

**Agent:** Grok (xAI)
**Task:** Advance Denmark first-wave research using webhistorie.dk timeline and research-project context.
**Branch policy:** main only.
**Files inspected:** research/denmark.md, webhistorie.dk timeline (http://webhistorie.dk/timeline-2/), related search results.
**Files touched:** research/denmark.md (appended “Additional leads from webhistorie.dk timeline” section); coop.log.md (this entry).

**Findings:**
- Reinforced the Royal Danish Library / Niels Brügger *History of the Danish web 1992–1997* project (Netarkivet WARC + SolrWayback) as the primary systematic route for extracting early personal pages.
- Added discovery leads from the project timeline: Helle Degn as first Danish MP with a personal web page (mid-1995 context); Uffe Ellemann Jensen weekly newsletter; first primary-school site (Stensgård Skole, Gladsaxe); first amt website (Aarhus Amt, Nov 1995); spring 1995 as major growth period.
- No new verified personal-homepage captures; Maardt (Feb 1995 contemporary broadcast) remains the strongest named individual candidate; Madsen Smed (Nov 1995) remains the family-homepage candidate. New leads are grade D until archive recovery.

**Status:** Denmark status unchanged in substance — early personal-page candidates identified; none independently verified from primary 1995 captures.

**Unresolved / next concrete steps:**
1. Netarkivet / SolrWayback searches for Maardt 1995 URL, Madsen Smed CompuServe page, Helle Degn early page, and other timeline-named sites.
2. DR Radio & TV Collection request for the 19 Feb 1995 Harddisken recording (exact metadata already recorded).
3. Continue Atagu / Faroe / Iceland open items from prior entries.
4. Parallel scouting on Iran and Uruguay.
5. Tree: identify actual Dybbøl 1866 marriage image (volume now confirmed as Ab 4) before any p53 parentage change.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible.

---

## 2026-11-16 (continued) — Grok agent: parallel scouting + Tree status check

**Agent:** Grok (xAI)
**Task:** Parallel first-wave / Tree coordination pass; no new personal-page verification this cycle.
**Branch policy:** main only.
**Files inspected:** research/uruguay.md (already dense), research/denmark.md, Tree research_method.md (Dybbøl status), Arkivalieronline / Rigsarkivet guidance, web searches for Dybbøl 1866 marriage and Helle Degn early page.
**Files touched:** coop.log.md (this entry). No country research files changed this pass (Denmark already updated earlier; Uruguay already comprehensive).

**Findings:**
- Uruguay research file is already extensive (Chasque 1995 public hosting, NSRC 1995–96 records, Quinquenio 1997 candidate, full pre-Web chronology). No incremental change required this cycle.
- Helle Degn: no contemporary 1995–96 URL or launch notice recovered beyond the webhistorie.dk timeline claim; later helledegn.dk archive captures exist but do not prove mid-1990s origin.
- Tree / Dybbøl p53: volume confirmation (Ab 4, 1861–1927, marriages 1861–1906) stands. Specific 18 Sep 1866 Rasmus Jensen–Anne Christine Hansen marriage page/image still not located in public indexes or secondary sources. No person-data edit made. Recommendation remains: locate original register image (Arkivalieronline / Rigsarkivet Aabenraa) before any parentage inference.

**Status:** No change to any country’s personal-homepage verification status. Denmark, Iceland, Greenland, Faroe, Uruguay remain as previously logged.

**Unresolved / next concrete steps:**
1. Netarkivet research access or SolrWayback queries for early Danish personal pages (Maardt, Madsen Smed, Helle Degn).
2. Dybbøl Ab 4 1866 marriage image identification and transcription (Tree).
3. Atagu early captures; Faroe National Library archive request; Iceland original Björn files.
4. Iran first-wave scouting if capacity allows.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Tree and earlysmolweb continue in parallel on main.

---

## 2026-11-16 (continued) — Grok agent: Costa Rica web milestone

**Agent:** Grok (xAI)
**Task:** Advance Costa Rica research with institutional first-website claim and personal-page status.
**Branch policy:** main only.
**Files inspected:** research/costa-rica.md, UCR University Council pronunciamientos, La Revista CR chronology, related search results.
**Files touched:** research/costa-rica.md (appended 1995 www.cr claim + personal-page status note); coop.log.md (this entry).

**Findings:**
- Added the UCR Unidad de Redes claim that it created the first Costa Rican website in 1995 at www.cr (grade C institutional retrospective; no contemporary capture recovered yet).
- Confirmed La Nación Digital (7 Apr 1995) remains the strongest dated early Web publication already on file.
- No named individual personal homepage from 1993–1997 verified for Costa Rica. 1994 HTML courses at ECCI-UCR and 1995 commercial opening (RACSA) create a plausible window; search continues.

**Status:** Costa Rica network chronology remains strong (1990 BITNET, 1993 TCP/IP). Web milestones now include the 1995 institutional www.cr claim. Personal-homepage status: none verified.

**Unresolved / next concrete steps:**
1. Recover capture or contemporary description of www.cr (1995).
2. Continue personal-page scouting for Costa Rica (student/staff directories, early ISP pages).
3. Netarkivet / Dybbøl / Atagu / Faroe / Iceland open items as previously logged.
4. Iran or other first-wave countries as capacity allows.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible.

---

## 2026-11-16 (continued) — Grok agent: Nauru Track A scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on high-priority small Pacific jurisdiction Nauru (priority list after Kiribati/Tuvalu); create initial research file.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** research/tuvalu.md, research/kiribati.md, COUNTRIES.md, WORK_METHOD.md, coop.log.md; web sources on CenpacNet and .nr.
**Files touched:** research/nauru.md (new); coop.log.md (this entry).

**Findings:**
- Created research/nauru.md. Documented 1998 CenpacNet ISP launch (contemporary Sept 1998 newswire of ~50 customers; Garoa retrospective 1998 with minor internal date note; IANA .nr 30 March 1998). No personal-homepage candidates located. No earlier network evidence found in readily available sources. Status: scouting.
- Null result on personal expression; infrastructure/publishing window opens 1998.

**Status:** Nauru added to research coverage as scouting / low-yield for personal pages for now. First-wave countries remain as previously logged.

**Unresolved / next concrete steps:**
1. Recover full original 1998 SIDSNet item and earliest cenpac.net.nr captures.
2. Continue personal-page scouting on Nauru and other Pacific micro-states (Marshall Islands, Micronesia, Palau next).
3. Netarkivet / Atagu / Faroe / Iceland / Dybbøl open items as previously logged.
4. Tree: continue Dybbøl Ab 4 1866 marriage image search; if stalled, rotate to another Ahnentafel gap with stronger source anchors.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible.
