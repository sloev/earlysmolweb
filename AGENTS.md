# Agent instructions — sloev/earlysmolweb

## Project boundary (mandatory)
This repository is exclusively the early Internet / small-web history research project.

- Work only on early Internet history, UUCP, EUnet, networking, regional connectivity histories, and this repository's website/content.
- Never import, copy, summarize, or publish Gårdsted/Gedde genealogy, family-tree data, family members' personal information, or family-tree website content from `sloev/tree` here.
- Do not use one repository's task list, notes, files, or research as context for work in the other. If a request is ambiguous, stop and ask which repository it concerns.
- Icelandic UUCP/EUnet research belongs here, in `sloev/earlysmolweb`, not in `sloev/tree`.
- Before editing, confirm the repository is `sloev/earlysmolweb` and the branch is `main`. Work directly on `main`; do not create feature branches.
- Never claim a website is published or updated until the build/deployment has actually completed and been checked.


## Public country articles — mandatory for every research task

Every agent that creates or materially updates a country/territory research file MUST also create or update that file's structured `article-data` block. The public site reads this data directly from the same Markdown file and generates the article cards and article pages automatically. Do not hand-edit article HTML or create a second copy of findings.

Place exactly one JSON block in an HTML comment near the top of each `research/<slug>.md` file, after the opening title/status lines:

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
- The block is required for new country files and must be refreshed when meaningful new evidence changes the story. Keep it valid JSON (double quotes, no trailing commas). Do not wrap it in a Markdown code fence.
- Write an actual short article, not a status dump or a copy of the candidate register. Use a clear lead and coherent sections; explain what happened, who operated it, what kind of network/service it was, and what remains uncertain. A useful initial article is normally 400–900 words when the evidence supports that length; do not pad thin research.
- The article is an editorial presentation of the canonical research below it. Every factual claim must already be supported in the research file and linked to its source. Do not invent dates, operators, authors, URLs, quotations, or a "first" claim.
- Explain the connection basis and geography. Distinguish locally operated infrastructure, remote hosting, diaspora activity, DNS delegation, store-and-forward email, UUCP/BITNET, TCP/IP, and Web publishing. Qualify "earliest" and preserve conflicting dates.
- Use the research status honestly. A country with only infrastructure leads can still have a valuable article about that infrastructure and the evidence gap; never imply a verified personal homepage if none is documented.
- Add one relevant, legally reusable image when possible. Prefer Wikimedia Commons, government/national-library collections, or public-domain archival material. Record the direct HTTPS image URL, accurate alt text, caption, creator, exact license, and source/file page URL. Check that the license permits this use and retain attribution. Do not hotlink arbitrary search-result images, copy copyrighted photos, or use an image merely because it depicts the country.
- If no suitable image is verified, set `"image": null`; the site will try to find an attributed image from Wikimedia Commons automatically. Never invent image credits or licenses.
- Add 2–6 key sources to the article's `sources` array, prioritising the strongest evidence. The detailed bibliography remains in the research note. Use `"sources": []` if there are no reliable public links yet.
- Article content and imagery are generated from this data block by the shared site template. Never add manually maintained article HTML, CSS, or JavaScript.
- After every change, verify the JSON parses, links work, image attribution is complete, and article claims match the research note. Commit the research and article data together on `main`.
