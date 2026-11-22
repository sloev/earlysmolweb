# Federated States of Micronesia — early internet activity, networks, and web research

**Status:** active; connectivity candidates plus January 1997 directory-listed government, educational and individual-hosted page leads recorded; no earliest-personal-page candidate verified.  
**Focus:** locate personal pages made possible by early commercial dial-up and institutional connectivity in the mid-to-late 1990s; distinguish resident authors from diaspora or external hosts.\n**Last checked:** 2026-11-22

## Early connectivity and ISP context (not personal-page evidence)

### 1995 — medical email precursor in Yap
A 2000 peer-reviewed telemedicine account reports that, approximately four years earlier, the Yap State Department of Health Service arranged local access (medical use only) via Continental Airlines trunk lines to CompuServe at 300 bps. FSM TeleCom provided this free service. It enabled text-based email between Yap State Hospital staff and external consultants. This is a specialized email route, not public Internet access or web publishing.

- Source: Rutstein D., “Telemedicine in the Federated States of Micronesia,” *Pacific Health Dialog* 7(2), 2000 (PubMed abstract and full-text excerpts): https://pubmed.ncbi.nlm.nih.gov/11588919/
- Evidence grade: **B** (near-contemporary professional account).

### March 1996 — commercial ISP service begins in Yap
The same telemedicine paper states that in March 1996 FSM TeleCom became a full-scale commercial Internet Service Provider in Yap, with reasonable rates; the limited CompuServe medical access was phased out. Full Internet service then supported email attachments, literature search, image transmission, and real-time teleconferencing.

- Source: same Rutstein 2000 account.
- Evidence grade: **B**.

### November 1996 – February 1997 — national dial-up service and named web host
Primary NSRC records establish public reachability and operator-reported service details:

- 4 November 1996: Olivier MJ Crepin-Leblond traceroute from the UK to www.telecom.fm (resolving to 206.49.89.8), 18 hops, final probes ~708–738 ms. Title: “First Ping FM - Micronesia on line (1996.11.04)”.
- 17 November 1996: Robert H. Blissmer (FSM Telecom) reports Windows NT-based system with IIS, three PCs running DNS/Web/Mail/News servers, dial-in access to customers in Kosrae, Chuuk, Pohnpei and Yap, 128 kbps Sprint link Pohnpei to Stockton CA, and invites visitors to http://www.fm.
- 28 February 1997: Blissmer reports 280 dial-up subscribers as of 25 February 1997 (no dedicated-line customers), pricing US$19.95 startup + US$19.95/month for 5 hours then US$1.95/hour, estimated dedicated 64 kbps ≈ US$4,625/month.

- Sources:
  - NSRC First Ping FM, 4 Nov 1996: https://nsrc.org/db/lookup/report.php?id=890202503340:497431180&fromISO=FM
  - NSRC Micronesia Connectivity Update (11/96), 17 Nov 1996: https://nsrc.org/db/lookup/report.php?fromISO=FM&id=890202503239:497432694
  - NSRC FSM Connectivity in Micronesia (2/97), 28 Feb 1997: https://nsrc.org/db/lookup/report.php?fromISO=FM&id=890202503125:497434014
- Evidence grade: **A** (contemporary operator reports and traceroute preserved by NSRC).

### Domain registration
IANA root-whois and delegation records confirm `.fm` was created/delegated on 19 April 1995, with FSM Telecommunications Corporation as the sponsoring organisation. This is an infrastructure milestone only; it does not establish operational IP service or local hosting.

- Source: IANA .fm delegation (created 1995-04-19): https://www.iana.org/domains/root/db/.fm.html (and whois.iana.org).
- Evidence grade: **A** for the delegation date.

## January 1997 Pacific Society directory leads

Mark C. Goniwiecha's “Guam & Micronesia in Cyberspace,” *Journal of the Pacific Society*, January 1997, lists several FSM-associated pages under “Internet Resources and Home Pages”. These are dated directory references, not page launch dates; no original page content or Wayback capture was recovered in this pass.

- **Federated States of Micronesia Government** — http://fsmgov.org
- **Federated States of Micronesia Information** — http://fsmgov.org/info.html
- **College of Micronesia, Pohnpei, FSM** — http://ourworld.compuserve.com/homepages/danaleeling/comsci.htm. The URL path is an individual CompuServe homepages account, so this may be a student/staff or personal page associated with the college; the directory label alone does not establish an official college site or identify the author.
- **Micronesian Seminar, Pohnpei, FSM** — http://microstate.com/micsem
- **Ponape Agriculture and Trade School, Pohnpei, FSM** — http://pats.edu
- **Chuuk Visitors Bureau, Chuuk, FSM** — http://www.divetravel.com/c-chuuk.html

