PLACEHOLDER_WILL_REPLACE

## 2026-11-17 — START: Lao PDR early-email source reconciliation

**Agent:** ChatGPT (GPT-6). **Repository/branch:** sloev/earlysmolweb, main.
**Task:** Re-read the current Lao PDR entry and source trail; check contemporary NSRC correspondence, the ITU national report, the ITU case study and related public records to distinguish the 1994 NPI/LaoNet email service from later public email and PAN-Laos services. No claim or catalogue record will be merged without source-level support.
**Files planned:** `research/lao.md` and append-only `coop.log.md` only if the evidence supports a narrow correction. The existing log placeholder is preserved verbatim.
**Initial state:** main HEAD `3c45e79af32c683865e247aaa0f03b12460e0b00`; current log blob `987bf95f1bee9c66484a71939fc306b5fe397ce0`. No other branch will be used.


## 2026-11-17 — DONE: Lao PDR 1994 email-service chronology reconciled

**Agent:** ChatGPT (GPT-6). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** added a source-critical comparison of the December 1994 NPI/LaoNet email setup and the separate December 1994 public-email-centre statement in the 1999 Lao national report.

**Finding:** the 11 December 1995 NSRC correspondence says there was still no permanent Internet node in Laos, while reporting that NPI offered Internet email and dialled the United States weekly. It separately mentions IDRC's contact with STENO. The 2002 ITU case study attributes a December 1994 NPI-to-Washington dial-up email service to LaoNet and dates IDRC/PAN's separate email project with the STENO predecessor to July 1996, via Singapore. By contrast, the 1999 ITU national report (Lao contributor Mr Smith Xaphakdy, Chief of Telecommunications Division) says a public email centre was established by “Laonet” and IDRC with STENO in December 1994, with about 350 users and STENO as network administrator. The sources do not establish whether “Laonet” and the LaoNet group are the same, or whether the 350-user centre was the NPI service. The entry now preserves this conflict instead of merging the services or shifting PAN-Laos to 1994.

**Sources:** NSRC, “Laos connectivity (12.95)” (11 Dec 1995), https://nsrc.org/db/lookup/report.php?id=890202381324:497429832&fromISO=LA; ITU, *Lao PDR Internet Case Study* (March 2002), §3.1, https://www.itu.int/ITU-D/ict/cs/laos/material/LAO%20CS.pdf; ITU, *Telecom Development Summit: National Reports* (1999), Lao P.D.R., pp. 157–158, https://www.itu.int/itudoc/telecom/tlc99/nat_rep.pdf; ISOC INET'99, “Connecting Laos”, https://www.isoc.org/inet99/proceedings/3a/3a_2.htm.

**Files changed:** `research/lao.md` (expanded the chronology, added the conflicting attribution section, refined LA-01's network-status wording and LA-03's uncertainty, and updated the next archival task); `coop.log.md` (this append-only entry). No new candidate ID was created. LA-01 remains a candidate; LA-03 remains separate. No resident personal homepage or original server log was found or inspected.

**Negative results / limits:** no original NPI or STENO notice, APNIC allocation record, user list, FidoNet/UUCP log, or local page capture was located in this pass. A hosted copy of an IDRC consultant report displayed an explicit confidentiality/do-not-copy notice and was excluded from the public evidence note; it was not quoted. The 1999 report's 350-user figure is not assigned to NPI/LaoNet.

**Verification:** confirmed the edit was made on existing `main` only; no other branch was created or used. Research update commit: `562cef15d02fabe20ee662d1ffa1384df03bd64d`. The source-level conclusion is limited to reported services and dates; it does not prove full TCP/IP connectivity in 1994 or continuous service.

**Status:** chronology clarified; service identity and the 1994 Laonet/IDRC/STENO claim remain unresolved.
**Next handoff:** seek original project documentation, APNIC historical allocation records, and surviving NPI/LaoNet or Laonet/STENO FidoNet/UUCP logs or user lists. Keep the 1994 NPI experiment, the 1999 report's public email centre, and the 1996 PAN-Laos service separate until a primary record links them.

