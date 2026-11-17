# Papua New Guinea — early internet activity

**Status:** scouting (ccTLD 1991; Unitech UUCP email operational by Jan 1997; public commercial TCP/IP staged 1997; no personal homepage verified yet)

## Internet context

- **.pg ccTLD:** Delegated 26 September 1991 to PNG DNS Administration, Vice Chancellor's Office, Papua New Guinea University of Technology (Unitech), Lae (grade A for DNS registration only; IANA records). Does not by itself prove local hosting or resident operators. Registry remains with Unitech.
- **Early academic access / UUCP (by 22 January 1997):** Primary NSRC report from root@ee.unitech.ac.pg states there are only a very limited number of sites connected to the Internet. DNS for PNG started with help from Robert Elz (University of Melbourne); database kept and updated in Melbourne with plans to move it. No ISP providers yet in PNG. Telikom has illegalized message switching and Internet falls under that category. Unitech operates an Intel-based machine (40 MB disk) running modified Microport Unix v.II for UUCP-only message switching with Internet-style (user@domain) addressing; local users connect via UUCP for delivery/pickup. Connection to Melbourne is the bottleneck. A SUN SPARC 5 is being configured as replacement. This is grade A contemporary operator evidence of institutional UUCP email; it does not establish public TCP/IP or a commercial ISP.
- **Public / commercial TCP/IP (1997):** Staged rollout. A 1997 Waigani Seminar paper (Nathan Kwasam) reports PNG Post and Telikom launched the Internet on 12 March 1997; DataNets launched as ISP at a subsequent Port Moresby seminar; first University of Papua New Guinea website 19 August 1997. Contemporary Pacific Journalism Review (1997) places the country online in May. Later regulatory account (Lois Stanley 2008) dates commencement of Internet services to April 1997 with Telikom’s Tiare gateway (operated by Pacific Mobile Communications subsidiary; wholesale bandwidth from Telikom, retailed via ISPs). NSRC provider database entry for Datec created 10 May 1997, self-described as “the first ISP in PNG” (grade B/C for dates; distinctions between carrier announcement, gateway, retail ISP, and institutional site must be preserved).
- **Academic / publishing:** Journalism UPNG webserver online August 1997 (temporarily intranet while awaiting Telikom fixes); The National newspaper website launched 5 August 1997. ERNet (education and research network) planned later with Australian academic partners.

## Personal web ecology / leads

- No locally hosted personal homepage or resident-authored personal site verified in current sources.
- Early activity concentrated in universities (UPNG, Unitech) and commercial ISPs (Datec, DataNets / Online South Pacific, Daltron, Global Technologies, High Tech Industries).
- Diaspora or external leads possible but not pursued this pass.

## Earliest known examples by category

| Category | Example | Date | Medium | Operator | Network status | Evidence grade | Notes |
|----------|---------|------|--------|----------|----------------|----------------|-------|
| Infrastructure | .pg delegation | 26 Sep 1991 | dns | academic (Unitech) | unknown | A | DNS only |
| Communication / email | Unitech UUCP email service | by 22 Jan 1997 | uucp | academic | inter-network | A | Primary NSRC; no public ISP yet |
| Connectivity | Academic dial-up to Australia | early 1990s | internet-access | academic | internet-connected | C | Retrospective; institutions |
| Infrastructure / service | Telikom / Tiare gateway | Apr 1997 | gateway | commercial / government | internet | B/C | Staged; wholesale |
| Service | DataNets / Datec ISPs | Mar–May 1997 | internet-access | commercial | internet | B/C | Competing “first ISP” claims |
| Publishing | UPNG website; Journalism UPNG server; The National online | Aug 1997 | website | academic / commercial | internet | B | Institutional / newspaper |

## Structured candidate records

### PG-01 — Unitech UUCP email service (January 1997)

```yaml
id: PG-01
status: candidate
person_or_project: Unitech / ee.unitech.ac.pg
title: Unitech UUCP-based institutional email service
url_original:
url_archived:
country_or_territory: Papua New Guinea
connection_basis: other
medium: uucp
activity_type: communication
operator_type: academic
network_status: inter-network
date_claimed: 1997-01-22
date_type: inferred
date_precision: exact
evidence:
  - source_url: https://www.nsrc.org/db/lookup/report.php?id=890202505236:497428747&fromISO=PG
    source_type: contemporary NSRC operator report from Unitech
    observed_date: 1997-01-22
    supports: Unitech reports limited Internet-connected sites, DNS assistance from Melbourne, no ISP providers yet, Telikom illegalized message switching; operates UUCP-only Intel/Microport Unix mailserver for local users with Internet-style addressing; Melbourne connection is bottleneck
    grade: A
author_attribution: Unitech (root@ee.unitech.ac.pg)
language: English
notes: Primary evidence of institutional UUCP email before public commercial TCP/IP. Does not prove public dial-up or full TCP/IP Internet for general users.
uncertainties: Exact start date of the UUCP service and continuous operation not established; no user list or original logs recovered. Relationship to earlier academic dial-up to Australia remains retrospective.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

## Gaps and next leads

1. Locate original Kwasam Waigani paper, Stanley 2008 regulatory paper, and contemporary Telikom/Tiare announcements for precise gateway and ISP start dates.
2. Confirm early Unitech or UPNG email/UUCP or dial-up records from Australian university partners (AARNet etc.) and recover any pre-1997 UUCP logs.
3. Search National Library of Papua New Guinea, UPNG/Unitech archives, or local press (The National, Post-Courier) for early personal or community pages.
4. Recover Wayback captures of early .pg sites (e.g., unitech.ac.pg, datec.com.pg, journ.upng.ac.pg).
5. Investigate any pre-1997 UUCP or email gateways beyond academic dial-up; clarify Telikom’s “illegalized message switching” policy and its practical effect.

## Bibliography / evidence log

- IANA / ICANNWiki .pg records (delegation 26 September 1991 to Unitech).
- NSRC, “PG Networking Update (1/97)” (22 January 1997), from root@ee.unitech.ac.pg: https://www.nsrc.org/db/lookup/report.php?id=890202505236:497428747&fromISO=PG
- NSRC Datec (PNG) Pty Ltd provider record (created 10 May 1997): https://nsrc.org/db/lookup/provider.php?id=890201929152:497393788&fromISO=PG
- Nathan Kwasam Waigani Seminar paper 1997 (cited in secondary summaries; primary preferred).
- Lois Stanley, University of Papua New Guinea regulatory paper 2008.
- Pacific Journalism Review 1997 (online newspapers and Journalism UPNG).
- Logan & Suwamaru, “Land of the Disconnected” (Routledge Companion to Global Internet Histories, 2017; retrospective).
- Accessed 18 November 2026.

**Researcher:** Grok (xAI)  
**Last checked:** 2026-11-18
