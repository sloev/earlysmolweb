# Nauru

**Status:** evidence review (Track B); connectivity candidate strengthened with 2005 primary NSRC report; no personal-page candidate yet.
**Priority:** high (small-island, under-documented).
**Last checked:** 2026-11-20

## Internet context

Nauru (population ~10,000) had no public Internet service before 1998. CenpacNet Inc. was established as the island's ISP that year through a joint venture involving the Nauru Phosphate Royalties Trust and RONTEL / government entities. A September 1998 newswire reported that Internet had arrived, with CenpacNet then having about 50 customers and potential for more; revenue was intended to upgrade communications, and email was highlighted as a cost-saving alternative to fax.

- **.nr domain:** IANA registration date 30 March 1998; managed by CenpacNet. Original configuration associated with the first connectivity effort (Shaun Moran / ComTech Communications, Australia). Sources: IANA delegation record; Wikipedia / secondary summaries.
- **First public ISP / connectivity:** CenpacNet manager Rudolph Garoa (PacNOG 6 presentation, 2009) states Internet began in 1998 and the company was created to be the ISP; the same deck also labels it "since 2000" in one place, leaving a minor internal date discrepancy. Contemporary September 1998 report confirms service was operational with paying customers. 2002 Commonwealth of Learning survey: sole ISP, ~70 subscribers, dial-up, high cost, limited reliability.
- **2005 primary operational confirmation:** On 16 May 2005 Criden Appi (cappi@cenpac.net.nr) reported to NSRC that Cenpac Net Inc. was the sole ISP, with external connectivity of 64 kbps to Reach global services in Sydney, website at www.cenpac.net.nr, and approximately 5% population penetration. This is a contemporaneous operator report preserved in the NSRC Connectivity Providers Database.
- **No earlier email/UUCP/BITNET/Gopher evidence located** in readily available sources. Precursor: fully digital national telephone network with international satellite gateway (ITU 1998 report); no Internet circuit documented prior to CenpacNet.



### 1995 institutional computer-network lead — USP Nauru Centre and Vocational Centre

Denis Brandjes's April 2002 *School Networking in the Pacific Island States* (Commonwealth of Learning) records in the Nauru profile: **“In 1995 a computer network was provided for the University of the South Pacific and the Vocational Centre.”** The report's field visits took place in August 2001. In the same Nauru profile, it says that only one school had an Internet connection, Cenpac was the island's only ISP, and about 70 subscribers used unreliable dial-up. The report does **not** say that the 1995 institutional network used TCP/IP, carried Internet traffic, provided email, or connected to USP in Fiji.

This is therefore a **lead for an institutional/local network in 1995**, not evidence of Internet access or personal expression. A later USP history, *A University for the Pacific: 50 Years of USP* (2018, p. 121), says short-wave links to Nauru, Tuvalu and Western Samoa had not proved satisfactory and that in 1996 only four centres (Cook Islands, Solomon Islands, Tonga and Vanuatu) were linked by satellite. This makes it especially important not to assume the 1995 Nauru network was part of a working regional Internet link.

The 2002 report names the following Nauru interviewees: Baron Waqa (Director of Education), Ruby Willis (Acting Secretary of Education), Alfonso Pelizzo (technical consultant, Austron Hall Computer Specialists, an Australian company consulting in Nauru), Richard Lewis (Nauru College principal) and Venos Agege (teacher). These are **research contacts only**; the report does not attribute the 1995 network installation to any of them.

**Primary follow-up:** identify the 1995 equipment/provider and network topology through USP Nauru Centre records, Nauru Department of Education files, Austron Hall/Pelizzo records, and former campus or vocational-centre staff. Seek any contemporary description of LAN, dial-up, email, UUCP, X.25, satellite or Internet service before classifying the network.

#### Structured lead

```yaml
id: NR-02
status: lead
person_or_project: University of the South Pacific Nauru Centre and Nauru Vocational Centre
title: Institutional computer network provided in 1995
url_original:
url_archived:
country_or_territory: Nauru
connection_basis: local-hosting
medium: other
activity_type: infrastructure
operator_type: academic
network_status: unknown
date_claimed: 1995
date_type: creation
date_precision: year
evidence:
  - source_url: https://oasis.col.org/bitstreams/c9d8eae2-8242-4659-95f6-bf0f8b1c653f/download
    source_type: retrospective institutional survey based on August 2001 Nauru visits
    observed_date: 2002-04
    supports: report states a computer network was provided for USP and the Vocational Centre in 1995
    grade: B
  - source_url: https://fliphtml5.com/bacdt/asgl/A_UNIVERSITY_FOR_THE_PACIFIC_-_50_YEARS_OF_USP_-_Jacqueline_Leckie_(with_contributors/
    source_type: institutional history
    observed_date: 2018
    supports: later history says short-wave links to Nauru were unsatisfactory and Nauru was not among four satellite-linked centres in 1996
    grade: C
author_attribution: unknown; Denis Brandjes is the 2002 report author, not the 1995 network operator
language: English
notes: The report does not identify topology, protocol, provider, users, email or Internet connectivity. It separately reports Cenpac as the sole ISP and only one school with Internet access during the 2001 survey.
uncertainties: Who supplied/maintained the 1995 network; whether it was a local LAN; whether any external email or network service existed; relationship to USP regional systems.
researcher: OpenAI GPT-6
last_checked: 2026-11-20
```

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
