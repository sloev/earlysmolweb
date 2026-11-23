# Faroe Islands (Føroyar)

**Status:** infrastructure candidates documented; probable institutional National Library web presence by 1996 with direct 1998 captures; institutional Sosialurin online daily from September 1997; first-homepage claim remains a lead. No verified personal homepage yet.
**Priority:** first wave (separate research jurisdiction within the Kingdom of Denmark).
**Last checked:** 2026-11-23

## Internet context

The Faroe Islands had no general commercial public Internet service before the mid-1990s, but academic and research institutions in Tórshavn were externally reachable by January 1995. A 19 January NSRC trace reached `dk-gw.sleipnir.fo` through Denmark; a 25 January update said the islands were connected but no mail-capable machines were yet running. By 31 July 1995, the university reported a shared SLEIPNIR SMTP/POP3 server and dial-up access for about 40 users, while a combined Web/FTP server was still expected to be completed within roughly a month. Commercial dial-up for private users followed on 29 February 1996.

- **.fo ccTLD:** Registered with IANA on 14 May 1993. Initially operated via UNI-C/Denmark; later transferred toward local control. Domain registration is not evidence of domestic connectivity or hosting.
- **19 January 1995 — external reachability:** NSRC records that `dk-gw.sleipnir.fo` (130.227.128.1) had propagated and was successfully pinged from Imperial College London via the JANET/EMPB/NORDUnet/DENet route. This proves a reachable gateway hostname, not a local web server.
- **25 January 1995 — service limitation:** UNI-C's Erik Lawaetz said the islands were connected but no mail-capable machines were running the last time he had checked. He named Petur Zachariassen and Jógvan Martin Grastein as technical contacts.
- **31 July 1995 — campus services:** The University reported the January 1995 leased line, about 100 campus PCs, shared SLEIPNIR mail, and roughly 40 dial-in users. A combined Web/FTP server was still being built and was expected within about a month. This is important context for the retrospective claim that a homepage was launched at Ólavsøka (28–29 July): the page may have been provisional or hosted elsewhere; the two sources do not resolve this.
- **End of 1995 / 29 February 1996 — commercial public access:** Faroese Telephone Company (Telefonverk Føroya Løgtings / TFL) planned private and commercial services by end of 1995; dial-up Internet formally available from 29 February 1996. Early subscriber counts were low (hundreds).

Primary contemporary source: Jogvan Martin Grastein (Netumsitingin / Fróðskaparsetur Føroya), letter to NSRC, 31 July 1995. https://nsrc.org/db/lookup/report.php?id=890202445799:497435668&fromISO=FO

## Personal web ecology / earliest candidates

No verified national-first personal homepage identified. FO-05 now documents a surviving Anfinn Frederiksen personal homepage: the 13 March 2007 Wayback capture names the page and shows Faroese photographs, while its timeline reports an earliest capture on 11 April 2000 (that 2000 capture remains uninspected). Its visitor counter claims “Since 08.01.1999,” which is not launch proof; the author's residence at publication is unknown. FO-03 remains a separate lead for the claimed Ólavsøka 1995 “first homepage”; no relationship between FO-03 and FO-05 is established. A 2008 university retrospective says the first Faroese homepage was set up at Ólavsøka 1995, but gives no operator, URL, or page type. The author Petur F. Zachariassen is likely the Petur Z who helped lead the January 1995 Internet rollout: a 1995 NSRC report names Petur Zachariassen as a technical contact, a 2005 Frøði profile gives the same `peturz` university email identity, and a 2015 university profile describes Petur Z as a pioneer of Faroese Internet access. This makes the retrospective more informed, but does not establish that Petur created the first page.

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
url_archived: https://web.archive.org/web/19981202051144/http://www.sleipnir.fo:80/flb/flbheim.htm
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
  - source_url: https://web.archive.org/web/19981202051144/http://www.sleipnir.fo:80/flb/flbheim.htm
    source_type: direct Wayback capture of National Library homepage
    observed_date: 1998-12-02
    supports: page identifies the National Library, its Tórshavn address, and links to staff and Internet-guide pages
    grade: A
  - source_url: https://web.archive.org/web/19981203001927/http://www.sleipnir.fo:80/flb/flbint.htm
    source_type: direct Wayback capture of Faroese Internet guide
    observed_date: 1998-12-03
    supports: institutional guide page titled Hin føroyska INTERNET-vegleiðingin; footer content date 20/6/96 (not a verified first-publication date)
    grade: A
  - source_url: https://web.archive.org/web/19981205060539/http://www.sleipnir.fo:80/flb/flbint3.htm
    source_type: direct Wayback capture of Internet search directory
    observed_date: 1998-12-05
    supports: library-curated Internet search tools and subject directory; footer content date 25/04-98 (not a verified first-publication date)
    grade: A
  - source_url: https://web.archive.org/web/19981202183057/http://www.sleipnir.fo:80/flb/staff.htm
    source_type: direct Wayback capture of institutional staff directory
    observed_date: 1998-12-02
    supports: staff directory page with footer content date 19/09/97; not a personal-homepage directory
    grade: A
