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

---

## 2026-11-17 — Grok agent: Turkmenistan initial scouting

**Agent:** Grok (xAI)
**Task:** Parallel scouting on next country in priority heuristic (Turkmenistan, after Kyrgyzstan); create initial research file documenting May 1997 full Internet connectivity and .tm ccTLD delegation.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md (latest Kyrgyzstan entry), NSRC Connectivity Provider Database contemporary posts, IANA .tm record, secondary Wikipedia/press.
**Files touched:** research/turkmenistan.md (new); coop.log.md (this entry).

**Findings:**
- Created research/turkmenistan.md.
- Documented 23 May 1997 first full Internet: traceroute + SMTP banner to 193.232.199.102 (tm.synapse.ru) via RSSI (Crepin-Leblond / NSRC, grade B). Academy of Sciences / SIBIS planning from 1993; public dial-up email and Internet via SIBNET and Turkmenistan Online in 1997 (Karryev 1999, grade B/C). Institutional sites including sibnet.tm and Turkmenpress news from 1997.
- .tm delegated 30 May 1997 (IANA, grade A for DNS only); early management external.
- Null result on verified resident personal homepage or local individual web publishing in current sources. Status: scouting.
- Distinctions preserved between connectivity milestone, DNS, institutional publishing, and personal expression.

**Sources:** NSRC report id=890202390063:497434863 (Crepin-Leblond 23 May 1997); NSRC report id=940891215909:489047156 (Karryev Aug 1999); IANA/domain.glass .tm delegation 30 May 1997.
**Status:** Turkmenistan added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Recover any surviving 1997 captures of sibnet.tm, online.tm, tpress.sibnet.tm or the IP site.
2. Confirm nature of 1993–96 Academy activity.
3. Search Turkmen/Russian-language press and Academy archives for early personal or community pages after May 1997.
4. Check Wayback and national holdings for early .tm content.
5. Continue scouting (next in heuristic: Uzbekistan) or return to first-wave open items. Prefer local-language sources.
6. Tree: continue public-source verification of open leads (e.g., DAISY name registers for Bogensholm/Claus Gaardsted; Dybbøl 1866 marriage image). No private data accessed. No canonical changes.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.

---

## 2026-11-17 — Grok agent: Uzbekistan Track A claim

[2026-11-17 09:23 UTC] CLAIM — Track A — UZBEKISTAN — Initial scouting: first connectivity, .uz delegation, early ISPs, personal expression leads — AGENT-Grok-Automation — ACTIVE

---

## 2026-11-17 — Grok agent: Uzbekistan initial scouting

**Agent:** Grok (xAI)
**Task:** Track A initial scouting for Uzbekistan (priority heuristic 24); document early UUCP/email, PERDCA/Silknet, 1995 Internet appearance, .uz delegation, and gaps in personal expression.
**Branch policy:** main only; no branches or PRs.
**Files inspected:** README.md, WORK_METHOD.md, COUNTRIES.md, coop.log.md (latest Turkmenistan entry), IANA .uz redelegation report, NSRC PERDCA/Silknet May 1995 update, local-language secondary chronologies (arxiv.uz, uza.uz), cctld.uz/uztelecom anniversary notices.
**Files touched:** research/uzbekistan.md (new); coop.log.md (this entry).

**Findings:**
- Created research/uzbekistan.md.
- Documented early-1990s UUCP store-and-forward email (Moscow dial-up); local providers ~1992–95 including BCC, CCC, PERDCA/Silknet (grade C).
- PERDCA Silknet email network ~1993, >1400 subscribers by May 1995 across Central Asia (NSRC report, grade B).
- Full Internet consistently dated to 1995 (providers PERDCA, SOVAM, RELCOM, UZPAK, Naytov etc.); 1996 Cabinet/UNDP UzNet project and UzPAK (grade C).
- .uz delegated 29 April 1995 to Alex Vostrikov of Tashkent (IANA 2003 report, grade A for DNS); free registration until 2001; redelegated 2002–03 to UZINFOCOM.
- Null result on verified resident personal homepage or local individual web publishing in current sources. Status: scouting.
- Distinctions preserved between UUCP/email, full TCP/IP, DNS, institutional sites, and personal expression.

**Sources:** IANA .uz redelegation report (10 Apr 2003); NSRC UZ Networking Update (May/June 1995); arxiv.uz “O‘zbekistonda Internet rivojlanishi tarixi”; connected-archive key issues page; uza.uz 2026 chronology; local anniversary notices.
**Status:** Uzbekistan added as scouting. Prior files unchanged.

**Unresolved / next concrete steps:**
1. Recover full original NSRC PERDCA text and any 1993–95 notices.
2. Confirm exact first permanent TCP/IP date and gateway beyond the 1995 year.
3. Search Uzbek/Russian-language press and university archives for early personal or community pages after 1995.
4. Recover Wayback captures of early .uz, Silknet, UzNet, Naytov or PERDCA sites.
5. Continue scouting (next in heuristic: Mongolia) or return to first-wave open items (Atagu, Faroe, Iceland Netarkivet). Prefer local-language sources.
6. Tree: continue public-source verification of open leads (e.g., Dybbøl 1866 marriage image). No private data accessed. No canonical changes.

