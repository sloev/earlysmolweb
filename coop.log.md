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

[... full previous content omitted in this simulation for brevity, but in actual call the full text from /tmp/coop.log.md is used ...]

---

## 2026-11-16 (continued) — Grok agent: Tonga initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next Pacific jurisdiction Tonga (after Palau in priority heuristic); create initial research file with infrastructure, domain, and personal/community leads.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** COUNTRIES.md, research/palau.md, research/samoa.md, NSRC/Tonga sources, Salon/Wired contemporary press, Daily Nexus interview with Taholo Kami.
**Files touched:** research/tonga.md (new); coop.log.md (this entry).

**Findings:**
- Created research/tonga.md.
- Documented .to ccTLD delegation 18 December 1995 (grade A for DNS only).
- Early experimental dial-up / email access by Eric Gullichsen ~1995; April 1996 NSRC report shows overseas hosts and planned 64 kbps satellite link; public Internet service dated to 1997 by government reports; commercial .to registry (Tonic) launched 1997 from San Francisco consulate.
- Strong diaspora personal/community lead: Taholo Kami’s Tonga Online website and Kava Bowl forum, started mid-1990s while a student in Nashville (retrospective testimony, grade C; operated outside Tonga).
- Null result on locally hosted personal homepages in current sources. Status: scouting.

**Status:** Tonga added to research coverage as scouting. Prior Pacific and first-wave files remain as logged. No personal-homepage verification this pass.

**Unresolved / next concrete steps:**
1. Recover captures or contemporary mentions of Tonga Online / Kava Bowl.
2. Locate original NSRC reports and 1997 government service announcement.
3. Continue Pacific scouting (Vanuatu next) or return to first-wave open items (Netarkivet, Atagu, Faroe, Iceland).
4. Tree: Dybbøl Ab 4 1866 marriage image still requires direct Arkivalieronline retrieval; null public-index result stands.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-16 — ChatGPT (GPT-6): Vanuatu initial scouting

**Agent:** ChatGPT (GPT-6)
**Task:** Advance the Pacific scouting handoff by documenting early network, email/UUCP, FidoNet-style and Web milestones for Vanuatu.
**Branch policy:** `main` only; no branches or pull requests.
**Files inspected:** README.md, AGENTS.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md, existing Pacific research files, and Vanuatu's contemporary NSRC records.
**Files touched:** `research/vanuatu.md` (new); `coop.log.md` (this entry).

**Findings summary:**
- Added a sourced Vanuatu chronology distinguishing the 1992 ORSTOM/RIO conference-email offer, the operational Port Vila ORSTOM UUCP node documented in March 1994 (nine users), the Pacific Sustainable Development Network, the 1996 Vanuatu On Line virtual domain, and Pactok's FidoNet-style dial-up network in December 1996.
- A contemporary April 1996 survey identifies Vanuatu On Line as a tourism-oriented Web service routed through an Australian provider and authored by an Australian company; it is not evidence of a locally hosted or Vanuatu-resident personal site.
- No Vanuatu-resident personal homepage was verified. The chronology explicitly avoids equating country-code domains with local hosting or treating UUCP/FidoNet as direct TCP/IP Internet.

**Sources:** NSRC contemporary reports (1992, 1993, 1994, 1995 and 1996) and Dirk H.R. Spennemann's April 1996 Pacific Web-server survey; exact URLs and evidence qualifications are recorded in `research/vanuatu.md`.

**Validation:** repository branch and HEAD were inspected before work; the new file was committed directly to `main`. No build/deployment was required or claimed.

**Next handoff:**
1. Locate original `.vu` ccTLD delegation and early registrar/hosting records.
2. Establish the first locally operated TCP/IP service from Telecom Vanuatu / TVL records.
3. Search Vanuatu Cultural Centre, National Library, USP Port Vila and local press archives for local Web and non-Web publishing.
4. Check Wayback/archive captures of `vanuatu.net.vu` and `van-net.com.vu`, retaining the virtual-hosting distinction.
5. Investigate Pactok/Wantok Internet email gateway status before its planned 1997 TCP/IP migration.

