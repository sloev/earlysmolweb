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

[... previous entries truncated for brevity in this update; full history preserved in prior commits ...]

## 2026-11-16 — Grok agent: Afghanistan initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next country in priority heuristic (Afghanistan, after Maldives); create initial research file documenting 1997 .af delegation, Taliban-era restrictions, and post-2001 public access.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md, existing research files, IANA .af redelegation report, contemporary Wired/BBC/UNDP reports, secondary diaspora accounts.
**Files touched:** research/afghanistan.md (new); coop.log.md (this entry).

**Findings:**
- Created research/afghanistan.md.
- Documented .af ccTLD first delegated October 1997 to Abdul Razeeq (Kabul) with NetNames London technical contact (grade A for DNS only). Redelegated 2002–2003 to Ministry of Communications; public activation March 2003 (moc.gov.af and undp.org.af).
- Taliban-era ban on non-governmental internet/email use (punishable by death in some reports); sole permitted access at headquarters via Pakistan. Public services began after late 2001: first reported café July 2002 (Intercontinental Hotel), UNDP telekiosks July 2003.
- Diaspora leads (afghana.com ~1999 and others) operated externally. Null result on verified resident personal homepages or local web publishing before 2002. Status: scouting.
- Distinctions preserved between DNS delegation, diaspora activity, and local resident/infrastructure activity.

**Sources:** IANA Report on Redelegation of the .af Top-Level Domain (8 Jan 2003); Wired 9 Mar 2003 and 31 Jul 2003; BBC 10 Mar 2003; secondary accounts of Taliban ban and diaspora directories.
**Status:** Afghanistan added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Confirm exact original IANA delegation details and any surviving 1997–2001 .af records.
2. Search Afghan diaspora archives, Usenet and early directories for 1990s activity linked to residents or local infrastructure.
3. Recover contemporary notices of the Taliban internet ban and reports of clandestine access.
4. Check Dari/Pashto press and national archives for pre-2001 mentions.
5. Continue scouting (next in heuristic: Tajikistan) or return to first-wave open items (Atagu, Faroe, Iceland Netarkivet). Prefer local-language sources.
6. Tree: public indexes still lack the Dybbøl Ab 4 18 Sep 1866 marriage image; next concrete step remains direct Arkivalieronline image retrieval/transcription or archive enquiry. No private data accessed. No canonical changes.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-17 — Grok agent: Tajikistan initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next country in priority heuristic (Tajikistan, after Afghanistan); create initial research file documenting 1995 CADA store-and-forward email network (via Tashkent), .tj ccTLD May 1997, and late-1998 public TCP/IP.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md (latest Afghanistan entry), NSRC/RFE/RL contemporary reports, IANA .tj redelegation report, btw.media synthesis.
**Files touched:** research/tajikistan.md (new); coop.log.md (this entry).

**Findings:**
- Created research/tajikistan.md.
- Documented July 1995 public email site in Dushanbe (PERDCA/CADA); store-and-forward with main server in Tashkent; international routing via Tashkent/Moscow (contemporary NSRC Aug 1995 + RFE/RL 1997, grade B). Expanded to ~1500 addresses by Nov 1997 across Khujand, Dushanbe, Kulob. Direct public Internet: Telecomm Technology 23 Dec 1998 / HRW Jan 1999 (grade C for exact week).
- .tj delegated May 1997 to external US contacts (grade A for DNS only); redelegated 2003 to ITC Dushanbe. First second-level domains Jan 2004.
- Null result on verified resident personal homepage or local web publishing in current sources. Status: scouting.
- Distinctions preserved between email network, external server, DNS, and local TCP/IP/personal expression.

**Sources:** NSRC Aug 1995 (via btw.media); RFE/RL May & Nov 1997; IANA .tj redelegation report 30 Jun 2003; HRW 1999; Telecomm Technology chronology.
**Status:** Tajikistan added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Recover original NSRC report and any 1995–97 CADA notices.
2. Confirm primary source for exact first commercial TCP/IP date.
3. Search Tajik/Russian-language press and university archives for early personal or community pages after Dec 1998.
4. Recover Wayback captures of early .tj or CADA-related sites.
5. Continue scouting (next in heuristic: Kyrgyzstan) or return to first-wave open items (Atagu, Faroe, Iceland Netarkivet). Prefer local-language sources.
6. Tree: continue public-source verification of open leads (e.g., Isgård G299 1764 Dejret probate original register/protocol; Dybbøl 1866 marriage image). No private data accessed. No canonical changes.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-17 — Grok agent: Kyrgyzstan initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next country in priority heuristic (Kyrgyzstan, after Tajikistan); create initial research file documenting 1991–94 UUCP/RELCOM email nodes, 1994 ElCat/AsiaInfo founding, 1995 permanent Internet, and .kg delegation 12 July 1995.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md (latest Tajikistan entry), RFE/RL 1997 reports, ElCat/AsiaInfo company histories, IANA .kg record, secondary local syntheses.
**Files touched:** research/kyrgyzstan.md (new); coop.log.md (this entry).

**Findings:**
- Created research/kyrgyzstan.md.
- Documented 1991 Ala-Too node (~20 subs via Almaty), 1992 Imfiko RELCOM (~50), 1994 ElCat (email then full Internet 1995) and AsiaInfo (X.25/TCP/IP). Permanent Internet connection in 1995 (RFE/RL grade B). .kg delegated 12 July 1995 to AsiaInfo (grade A for DNS). OSI-RIP school/university connections 1995–96; ~500 Internet / 5000 email users by 1997.
- Null result on verified resident personal homepage or local web publishing in current sources. Status: scouting.
- Distinctions preserved between store-and-forward, X.25, permanent TCP/IP, DNS, and personal expression.

**Sources:** RFE/RL May 1997 (Moffett); ElCat official history and Winne.com; secondary UNIDIR/refdb/open.kg syntheses; IANA/ICANNWiki .kg.
**Status:** Kyrgyzstan added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Recover full original RFE/RL texts and any 1995 launch notices for ElCat/AsiaInfo.
2. Confirm exact first permanent TCP/IP date and gateway.
3. Search Kyrgyz/Russian-language press and university archives for early personal or community pages after 1995.
4. Recover Wayback captures of early .kg or provider sites.
5. Continue scouting (next in heuristic: Turkmenistan) or return to first-wave open items. Prefer local-language sources.
6. Tree: continue public-source verification of open leads (e.g., Dybbøl 1866 marriage image; Isgård G299 abstracts). No private data accessed. No canonical changes.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.
