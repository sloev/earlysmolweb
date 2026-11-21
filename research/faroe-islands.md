# Faroe Islands (Føroyar)

**Status:** infrastructure candidates documented; one probable institutional homepage by 1996; first-homepage claim remains a lead. No verified personal homepage yet.
**Priority:** first wave (separate research jurisdiction within the Kingdom of Denmark).
**Last checked:** 2026-11-21

## Internet context

The Faroe Islands had no general commercial public Internet service before the mid-1990s, but academic and research institutions in Tórshavn were externally reachable by January 1995. A 19 January NSRC trace reached `dk-gw.sleipnir.fo` through Denmark; a 25 January update said the islands were connected but no mail-capable machines were yet running. By 31 July 1995, the university reported a shared SLEIPNIR SMTP/POP3 server and dial-up access for about 40 users, while a combined Web/FTP server was still expected to be completed within roughly a month. Commercial dial-up for private users followed on 29 February 1996.

- **.fo ccTLD:** Registered with IANA on 14 May 1993. Initially operated via UNI-C/Denmark; later transferred toward local control. Domain registration is not evidence of domestic connectivity or hosting.
- **19 January 1995 — external reachability:** NSRC records that `dk-gw.sleipnir.fo` (130.227.128.1) had propagated and was successfully pinged from Imperial College London via the JANET/EMPB/NORDUnet/DENet route. This proves a reachable gateway hostname, not a local web server.
- **25 January 1995 — service limitation:** UNI-C's Erik Lawaetz said the islands were connected but no mail-capable machines were running the last time he had checked. He named Petur Zachariassen and Jógvan Martin Grastein as technical contacts.
- **31 July 1995 — campus services:** The University reported the January 1995 leased line, about 100 campus PCs, shared SLEIPNIR mail, and roughly 40 dial-in users. A combined Web/FTP server was still being built and was expected within about a month. This is important context for the retrospective claim that a homepage was launched at Ólavsøka (28–29 July): the page may have been provisional or hosted elsewhere; the two sources do not resolve this.
- **End of 1995 / 29 February 1996 — commercial public access:** Faroese Telephone Company (Telefonverk Føroya Løgtings / TFL) planned private and commercial services by end of 1995; dial-up Internet formally available from 29 February 1996. Early subscriber counts were low (hundreds).

Primary contemporary source: Jogvan Martin Grastein (Netumsitingin / Fróðskaparsetur Føroya), letter to NSRC, 31 July 1995. https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO

## Personal web ecology / earliest candidates

No verified personal homepage identified. A 2008 university retrospective says the first Faroese homepage was set up at Ólavsøka 1995, but gives no operator, URL, or page type. The author Petur F. Zachariassen is likely the Petur Z who helped lead the January 1995 Internet rollout: a 1995 NSRC report names Petur Zachariassen as a technical contact, a 2005 Frøði profile gives the same `peturz` university email identity, and a 2015 university profile describes Petur Z as a pioneer of Faroese Internet access. This makes the retrospective more informed, but does not establish that Petur created the first page.

A contemporary 1996 Ariadne article by John Kirriemuir identifies the Faroese National Library's institutional homepage at `http://www.sleipnir.fo/flb/flbheim.htm` and its first Faroese Internet guide at `http://www.sleipnir.fo/flb/flbint.htm`. It also links to the university research page (`http://www.sleipnir.fo/research.htm`), the general Faroe information page (`http://www.sleipnir.fo/faroe/faroe.htm`) and the library information page (`http://www.sleipnir.fo/flb/flbst.htm`). These are institutional pages, not personal homepages; the article establishes existence by 1996 but not launch dates.

The Sosialurin archive has an issue dated 28 July 1995 (24 pages), exactly at the Ólavsøka period. Only the issue metadata and page-one thumbnail were accessible in this pass; full page images/OCR require a subscription, so no press confirmation was extracted. Later portals such as Faroenet hosted political and community content from 1997. `sleipnir.fo` was still active enough to be defaced in December 2000.

## Candidate register