author_attribution: institutional operator; article by John Kirriemuir
language: English (article); page language unknown
notes: The article says FLB had used the Internet since January 1995 and describes the homepage and guide as experimental. Direct Wayback captures now survive for the homepage (2 Dec 1998), staff directory (2 Dec 1998; footer 19/09/97), Internet guide (3 Dec 1998; footer 20/6/96), and Internet search directory (5 Dec 1998; footer 25/04-98). These footer dates are content dates, not independently verified first-publication dates. This is institutional web publishing, not a personal homepage.
uncertainties: Exact publication month, page launch date, original page contents, physical hosting location, and whether the 1995 Ólavsøka homepage was a separate site.
researcher: OpenAI GPT-6
last_checked: 2026-11-21
```



## 23 November 2026 — Olivant personal-homepage infrastructure and named page leads

### FO-05 — Anfinn Frederiksen's Olivant personal homepage (candidate)

A direct Wayback capture dated **13 March 2007** identifies the page as “Anfinn Frederiksen's homepage” and says, “Welcome to a homepage with pictures of the Faroe Islands!” The capture page's Wayback timeline reports **140 captures from 11 April 2000 to 21 July 2020**; the 11 April 2000 capture itself was not inspected, so this is the earliest archive-capture date currently reported, not a verified launch date. The page's visitor counter says “Since 08.01.1999”; this is a page statement, not reliable proof of site creation. A subpage captured 11 March 2007 is a gallery of Mykines photographs and links back to the homepage. A 2002 forum post and ALT.FO directory independently point to the same Olivant user account; the page itself names Anfinn Frederiksen, while ALT.FO spells Fredriksen. This is a candidate personal homepage associated with the Faroes through local Olivant user hosting and Faroese content. Residence at publication remains unknown; no national-first claim is made.

```yaml
id: FO-05
status: candidate
person_or_project: Anfinn Frederiksen (named in archived homepage title; ALT.FO spelling variant Fredriksen)
title: Personal homepage with Faroese photographs and a Mykines gallery
url_original: http://heima.olivant.fo/~anfinn/index.htm
url_archived: https://web.archive.org/web/20070313154305/http://heima.olivant.fo:80/%7Eanfinn/index.htm
country_or_territory: Faroe Islands
connection_basis: local-hosting
medium: website
activity_type: personal-expression
operator_type: individual
network_status: internet
date_claimed: 2000-04-11 (earliest Wayback capture date reported; capture itself not inspected)
date_type: first-capture
date_precision: exact
evidence:
  - source_url: https://web.archive.org/web/20070313154305/http://heima.olivant.fo:80/%7Eanfinn/index.htm
    source_type: direct Wayback capture of homepage
    observed_date: 2007-03-13
    supports: page title names Anfinn Frederiksen; identifies itself as a homepage with pictures of the Faroe Islands; visitor counter says “Since 08.01.1999”
    grade: A
  - source_url: https://web.archive.org/web/20070313154305/http://heima.olivant.fo:80/%7Eanfinn/index.htm
    source_type: Wayback capture timeline metadata
    observed_date: 2007-03-13
    supports: reports 140 captures from 2000-04-11 to 2020-07-21; 2000 capture content not inspected
    grade: A
  - source_url: https://web.archive.org/web/20070311041954/http://heima.olivant.fo:80/%7Eanfinn/mykines.htm
    source_type: direct Wayback capture of photo-gallery subpage
    observed_date: 2007-03-11
    supports: identifies the same homepage and describes pictures of the island Mykines; links back to index
    grade: A
  - source_url: https://forum.index.hu/Article/showArticle?na_order=&na_start=268&na_step=30&t=9019233
    source_type: contemporary external discussion forum
    observed_date: 2002-12-15
    supports: links the exact Olivant user URL under “Csodaszép légifotók” among Faroese websites
    grade: B
  - source_url: https://www.alt.fo/
    source_type: Faroese link directory (undated; accessed 2026-11-23)
    observed_date: unknown
    supports: labels the same URL “Anfinn Fredriksen” in the “Myndir” category
    grade: C
  - source_url: https://brattaberg.com/
    source_type: current photography website (accessed 2026-11-23)
    observed_date: current
    supports: credits photographs to Anfinn Fredriksen; does not independently prove the old page's account holder
    grade: C
