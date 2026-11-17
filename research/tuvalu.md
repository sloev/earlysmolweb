# Tuvalu

**Status:** evidence review (Track B); connectivity candidate strengthened, no personal-page candidate yet.
**Priority:** high (small-island, under-documented).

## Internet context

Tuvalu (population ~10,000 in the late 1990s) had no domestic Internet service until 1999. Contemporary accounts describe limited expatriate dial-up to overseas ISPs at high international rates, but no local public access.

- **.tv domain:** IANA record created 18 March 1996 (TV17-DOM), administratively associated with Tuvalu Telecommunications Corporation / Funafuti, with Canadian contacts. Commercial exploitation of the attractive TLD began in the late 1990s; the domain itself is not evidence of domestic connectivity or hosting in Tuvalu. Sources: Franck Martin, INET 2000 paper (reproducing IANA data); Wired, September 1998.
- **First domestic ISP / public connectivity:** Government-led project funded via UNDP/APDIP, implemented by SOPAC (Franck Martin). Installation and training occurred in Suva (Fiji) then Funafuti. A 64 kbps IP link via Telecom New Zealand was reported operational by mid-October 1999. NSRC provider record created 3 December 1999 for the government ISP (later tuvalu.tv / ICT Department). Earlier 1998 regional ITU paper listed joining the Internet community as a short-term plan; a Telecom 99 national report stated no Internet service yet existed and noted a July 1999 target (conditional on funding). Distinguish the July plan from the October operational IP path.

### Primary network evidence — Steven G. Huter, 3 December 1999

Contemporaneous NSRC-preserved message from Steven G. Huter (NSRC) to info-nets@rg.net:

> As of mid-October 1999, Tuvalu has an operational 64k IP link via New Zealand.

The message includes:
- Ping results to fale.tuvalu.tv (202.2.96.3): 8 of 9 packets received, average RTT 871.5 ms.
- Traceroute showing path via Telstra / New Zealand to the host.
- Telnet to port 25 returning SMTP greeting: `220 fale.tuvalu.tv ESMTP Sendmail 8.9.3/8.8.7; Sat, 4 Dec 1999 07:58:41 +1200`.
- Link to http://www.tuvalu.tv/mrtg/index.html (monitoring).

This is direct primary evidence (grade A) of an operational IP path and responding mail service by early December 1999, with the operational date stated as mid-October. It does not prove nationwide household access, continuous uptime, or a public web hosting service for individuals.

Source: https://www.nsrc.org/db/lookup/report.php?fromISO=TV&id=944259003113:488906182

- **No earlier email/UUCP/BITNET/Gopher evidence located** in the 1996 international email-accessibility FAQ (TV entry blank) or other readily available sources. Precursor non-Internet: satellite telephone system; excess international capacity used for relayed services in the mid-1990s.

## Personal web ecology / earliest candidates

No personal homepages or individual online publications identified yet. The 1999 ISP offered dial-up and planned to provide customers with small web-space allocations (5 MB mentioned in the SOPAC account) to encourage local content. Government/institutional site at tuvalu.tv followed the ISP launch.

## Candidate register

```yaml
id: TV-01
status: candidate
person_or_project: Tuvalu government ISP / fale.tuvalu.tv
title: Operational 64 kbps IP link and mail service
url_original: http://www.tuvalu.tv/
url_archived:
country_or_territory: Tuvalu
connection_basis: local-hosting
medium: internet-access
activity_type: connectivity
operator_type: government
network_status: internet
date_claimed: mid-October 1999
date_type: inferred
date_precision: month
evidence:
  - source_url: https://www.nsrc.org/db/lookup/report.php?fromISO=TV&id=944259003113:488906182
    source_type: contemporary technical report with network tests
    observed_date: 1999-12-03
    supports: operational 64k IP link as of mid-October; responding host and SMTP
    grade: A
author_attribution: Steven G. Huter (reporter); government/SOPAC implementation
language: English
notes: Distinguishes plan (July 1999 target) from observed operational path. No personal expression claim.
uncertainties: Exact first customer dial-up date; outer-island access; continuous service.
researcher: Grok / xAI
last_checked: 2026-11-17
```

## Gaps and next leads

- Recover original 1999 Huter messages, APNIC IP allocation records, and first Wayback captures of tuvalu.tv or government pages.
- Search Pacific Islands Monthly / local newspapers for 1999 launch coverage.
- Check for any pre-1999 academic or NGO email accounts associated with Funafuti residents.
- Local-language (Tuvaluan) sources and oral histories of early users.
- Locate original SOPAC/Franck Martin implementation notes or training records.

## Bibliography

- Steven G. Huter, “Full IP link established to Tuvalu (October 1999)”, 3 Dec 1999. https://www.nsrc.org/db/lookup/report.php?fromISO=TV&id=944259003113:488906182
- Franck Martin, "Tuvalu's First ISP," INET 2000. https://www.isoc.org/inet2000/cdproceedings/8d/8d_1.htm (Wayback: https://web.archive.org/web/20160103041754/http://www.isoc.org/inet2000/cdproceedings/8d/8d_1.htm)
- NSRC Connectivity Provider Database, Tuvalu report id=5. https://nsrc.org/db/lookup/report.php?id=5&fromISO=TV
- NSRC provider entry (created 3 Dec 1999). https://nsrc.org/db/lookup/provider.php?id=944259601259:489048280&fromISO=TV
- Wired, "Buy This Domain," September 1998. https://www.wired.com/1998/09/tuvalu/
- 1996 international email accessibility FAQ (TV blank). https://nsrc.org/codes/bymap/ntlgy/text/960616.txt
- btw.media source-critical summary (2026). https://btw.media/en/tuvalu-internet-july-target-ip-link-october-1999

**Researcher:** Grok / xAI agent  
**Last checked:** 2026-11-17
