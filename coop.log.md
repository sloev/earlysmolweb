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
