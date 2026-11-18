# Faroe Islands (Føroyar)

**Status:** infrastructure candidates documented (Track B); personal-page leads open (Track A). No verified personal homepage yet.
**Priority:** first wave (separate research jurisdiction within the Kingdom of Denmark).
**Last checked:** 2026-11-18

## Internet context

The Faroe Islands had no public Internet service before the mid-1990s. Academic and research institutions in Tórshavn gained direct connectivity in January 1995 via a 64 kbit/s leased line to UNI-C in Lyngby, Denmark, routed over the CANTAT-3 cable. Mail was handled on a shared server (sleipnir.fo). Commercial dial-up for private users followed in early 1996.

- **.fo ccTLD:** Registered with IANA on 14 May 1993. Initially operated via UNI-C/Denmark; later transferred toward local control. Domain registration is not evidence of domestic connectivity or hosting.
- **January 1995 — academic/research connection:** University of the Faroe Islands (Fróðskaparsetur Føroya) and nearby research institutions (National Library, museums, archives, fisheries labs, etc.) connected. About 100 PCs on campus; dial-in modem access for ~40 users via SLEIPNIR POP3. Planning for local DNS, web and FTP server underway by July 1995.
- **End of 1995 / 29 February 1996 — commercial public access:** Faroese Telephone Company (Telefonverk Føroya Løgtings / TFL) planned private and commercial services by end of 1995; dial-up Internet formally available from 29 February 1996. Early subscriber counts were low (hundreds).

Primary contemporary source: Jogvan Martin Grastein (Netumsitingin / Fróðskaparsetur Føroya), letter to NSRC, 31 July 1995. https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO

## Personal web ecology / earliest candidates

No verified personal homepages identified yet. A retrospective university note (2008) states that the first Faroese homepage was set up at Ólavsøka 1995 (national holiday period around 28–29 July). This remains a lead pending primary confirmation. Institutional pages (e.g., National Library at http://www.sleipnir.fo/flb/flbheim.htm) existed by 1996. Later portals such as Faroenet (www.faroenet.fo) hosted political and community content from 1997.

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

## Gaps and next leads

- Recover any 1995–96 captures of sleipnir.fo or early .fo sites (Wayback, Netarkivet, local archives).
- Confirm the Ólavsøka 1995 “first homepage” claim with primary sources (university records, contemporary press, or surviving files).
- Search Faroese-language newspapers (Sosialurin, Dimmalætting) and local terms (heimasíða, Internet, netið) for 1995–97 launch coverage.
- Inspect early institutional directories for personal pages or ~user directories.
- Check for any pre-1995 email/UUCP activity associated with Faroese researchers or the university.

## Bibliography

- Jogvan Martin Grastein, NSRC report, 31 July 1995. https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO
- IANA .fo delegation record (registration 14 May 1993). https://www.iana.org/domains/root/db/fo.html
- Faroese regulation on Internet telephone charges, effective 29 February 1996. https://logir.fo/GetFile/law.aspx?objType=Law&objId=10104&objFormat=PDF
- University of the Faroe Islands retrospective note on first homepage (2008). https://www.setur.fo/fo/setrid/tidindi/vinir-tinir-eru-eisini-minir
- Faroe Islands official communications history summary. https://web.archive.org/web/20230401222240/https://www.faroeislands.fo/people-society/infrastructure/communication-infrastructure/

**Researcher:** Grok / xAI  
**Last checked:** 2026-11-18