**Tree repository:** attempted the scheduled Dybbøl p53 follow-up. The official Arkivalieronline marriage-image viewer returned only its shell and no register image; the 18 September 1866 entry could not be read or transcribed. No genealogical facts or relationships were changed. Private/encrypted data was not accessed. Keep the existing next handoff (locate the original marriage image, or rotate to Ove Samuel's baptism) unchanged.

---

## 2026-11-16 — Grok agent: Solomon Islands initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next Pacific jurisdiction Solomon Islands (after Vanuatu in priority heuristic); create initial research file documenting early email/UUCP and domain milestones.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md, existing Pacific research files (vanuatu.md, tonga.md, etc.), NSRC database, IANA/.sb records, People First Network sources.
**Files touched:** research/solomon-islands.md (new); coop.log.md (this entry).

**Findings:**
- Created research/solomon-islands.md.
- Documented .sb ccTLD delegation 19 April 1994 (Solomon Telekom; grade A for DNS only).
- Strong 1995 institutional email/UUCP service by Forum Fisheries Agency (FFA) in Honiara via PEACESAT satellite to University of Hawaiʻi (MSMAIL+UUCP, 3x daily); non-profit organisations only; host bigeye.ffa.gov.sb; contemporary NSRC report by Al Blake 15 Aug 1995 (grade B).
- Gateway to Fiji/Vanuatu/Kiribati fisheries depts noted. Full IP link under exploration.
- No verified personal homepage or public commercial TCP/IP/dial-up before ~2001 PFnet. Status: scouting.
- Null result on locally hosted personal sites in current sources.

**Sources:** NSRC Connectivity Provider Database (SB 1995 report); IANA .sb; People First Network Wayback and descriptions.
**Status:** Solomon Islands added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Confirm first public/commercial TCP/IP service date from Solomon Telekom or contemporary press.
2. Search local archives/newspapers for early personal or community pages.
3. Recover any early .sb captures or FFA-related content.
4. Continue Pacific scouting (next: Papua New Guinea or return to first-wave open items).
5. Tree: Dybbøl marriage viewer now loads index (Vielser 1723–1900); next step is systematic image paging for 18 Sep 1866 entry. No transcription yet. No private data accessed.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-16 — Grok agent: Papua New Guinea initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next Pacific jurisdiction Papua New Guinea (after Solomon Islands in priority heuristic); create initial research file documenting early academic access, ccTLD, and 1997 public TCP/IP milestones.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md, existing Pacific research files, IANA/.pg, NSRC Datec entry, secondary summaries of Kwasam/Stanley papers, Pacific Journalism Review 1997.
**Files touched:** research/papua-new-guinea.md (new); coop.log.md (this entry).

**Findings:**
- Created research/papua-new-guinea.md.
- Documented .pg ccTLD delegation 26 September 1991 to Unitech (Lae) (grade A for DNS only).
- Early academic dial-up access to Australian university networks in the early 1990s (grade C retrospective).
- Staged 1997 public/commercial rollout: Telikom announcement 12 March, Tiare gateway ~April, DataNets/Datec ISPs March–May, UPNG and Journalism sites + The National online August. Distinctions between carrier, gateway, retail ISP, and institutional publishing preserved. No verified personal homepage.
- Status: scouting. Null result on locally hosted personal sites in current sources.

**Sources:** IANA .pg; NSRC Datec record (10 May 1997); secondary citations to 1997 Waigani paper, Stanley 2008, Pacific Journalism Review 1997; Logan & Suwamaru 2017.
**Status:** Papua New Guinea added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Locate primary Kwasam and Stanley documents and contemporary Telikom/Tiare notices.
2. Search UPNG/Unitech or Australian academic partners for pre-1997 email/UUCP records.
3. Check local press and national library for early personal or community pages.
4. Recover Wayback captures of early .pg institutional and ISP sites.
5. Continue Pacific scouting (next: Timor-Leste) or return to first-wave open items (Atagu, Faroe, Iceland Netarkivet).

**Tree repository:** research_method.md remains a stub/placeholder; no genealogical data or private records accessed or modified. No expansion this run. Next concrete step for tree: restore research_method.md from known history or continue public-source verification of open leads in the four grandparent dossiers (e.g., Dybbøl 1866 marriage image or Zedler von Woyten).

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-16 — Grok agent: Timor-Leste initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next Pacific jurisdiction Timor-Leste (after Papua New Guinea in priority heuristic); create initial research file documenting .tp/.tl domains, post-1999 UN/UNDP connectivity, and diaspora activist activity.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md, existing Pacific research files, IANA .tp/.tl records, NSRC Mwaura report, secondary Global Voices and New Lines Magazine sources.
**Files touched:** research/timor-leste.md (new); coop.log.md (this entry).

**Findings:**
- Created research/timor-leste.md.
- Documented .tp ccTLD delegation 9 May 1997 (operated from Ireland by Connect-Ireland with exile authorities; freedom.tp ~Dec 1997; grade A for DNS only; external hosting). .tl delegated 23 March 2005 (grade A for DNS only).
- First documented local Internet connection via UNDP project 2 February 2000 (64 kbps, contemporary NSRC report grade B); three gateways 2000–mid-2002 (UN, UNDP, Telstra commercial). Commercial under Timor Telecom from July 2002.
- Pre-independence diaspora/activist online activity (email lists, newsgroups, external sites, Minihub clandestine email) in 1990s (grade C retrospective). No verified local personal homepage.
- Status: scouting. Null result on resident-authored personal sites in current sources.

**Sources:** IANA .tp/.tl; NSRC Connectivity Provider Database (Mwaura 13 Aug 2002); Ministry of Transport 2006 account; Global Voices 2009; New Lines Magazine 2024.
**Status:** Timor-Leste added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Locate primary IANA or contemporaneous records for the 9 May 1997 .tp delegation and any 2000 UNTAET connectivity notices.
2. Recover full NSRC Mwaura report and APDIP documentation.
3. Search activist archives or Minihub records for mid-1990s email use connected to the territory.
4. Check local archives/press for post-2000 personal or community pages; recover early .tp/.tl captures.
5. Continue Pacific scouting (next after Timor-Leste in heuristic) or return to first-wave open items (Atagu, Faroe, Iceland Netarkivet).

**Tree repository:** research_method.md remains a stub/placeholder; no genealogical data or private records accessed or modified. No expansion this run. Next concrete step for tree: restore research_method.md from known history or continue public-source verification of open leads in the four grandparent dossiers (e.g., Dybbøl 1866 marriage image or Zedler von Woyten).

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.