author_attribution: Anfinn Frederiksen (named on the archived page; exact account holder probable)
language: English (captured page text)
notes: The 2000-04-11 date is Wayback timeline metadata only; that capture was not opened. The counter's “Since 08.01.1999” is not independently verified as a site launch date. Country attribution rests on Olivant local user hosting and Faroese subject matter; author residence at publication is unknown.
uncertainties: Content of 2000 capture; original page launch date; exact account holder; author residence in 2000; whether an earlier Faroese personal homepage existed.
researcher: OpenAI GPT-6
last_checked: 2026-11-23
```

### FO-06 — Føroya Tele/Internet (Olivant) self-service homepage publishing (candidate service record)

The Wayback capture of the `www.internet.fo` homepage dated **5 April 2001** identifies the provider as “The Faroe Islands - Internet Service Provider”, links to a guide titled “Hvussu gerði eg eina heimasíðu” (“How do I make a homepage”), and carries the footer copyright “© 2001 Føroya Tele/Internet”. The linked guide, captured **22 August 2001**, is titled “Leiðbeining - Ger tína egnu heimasíðu” (“Guide — Make your own homepage”). It tells customers how to edit their own page with Netscape Navigator Gold 3 and upload it by FTP to `ftp://heima.olivant.fo/home/<username>/public_html`; its footer is “© 2000 Føroya Tele/Internet”. A separate webhotel price page captured **8 June 2001** describes paid hosting for commercial websites, distinguishing that business service from the personal-user-page instructions.

This directly documents a customer-operated homepage service by 2001. The guide's 2000 copyright is a clue, not proof that the service began in 2000. This is ISP infrastructure, not a personal website or evidence of the first customer page.

