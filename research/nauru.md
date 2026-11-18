# Nauru

**Status:** evidence review (Track B); connectivity candidate strengthened with 2005 primary NSRC report; no personal-page candidate yet.
**Priority:** high (small-island, under-documented).
**Last checked:** 2026-11-18

## Internet context

Nauru (population ~10,000) had no public Internet service before 1998. CenpacNet Inc. was established as the island's ISP that year through a joint venture involving the Nauru Phosphate Royalties Trust and RONTEL / government entities. A September 1998 newswire reported that Internet had arrived, with CenpacNet then having about 50 customers and potential for more; revenue was intended to upgrade communications, and email was highlighted as a cost-saving alternative to fax.

- **.nr domain:** IANA registration date 30 March 1998; managed by CenpacNet. Original configuration associated with the first connectivity effort (Shaun Moran / ComTech Communications, Australia). Sources: IANA delegation record; Wikipedia / secondary summaries.
- **First public ISP / connectivity:** CenpacNet manager Rudolph Garoa (PacNOG 6 presentation, 2009) states Internet began in 1998 and the company was created to be the ISP; the same deck also labels it "since 2000" in one place, leaving a minor internal date discrepancy. Contemporary September 1998 report confirms service was operational with paying customers. 2002 Commonwealth of Learning survey: sole ISP, ~70 subscribers, dial-up, high cost, limited reliability.
- **2005 primary operational confirmation:** On 16 May 2005 Criden Appi (cappi@cenpac.net.nr) reported to NSRC that Cenpac Net Inc. was the sole ISP, with external connectivity of 64 kbps to Reach global services in Sydney, website at www.cenpac.net.nr, and approximately 5% population penetration. This is a contemporaneous operator report preserved in the NSRC Connectivity Providers Database.
- **No earlier email/UUCP/BITNET/Gopher evidence located** in readily available sources. Precursor: fully digital national telephone network with international satellite gateway (ITU 1998 report); no Internet circuit documented prior to CenpacNet.

### Structured candidate

```yaml
id: NR-01
status: candidate
person_or_project: CenpacNet Inc. (first public ISP)
title: CenpacNet dial-up Internet service launch
url_original: http://www.cenpac.net.nr/
url_archived: https://web.archive.org/web/20070927015139/http://www.sidsnet.org/archives/other-newswire/9809/0004.html
country_or_territory: Nauru
connection_basis: local-hosting
medium: internet-access
activity_type: connectivity
operator_type: commercial
network_status: internet
date_claimed: 1998
date_type: first-publication
date_precision: year
evidence:
  - source_url: https://web.archive.org/web/20070927015139/http://www.sidsnet.org/archives/other-newswire/9809/0004.html
    source_type: contemporary newswire
    observed_date: 1998-09
    supports: operational ISP with ~50 customers, email use
    grade: B
  - source_url: https://nsrc.org/db/lookup/report.php?id=7&fromISO=NR
    source_type: contemporary operator report (NSRC)
    observed_date: 2005-05-16
    supports: sole ISP, 64 kbps to Sydney, website, ~5% penetration
    grade: A
  - source_url: https://nsrc.org/workshops/2009/pacnog6/presentations/nauru-pacnog6.pdf
    source_type: retrospective operator presentation
    observed_date: 2009
    supports: company formed as ISP; Internet began 1998 (with internal discrepancy)
    grade: C
author_attribution: Criden Appi (2005 report); Rudolph Garoa (2009)
language: English
notes: Contemporary September 1998 report confirms paying customers and email as alternative to fax. 2005 NSRC report provides primary operator confirmation of operational parameters. Garoa presentation has date conflict ("since 2000" on one slide). No personal homepage identified.
uncertainties: Exact first customer date; whether any pre-1998 academic/NGO email existed; personal-expression track open.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

## Personal web ecology / earliest candidates

No personal homepages or individual online publications identified yet. Early service focused on email, dial-up access, and institutional/commercial use. Government and commercial sites followed the ISP launch; local content remained limited.

## Gaps and next leads

- Recover full original September 1998 SIDSNet / newswire item and any contemporaneous local or regional coverage.
- Locate earliest Wayback captures of cenpac.net.nr or government pages.
- Search for pre-1998 academic, NGO, or expatriate email accounts associated with Nauru residents.
- Local oral histories and Pacific regional newspapers for launch details.
- Inspect any surviving user directories or early personal pages on cenpac.net.nr hosting.

## Bibliography

- SIDSNet Other Newswire, September 1998: "Internet arrives in Nauru." https://web.archive.org/web/20070927015139/http://www.sidsnet.org/archives/other-newswire/9809/0004.html
- Criden Appi, “The state of the Net in Nauru”, 16 May 2005. https://nsrc.org/db/lookup/report.php?id=7&fromISO=NR
- Rudolph Garoa, PacNOG 6 presentation (2009). https://nsrc.org/workshops/2009/pacnog6/presentations/nauru-pacnog6.pdf
- IANA .nr delegation record (registration 1998-03-30). https://www.iana.org/domains/root/db/.nr.html
- ITU, Pacific Islands Telecommunications, 1998 (telephone network description).
- Commonwealth of Learning school connectivity scan, April 2002.

**Researcher:** Grok / xAI agent  
**Last checked:** 2026-11-18