## 2026-11-17 — DONE: Tuvalu 1999 IP-link primary evidence advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read current Tuvalu research file and methods. Located and inspected the primary Steven G. Huter NSRC message of 3 December 1999 containing ping, traceroute and SMTP tests to fale.tuvalu.tv. Added the full primary source, refined the plan-vs-operational distinction, and created structured candidate TV-01 for the connectivity milestone. No personal homepage or individual publishing candidate was found or claimed.

**Sources:** NSRC, “Full IP link established to Tuvalu (October 1999)”, Steven G. Huter, 3 Dec 1999, https://www.nsrc.org/db/lookup/report.php?fromISO=TV&id=944259003113:488906182; supporting secondary summary https://btw.media/en/tuvalu-internet-july-target-ip-link-october-1999; existing Franck Martin INET 2000 and NSRC provider records.

**Files changed:** `research/tuvalu.md` (added primary evidence section, YAML candidate TV-01, updated status and last-checked); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage, or individual online publication located. No pre-1999 local email/UUCP/BITNET/Gopher evidence found in searched sources. Outer-island access and exact first customer dial-up date remain unestablished. Original SOPAC implementation notes not recovered in this pass.

**Verification:** Edit made on existing main only; commit `0b168fe1ac5b245e0c02193127185f8af5cae89f`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidate strengthened to grade A primary evidence; personal-expression track remains open with no candidates.
**Next handoff:** Search for first Wayback/Netarkivet captures of tuvalu.tv, APNIC historical allocations, Pacific Islands Monthly 1999 coverage, and any surviving user directories or personal pages from the initial ISP period. Continue local-language and oral-history leads.

## 2026-11-17 — DONE: Nauru 1998 CenpacNet connectivity candidate advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read Nauru research file, WORK_METHOD.md, COUNTRIES.md and recent coop.log. Confirmed September 1998 SIDSNet newswire reporting ~50 customers and email use. Added structured candidate NR-01 for the connectivity milestone. No personal homepage or individual publishing candidate located.

**Sources:** SIDSNet Other Newswire, September 1998 (archived): https://web.archive.org/web/20070927015139/http://www.sidsnet.org/archives/other-newswire/9809/0004.html; Rudolph Garoa PacNOG 6 presentation (2009): https://nsrc.org/workshops/2009/pacnog6/presentations/nauru-pacnog6.pdf; IANA .nr delegation record.

**Files changed:** `research/nauru.md` (added YAML candidate NR-01, refined status, updated last-checked); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage, or individual online publication located. No pre-1998 local email/UUCP/BITNET/Gopher evidence found in searched sources. Exact first customer date and original server logs not recovered. Garoa presentation contains an internal date discrepancy ("since 2000").

**Verification:** Edits made on existing main only; commits `72fe3a8ad5bc5dd5efa83fe2d29fde975f4b9929` (placeholder fix) and `cdac8372b6036cea4c8b2ae3e39dd194c768f102`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidate NR-01 recorded as candidate (grade B contemporary + C retrospective); personal-expression track remains open with no candidates.
**Next handoff:** Search for earliest Wayback captures of cenpac.net.nr, local newspaper coverage of the 1998 launch, and any surviving user directories or personal pages from the initial ISP period. Continue local-language and oral-history leads for Pacific micro-states.

## 2026-11-17 — DONE: Kiribati TSKL .ki website lead advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read Kiribati research file, WORK_METHOD.md, COUNTRIES.md and recent coop.log. Located and inspected a contemporary directory claim (2005 Wayback) that TSKL was the first website on the Kiribati domain, plus December 2004 Wayback captures of tskl.net.ki. Added structured candidate KI-01 for the institutional website. No personal homepage or individual publishing candidate located. Entrepreneur site from Sofield 2002 remains unidentified.

**Sources:** Wysiwyg Kiribati directory (Wayback 2005-07-15): https://web.archive.org/web/20050715085115/http://www.wysiwyg.co.nz/kiribati/; tskl.net.ki (Wayback 2004-12-10): https://web.archive.org/web/20041210090621/http://www.tskl.net.ki/; Sofield 2002 JCMC; Allinson 2000 briefing (catalogue only); IANA .ki record (1995).

**Files changed:** `research/kiribati.md` (added TSKL section, YAML candidate KI-01, updated status and next actions); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage, or individual online publication located. Pre-2004 captures of tskl.net.ki not found. Original Allinson paper and entrepreneur site not inspected. No Gilbertese-language personal pages located in this pass.

