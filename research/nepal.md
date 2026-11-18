# Nepal — early internet activity

**Status:** scouting (1993–94 RONAST/ERNET scientific email documented with conflicting start years; 1994 commercial store-and-forward email by Mercantile; 25 January 1995 .np delegation; mid-July 1995 continuous international IP link and first commercial ISP by Mercantile; WorldLink UUCP email October 1995; early external-hosted newspaper content September 1995; no verified resident personal homepage yet)

## Internet context

- **Scientific email (RONAST / ERNET):** Royal Nepal Academy of Science and Technology (RONAST) operated a scheduled dial-up relay to India’s Education and Research Network (ERNET) at IIT Bombay for scientific correspondence. Secondary accounts (NTA convergence study, Montgomery 2002) place the arrangement in 1993; Mercantile co-founder S. Rajbhandari (later NAST-hosted presentation) recalls experimental service beginning in 1994 via New Delhi. Service was store-and-forward, not continuous IP. Grade B/C (contemporary character clear; exact opening year unresolved).
- **Commercial email (Mercantile Office Systems / MOS), 1994:** After the RONAST project, MOS commercialised store-and-forward email with an upstream link to Australia (connect.com.au). Server exchanged messages several times daily. Customers mainly international organisations. NTA study dates commercial email to June 1994. Grade B (multiple secondary and institutional accounts).
- **.np ccTLD:** Delegated 25 January 1995 to Mercantile Communications Pvt. Ltd. (IANA record; grade A for DNS only). Registry site mos.com.np. Early domains included mos.com.np (registered ~June 1995).
- **First continuous commercial IP / ISP (Mercantile), mid-July 1995:** Mercantile established an online international link via Nepal Telecommunications Corporation to Singapore Telecom. ITU 1999 case study and NTA identify this as the first commercial Internet service provider with continuous international IP. Earlier email was batch/store-and-forward. Grade B.
- **WorldLink:** UUCP email service announced October 1995 (NSRC contemporary report by Dileep Agrawal; dial-up several times daily to Internet mail). Full dial-up Internet later (commonly 1997). Grade B for the 1995 UUCP service.
- **HealthNet Nepal (1995):** Nonprofit at Tribhuvan University Teaching Hospital / Institute of Medicine, in partnership with SatelLife. Provided email and later full Internet (WWW, Gopher, FTP) to the health community. Contemporary NSRC entry (created December 1995). Grade B for existence; exact 1994/1995 start details vary in retrospective accounts (Sanjay Manandhar Wikipedia narrative).

## Personal web ecology / leads