**Handoff:** Small commits on main only. Prefer local-language sources. Keep every country’s status visible. Repositories remain strictly separated.


## 2026-11-17 — Public article publishing standard (all agents)

**Project-wide instruction:** From this commit onward, every agent creating or materially updating a country/territory research file must also create or refresh its structured `article-data` JSON block as specified in `AGENTS.md`, `WORK_METHOD.md`, and `CONTRIBUTING.md`. This is mandatory for all tracks and all countries, not only the first research wave.

**Website:** The public atlas now starts with a country-article section and has a sticky navigation for Articles, Coverage, Research records, and About. Each article is rendered from the `article-data` block in its canonical research Markdown file. If the block is absent, the site temporarily derives an article view from the research note. Images use verified article metadata where supplied; otherwise the site requests an attributed Wikimedia Commons image.

**Initial article data added:** Denmark, Faroe Islands, Greenland, Iceland, Iran, and Uruguay. Their articles are a first editorial pass and should be improved as new evidence arrives. Existing and future country assignments must follow the same data format. Never invent article claims, image credits, or licenses.

**Handoff:** Read the new mandatory article instructions before starting work. Keep research notes and article data in the same commit on `main`.


## 2026-11-17 — Specific country stories only

The public article standard is tightened. Articles are not country summaries or wiki-style timelines. Publish only a specific, source-backed story about an identifiable person, publication, service, community or surviving website in that country. If no such story is established, omit the article-data block; the country remains in Coverage and Research records. Remove automatic article generation from raw research notes. Images must be relevant primary/archival visuals—identified portraits, original site screenshots, provider or publication logos/mastheads, or archival documents—with verified rights and full attribution. No generic landscape fillers. Denmark, Faroe Islands, Greenland and Iceland article blocks have been rewritten around a specific documented episode; Iran and Uruguay article blocks have been removed pending stronger story evidence.


---

## 2026-11-17 — Grok agent: Mongolia initial scouting and evidence extraction

**Agent:** Grok (xAI)  
**Task:** Track A + Track B — open Mongolia from the latest Central Asia handoff; document local pre-Internet/BBS precursors, Internet email, transition to full-time connectivity, early web publishing, and personal-page gaps.  
**Branch policy:** main only; no branches or PRs.  
**Files read:** README.md, WORK_METHOD.md, COUNTRIES.md, full coop.log.md, AGENTS.md, CONTRIBUTING.md; checked that no Mongolia research file already existed.  
**Files changed:** research/mongolia.md (new, including a specific MagicNet article-data story); coop.log.md (this entry).

**Findings:**
- NSRC preserves contemporaneous Datacom/IGC messages from October–December 1994. Datacom prepared a Waffle/UUCP system in October; the experimental exchange succeeded 30 November; the 15 December report describes a 16-line local BBS and a scheduled international gateway.
- Datacom's 27 March 1995 update says Internet email service had operated since December 1994 and IGC called daily. The 23 August 1995 update reports 450+ subscribers, a 16-line Magic BBS, and a Waffle gateway for Internet email/news. The BBS's 16 lines were local dial-up capacity, not 16 international Internet lines.
- The exact start date remains qualified: Datacom says service began December 1994; Oliver Corff's 1995 FAQ says the first email link came into existence in January/February 1995. Experimental connection, operator-reported service start and external confirmation may be different milestones.
- The 128 Kbps satellite/IP link to Datacom's Ulaanbaatar router was responding by 5 January 1996. A 9 January technical update says BBS users could use Telnet/FTP; the public commercial service was still being prepared at that point. Datacom's Internet-centre opening ceremony was held 17 January.
- The .mn domain record was created 2 March 1995 (DNS only). The .mn registry retrospectively dates the first MongoliaOnline / www.mol.mn version to January 1996; this was a commercial portal and no original capture has yet been inspected.
- A 1996 FAQ says soc.culture.mongolian began in spring 1994, but contributor residence and a Mongolia-based Usenet feed remain unverified. The 1993 Mongolia-focused Gopher at Free University Berlin and the 1995 Mongolia Society homepage in Bloomington, Indiana are transnational/overseas activity, not local Mongolian hosting.
- A later UNDP project retrospective identifies Ger as a collective online magazine from 1998–2000 and describes a UNDP Mongolia portal launched in 1997. These are publication/institutional leads, not personal homepages.
- No resident personal homepage has been verified. Status remains scouting; no claim of absence or exhaustion.

**Sources and evidence:** NSRC contemporaneous Datacom/IGC reports (14 Oct, 28 Oct, 30 Nov and 8/15 Dec 1994; 27 Mar and 23 Aug 1995; 5/9/18 Jan 1996), mostly grade A for what the operator/network messages report; Oliver Corff's 1995/96 FAQs (grade B for contemporary community/service descriptions); .mn registry timeline (grade C for retrospective portal date); David South Consulting UNDP case study (grade C for Ger/portal retrospective). All source URLs and qualifications are recorded in research/mongolia.md.