```yaml
id: FO-01
status: candidate
person_or_project: University of the Faroe Islands / research institutions (SLEIPNIR)
title: Academic/research Internet connection and shared mail service
url_original: http://www.sleipnir.fo/
url_archived:
country_or_territory: Faroe Islands
connection_basis: local-hosting
medium: internet-access
activity_type: connectivity
operator_type: academic
network_status: internet
date_claimed: January 1995
date_type: inferred
date_precision: month
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO
    source_type: contemporary technical correspondence
    observed_date: 1995-07-31
    supports: 64 kbit/s leased line operational since January 1995; campus institutions connected; mail via SLEIPNIR; web/FTP server planned
    grade: A
author_attribution: Jogvan Martin Grastein / Petur Zachariassen (university)
language: English
notes: Distinguishes research/academic access from later commercial public service. No personal expression claim.
uncertainties: Exact first packet/email date in January; whether any public users existed before commercial launch; first web server launch date.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

```yaml
id: FO-02
status: candidate
person_or_project: Faroese Telephone Company (TFL / Telefonverk Føroya Løgtings)
title: Commercial dial-up Internet service launch
url_original:
url_archived:
country_or_territory: Faroe Islands
connection_basis: local-hosting
medium: internet-access
activity_type: service
operator_type: commercial
network_status: internet
date_claimed: 29 February 1996
date_type: inferred
date_precision: exact
evidence:
  - source_url: https://logir.fo/GetFile/law.aspx?objType=Law&objId=10104&objFormat=PDF
    source_type: official regulation (kunngerð)
    observed_date: 1996-02-16 (effective 1996-02-29)
    supports: telephone charges for dial-up Internet connections effective 29 February 1996
    grade: B
  - source_url: https://web.archive.org/web/20230401222240/https://www.faroeislands.fo/people-society/infrastructure/communication-infrastructure/
    source_type: retrospective official summary
    observed_date: 2023
    supports: dial-up began 1996 with ~400 early subscribers
    grade: C
author_attribution: institutional
language: Faroese / English
notes: Confirms transition from research-only to public commercial access. Does not establish personal pages.
uncertainties: Exact first private customer connection date; pricing and uptake details.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

```yaml
id: FO-03
status: lead
person_or_project: Unknown (claimed first Faroese homepage)
title: First Faroese homepage at Ólavsøka 1995
url_original: unknown (possibly on sleipnir.fo)
url_archived:
country_or_territory: Faroe Islands
connection_basis: other (retrospective national attribution; hosting unknown)
medium: website
activity_type: publishing
operator_type: unknown
network_status: unknown
date_claimed: 28–29 July 1995 (Ólavsøka)
date_type: inferred
date_precision: range
evidence:
  - source_url: https://www.setur.fo/fo/setrid/tidindi/vinir-tinir-eru-eisini-minir
    source_type: retrospective university note (2008)
    observed_date: 2008-06-17
    supports: claim that the first Faroese homepage was set up at Ólavsøka 1995
    grade: C
author_attribution: unknown; 2008 article byline Petur F. Zachariassen, likely the university network pioneer Petur Z but not conclusively matched to the 1995 contact
language: Faroese (source)
notes: The 2008 retrospective says a first Faroese homepage was set up at Ólavsøka 1995. It does not name the author/operator, give the URL, describe the content, or say whether it was personal or institutional. The 31 July 1995 NSRC report says the university's Web/FTP server was still being built and expected within about a month; the page may have been provisional or hosted elsewhere. The Sosialurin 28 July 1995 issue is a promising contemporary press target, but its OCR/full pages were not accessible in this pass.
uncertainties: Exact URL, launch day, author, hosting location, page type, and meaning of “first Faroese homepage”; no surviving capture or direct contemporary confirmation.
researcher: OpenAI GPT-6
last_checked: 2026-11-21
```


