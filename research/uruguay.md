# Uruguay — early internet activity

**Status:** active / evidence review  
**Last updated:** 2026-11-19  
**Researcher:** Grok (xAI)

## Internet context

Uruguay’s earliest documented public internet-related activity centers on academic UUCP email connectivity in 1988 and the non-profit Chasque network (Instituto del Tercer Mundo / APC node). Chasque offered email, conferences, Gopher, and Telnet from the early 1990s, then graphical SLIP/PPP Web access and member WWW pages from August 1995.

Key contemporary and primary retrospective sources:

- Roberto Bissio, “Un poco de historia” (Chasque.net): August 1995 launch of SLIP/PPP graphical access; members could browse the Web and have their own WWW pages. http://www.chasque.net/chasque2000/acerca_de/historia.htm (accessed 2026-11-19; grade C founder retrospective).
- NSRC Connectivity Provider Database, Gabriel Sere letter, 23 April 1996: lists Chasque (online since 1989) offering interactive and PPP/SLIP access; points to www.chasque.apc.org and gopher.item.org.uy. https://nsrc.org/db/lookup/report.php?id=890202529316:497425062&fromISO=UY (grade A contemporary technical correspondence).

Academic permanent connectivity is dated to March 1994 (RAU / SECIU to NSF). Commercial dial-up (Adinet / ANTEL) began in 1995. Montevideo Portal launched November 1995 as an early local web publication.

## Earliest known examples by category

### Communication / infrastructure (pre-Web and early Web)

- **UY-01** (probable): Chasque email / UUCP / conference services from ~1989–1991 (local 24-hour BBS-style, then automatic UUCP exchange with SECIU). Operator: nonprofit / APC. Medium: email, mailing-list/conferences, uucp. Connection basis: local operator and hosting. Evidence: Bissio retrospective (C); NSRC 1996 letter (A for ongoing service). Date claimed: 1989–1991. Uncertainties: exact first UUCP exchange date.
- **UY-02** (probable): August 1995 Chasque public SLIP/PPP graphical Internet access + member WWW page hosting. Medium: internet-access + website hosting. Activity type: service / personal-expression. Operator: nonprofit. Network status: internet. Date claimed: August 1995 (first-publication / first public service). Evidence: Bissio (C); corroborated by NSRC letter of April 1996 listing the service (A). Uncertainties: exact day; surviving 1995 user-page captures not yet located.

### Publishing

- Montevideo Portal (November 1995): early local online publication / portal. Lead only; not yet structured as a candidate.

## Gaps and next leads

- Exact hosting namespace / ~username or directory pattern used by Chasque for member pages in 1995–96.
- Surviving Wayback or local archive captures of early member pages or www.chasque.apc.org from 1995–1997 (current searches returned later captures only).
- Contemporary newspaper or directory notices confirming the precise August 1995 start date.
- Pre-1995 Gopher/Telnet service details and any institutional sites.

## Bibliography / evidence log

- Bissio, Roberto. “Un poco de historia.” Chasque.net. http://www.chasque.net/chasque2000/acerca_de/historia.htm. Accessed 2026-11-19.
- NSRC Connectivity Provider Database. Gabriel Sere to Steven Huter, 23 Apr 1996. https://nsrc.org/db/lookup/report.php?id=890202529316:497425062&fromISO=UY.
- Secondary academic and press accounts (El Observador, ICANNWiki, etc.) used only for context.

No article-data block: no single tellable personal homepage episode fully supported by primary evidence yet.


## Earlier mail and network milestones recovered — 1988–1993

### 2 December 1988 — InCo's experimental UUCP node

The University of the Republic Faculty of Engineering's 2014 institutional history reproduces a letter from InCo director **Juan José Cabezas** to the dean, dated 8 December 1988. It states that the experimental Uruguayan UUCP node had been installed and was functioning regularly from **2 December 1988**, on the Faculty of Engineering's fifth floor, under the supervision and maintenance of the InCo Programming Department, with assistance from the University of Buenos Aires.