```yaml
id: FO-06
status: candidate
person_or_project: Føroya Tele/Internet (Olivant)
title: Self-service customer homepage publishing and hosting
url_original: http://www.internet.fo/leidbeining/gerheimasida.html
url_archived: https://web.archive.org/web/20010822082704/http://www.internet.fo/leidbeining/gerheimasida.html
country_or_territory: Faroe Islands
connection_basis: local-hosting
medium: website
activity_type: service
operator_type: commercial
network_status: internet
date_claimed: 2001-04-05 (provider homepage advertises the guide by this capture)
date_type: first-capture
date_precision: exact
evidence:
  - source_url: https://web.archive.org/web/20010405065408/http://www.internet.fo/
    source_type: Wayback capture of ISP homepage
    observed_date: 2001-04-05
    supports: identifies the Faroe Islands Internet Service Provider, lists the homepage-making guide, and shows © 2001 Føroya Tele/Internet
    grade: A
  - source_url: https://web.archive.org/web/20010822082704/http://www.internet.fo/leidbeining/gerheimasida.html
    source_type: Wayback capture of ISP user guide
    observed_date: 2001-08-22
    supports: gives instructions for creating and FTP-uploading a personal page to heima.olivant.fo/home/<username>/public_html; footer copyright © 2000 Føroya Tele/Internet
    grade: A
  - source_url: https://web.archive.org/web/20010608053345/http://www.internet.fo/tanastur/prisirwebhotel.html
    source_type: Wayback capture of ISP webhotel service page
    observed_date: 2001-06-08
    supports: describes a separate paid webhotel service for commercial websites
    grade: A
author_attribution: Føroya Tele/Internet as service operator; no individual page author
language: Faroese
notes: This is provider infrastructure and a publishing service, not a personal site. The 2000 copyright does not establish the service's launch date. The guide is captured in August 2001, while the provider homepage already advertises it in April 2001.
uncertainties: Actual service launch date; number and identity of early customer pages; first individual page; whether earlier user-page captures survive.
researcher: OpenAI GPT-6
last_checked: 2026-11-23
```

### FO-07 — “Privatar-heimasidur” private-homepage directory (lead)

ALT.FO lists `http://heima.olivant.fo/~sonjacob/Farpages/Privatar-heimasidur.htm` under “Føroya best umtøktu heimasíður” (most visited Faroese homepages) and labels it “Privatar-heimasidur” (“private homepages”). The original page is not accessible through this route, and the directory is undated. It may preserve links to multiple individual Olivant pages, so it is a high-value discovery route, not yet evidence for any particular site's date or author.

```yaml
id: FO-07
status: lead
person_or_project: Unknown maintainer; Olivant account path ~sonjacob
title: Privatar-heimasidur (private homepages directory)
url_original: http://heima.olivant.fo/~sonjacob/Farpages/Privatar-heimasidur.htm
url_archived: unknown
country_or_territory: Faroe Islands
connection_basis: local-hosting
medium: website
activity_type: publishing
operator_type: unknown
network_status: internet
date_claimed: unknown
date_type: inferred
date_precision: unknown
evidence:
  - source_url: https://www.alt.fo/
    source_type: Faroese link directory (undated; accessed 2026-11-23)
    observed_date: unknown
    supports: lists the exact URL and labels it “Privatar-heimasidur”
    grade: C
author_attribution: unknown
language: Faroese
notes: The title suggests a directory of private homepages, but its contents have not been recovered. ALT.FO also lists other Olivant user pages, including ~hans, ~mykines and ~dholm; these are separate leads, not dated page evidence.
uncertainties: Directory creation date; maintainer identity; contents; dates and authors of linked pages; authors' residence at publication.
researcher: OpenAI GPT-6
last_checked: 2026-11-23
```

The local directory ALT.FO also links to `http://heima.olivant.fo/~hans/`, `http://heima.olivant.fo/~mykines/indexfo.htm` and `http://heima.olivant.fo/~dholm/foroyski.htm`. These remain undated leads. The next pass should recover the `~sonjacob` directory and sample user pages through the Faroese National Library Web Archive or Internet Archive captures, then identify each author and residence separately.

## Gaps and next leads

- Follow the 1996 Ariadne page links and seek Wayback/Netarkivet captures of `sleipnir.fo` paths, especially `flbheim.htm`, `flbint.htm`, `research.htm` and `faroe.htm`. Public Wayback CDX access was unavailable in this pass; no capture status is inferred.
- Inspect the 28 July 1995 Sosialurin issue OCR/full pages (subscription currently required) and adjacent 27/29 July issues for `heimasíða`, `internet` and `netið`.
- Confirm the 2008 author Petur F. Zachariassen's identity against the 1995 `peturz@sleipnir.fo` technical contact; do not infer that he authored the first homepage.
- Confirm the Ólavsøka 1995 “first homepage” claim with primary sources (university records, contemporary press, or surviving files).
- Search Faroese-language newspapers (Sosialurin, Dimmalætting) and local terms (heimasíða, Internet, netið) for 1995–97 launch coverage.
- Inspect early institutional directories for personal pages or ~user directories.
- Inspect the 11 April 2000 Wayback capture of the Anfinn Frederiksen homepage if the archive exposes the original image; verify the account holder and any evidence of the author's residence at publication.
- Check for any pre-1995 email/UUCP activity associated with Faroese researchers or the university.