The article's list mixes personal pages with government, academic, commercial, community and regional resources. The titles above support a country/place association, but do not establish the author's residence, local hosting, or exact operator. The College of Micronesia CompuServe path is the most promising individual-hosted lead; it remains unclassified until the page is recovered.

Source: Mark C. Goniwiecha, “Guam & Micronesia in Cyberspace,” *Journal of the Pacific Society*, January 1997, printed pp. 119–120 / PDF pp. 3–5, ERIC ED 437 020: https://files.eric.ed.gov/fulltext/ED437020.pdf (accessed 22 November 2026).

```yaml
id: FM-03
status: lead
person_or_project: Federated States of Micronesia Government / FSM Information
title: Government and country-information pages
url_original: http://fsmgov.org
related_urls:
  - http://fsmgov.org/info.html
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: website
activity_type: publishing
operator_type: government
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: lists “Federated States of Micronesia Government” and “Federated States of Micronesia Information” with URLs
    grade: B
author_attribution: institutional attribution in directory; no individual author identified
language: unknown
notes: The directory title identifies a government page, but the page itself was not recovered; exact operator, content and hosting location remain unverified. Not personal expression.
uncertainties: Original page content; precise government office/operator; launch date; physical hosting; earliest capture.
researcher: OpenAI GPT-6
last_checked: 2026-11-22
```

```yaml
id: FM-04
status: lead
person_or_project: Unknown operator associated with College of Micronesia, Pohnpei
title: College of Micronesia page on a CompuServe personal-homepage path
url_original: http://ourworld.compuserve.com/homepages/danaleeling/comsci.htm
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: website
activity_type: publishing
operator_type: unknown
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: lists “College of Micronesia, Pohnpei, FSM” and a CompuServe homepages URL
    grade: B
author_attribution: unknown; URL path contains “danaleeling” but no person identity is independently established
language: unknown
notes: The URL path suggests an individual CompuServe account, making this a promising student/staff/personal-page lead. The directory's College of Micronesia label does not prove that the page was an official college site or that its author lived in Pohnpei.
uncertainties: Page content; author identity and residence; whether author was a student/staff member; page genre; launch date; earliest capture.
researcher: OpenAI GPT-6
last_checked: 2026-11-22
```

```yaml
id: FM-05
status: lead
person_or_project: Micronesian Seminar, Pohnpei
title: Micronesian Seminar website
url_original: http://microstate.com/micsem
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: website
activity_type: publishing
operator_type: institutional
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: lists “Micronesian Seminar, Pohnpei, FSM” and its URL
    grade: B
author_attribution: institutional attribution in directory; no individual author identified
language: unknown
notes: Institution and Pohnpei association are supplied by the directory title. Physical hosting and original page content are unknown. Not personal expression.
uncertainties: Original content; exact operator; local hosting; launch date; archive captures.
researcher: OpenAI GPT-6
last_checked: 2026-11-22
```

```yaml
id: FM-06
status: lead
person_or_project: Ponape Agriculture and Trade School, Pohnpei
title: Ponape Agriculture and Trade School website
url_original: http://pats.edu
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: website
activity_type: publishing
operator_type: institutional
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: lists “Ponape Agriculture and Trade School, Pohnpei, FSM” and its URL
    grade: B
author_attribution: institutional attribution in directory; no individual author identified
language: unknown
notes: Institutional listing only; the original page and physical hosting location were not recovered. Not personal expression.
uncertainties: Original content; exact operator; launch date; earliest capture.
researcher: OpenAI GPT-6
last_checked: 2026-11-22
```

```yaml
id: FM-07
status: lead
person_or_project: Unknown operator; Chuuk Visitors Bureau page
title: Chuuk Visitors Bureau, Chuuk, FSM
url_original: http://www.divetravel.com/c-chuuk.html
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: website
activity_type: publishing
operator_type: unknown
network_status: internet
date_claimed: 1997-01 (contemporary directory listing; launch date unknown)
date_type: inferred
date_precision: month
evidence:
  - source_url: https://files.eric.ed.gov/fulltext/ED437020.pdf
    source_type: contemporary Internet-resources directory in Journal of the Pacific Society
    observed_date: 1997-01
    supports: lists “Chuuk Visitors Bureau, Chuuk, FSM” and its URL
    grade: B
author_attribution: unknown; directory label identifies the bureau but not the page operator
language: unknown
notes: Hosted under divetravel.com rather than an .fm domain; the directory label does not prove the bureau itself maintained the page or that it was locally hosted. Not personal expression.
uncertainties: Original content; operator/sponsorship; launch date; physical hosting; archive captures.
researcher: OpenAI GPT-6
last_checked: 2026-11-22
```

