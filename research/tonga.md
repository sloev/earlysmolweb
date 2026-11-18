# Tonga — early internet research

**Status:** infrastructure and DNS leads documented; no personal-page candidate verified. Country status: scouting / active (first infrastructure chronology established).
**Priority:** mid-list discovery heuristic (Pacific island states).
**Research jurisdiction:** Kingdom of Tonga.

## Context and connectivity chronology

Tonga’s documented path into internet activity separates DNS/administrative presence, overseas-hosted .to hosts, planned local satellite connectivity, and later public internet service. These are distinct milestones.

- **18 December 1995:** .to country-code top-level domain introduced (IANA delegation record). Registry later operated by Tonga Network Information Center (Tonic). Source: IANA root zone database; Wikipedia summary citing primary delegation (grade B for introduction date).
- **11 April 1996:** Eric Gullichsen reports to NSRC that primary and secondary nameservers for .to are operational (listed at dns.aa.msen.com, ns.ripe.net, auth02.ns.uu.net, ns1.iafrica.com, munnari.oz.au, nbn.nbn.com). He states the first machines in the domain are running at the Consulate of Tonga in San Francisco (sfconsulate.gov.to, www.vacations.tvb.gov.to). He is travelling to Tonga to finalize a 64 kbps earth station via PAS-2, expected operational in 3Q 1996. This is contemporary technical correspondence (grade A for the DNS/hosts status at that date; the earth-station date is a forecast). Source: NSRC Connectivity Provider Database, Tonga Connectivity Update (4/96). https://nsrc.org/db/lookup/report.php?fromISO=TO&id=890202506375:497436004
- **13 January 1997:** Olivier M. J. Crepin-Leblond posts a traceroute from Imperial College (UK) to candw.to (207.124.73.129). Hops remain in UK/US networks; the title “First Ping TO” should not be read as proof of a first connection originating in Tonga. Contemporary observation of external reachability of a .to host (grade B). Source: NSRC, First Ping TO — Tonga on the Net (1997.01.13). https://nsrc.org/db/lookup/report.php?fromISO=TO&id=890202506243:497437449
- **1997:** Government of Tonga report (reproduced in ITU Telecom Asia 2000) states that internet service was introduced in the Kingdom in 1997. By the time of the report, Tonga had dedicated links of 128 kbit/s to the United States and 256 kbit/s to Australia. Retrospective/official country report (grade B). Source: https://www.itu.int/itudoc/telecom/tlc2000/nat_rep.pdf (national report section).
- **Earlier message services (retrospective, approximate):** A 2005 NSRC response by Samiuela LV Taufa recalls a FidoNet-style email service around 1994 with fewer than ten customers, and UUCP feeds around 1995 that carried messages from Vava’u and Ha’apai to Tongatapu for daily international batching. These are later recollections of email systems, not interactive public internet (grade C). Source: NSRC historical response (2005). https://nsrc.org/db/lookup/report.php?fromISO=TO&id=3

Retrospective accounts (Salon 1999, Wired 1997, LA Times 1997) describe Gullichsen arranging dial-up email to a Sausalito server in the mid-1990s with the Crown Prince’s involvement, and commercial .to domain sales beginning in 1997 via the San Francisco consulate (Tonic). These are useful leads but secondary to the NSRC primary correspondence.

## Track A — next lead-finding actions

1. Search for surviving 1995–1997 captures of sfconsulate.gov.to, www.vacations.tvb.gov.to, tonic.to, or early .to institutional pages in Wayback/Netarkivet or other Pacific archives.
2. Seek local-language (Tongan) newspaper or government notices from 1996–1997 about internet, email, or the satellite link.
3. Follow Gullichsen, Lyons, and early Tonic/ISP contacts for any personal or institutional homepage leads hosted in or connected to Tonga.
4. Check University of the South Pacific campus network records for Tonga (mentioned in later NSRC notes) and any academic email/UUCP activity before 1997.

## Track B — evidence and write-up

- No earliest personal homepage is asserted.
- DNS resolution and overseas .to hosts in April 1996 are contemporary; local permanent public internet service is dated by the government report to 1997.
- Distinguish FidoNet/UUCP email (precursor) from TCP/IP internet and from Web publishing.
- Connection basis for early .to activity includes government/consular hosting and later commercial registry; do not infer residence solely from the domain.

## Candidate register

_No personal-page or verified local web-publication candidates yet. Infrastructure candidates only:_

```yaml
id: TO-01
status: probable
person_or_project: .to TLD and early hosts (Consulate of Tonga, San Francisco)
title: Early .to nameservers and consular hosts
url_original: sfconsulate.gov.to ; www.vacations.tvb.gov.to (reported 1996)
url_archived: unknown
country_or_territory: Tonga
connection_basis: government / consular
medium: dns / website
activity_type: infrastructure
operator_type: government
network_status: internet
date_claimed: 11 April 1996 (nameservers operational; hosts reported)
date_type: inferred from contemporary report
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?fromISO=TO&id=890202506375:497436004
    source_type: contemporary technical correspondence
    observed_date: 1996-04-11
    supports: nameservers answering; first machines at SF consulate
    grade: A
author_attribution: Eric Gullichsen (Warp Ltd.)
language: English
notes: Earth-station forecast is not activation evidence. Hosts may have been reachable without local Tongan termination of the circuit.
uncertainties: Exact first local-hosting date in Tonga; survival of 1996 page content.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

```yaml
id: TO-02
status: candidate
person_or_project: Public internet service introduction
title: Kingdom internet service (government report)
url_original: unknown
url_archived: unknown
country_or_territory: Tonga
connection_basis: local infrastructure
medium: internet-access
activity_type: connectivity
operator_type: government / commercial (later ISPs)
network_status: internet
date_claimed: 1997
date_type: first-publication (service introduction)
date_precision: year
evidence:
  - source_url: https://www.itu.int/itudoc/telecom/tlc2000/nat_rep.pdf
    source_type: official country report
    observed_date: circa 2000
    supports: service introduced 1997; bandwidth figures
    grade: B
author_attribution: Government of Tonga
language: English
notes: Do not equate with the 1996 DNS/hosts or earlier email. Exact month and first public ISP remain open.
uncertainties: Precise start date within 1997; first local website or personal page after service launch.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

## Gaps and next leads

- No 1995–1996 Wayback captures of the reported consular sites have been confirmed in this pass.
- Local Tongan-language sources and contemporary press not yet systematically searched.
- Personal expression / individual homepages remain unlocated.

## Bibliography / evidence log

- NSRC Tonga Connectivity Update, 11 Apr 1996 (Gullichsen).
- NSRC First Ping TO, 13 Jan 1997 (Crepin-Leblond).
- ITU Telecom Asia 2000 national report (Tonga section).
- NSRC 2005 historical note (Taufa) on earlier email.
- IANA .to delegation; contemporary press (Wired 1997, Salon 1999) as secondary leads.