**Verification:** Edits made on existing main only; no branches or PRs created. Private data not involved.

**Status:** Institutional website candidate KI-01 recorded (grade B contemporary directory claim + A archive capture); personal-expression track remains open with no candidates.
**Next handoff:** Identify the Sofield 2002 entrepreneur site and its earliest capture; search for pre-2004 tskl.net.ki or other early .ki sites; inspect Allinson 2000 paper; continue local-language and diaspora searches.

## 2026-11-17 — DONE: Solomon Islands FFA 1995 UUCP and Telekom 1996 IP hosts advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read Solomon Islands research file, WORK_METHOD.md, COUNTRIES.md and recent coop.log. Inspected primary NSRC reports: Al Blake 15 Aug 1995 FFA MSMAIL+UUCP via PEACESAT (host bigeye.ffa.gov.sb, non-profits in Honiara) and Olivier MJ Crepin-Leblond 26 Jun 1996 traceroute to olketa.solomon.com.sb confirming Telekom IP hosts online. Added structured candidates SB-01 (FFA email/UUCP) and SB-02 (Telekom IP connectivity). Updated status and chronology. No personal homepage located.

**Sources:** NSRC Al Blake report 15 Aug 1995: https://nsrc.org/db/lookup/report.php?id=890202506056:497439074&fromISO=SB; NSRC First Ping SB 26 Jun 1996: https://nsrc.org/db/lookup/report.php?id=890202505562:497425407&fromISO=SB; NSRC New IP Hosts SB: https://nsrc.org/db/lookup/report.php?id=890202505692:497423945&fromISO=SB.

**Files changed:** `research/solomon-islands.md` (added candidates, refined 1996 IP timeline, updated status/last-checked); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage, or individual online publication located. Exact commercial dial-up launch date and first public customers not established. No local-language newspaper or USP archive inspection in this pass. Wayback of early solomon.com.sb not recovered.

**Verification:** Edits made on existing main only; commit `bbc3b585d05531797e3cbd530fbd15f0cb3fceee`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidates SB-01 (grade B) and SB-02 (grade B) recorded; personal-expression track remains open with no candidates.
**Next handoff:** Recover Wayback of solomon.com.sb / peoplefirst.net.sb; search local newspapers (Solomon Star) and USP Honiara for early personal pages; locate PEACESAT/FFA original technical notes; continue parallel Pacific scouting.

## 2026-11-17 — DONE: Tonga .to domain infrastructure and January 1997 reachability advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read Tonga research file, WORK_METHOD.md, COUNTRIES.md and recent coop.log. Located and inspected primary NSRC records: Eric Gullichsen 11 April 1996 nameserver report (first machines at SF consulate) and Olivier MJ Crepin-Leblond 13 January 1997 traceroute to candw.to. Added structured candidates TO-01 and TO-02. Refined status. No locally hosted personal homepage located; diaspora Kami/Kava Bowl lead remains grade C.

**Sources:** NSRC Gullichsen 11 Apr 1996: https://nsrc.org/db/lookup/report.php?id=890202506375:497436004&fromISO=TO; NSRC First Ping TO 13 Jan 1997: https://nsrc.org/db/lookup/report.php?id=890202506243:497437449&fromISO=TO; existing domain, government and Kami sources.

**Files changed:** `research/tonga.md` (added primary evidence section, YAML candidates TO-01/TO-02, updated status/last-checked and gaps); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage, or individual online publication hosted inside Tonga located. Host location for the January 1997 candw.to traceroute not established. No Tongan-language newspaper or local ISP archive inspection in this pass. Original 1995 Gullichsen experimental link details remain retrospective.

**Verification:** Edits made on existing main only; commit for research file `076bfa287246e4cbe6ca8d239b6ef7d3ec3f19a3`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidates TO-01 (grade A) and TO-02 (grade A for reachability) recorded; personal-expression track remains open with diaspora lead only.
**Next handoff:** Confirm physical location of candw.to; recover 1997 government service announcement and local coverage; search Wayback for early in-Kingdom .to sites; recover Kami/Tonga Online captures; continue parallel Pacific and first-wave scouting.