## Structured candidates

```yaml
id: FM-01
status: candidate
person_or_project: FSM Telecommunications Corporation (FSMTC) national dial-up and IP hosts
title: First known public IP reachability and commercial dial-up Internet service
url_original: http://www.telecom.fm/ and http://www.fm/
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: local-hosting
medium: internet-access
activity_type: connectivity
operator_type: commercial
network_status: internet
date_claimed: 1996-11-04
date_type: first-capture
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202503340:497431180&fromISO=FM
    source_type: contemporary traceroute / NSRC report
    observed_date: 1996-11-04
    supports: public reachability of www.telecom.fm (206.49.89.8)
    grade: A
  - source_url: https://nsrc.org/db/lookup/report.php?fromISO=FM&id=890202503125:497434014
    source_type: contemporary operator report
    observed_date: 1997-02-28
    supports: 280 dial-up customers, service scope across four states, pricing
    grade: A
author_attribution: FSM Telecommunications Corporation (operator); Olivier MJ Crepin-Leblond (traceroute)
language: en
notes: Traceroute confirms external reachability on 4 Nov 1996. Operator statements describe dial-up service covering all four states by mid-November 1996 and 280 subscribers by late February 1997. Exact first customer dial-up date and continuous operation not fully established. No dedicated-line customers reported in Feb 1997.
uncertainties: Precise start of commercial service in each state; whether the 4 Nov 1996 host was the first operational IP host; location of the Sprint landing and any intermediate gateways.
researcher: Grok (xAI)
last_checked: 2026-11-17
```

```yaml
id: FM-02
status: candidate
person_or_project: .fm ccTLD delegation
title: Domain infrastructure milestone
url_original: unknown
url_archived: unknown
country_or_territory: Federated States of Micronesia
connection_basis: other
medium: infrastructure
activity_type: infrastructure
operator_type: commercial
network_status: internet
date_claimed: 1995-04-19
date_type: inferred
date_precision: exact
evidence:
  - source_url: https://www.iana.org/domains/root/db/.fm.html
    source_type: IANA root-whois / delegation record
    observed_date: 2026-11-17
    supports: creation date of .fm zone
    grade: A
author_attribution: IANA / FSM Telecommunications Corporation
language: en
notes: Delegation date only. Does not prove operational DNS service, local hosting, or any public website at that date. .fm later became widely used for radio/podcast branding outside the FSM.
uncertainties: Exact first nameserver operational date; whether any second-level domains were registered or resolving in 1995–96.
researcher: Grok (xAI)
last_checked: 2026-11-17
```

## Research interpretation

- The 1995 domain delegation and 1996–97 dial-up/IP milestones establish a clear window for possible personal expression, but no named individual personal homepage has yet been identified.
- `www.telecom.fm` and `www.fm` are institutional/provider hosts, not personal pages; they are useful discovery leads for any linked user directories or early pages.
- Search for terms such as “home page”, “personal page”, “my page”, local names, and early `.fm` user paths; also check external hosts used by FSM residents.
- Distinguish resident authors from diaspora or temporary external hosting.

## Next actions

1. Recover any surviving Wayback or other captures of `www.telecom.fm`, `www.fm`, or early `.fm` hosts from 1996–1999 and inspect for personal links or directories.
3. Seek contemporary FSM Telecom user directories, local newspaper mentions (e.g., Kaselehlie Press), or university/staff pages.
4. Locate any pre-1996 email/UUCP or academic network activity.
5. Continue parallel Pacific scouting and first-wave items.

**Personal-homepage status:** none verified. Infrastructure and commercial dial-up window opens 1996.

- Mark C. Goniwiecha, “Guam & Micronesia in Cyberspace,” *Journal of the Pacific Society*, January 1997, ERIC ED 437 020 (FSM-associated entries on printed pp. 119–120 / PDF pp. 3–5): https://files.eric.ed.gov/fulltext/ED437020.pdf