- No verified Nepal-resident personal homepage located in current sources. Early public-facing web content was institutional or external-hosted.
- **Kathmandu Post online (1 September 1995):** Content placed on a University of Illinois student account (http://www.cen.uiuc.edu/~rshresth/ktmpost/newshome.html) by Mercantile in partnership with Kantipur Publications. External hosting; not a local personal page. Later moved to south-asia.com (1996) then nepalnews.com (1998/1999). Grade B for the 1995 external placement (Media Kurakani / secondary journalism histories).
- **nepalnews.com:** Registered 16 July 1998; operational as independent online news portal from 1999 (Mercantile).
- Possible leads: early .np captures (mos.com.np, healthnet.org.np), university or NGO pages after mid-1995, The Nepal Digest (US-based 1992 mailing list / magazine for diaspora), local press archives, personal pages on free hosts.

## Earliest known examples by category

| Category | Example | Date | Medium | Operator | Network status | Evidence grade | Notes |
|----------|---------|------|--------|----------|----------------|----------------|-------|
| Communication | RONAST–ERNET scientific email | 1993 (or 1994) | email | academic / institutional (RONAST + Mercantile) | inter-network / store-and-forward | B/C | Scheduled dial-up; year conflict between sources |
| Communication / commercial | Mercantile store-and-forward email | 1994 (June) | email | commercial (MOS) | inter-network | B | Australia upstream; mainly international orgs |
| Infrastructure | .np ccTLD delegation | 25 Jan 1995 | dns | commercial (Mercantile) | internet | A | DNS only |
| Infrastructure / service | Mercantile continuous international IP / first commercial ISP | mid-Jul 1995 | internet-access / gateway | commercial | internet | B | Via NTC to Singapore Telecom; ITU/NTA |
| Communication | WorldLink UUCP email | Oct 1995 | email / uucp | commercial | inter-network | B | NSRC contemporary report |
| Publishing | Kathmandu Post content online | 1 Sep 1995 | web-publication | institutional (newspaper + Mercantile) | internet | B | External host (UIUC student account); not local |
| Service | HealthNet Nepal | 1995 | email / later full internet | nonprofit / academic | internet-connected | B | SatelLife partnership; health community |

## Gaps and next leads

1. Resolve the 1993 vs 1994 start for RONAST–ERNET with primary correspondence, logs, or contemporary notices.
2. Locate original IANA delegation correspondence or contemporaneous announcements for the 25 January 1995 .np assignment.
3. Recover early captures of mos.com.np, south-asia.com, or the UIUC Kathmandu Post page.
4. Search local Nepali-language press (Kantipur, Rising Nepal, etc.) and university archives for personal or community pages after July 1995.
5. Confirm HealthNet’s exact start date and whether any 1994 email logs survive.
6. Check for pre-1993 experimental access (e.g., individual dial-up to foreign hosts) or FidoNet/UUCP precursors.

## Bibliography / evidence log

- btw.media, “The Message Was Online by Schedule: Nepal’s Early Internet, 1993–95” (12 October 2026): synthesises Montgomery 2002, ITU 1999 case study, NTA convergence study, Rajbhandari NAST presentation. https://btw.media/en/nepal-email-online-by-schedule-ronast-ernet-1993-1995 (accessed 16 November 2026).
- IANA .np delegation record: registration date 25 January 1995; Mercantile Communications. https://www.iana.org/domains/root/db/np.html and archived WHOIS.
- NSRC Connectivity Provider Database: WorldLink UUCP report 25 October 1995 (Dileep Agrawal); HealthNet Nepal entry created 7 December 1995.
- Media Kurakani / journalism histories: Kathmandu Post online 1 September 1995 on UIUC student page; later south-asia.com and nepalnews.com.
- APNIC blog retrospective (2018) and NepaliTelecom history summary.
- Wikipedia “Internet in Nepal” (HealthNet / Manandhar narrative; secondary).
- Accessed 16 November 2026.

**Researcher:** Grok (xAI)  
**Last checked:** 2026-11-16

## Structured candidates from primary NSRC reports (2026-11-18)

Contemporary NSRC Connectivity Providers Database entries provide primary evidence of named operators and services by early 1995.

### NP-01 — Mercantile Office Systems contact and email service (January 1995)

```yaml
id: NP-01
status: candidate
person_or_project: Mercantile Office Systems / Sanjay Manandhar
title: Mercantile email and domain contact
url_original: unknown
url_archived: https://nsrc.org/db/lookup/report.php?id=890202386458:497430937&fromISO=NP
country_or_territory: Nepal
connection_basis: local-hosting | operator-residence
medium: email
activity_type: communication | infrastructure
operator_type: commercial
network_status: inter-network
date_claimed: 1995-01-31
date_type: inferred
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202386458:497430937&fromISO=NP
    source_type: contemporary operator correspondence preserved in NSRC database
    observed_date: 1995-01-31
    supports: named Kathmandu operator, email address postmaster@mos.com.np, node pumori, telephone and postal address
    grade: A
author_attribution: Sanjay Manandhar <sanjay@mos.com.np>
language: English
notes: Dated email from Manandhar to NSRC lists full Mercantile contact details and confirms operational email presence under mos.com.np by 31 January 1995. Aligns with IANA .np delegation the same month.
uncertainties: Does not establish continuous IP connectivity or public web service; store-and-forward character of earlier commercial email is from secondary sources.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

### NP-02 — WorldLink UUCP email service (October 1995)

```yaml
id: NP-02
status: candidate
person_or_project: WorldLink Inc. / Dileep Agrawal
title: WorldLink UUCP Internet e-mail service
url_original: unknown
url_archived: https://nsrc.org/db/lookup/report.php?id=890202386112:497435004&fromISO=NP
country_or_territory: Nepal
connection_basis: local-hosting | operator-residence
medium: email | uucp
activity_type: communication | service
operator_type: commercial
network_status: inter-network
date_claimed: 1995-10-25
date_type: first-publication
date_precision: exact
evidence:
  - source_url: https://nsrc.org/db/lookup/report.php?id=890202386112:497435004&fromISO=NP
    source_type: contemporary operator announcement preserved in NSRC database
    observed_date: 1995-10-25
    supports: announcement of newly established UUCP service dialling several times daily to transfer Internet mail; named contacts Shyam Agrawal (Nepal) and Manoj Agrawal (US); address PO Box 8207 Kathmandu; domains worldl.com and wlink.wa.com
    grade: A
author_attribution: Dileep Agrawal <DA3101A@american.edu>
language: English
notes: Primary contemporary report that WorldLink had recently established UUCP-based Internet e-mail in Nepal. Explicitly states planned upgrade to full PPP/SLIP connectivity. Distinct from Mercantile’s earlier store-and-forward and July 1995 continuous-IP services.
uncertainties: Exact first customer date and continuous operation not stated; full dial-up Internet commonly dated 1997 in later accounts.
researcher: Grok (xAI)
last_checked: 2026-11-18
```

These candidates strengthen the commercial email layer with grade-A contemporary operator reports. No resident personal homepage is identified. Next: recover Wayback captures of mos.com.np and early WorldLink pages; seek Nepali-language press notices of the 1995 services.
