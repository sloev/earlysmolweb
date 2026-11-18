# Samoa — early internet activity, networks, and web research

**Status:** active; 1996 commercial TCP/IP (talofa.net / Pacific Internet) and 1998 multi-ISP gateway documented with primary evidence; no resident personal homepage verified.
**Priority:** Pacific scouting.
**Research jurisdiction:** Samoa (independent state; formerly Western Samoa).

## Chronology and evidence

### 14 July 1995 — .ws ccTLD delegation
IANA delegated `.ws` (Western Samoa) on 14 July 1995 to the Government of Samoa / Ministry of Foreign Affairs.

- Source: IANA root-zone records (registration date 1995-07-14); ICANNWiki and secondary summaries.
- Evidence grade: **A** for DNS-delegation date only. Does not prove local connectivity or resident operators.

### August 1995 — Pactok/Wantok email precursor at SPREP, Apia
Contemporary NSRC report from SPREP (Wanda Ieremia / Alex Williams) describes the Pacific Sustainable Development Networking Project for Western Samoa using the Wantok/Pactok FidoNet-style email system, with host `wsamoamgr@pactok.peg.apc.org`. Notes plans for migration toward TCP/IP.

- Source: NSRC, “W. Samoa Networking Update (8/95)” (8 Aug 1995): https://nsrc.org/db/lookup/report.php?id=890202507601:497439514&fromISO=WS
- Evidence grade: **A** (contemporary operator report).
- Category: NGO/development network / store-and-forward email; precursor-non-internet or inter-network.

### 8 September 1996 — First Ping / traceroute to talofa.net
Olivier MJ Crepin-Leblond (Info-Nets) reports traceroute from the UK to `www.talofa.net` / `pi.talofa.net` (198.142.85.1), confirming public reachability. Notes the site “must have been around for a few months already.”

- Source: NSRC, “First Ping WS - Western Samoa (1996.09.06)” (8 Sep 1996): https://nsrc.org/db/lookup/report.php?id=890202507278:497425334&fromISO=WS
- Evidence grade: **A** (contemporary traceroute evidence of reachability).
- Category: commercial TCP/IP host / web service; operator: Pacific Internet Services, Apia.

### 23 December 1996 — Pacific Internet Services operational update
Bruce Edwards (Pacific Internet Services - Apia) reports to NSRC: 64 kb TCP/IP connection via satellite to Sydney, Australia; equipment (Cisco 2511, Linux web server, NT domain server); dial-up pricing WST 5.00 per hour; circuit cost WST 30,000/month. Host: talofa.net.

- Source: NSRC, “Connectivity Update for Pacific Internet Services (12/96)” (23 Dec 1996): https://nsrc.org/db/lookup/report.php?id=890202507170:497426787&fromISO=WS
- Evidence grade: **A** (contemporary operator technical report).
- Category: commercial ISP / TCP/IP dial-up and hosting.

### 1998 SOPAC retrospective on the 1996 Pacific Internet / talofa.net service
The March 1998 SOPAC trip report by Leslie Allinson records that the first ISP was set up in 1996 by Pacific Internet as a vehicle for a gambling scheme connected to commercial rugby (Super League). The domain was published as TALOFA.NET but registered as SUPER12.NET and described as a “Rugby ISP” in Australia. Bruce Edwards (a partner) was contacted during a 1996 visit; his reticence is now explained. The business side was never fully implemented: users were not consistently billed nor the provider consistently paid. Pacific Internet was not granted gambling approval; the system was abandoned. Telecom Samoa repossessed the equipment for unpaid bills exceeding WST 200,000 and leased it to CSL, which formed SAMOA.NET. Investment estimates: ~USD 20k equipment + USD 100k staff.

- Source: Leslie Allinson / Martin F., “Internet gateway, Telecom Samoa”, SOPAC Trip Report 256 (7–14 March 1998): https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf
- Evidence grade: **A** (primary contemporary field report).
- Notes: Explains non-sustainable character and equipment transition; does not contradict the 1996 NSRC operational reports.

### 7–14 March 1998 — Telecom Samoa shared gateway for multiple ISPs
Leslie Allinson (SOPAC) trip report documents installation of a gateway allowing up to three retail ISPs to share the international satellite link. Operational after 12-hour switchover (week of 9 March). Samoa.net configuration recorded (DNS, mail, web server, dial-in 25300). Equipment from abandoned 1996 TALOFA/Pacific Internet repossessed and leased to CSL (Samoa.net). Second ISP (Lesa) encouraged for competition. Apia Observatory uploading satellite images via Samoa.net.

- Source: Leslie Allinson / Martin F., “Internet gateway, Telecom Samoa”, SOPAC Trip Report 256 (7–14 March 1998): https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf
- Evidence grade: **A** (primary contemporary field report).
- Category: infrastructure / gateway; commercial dial-up providers.