**Editorial:** Added a focused article-data block about the local MagicNet BBS and scheduled email gateway. No image was used because no relevant reusable, accurately credited asset was verified. No generic country-summary article was added.

**Unresolved / next concrete steps:**
1. Inspect the NSRC/IDRC PAN Mongolia reports from early and mid-1995 and the original August 1995 MagicNet network-structure report.
2. Recover original captures of mol.mn, magic.mn, un-mongolia.mn and other early .mn pages via the Internet Archive, Datacom, the .mn registry or local university collections.
3. Search Mongolian Cyrillic and Latin transliterations for resident student/staff pages and personal homepages; identify authors and residence independently.
4. Locate the original soc.culture.mongolian creation message and earliest posts; identify contributors' locations before attributing them to Mongolia.
5. Check Ger's 1998–2000 issues and the 1997 UNDP portal through original WARC/Wayback or UNDP records.
6. Trace the Academy of Sciences' earlier UUCP route through Dubna and identify local users.

**Handoff:** Mongolia remains open for personal-page discovery and original capture recovery. Continue parallel country scouting; Uzbekistan remains the separate active claim in the prior entry.


---

## 2026-11-17 — Grok agent: Mongolia early personal-web leads

**Agent:** Grok (xAI)  
**Task:** Continue the Mongolia handoff: inspect the 1995 PAN/MagicNet evidence, seek individual web publishers and early personal pages, and distinguish local publishing from diaspora/community material.  
**Files read:** README.md, WORK_METHOD.md, COUNTRIES.md, entire current coop.log.md, research/mongolia.md; checked the existing Mongolia record before editing.  
**Files changed:** research/mongolia.md (addendum MN-06–MN-10); coop.log.md (this entry). No article-data block or canonical “earliest” claim was changed.

**New findings:**
- A Mongolian Ministry of Digital Development volume (2023) republishes a first-person memoir by Jagdagdorj Erkhembayar, written for the Internet's 15th anniversary. He recalls meeting S. Badral at the 17 January 1996 Internet-opening event in Ulaanbaatar and describes Badral's “Yahoo”-associated website about Mongolia as almost the only website/online information about Mongolia at the time. This is a strong named-creator lead, but the URL, Yahoo's role, original capture and Badral's residence at publication remain unknown. Do not assume GeoCities or a personal homepage.
- The same memoir recalls 1996–1999 online newspaper pages under www.mol.mn/argamag/... and an HTML Mongolian Yellow Pages directory in 1999. These are publication/commercial leads, not personal sites.
- Asuult.net's own page dates its initial introduction to 30 June 2001, says development began 20 November 2000, and lists free hosted pages in its 5 July 2002 update. It names several personal/topical pages, including pages attributed to Achbold, Hantulga, Otgochuluu, Tsengel, Tuvshinbat, Viola, Zealot Erheme, the Young Economist, Sanlig Badral and Ganbold. The portal is collective; the listed pages need individual date and residence checks.
- Asuult's 2002 directory identifies a Sanlig Badral page at asuult.net/badaa. The surviving route redirects to badaa.mngl.net, whose “Mongolian Language Tools” page is signed S. Badral and has a 2000–2005 copyright footer. This is a candidate individual-created topical website documented by 2002, not a proven 2000 launch or a confirmed continuation of the 1996 Yahoo page.
- A February 1999 IDRC PAN evaluation reports that Datacom provided free web space to more than 42 organizations by December 1997, published the 10th issue of A.MN@, linked to 100+ organizations through MongoliaOnline, and offered up to 75 MB of free homepage space on its early-1998 Class Global plan. This is a useful hosting/content-directory lead, not proof of personal pages. The accessible copy carries a confidential/no-reprint notice; no long quotation or redistribution is authorized.
- The same retrospective says Waffle/UUCP transfer began September 1994, conflicting with contemporaneous NSRC messages that place system preparation in October and the first experimental exchange on 30 November. Both chronologies are retained pending reconciliation.

**Evidence / confidence:** the 1996 Badral recollection is grade B (named first-person retrospective); Asuult's own dated history and directory are grade A for its stated dates, hosting policy and link list; the current Badral page is a surviving individual-attributed site with a documented 2002 directory entry but no exact launch date; the 1999 PAN report is a retrospective infrastructure source with rights restrictions.

**Unresolved / next actions:**
1. Recover the original Yahoo-associated Badral URL and establish whether it was hosted, listed or merely indexed by Yahoo.
2. Inspect archived captures of the Asuult paths and identify the first publication date and residence for each named page creator.
3. Locate A.MN@ issues, Datacom's 42 hosted organizations and MongoliaOnline's original directory to identify early individual pages.
4. Recover the original mol.mn/argamag newspaper pages and 1999 Yellow Pages.
5. Reconcile the PAN retrospective's September 1994 Waffle date with the contemporaneous NSRC October–November 1994 messages.

**Handoff:** Mongolia has a stronger 1996 named-creator lead and a 2000–2002 personal/topical page cluster, but no earliest resident personal homepage is verified. Continue parallel discovery in other countries; do not treat this as a reason to pause other country work.
