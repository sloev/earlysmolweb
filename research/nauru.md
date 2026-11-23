# Nauru

**Status:** evidence review; 1995 institutional network and 1998 ISP candidates; 1997 externally hosted Nauru country-page lead now cross-referenced by later government and agency sources; no personal-page candidate yet.
**Priority:** high (small-island, under-documented).
**Last checked:** 2026-11-23

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

## January 1997 directory-listed Nauru Page (new lead)

Mark C. Goniwiecha's “Guam & Micronesia in Cyberspace,” published in the *Journal of the Pacific Society* in January 1997, includes an “Internet Resources and Home Pages” list. It names **“Nauru Page, Republic of Nauru”** and gives:

http://www.tbc.gov.bc.ca/cwgames/country/Nauru/nauru.html

This is a contemporary, dated directory reference to a Nauru-labelled web page by January 1997. The hostname is under a British Columbia government domain, and the path contains “cwgames”, but the original page could not be opened and its content/operator were not recovered. The title alone does not establish that the page was maintained by the Nauruan government, that it was locally hosted, or that it was personal. No Wayback capture was recovered through this access route. Treat it as an externally hosted country-information lead, distinct from the 1995 USP/Vocational Centre network and the 1998 CenpacNet launch.

Source: Mark C. Goniwiecha, “Guam & Micronesia in Cyberspace,” *Journal of the Pacific Society*, January 1997, printed p. 118 / PDF page 5, ERIC document ED 437 020, https://files.eric.ed.gov/fulltext/ED437020.pdf (accessed 22 November 2026). Goniwiecha authored the directory article, not necessarily the Nauru page.

```yaml
id: NR-03
status: lead
person_or_project: Unknown operator; “Nauru Page, Republic of Nauru”
title: Nauru country page (directory-listed January 1997)
url_original: http://www.tbc.gov.bc.ca/cwgames/country/Nauru/nauru.html
url_archived: unknown
country_or_territory: Nauru
connection_basis: other
medium: website
activity_type: publishing
operator_type: unknown
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; page launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: identifies the title “Nauru Page, Republic of Nauru” and gives the original URL
    grade: B
  - source_url: https://idahodocs.contentdm.oclc.org/digital/api/collection/p16293coll6/id/245290/download
    source_type: Organization of American States / University of Idaho comparative tourism-agency study
    observed_date: 1998
    supports: identifies tbc.gov.bc.ca as the website of Tourism British Columbia and describes the agency as a Crown Corporation; it does not describe the Nauru subpage
    grade: C
  - source_url: https://dirco1.azurewebsites.net/foreign/bilateral/nauru.html
    source_type: South African Department of Foreign Affairs country profile
    observed_date: 2021-06-21 (page copyright © 2003)
    supports: links directly to the exact Nauru Page URL as further information on Nauru
    grade: C
author_attribution: unknown; Mark C. Goniwiecha authored the directory article, not necessarily the page
language: unknown (directory is English)
notes: The hostname tbc.gov.bc.ca is identified in a 1998 OAS study as Tourism British Columbia's website; the agency is described as a Crown Corporation. A South African government country profile (copyright © 2003; last updated 2021-06-21) links to this exact Nauru URL as further information. These are host-domain and later directory cross-checks only: the exact subpage content, operator, purpose and sponsorship remain unverified. The path includes cwgames but does not establish a Commonwealth Games connection. Not evidence of a Nauruan government or personal site.
uncertainties: Original page content; operator; official vs independent country profile; launch date; archive captures; author and hosting location.
researcher: OpenAI GPT-6
last_checked: 2026-11-23
```

## Personal web ecology / earliest candidates

No personal homepages or individual online publications identified yet. Early service focused on email, dial-up access, and institutional/commercial use. Government and commercial sites followed the ISP launch; local content remained limited.

## Gaps and next leads

- Recover the January 1997 Nauru Page at tbc.gov.bc.ca through a working Wayback/CDX or British Columbia government archive route; identify its operator and page type before assigning official status.\n- Recover full original September 1998 SIDSNet / newswire item and any contemporaneous local or regional coverage.
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
- Denis Brandjes, *School Networking in the Pacific Island States*, Commonwealth of Learning, April 2002, Annex C, Nauru profile, items 65–70 (printed p. 52). https://oasis.col.org/bitstreams/c9d8eae2-8242-4659-95f6-bf0f8b1c653f/download
- Rudolph Garoa, *Nauru Internet Update*, PacNOG 6, 2009, especially slides/pages 8–10 (and the conflicting “since 2000” label on p. 1). https://www.pacnog.org/pacnog6/presentations/nauru-pacnog6.pdf
- CenpacNet official homepage, current self-description “The Republic of Naoero's ISP since 1998” (accessed 2026-11-20). https://www.cenpac.net.nr/
- Jacqueline Leckie, *A University for the Pacific: 50 Years of USP*, USP, 2018, p. 121 (FlipHTML5 copy). https://fliphtml5.com/bacdt/asgl/A_UNIVERSITY_FOR_THE_PACIFIC_-_50_YEARS_OF_USP_-_Jacqueline_Leckie_(with_contributors/

**Researcher:** OpenAI GPT-6 (current pass; earlier work by Grok / xAI)  
**Last checked:** 2026-11-20

- Mark C. Goniwiecha, “Guam & Micronesia in Cyberspace,” *Journal of the Pacific Society*, January 1997, ERIC ED 437 020 (Nauru Page URL listed on printed p. 118 / PDF p. 5): https://files.eric.ed.gov/fulltext/ED437020.pdf
- Stephen N. Edwards, William J. McLaughlin and Sam H. Ham, *Comparative Study of Ecotourism Policy in the Americas* (1998), British Columbia agency profile: https://idahodocs.contentdm.oclc.org/digital/api/collection/p16293coll6/id/245290/download
- South African Department of Foreign Affairs, “Republic of Nauru” country profile (copyright © 2003; last updated 21 June 2021): https://dirco1.azurewebsites.net/foreign/bilateral/nauru.html