```yaml
id: FO-04
status: probable
person_or_project: Faroese National Library (Føroya Landsbókasavn / FLB)
title: Institutional homepage and first Faroese Internet guide
url_original: http://www.sleipnir.fo/flb/flbheim.htm
related_urls:
  - http://www.sleipnir.fo/flb/flbint.htm
  - http://www.sleipnir.fo/flb/flbst.htm
  - http://www.sleipnir.fo/research.htm
  - http://www.sleipnir.fo/faroe/faroe.htm
url_archived:
country_or_territory: Faroe Islands
connection_basis: other (published under sleipnir.fo; physical hosting location not independently established)
medium: website
activity_type: publishing
operator_type: institutional
network_status: internet
date_claimed: 1996
date_type: first-known-publication
date_precision: year
evidence:
  - source_url: https://www.ariadne.ac.uk/issue/2/faroe/
    source_type: contemporary library/internet journal article
    observed_date: 1996
    supports: FLB had its own homepage at flbheim.htm and published the first Faroese Internet guide at flbint.htm; article also identifies related university and general-information pages
    grade: B
author_attribution: institutional operator; article by John Kirriemuir
language: English (article); page language unknown
notes: The article says FLB had used the Internet since January 1995 and describes the homepage and guide as experimental. This verifies an institutional web presence by 1996, not its launch date and not a personal homepage. No original page capture recovered.
uncertainties: Exact publication month, page launch date, original page contents, physical hosting location, and whether the 1995 Ólavsøka homepage was a separate site.
researcher: OpenAI GPT-6
last_checked: 2026-11-21
```

## Gaps and next leads

- Follow the 1996 Ariadne page links and seek Wayback/Netarkivet captures of `sleipnir.fo` paths, especially `flbheim.htm`, `flbint.htm`, `research.htm` and `faroe.htm`. Public Wayback CDX access was unavailable in this pass; no capture status is inferred.
- Inspect the 28 July 1995 Sosialurin issue OCR/full pages (subscription currently required) and adjacent 27/29 July issues for `heimasíða`, `internet` and `netið`.
- Confirm the 2008 author Petur F. Zachariassen's identity against the 1995 `peturz@sleipnir.fo` technical contact; do not infer that he authored the first homepage.
- Confirm the Ólavsøka 1995 “first homepage” claim with primary sources (university records, contemporary press, or surviving files).
- Search Faroese-language newspapers (Sosialurin, Dimmalætting) and local terms (heimasíða, Internet, netið) for 1995–97 launch coverage.
- Inspect early institutional directories for personal pages or ~user directories.
- Check for any pre-1995 email/UUCP activity associated with Faroese researchers or the university.

## Bibliography

- Jogvan Martin Grastein, NSRC report, 31 July 1995. https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO
- IANA .fo delegation record (registration 14 May 1993). https://www.iana.org/domains/root/db/fo.html
- Faroese regulation on Internet telephone charges, effective 29 February 1996. https://logir.fo/GetFile/law.aspx?objType=Law&objId=10104&objFormat=PDF
- University of the Faroe Islands retrospective note on first homepage (17 June 2008). https://www.setur.fo/fo/setrid/tidindi/vinir-tinir-eru-eisini-minir
- Petur Z / university Internet pioneer profile (22 January 2015). https://www.setur.fo/fo/setrid/tidindi/petur-z-valt-at-gevast
- Frøði 1/2005 profile of Petur Zachariasen, including `peturz@setur.fo`. https://frodskaparfelag.fo/wp-content/uploads/frodi-2005-nummar-1.pdf
- NSRC, “FO update (1/95)” (25 January 1995). https://nsrc.org/db/lookup/report.php?fromISO=FO&id=890202445976:497434210
- NSRC, “Faroe Islands (FO) now with FI (1995.01.19)” (19 January 1995). https://nsrc.org/db/lookup/report.php?fromISO=FO&id=890202446086:497432752
- John Kirriemuir, “Down Your Very Long Way Away,” Ariadne, issue 2 (1996). https://www.ariadne.ac.uk/issue/2/faroe/
- Ariadne BibTeX citation metadata (author John Kirriemuir; year 1996). https://wvyw.ariadne.ac.uk/issue/2/faroe/citation.bibtex
- Sosialurin archive, issue 28 July 1995 (metadata; full pages subscription-gated). https://arkiv.sosialurin.fo/blad/1995-07-28
- Sosialurin archive, page 1 thumbnail for 28 July 1995. https://arkiv.sosialurin.fo/sida/169386
- Faroe Islands official communications history summary. https://web.archive.org/web/20230401222240/https://www.faroeislands.fo/people-society/infrastructure/communication-infrastructure/
- Attrition defacement notice for www.sleipnir.fo (Dec 2000). https://seclists.org/attrition-defaced/2000/Dec/88

**Researcher:** Grok / xAI  
**Last checked:** 2026-11-18
