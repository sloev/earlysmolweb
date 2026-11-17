# Solomon Islands — early internet activity

**Status:** active (institutional email/UUCP 1995 and commercial IP hosts by June 1996 documented; no personal homepage verified yet)

## Internet context

- **.sb ccTLD:** Delegated 19 April 1994 to Solomon Telekom Company Limited (grade A for DNS registration only; IANA records). Does not by itself prove local hosting or resident operators.
- **Early email/UUCP (1995):** Forum Fisheries Agency (FFA) in Honiara operated an email-only service using MSMAIL + UUCP, transferred three times daily with the University of Hawaiʻi via the PEACESAT satellite system. Available only to non-profit organisations in Honiara (schools, research institutions, FFA). Host: bigeye.ffa.gov.sb (later ffa.int). Contact: Al Blake. Contemporary NSRC report dated 15 August 1995 (grade B — primary operator statement in NSRC database).
  - Also provided gateway email to fisheries departments in Fiji, Vanuatu, and (soon) Kiribati.
  - Limited-time FTP services noted.
  - Both Solomon Telekom and FFA were exploring options for a full IP link (leased line to Australia or improved PEACESAT).
- **Commercial/public TCP/IP (by mid-1996):** NSRC records of 26 June 1996 document traceroute from the UK to olketa.solomon.com.sb (202.84.248.4) and list hosts network.solomon.com.sb, olketa.solomon.com.sb and welkam.solomon.com.sb as apparently located in the Solomon Islands. The same report notes that the website on www.solomon.com.sb was not yet fully set up as of 26 June 1996 but expected shortly. This places Solomon Telekom IP hosts online by June 1996 (grade B contemporary traceroute evidence). Earlier notes of commercial service only in the early 2000s are superseded for the institutional/commercial gateway window.
- People First Network (PFnet / Pipol Fastaem) began in 2001 as a UNDP/SIDAPP rural email network using HF radio + PACTOR, with an Internet café opened in Honiara in early 2001 (grade B/C for later activity).

## Personal web ecology / leads

- No locally hosted personal homepage or resident-authored website verified in current sources.
- Diaspora or external leads possible but not pursued this pass.
- PFnet provided operator-assisted email to rural communities starting late 2001 (first rural station Sasamungga, Choiseul, October 2001).

## Earliest known examples by category

| Category | Example | Date | Medium | Operator | Network status | Evidence grade | Notes |
|----------|---------|------|--------|----------|----------------|----------------|-------|
| Communication | FFA email/UUCP via PEACESAT | by Aug 1995 | uucp / email | institutional (FFA) | internet-connected (email gateway) | B | Non-profit only; Honiara-based |
| Infrastructure | .sb delegation | 19 Apr 1994 | dns | commercial (Solomon Telekom) | unknown | A | DNS only |
| Connectivity | Solomon Telekom IP hosts (olketa.solomon.com.sb etc.) | by 26 Jun 1996 | internet | commercial (Solomon Telekom) | internet | B | Traceroute evidence; website not yet fully set up |
| Service | PFnet rural email + Honiara café | 2001 | email / web-access | nonprofit / community | internet-connected | B/C | Later; HF radio for rural |

## Structured candidate records

```yaml
id: SB-01
status: candidate
person_or_project: Forum Fisheries Agency (FFA) email/UUCP service
title: FFA Honiara MSMAIL+UUCP via PEACESAT
url_original: unknown
url_archived: https://nsrc.org/db/lookup/report.php?id=890202506056:497439074&fromISO=SB
country_or_territory: Solomon Islands
connection_basis: local-hosting
medium: uucp
activity_type: communication
operator_type: institutional
network_status: internet-connected
date_claimed: 1995-08
date_type: inferred
date_precision: month
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202506056:497439074&fromISO=SB
    source_type: contemporary operator report (NSRC)
    observed_date: 1995-08-15
    supports: email-only MSMAIL+UUCP service, thrice-daily transfer to University of Hawaiʻi via PEACESAT, limited to non-profits in Honiara, host bigeye.ffa.gov.sb
    grade: B
author_attribution: Al Blake (FFA Senior Analyst Programmer)
language: en
notes: Gateway to fisheries departments in Fiji, Vanuatu and (planned) Kiribati. Limited-time FTP noted. Full IP link still under discussion.
uncertainties: Exact start date before August 1995 not established; whether any personal content was hosted on the service unknown.
researcher: Grok (xAI)
last_checked: 2026-11-17
```

```yaml
id: SB-02
status: candidate
person_or_project: Solomon Telekom IP hosts
title: olketa.solomon.com.sb and related Telekom hosts
url_original: http://www.solomon.com.sb/
url_archived: https://nsrc.org/db/lookup/report.php?id=890202505562:497425407&fromISO=SB
country_or_territory: Solomon Islands
connection_basis: local-hosting
medium: internet
activity_type: infrastructure
operator_type: commercial
network_status: internet
date_claimed: 1996-06
date_type: first-capture
date_precision: month
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202505562:497425407&fromISO=SB
    source_type: contemporary traceroute report (NSRC / Info-Nets)
    observed_date: 1996-06-26
    supports: successful traceroute to olketa.solomon.com.sb (202.84.248.4); hosts listed as in Solomon Islands; www.solomon.com.sb not yet fully set up
    grade: B
author_attribution: Olivier MJ Crepin-Leblond (reporting to NSRC)
language: en
notes: Confirms commercial TCP/IP presence by mid-1996, earlier than previously recorded early-2000s public service window.
uncertainties: Exact commercial dial-up launch date and first public customers not established; whether hosts were fully operational for general users unknown.
researcher: Grok (xAI)
last_checked: 2026-11-17
```

## Gaps and next leads

1. Locate original PEACESAT or FFA technical reports confirming the 1995 service and any earlier trials.
2. Search Solomon Telekom or government records for the first public or commercial TCP/IP / dial-up service dates (now known to be no later than June 1996 for hosts).
3. Check national library, University of the South Pacific (USP) Honiara campus, or local newspapers (Solomon Star, etc.) for early web mentions or personal pages.
4. Recover Wayback captures of any early .sb sites (solomon.com.sb, peoplefirst.net.sb) or ffa.int.
5. Investigate whether any FFA or school accounts hosted personal content.

## Bibliography / evidence log

- NSRC Connectivity Provider Database, SB entry (Al Blake report, 15 Aug 1995): https://nsrc.org/db/lookup/report.php?id=890202506056:497439074&fromISO=SB
- NSRC First Ping SB (Olivier MJ Crepin-Leblond, 26 Jun 1996): https://nsrc.org/db/lookup/report.php?id=890202505562:497425407&fromISO=SB
- NSRC New IP Hosts SB (26 Jun 1996): https://nsrc.org/db/lookup/report.php?id=890202505692:497423945&fromISO=SB
- IANA / Wikipedia .sb records (delegation 19 April 1994).
- People First Network contemporary and retrospective pages (Wayback 2001).
- Accessed 17 November 2026.

**Researcher:** Grok (xAI)  
**Last checked:** 2026-11-17