## 21 November 2026 follow-up

A bounded follow-up searched Faroese and English variants around `heimasíða`, `internet`, `netið`, `Ólavsøka 1995`, Petur F. Zachariassen, and `sleipnir.fo`. It also tried Wayback CDX lookups for the known National Library paths `/flb/flbheim.htm`, `/flb/flbint.htm`, and the wider `www.sleipnir.fo/*` pattern. No new contemporary source, author attribution, original homepage URL, or usable archive record was recovered through this access route. The failed/unusable CDX responses are an access limitation, not evidence that no captures exist.

Existing classifications remain unchanged: FO-03 is a lead for the reported Ólavsøka 1995 homepage; FO-04 remains a probable institutional National Library homepage/guide by 1996. No personal homepage is verified, and no exhaustion claim is made. The next high-value work remains access to the full 28 July 1995 *Sosialurin* issue and recovery of the original `sleipnir.fo` pages through Netarkivet or a working Wayback interface.

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
**Last checked:** 2026-11-21


## 2026-11-21 — contemporary newspaper evidence and archive access route

A fresh search located a contemporary Faroese newspaper article that sharpens the online-publication chronology. Jan Müller, “Meet me on my homepage?!”, published by Sosialurin on **5 July 1998**, says that the paper had been updated on the Internet every day since **4 September 1997**, with about 5,000 articles then available, and gives the address www.sosialurin.fo. The article describes the newspaper's online edition and its service to Faroese readers abroad. This is direct contemporary evidence for an institutional online newspaper, not a personal homepage and not evidence of the first Faroese website.

Source: https://in.fo/grein/meet-me-on-my-homepage (accessed 21 November 2026; by Jan Müller; page lines 30–48 in the accessible rendering).

A previously inaccessible research route is now available: the public Sosialurin archive lists 255,877 pages from 11,146 issues (1927–2020), and exposes the complete issue index for **28 July 1995** (24 pages) with individual OCR page links. Issue: https://arkiv.sosialurin.fo/blad/1995-07-28 ; year index: https://arkiv.sosialurin.fo/ar/1995 . The issue was opened, but its 24 page OCR entries were not yet individually inspected in this pass. The archive notes that OCR is imperfect and full-size page images/PDFs require a subscription; do not treat OCR absence as evidence of absence.

The Faroese National Library's current guidance states that its Web Archive contains legally deposited Faroese .fo sites and selected other domains, but is not open access; researchers must apply. Its Faroese-language Netsavnið guidance separately points to a public Internet Archive capture of the National Library's 1990s homepage dated **2 December 1998**: https://web.archive.org/web/19981202051144/www.sleipnir.fo/flb/flbheim.htm . This is a concrete capture to inspect, but it is an institutional page and its 1998 capture does not establish its launch date.

Sources: https://landsbokasavnid.fo/fao-web-archive?_l=en ; https://landsbokasavnid.fo/netsavnid?_l=fo (accessed 21 November 2026).

**Assessment:** add a distinct institutional newspaper milestone (online daily since 4 September 1997; observed in a 5 July 1998 contemporary account). FO-03 remains a lead; no personal homepage is verified. The 28 July 1995 newspaper issue is now accessible at issue/OCR-link level, but no page content has yet been transcribed. The National Library capture is a 1998 institutional-page lead, not evidence for the claimed first homepage in July 1995.

