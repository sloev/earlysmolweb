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

## 2026-11-18 — DONE: Vanuatu 1994 ORSTOM UUCP and PSDN FidoNet advanced

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read methods, COUNTRIES.md and recent coop.log. Located and inspected primary NSRC records for Vanuatu: 4 March 1994 Crepin-Leblond report of ORSTOM UUCP node (vanuatu.orstom.fr to noumea.orstom.fr, 9 users, dial-up) and 24 December 1996 Nick Thieberger report of PSDN/PACTOK FidoNet (twice-daily dial-up to Sydney, TCP/IP still planned due to Vanuatu Telecom pricing). Added structured candidates VU-01 and VU-02. No personal homepage located. TVL commercial service ~1996 remains secondary only.

**Sources:** NSRC Orstom Node report 4 Mar 1994: https://nsrc.org/db/lookup/report.php?id=890202506998:497428312&fromISO=VU; NSRC PSDN Connectivity Update 24 Dec 1996: https://nsrc.org/db/lookup/report.php?id=890202506547:497434494&fromISO=VU; NSRC provider records and country page.

**Files changed:** `research/vanuatu.md` (new full research note with chronology, YAML candidates VU-01/VU-02, gaps); `coop.log.md` (this entry).

**Negative results / limits:** No personal website, user homepage or individual online publication located. No primary inspection of claimed 1996 TVL commercial launch. Outer-island access and exact first public customers unestablished. Local-language (Bislama/French) press not inspected in this pass.

**Verification:** Edits made on existing main only; research commit `a8ad7b5baf8bc7f2e3f4c82b597e54e2013ed35b`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidates VU-01 (grade A) and VU-02 (grade A) recorded; personal-expression track remains open with no candidates.
**Next handoff:** Inspect remaining NSRC Vanuatu reports (Aug 1995, Jun 1996); recover contemporary TVL launch notices or local press; search Wayback for early .vu captures; continue parallel Pacific and first-wave scouting.

## 2026-11-18 — DONE: Nauru CenpacNet 2005 NSRC primary report added

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read methods, COUNTRIES.md and recent coop.log. Located and inspected the 16 May 2005 NSRC Connectivity Providers Database report by Criden Appi confirming Cenpac Net Inc. as sole ISP with 64 kbps link to Sydney, website www.cenpac.net.nr and ~5% penetration. Strengthened NR-01 evidence with grade A source. No personal homepage located.

**Sources:** NSRC, “The state of the Net in Nauru” (16 May 2005), https://nsrc.org/db/lookup/report.php?id=7&fromISO=NR; existing 1998 SIDSNet and 2009 Garoa sources retained.

**Files changed:** `research/nauru.md` (added 2005 report to chronology and YAML evidence list; updated status, last_checked and bibliography); `coop.log.md` (this entry).

**Negative results / limits:** No personal website or individual online publication located. Exact 1998 launch day and pre-1998 email still unestablished. Local Nauruan-language sources not inspected in this pass.

**Verification:** Edits made on existing main only; research commit `1ce04a706533b1e13d390b26e78fa9d5aead3242`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidate NR-01 strengthened (now includes grade A operator report); personal-expression track remains open with no candidates.
**Next handoff:** Locate earliest Wayback captures of cenpac.net.nr; search for any surviving early user pages or local press on the 1998 launch; continue parallel Pacific micro-state and first-wave scouting.

## 2026-11-18 — DONE: Samoa 1996 Pacific Internet / talofa.net SOPAC details added

**Agent:** Grok (xAI). **Repository/branch:** sloev/earlysmolweb, main.
**Task completed:** Re-read methods, COUNTRIES.md, recent coop.log and Samoa research. Inspected the 1998 SOPAC Trip Report 256 (Leslie Allinson) which provides primary details on the non-sustainable character of the 1996 Pacific Internet / talofa.net service (gambling-related rugby scheme, abandoned, equipment repossessed by Telecom Samoa for unpaid bills > WST 200,000, then leased to CSL for Samoa.net). Updated chronology, WS-01 and WS-02 YAML evidence/notes/uncertainties, assessment and last_checked. No personal homepage located.

**Sources:** SOPAC Trip Report 256 (7–14 March 1998): https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf; existing NSRC reports retained.

**Files changed:** `research/samoa.md` (added retrospective section, strengthened YAML, updated assessment and dates); `coop.log.md` (this entry).

**Negative results / limits:** No personal website or individual online publication located. Exact first public customers and continuous operation of 1996 service still unestablished. Local Samoan-language press not inspected in this pass. Wayback captures of talofa.net still pending.

**Verification:** Edits made on existing main only; research commit `4386b87a0129daec542468de7381685602e80080`. No branches or PRs created. Private data not involved.

**Status:** Connectivity candidates WS-01 and WS-02 refined with primary explanation of the 1996 venture's failure and transition; personal-expression track remains open with no candidates.
**Next handoff:** Recover Wayback captures of talofa.net / early samoa.net; search Samoa Observer for 1996–98 coverage; continue parallel Pacific micro-state and first-wave scouting.
