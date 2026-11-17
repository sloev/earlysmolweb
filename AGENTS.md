# Agent instructions — sloev/earlysmolweb

## Project boundary (mandatory)
This repository is exclusively the early Internet / small-web history research project.

- Work only on early Internet history, UUCP, EUnet, networking, regional connectivity histories, and this repository's website/content.
- Never import, copy, summarize, or publish Gårdsted/Gedde genealogy, family-tree data, family members' personal information, or family-tree website content from `sloev/tree` here.
- Do not use one repository's task list, notes, files, or research as context for work in the other. If a request is ambiguous, stop and ask which repository it concerns.
- Icelandic UUCP/EUnet research belongs here, in `sloev/earlysmolweb`, not in `sloev/tree`.
- Before editing, confirm the repository is `sloev/earlysmolweb` and the branch is `main`. Work directly on `main`; do not create feature branches.
- Never claim a website is published or updated until the build/deployment has actually completed and been checked.


## Public country articles — publish only when a specific story is supported

Create or refresh an `article-data` block only when the evidence supports a specific, tellable country story. If it does not, omit the block; the country remains in Coverage and Research records. The public site does not generate an article from raw notes. Do not hand-edit article HTML or create a second copy of findings.

When a story qualifies, place exactly one JSON block in an HTML comment near the top of that research file, after the opening title/status lines:

```html
<!-- article-data
{
  "title": "A clear, reader-facing headline",
  "dek": "A short, carefully qualified standfirst.",
  "lead": "A concise opening paragraph that explains the country's early network history and the strongest current finding.",
  "sections": [
    {
      "heading": "Before the public web",
      "markdown": "A readable, sourced narrative in Markdown. Explain the context and distinguish network services from Web publishing."
    },
    {
      "heading": "The first documented milestones",
      "markdown": "Continue the story using only claims supported in the research record. Keep dates, categories and uncertainty explicit."
    }
  ],
  "image": {
    "url": "https://upload.wikimedia.org/...",
    "alt": "Accurate description of the image",
    "caption": "What the image depicts and why it is relevant",
    "credit": "Creator or rights holder",
    "license": "Exact license or public-domain status",
    "source_url": "https://commons.wikimedia.org/wiki/File:..."
  },
  "sources": [
    {
      "label": "Source title",
      "url": "https://example.org/source",
      "grade": "A"
    }
  ]
}
-->
```

Rules:
- The block is optional and evidence-gated. Add or refresh it only when there is a specific story; otherwise omit it. Keep it valid JSON (double quotes, no trailing commas). Do not wrap it in a Markdown code fence.
- Write reported, readable prose about the specific episode, not a status dump, wiki-style overview, or copy of the candidate register. Explain what happened, who was involved, when and where it happened, and what the sources actually prove. Aim for 300–700 words when supported; never pad.
- The article is an editorial presentation of the canonical research below it. Every factual claim must already be supported in the research file and linked to its source. Do not invent dates, operators, authors, URLs, quotations, or a "first" claim.
- Explain the connection basis and geography. Distinguish locally operated infrastructure, remote hosting, diaspora activity, DNS delegation, store-and-forward email, UUCP/BITNET, TCP/IP, and Web publishing. Qualify "earliest" and preserve conflicting dates.
- If the research contains only infrastructure leads, generic chronology, or unresolved candidates, do not publish an article yet. Never imply a verified personal homepage if none is documented.
- Add one relevant, legally reusable image when possible. Prefer Wikimedia Commons, government/national-library collections, or public-domain archival material. Record the direct HTTPS image URL, accurate alt text, caption, creator, exact license, and source/file page URL. Check that the license permits this use and retain attribution. Do not hotlink arbitrary search-result images, copy copyrighted photos, or use an image merely because it depicts the country.
- If no suitable image is verified, set `"image": null`; the site will publish the story without an image. It does not add generic scenery. Never invent image credits or licenses.
- Add 2–6 key sources to the article's `sources` array, prioritising the strongest evidence. The detailed bibliography remains in the research note. Use `"sources": []` if there are no reliable public links yet.
- Article content and imagery are generated from this data block by the shared site template. Never add manually maintained article HTML, CSS, or JavaScript.
- After every change, verify the JSON parses, links work, image attribution is complete, and article claims match the research note. Commit the research and article data together on `main`.


## Editorial gate for public articles — supersedes older broad article guidance

Do not write an article just because a country research file exists. Do not turn a country timeline, infrastructure summary, list of leads, or evidence-gap note into a generic country story. Publish an article only when the research supports a specific, tellable episode rooted in that country: for example, a named person publishing a homepage, a newspaper or community launching an online service, a local provider and its users, a particular online community, or a recoverable early website. The article must tell what happened, who did it, when, where, how, and what the sources actually establish. It should read as continuous reported prose, not a wiki entry, catalogue, bullet-point chronology, or general overview.

If no such episode is established, omit the article-data block entirely. The country remains discoverable in Coverage and Research records. Do not use the article slot as a placeholder. Remove any existing article block that no longer meets this test. The website must not auto-generate an article from raw research notes.

Images are editorial evidence, not decoration. Search for and prefer (in order of relevance) portraits of named participants, original screenshots/captures of the actual site or service, contemporary publication/provider logos, newspaper mastheads, event or workplace photographs, and relevant archival documents. Do not use generic country landscapes, generic flags, or unrelated stock imagery. Never imply that a portrait depicts a named person unless its identity is established by the source. For every image, verify that the exact asset is reusable and provide its direct HTTPS URL, meaningful alt text, contextual caption, creator/rights holder, exact license/rights statement, and source page. Link credits to the source page. If no suitable, reusable and accurately identified image is found, set image to null and publish without an image; do not fabricate or substitute scenery.

A short story is better than a padded one. Aim for a focused narrative, normally 300–700 words when the evidence supports it, with 2–5 key sources. Every material claim must be traceable to the canonical research note and cited source. Preserve disputed dates, distinguish first-hand contemporary evidence from retrospective accounts, and do not claim a national first unless comparative evidence supports it. If the evidence supports only a candidate or probable story, say so plainly in the prose.