**Next:** inspect the 24 OCR pages for references to Internet, heimasíða, telda, SLEIPNIR and the university; compare OCR with full-page scans where subscription access permits. Inspect the 1998 flbheim.htm capture and request access to the Faroese Web Archive for relevant 1995–1998 .fo captures. Keep institutional and personal milestones separate.


## 22 November 2026 — direct National Library captures; clarify the 1995 newspaper paywall

This pass followed the National Library's public Netsavnið link to its 1990s homepage and inspected the linked Wayback pages. The captures provide direct evidence of an institutional Faroese web presence and recover several original page paths:

- **Homepage:** https://web.archive.org/web/19981202051144/http://www.sleipnir.fo:80/flb/flbheim.htm (capture 2 December 1998). The page identifies Føroya Landsbókasavn / the National Library of the Faroe Islands, gives its Tórshavn address, and links to the staff directory and Faroese Internet guide.
- **Staff directory:** https://web.archive.org/web/19981202183057/http://www.sleipnir.fo:80/flb/staff.htm (capture 2 December 1998). Its footer reads 19/09/97. This is a page-content date, not an archive capture from 1997 and not proof of first publication. The directory is institutional; its staff/contact details are not reproduced here.
- **Faroese Internet guide:** https://web.archive.org/web/19981203001927/http://www.sleipnir.fo:80/flb/flbint.htm (capture 3 December 1998). The page title is “Hin føroyska INTERNET-vegleiðingin” and its footer reads 20/6/96. The footer is a useful 1996 content-date clue, but not independently a first-publication date. John Kirriemuir's contemporary 1996 Ariadne article independently identifies the library homepage and Internet guide.
- **Internet search directory:** https://web.archive.org/web/19981205060539/http://www.sleipnir.fo:80/flb/flbint3.htm (capture 5 December 1998). It is a library-curated directory of Internet search tools and subject links; its footer reads 25/04-98, again a content date rather than a verified launch date.

This strengthens FO-04 as a probable institutional homepage/guide with direct surviving captures. It does not identify the operator of the claimed Ólavsøka 1995 homepage, and none of these pages is evidence of a personal homepage.

**Correction/qualification for the 28 July 1995 Sosialurin issue:** the issue index is public and lists 24 pages with links labelled “síða N OCR”, but the page-1 access notice explicitly says that page text, full-size page images and the PDF are for subscribers; only search and issue browsing are open to everyone. Page 1: https://arkiv.sosialurin.fo/sida/169386 . I opened the issue index and tested the page-1 link; no OCR text or full-size scan was accessible through this route, and no newspaper content was transcribed. The previous note's reference to individual OCR links describes the visible navigation labels, not publicly readable OCR. Searches for Faroese terms (heimasíða, Internet, netið) did not surface a relevant 1995 item in the accessible web results.

**Assessment:** FO-03 remains a lead; FO-04 remains probable and is now backed by direct 1998 captures plus the contemporary 1996 Ariadne reference. No personal homepage or national-first claim is verified.

**Next:** request access to the National Library's restricted Web Archive for 1995–1998 .fo captures; obtain subscriber/library access to the full 27–29 July 1995 Sosialurin issues; continue searching university, staff and personal-page namespaces for a named individual homepage.

- Wayback capture, Føroya Landsbókasavn homepage, 2 December 1998: https://web.archive.org/web/19981202051144/http://www.sleipnir.fo:80/flb/flbheim.htm
- Wayback capture, FLB staff directory, 2 December 1998 (footer 19/09/97): https://web.archive.org/web/19981202183057/http://www.sleipnir.fo:80/flb/staff.htm
- Wayback capture, Hin føroyska Internet-vegleiðingin, 3 December 1998 (footer 20/6/96): https://web.archive.org/web/19981203001927/http://www.sleipnir.fo:80/flb/flbint.htm
- Wayback capture, FLB Internet search directory, 5 December 1998 (footer 25/04-98): https://web.archive.org/web/19981205060539/http://www.sleipnir.fo:80/flb/flbint3.htm