The same chapter reproduces the original UUCP map entry for the Montevideo node and early email headers. One message from Gastón Gonnet carries a 1 December 1988 header and is described by the compiler as the first email received in Uruguay from outside the Río de la Plata. Because the header records the upstream Waterloo relay and predates the letter's stated 2 December operational start, do not use that header alone as the node's launch date.

- Source: *Aportes para la historia del Instituto de Computación [1967–2012]*, Facultad de Ingeniería, Universidad de la República (2014), especially pp. 45–47 / PDF text lines 567–630: https://www.fing.edu.uy/sites/default/files/Aportes_para_la_Historia_del_INCO_0.pdf
- Evidence grade: **A/B** — institutional retrospective reproducing a dated contemporary letter, UUCP map entry and email headers.
- Classification: university UUCP/email node; **not direct TCP/IP Internet** and not personal publishing.

### 8 September 1992 — Chasque and SECIU services before direct Internet

A contemporaneous NSRC report from Miguel Peirano at Chasque says Uruguay had **no direct Internet connection** at that date and that external observers could not ping Uruguayan hosts. It describes most connections as UUCP over voice lines or X.25. It also records:

- Chasque, the Instituto del Tercer Mundo/APC node in Montevideo, fully operational since mid-July 1992 with about 120 users; it connected four times daily to `igc.org` and every two hours to SECIU.
- SECIU's email service to university facilities, mainly UUPC on MS-DOS PCs with some Unix hosts; SECIU polled `uunet.uu.net` and `dcfcen.edu.ar` three times daily and supplied fee-based feeds to non-university hosts.
- Chasque's work with Fido enthusiasts to provide an `rfmail` channel through its Unix system.

Source: NSRC, “status of networking in your area,” last updated 8 Sep 1992: https://nsrc.org/db/lookup/report.php?fromISO=UY&id=890202529785:497424205

**Interpretation:** this is strong evidence of local and store-and-forward networking, but it is an explicit negative checkpoint for direct Internet reachability in September 1992. It does not prove that no individual could use a foreign gateway or remote account.

### 19 February / 3 March 1993 — NGONET email file server

An NSRC archive entry dated 3 March 1993 reproduces an NGONET announcement originally sent on 19 February from `ngonet@chasque.apc.org`. It offers an **Electronic Mail File Server** for the UNCED/Eco 92 resource library, including NGO alternative treaties, Agenda 21 and NGO-originated background material. Documents were automatically returned by email; the announcement states a charge of US$0.06 per kilobyte.

Source: NSRC, “UNCED resources collection,” last updated 3 Mar 1993: https://nsrc.org/db/lookup/report.php?fromISO=UY&id=890202534901:497426495

Classification: NGO/community information service, operated through Chasque. It is a documented local online information service, not a personal page.

### 2 April 1993 — Ida Holz's ENREDO mailing-list message

A separate NSRC record preserves a message by **Ida Holz**, sent from `holz@SECIU.UY` to the ENREDO list at `ENREDO@UCHCECVM.BITNET`. Holz says she had been asked to distribute a Faculty of Economics and Administration document about the university's situation through the network and was sending it to as many organizations as possible.

Source: NSRC, “Conflicto en la Universidad de la Republica del Uruguay,” last updated 2 Apr 1993: https://nsrc.org/db/lookup/report.php?fromISO=UY&id=890202534324:497425387

Classification: **named individual email / mailing-list expression**, with a clear Uruguay institutional connection. The preserved list address is BITNET; this record alone does not prove direct TCP/IP transport or a personal homepage. Keep it distinct from the 1992 infrastructure report and from later web publishing.

### Chronology implications

These records add evidence earlier than the existing 1995 Chasque member-page and RAU WWW leads. They do not move the earliest verified personal website date: the 1988 node, 1992 Chasque/SECIU services and 1993 NGONET/ENREDO messages are network communication and institutional/community services, not personal homepages. The 1992 report's explicit “no direct Internet connection” statement is especially important when interpreting the 1988–93 activity.

**Next:** identify the Fido boards and their operators, recover the early Chasque and SECIU Gopher/FTP menus, and determine whether the 1993 BITNET list had an archive or gateway preserving additional named Uruguayan contributors.
