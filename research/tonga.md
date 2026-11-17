# Tonga — early internet activity, networks, and web research

**Status:** evidence review (Track B); connectivity candidates advanced with primary NSRC evidence; diaspora community lead remains grade C; no locally hosted personal homepage verified.
**Priority:** high (small-island, under-documented).
**Researcher:** Grok / xAI
**Last checked:** 2026-11-17

## Early connectivity, domain, and ISP context

### Domain delegation
The country-code top-level domain `.to` was delegated by IANA on 18 December 1995 (record created; sponsoring organization Government of the Kingdom of Tonga / Crown Prince).

- Source: IANA root-zone records and Wikipedia / ICANNWiki summaries.
- Evidence grade: **A** for the DNS-delegation date only. It does not prove local connectivity or user activity inside Tonga.

### 1995–1996 early access and overseas hosts
Eric Gullichsen (American software engineer) is reported to have set up dial-up email/Internet access during a prolonged visit around 1995, with the prince’s blessing, initially linking to a server in California. By April 1996 `.to` nameservers were answering from international machines and the first hosts were reported at the Tongan consulate in San Francisco. A 64 kbps satellite earth station via PAS-2 was still planned for later in 1996.

- Sources: Salon.com 1999 interview with Gullichsen; NSRC archived April 1996 nslookup report from Gullichsen; btw.media summary of the same.
- Evidence grade: **B/C** (contemporary technical report + retrospective interview).

NSRC later records also note a FidoNet-style email service circa 1994 (very small) and UUCP feeds circa 1995 from outer islands to Tongatapu for batching (retrospective).

### Primary NSRC evidence — April 1996 and January 1997

- **11 April 1996 — nameserver and overseas hosts:** Eric Gullichsen reported to NSRC that primary and secondary nameservers for `.to` were answering, and that the first machines in the domain were running at the Consulate of Tonga in San Francisco (`sfconsulate.gov.to`, `www.vacations.tvb.gov.to`). He noted a planned 64 kbps earth station via PAS-2 expected operational in 3Q96. This is contemporary technical evidence of domain infrastructure outside Tonga; it does not prove a live host inside the Kingdom.
  - Source: https://nsrc.org/db/lookup/report.php?id=890202506375:497436004&fromISO=TO
  - Grade: **A/B**

- **13 January 1997 — First Ping TO:** Olivier MJ Crepin-Leblond (Imperial College) posted a traceroute to `candw.to` (207.124.73.129) from the UK. The path reached the host after multiple US hops. The report is titled “First Ping TO - Tonga on the Net (1997.01.13)”. This demonstrates external reachability of a `.to` host by mid-January 1997; it does not by itself prove the host was located inside Tonga or that public dial-up service was available to residents.
  - Source: https://nsrc.org/db/lookup/report.php?id=890202506243:497437449&fromISO=TO
  - Grade: **A** for the observed traceroute/reachability; location of the host remains to be confirmed.

### 1997 public Internet service
Government reports and secondary accounts date the introduction of public Internet service in the Kingdom to 1997. By 2000 there were dedicated international bearers (128 kbit/s to US, 256 kbit/s to Australia) and hundreds of customers. Commercial domain sales via Tonic (Tonga Network Information Center) opened to the world in 1997, operated from the San Francisco consulate.

- Sources: ITU Telecom Asia 2000 national report; Salon, Wired, Irish Times contemporary press on the 1997 domain sale.
- Evidence grade: **B** for 1997 public-service window; **A/B** for the commercial registry activity.

No earlier sustained public TCP/IP dial-up service inside Tonga is documented beyond the 1995 personal/experimental link.

## Candidate register

```yaml
id: TO-01
status: candidate
person_or_project: .to domain infrastructure / overseas hosts
title: Nameservers answering and first hosts at Tongan consulate in San Francisco
url_original: www.vacations.tvb.gov.to
url_archived:
country_or_territory: Tonga
connection_basis: other
medium: domain-infrastructure
activity_type: infrastructure
operator_type: government
network_status: internet
date_claimed: 1996-04-11
date_type: inferred
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202506375:497436004&fromISO=TO
    source_type: contemporary technical report
    observed_date: 1996-04-11
    supports: nameservers answering; first machines at SF consulate; planned 64 kbps link
    grade: A
author_attribution: Eric Gullichsen (reporter)
language: English
notes: Domain infrastructure and overseas hosts; does not prove local Tonga connectivity.
uncertainties: Exact location of all hosts; whether any were inside the Kingdom.
researcher: Grok / xAI
last_checked: 2026-11-17

id: TO-02
status: candidate
person_or_project: candw.to host reachability
title: First recorded traceroute to a .to host (candw.to)
url_original: candw.to
url_archived:
country_or_territory: Tonga
connection_basis: other
medium: internet-access
activity_type: connectivity
operator_type: commercial
network_status: internet
date_claimed: 1997-01-13
date_type: first-capture
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202506243:497437449&fromISO=TO
    source_type: contemporary traceroute report
    observed_date: 1997-01-13
    supports: external reachability of candw.to; host resolved and responded
    grade: A
author_attribution: Olivier MJ Crepin-Leblond (reporter)
language: English
notes: Reachability evidence only. Host location (inside Tonga or elsewhere) not established by the traceroute alone.
uncertainties: Physical location of the host; relationship to public service launch.
researcher: Grok / xAI
last_checked: 2026-11-17
```

## Personal / community expression lead

### Taholo Kami — Tonga Online and the Kava Bowl (mid-1990s)
Taholo Kami (Tongan-born, then a student at Vanderbilt University in Nashville) has stated in interviews that in 1994–1995, unable to find news from home, he started a website called **Tonga Online** and an interactive forum called the **Kava Bowl**. It grew rapidly among Pacific Islanders in the diaspora (claims of high traffic within a few years). Later references place the Kava Bowl at pacificforum.com/kavabowl.

- Sources: Daily Nexus 2001 interview; National Geographic bio; YouTube oral history (2021); academic papers citing KBAdmin posts from ~2000.
- Evidence grade: **C** (retrospective personal testimony corroborated by later academic and community references). Strong lead for early Tongan-associated personal/community publishing, but the site was operated from the United States, not locally hosted in Tonga. Connection basis is self-described Tongan identity and diaspora community, not local infrastructure.

This is the strongest named personal/community candidate located. No contemporaneous 1995–1996 capture or original URL has been recovered in this pass.

## Research interpretation

- `.to` delegation in December 1995 and early experimental access by Gullichsen create an early infrastructure window.
- Primary NSRC records now document overseas domain infrastructure (April 1996) and external reachability of a `.to` host (January 1997).
- Public commercial Internet and the global marketing of `.to` open in 1997.
- The Kami / Tonga Online / Kava Bowl lead is the principal personal-expression and community candidate; it is diaspora-based and requires archive recovery to elevate beyond grade C.
- Local-language sources and in-country newspaper archives remain unexamined.

## Gaps and next leads

- Confirm the physical location of the candw.to host reached in the January 1997 traceroute.
- Recover original 1997 government service announcement and any local newspaper coverage.
- Search for early Wayback captures of .to sites hosted inside Tonga.
- Recover any surviving captures or contemporary mentions of Tonga Online / Kava Bowl.
- Search Tongan-language newspapers and local ISP records for personal pages once public access opened.
- Continue parallel scouting on Vanuatu and remaining Pacific jurisdictions; keep first-wave open items active.

**Personal-homepage status:** none verified locally; strong diaspora community lead (Kami / Kava Bowl) documented.