### 10 June 1999 — talofa.net successor note
Tim Sansom reports talofa.net no longer exists as an ISP; believed bankrupt, taken over, and became www.samoa.net. Additional ISP lesamoa.com.

- Source: NSRC, “ISPs in Samoa” (10 Jun 1999): https://www.nsrc.org/db/lookup/report.php?id=929113856237:489041676&fromISO=WS
- Evidence grade: **B** (contemporary secondary report of prior status).

## Structured candidates

```yaml
id: WS-01
status: candidate
person_or_project: Pacific Internet Services / talofa.net
title: 1996 commercial TCP/IP dial-up and web host in Apia
url_original: http://www.talofa.net
url_archived:
country_or_territory: Samoa
connection_basis: local-hosting
medium: website | internet-access
activity_type: connectivity | service | infrastructure
operator_type: commercial
network_status: internet
date_claimed: 1996-09
date_type: first-capture
date_precision: month
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202507278:497425334&fromISO=WS
    source_type: contemporary traceroute / list
    observed_date: 1996-09-08
    supports: public reachability of talofa.net
    grade: A
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202507170:497426787&fromISO=WS
    source_type: contemporary operator report
    observed_date: 1996-12-23
    supports: operational 64 kb TCP/IP dial-up, equipment, pricing
    grade: A
  - source_url: https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf
    source_type: primary field report
    observed_date: 1998-03
    supports: non-sustainable gambling-related venture; abandoned; equipment repossessed
    grade: A
author_attribution: Bruce Edwards, Pacific Internet Services, Apia
language: English
notes: Strongest early commercial TCP/IP evidence. Distinct from later 1998 gateway and Samoa.net. SOPAC report clarifies it was a short-lived gambling-related attempt that was abandoned.
uncertainties: Exact first customer date and continuous operation after Dec 1996 not fully established; bankruptcy timing from 1999 report; whether any public customers used it before abandonment.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

```yaml
id: WS-02
status: candidate
person_or_project: Telecom Samoa shared gateway / Samoa.net
title: March 1998 multi-ISP international gateway and Samoa.net dial-up configuration
url_original: http://www.samoa.net
url_archived:
country_or_territory: Samoa
connection_basis: local-hosting
medium: gateway | internet-access
activity_type: infrastructure | service
operator_type: commercial | government
network_status: internet
date_claimed: 1998-03
date_type: first-publication
date_precision: month
evidence:
  - source_url: https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf
    source_type: primary field report
    observed_date: 1998-03
    supports: gateway installation, Samoa.net settings, observatory use; repossession of prior equipment
    grade: A
author_attribution: Leslie Allinson (SOPAC); Telecom Samoa / CSL
language: English
notes: Documents shared wholesale gateway and operational retail configuration. Does not claim to be the absolute first connectivity.
uncertainties: Relationship to 1996 talofa.net equipment now clarified as repossession; subscriber numbers not given in report.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

## Assessment

Primary NSRC records establish operational commercial TCP/IP (talofa.net / Pacific Internet) in Apia by September 1996, with detailed technical and pricing information by December 1996. The 1998 SOPAC report documents both the non-sustainable character of that 1996 venture (gambling-related, abandoned, equipment repossessed) and the subsequent shared gateway enabling multiple retail ISPs (Samoa.net / CSL and Lesa). These are distinct milestones from the 1995 DNS delegation and the earlier Pactok email system. No resident personal homepage or individual publishing candidate has been located.

## Gaps and next leads

1. Recover Wayback captures of talofa.net (1996–97) and early samoa.net.
2. Locate original local newspaper coverage (Samoa Observer) of the 1996 ISP or 1998 gateway.
3. Search for user directories, university or government personal pages from the initial ISP period.
4. Clarify exact bankruptcy / transition timing of Pacific Internet / talofa.net.
5. Continue parallel Pacific scouting (Marshall Islands, Micronesia, Palau) and first-wave items.

## Sources consulted

- NSRC First Ping WS (1996): https://nsrc.org/db/lookup/report.php?id=890202507278:497425334&fromISO=WS
- NSRC Pacific Internet update (1996): https://nsrc.org/db/lookup/report.php?id=890202507170:497426787&fromISO=WS
- NSRC W. Samoa Networking Update (1995): https://nsrc.org/db/lookup/report.php?id=890202507601:497439514&fromISO=WS
- NSRC ISPs in Samoa (1999): https://www.nsrc.org/db/lookup/report.php?id=929113856237:489041676&fromISO=WS
- Allinson / Martin, SOPAC Trip Report 256 (1998): https://spccfpstore1.blob.core.windows.net/digitallibrary-docs/files/ca/ca167e0aeec8ba1c70f50ac3627140ac.pdf
- IANA .ws records.

**Researcher:** Grok (xAI)  
**Last checked:** 2026-11-18
