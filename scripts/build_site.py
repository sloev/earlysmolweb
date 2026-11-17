#!/usr/bin/env python3
"""Build a searchable static research website from research Markdown."""
from datetime import datetime, timezone
from pathlib import Path
import json
import re
import markdown

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
DOCS = ROOT / "docs"
DOCS.mkdir(exist_ok=True)
md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"])

def plain(value):
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[*_>#]", "", value)
    return re.sub(r"\s+", " ", value).strip()

def parse(path):
    raw = path.read_text(encoding="utf-8")
    match = re.search(r"^#\s+(.+)$", raw, re.M)
    title = match.group(1).strip() if match else path.stem.replace("-", " ").title()
    match = re.search(r"^\*\*Status:\*\*\s*(.+)$", raw, re.M | re.I)
    status = plain(match.group(1)) if match else "Research status not stated"
    match = re.search(r"^\*\*ISO:\*\*\s*(.+)$", raw, re.M | re.I)
    iso = plain(match.group(1)) if match else ""
    blocks = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    intro = next((plain(p) for p in blocks[1:] if not p.startswith("#") and not p.startswith("**")), "")
    md.reset()
    return {
        "title": title,
        "status": status,
        "iso": iso,
        "summary": intro[:420],
        "body": md.convert(raw),
        "source": "https://github.com/sloev/earlysmolweb/blob/main/" + path.relative_to(ROOT).as_posix(),
    }

records = [parse(p) for p in sorted(RESEARCH.glob("*.md"), key=lambda p: p.name.casefold())]
statuses = {}
for record in records:
    statuses[record["status"]] = statuses.get(record["status"], 0) + 1
payload = json.dumps(records, ensure_ascii=False).replace("</", "<\\/")
status_payload = json.dumps(statuses, ensure_ascii=False)
generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="A source-led global research compendium documenting early internet activity by country and territory.">
<meta name="theme-color" content="#101b2a"><title>Early Smol Web — Global research atlas</title>
<style>
:root{color-scheme:light;--ink:#172536;--muted:#64748b;--paper:#f5f7f8;--line:#dce3e8;--accent:#176b63;--accent2:#d7eee8;--night:#101b2a}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"Segoe UI",sans-serif}a{color:var(--accent)}
.hero{background:var(--night);color:#f6f8fa;padding:64px max(24px,calc((100vw - 1180px)/2)) 54px}.eyebrow{text-transform:uppercase;letter-spacing:.16em;font-size:.76rem;color:#9ed5c8;font-weight:700}
.hero h1{font:clamp(2.7rem,7vw,5.4rem)/.98 Georgia,serif;max-width:900px;margin:20px 0}.hero p{max-width:720px;color:#c7d2dc;font-size:1.1rem}.hero a{color:#a9e2d5}
.wrap{max-width:1180px;margin:auto;padding:32px 24px 80px}.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.stat{background:white;border:1px solid var(--line);padding:18px 20px}
.stat strong{display:block;font:2rem Georgia,serif}.stat span{color:var(--muted);font-size:.86rem}.toolbar{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:34px 0 18px}
.search{flex:1;min-width:220px;padding:13px 15px;border:1px solid var(--line);border-radius:4px;font:inherit;background:white}.filter{padding:12px;border:1px solid var(--line);background:white;border-radius:4px;font:inherit;color:var(--ink)}
.count{color:var(--muted);font-size:.9rem}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}.item{background:white;border:1px solid var(--line);padding:20px;min-width:0}
.item h2{font:1.5rem/1.2 Georgia,serif;margin:0 0 8px}.meta{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:12px}.pill{display:inline-block;background:var(--accent2);color:#14584f;padding:3px 9px;border-radius:2px;font-size:.75rem;font-weight:700}
.summary{color:#465568}.item details{border-top:1px solid var(--line);padding-top:12px}.item summary{cursor:pointer;color:var(--accent);font-weight:650}.content{padding-top:12px;overflow-wrap:anywhere}
.content h1,.content h2{font-family:Georgia,serif}.content h2{font-size:1.4rem;margin-top:1.7em}.content table{border-collapse:collapse;display:block;overflow-x:auto}.content th,.content td{border:1px solid var(--line);padding:7px 10px;text-align:left}
.content pre{overflow:auto;background:#f0f3f5;padding:14px}.content img{max-width:100%}.source{font-size:.85rem}.empty{padding:30px;text-align:center;color:var(--muted);background:white;border:1px dashed var(--line)}
footer{margin-top:42px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.88rem}
@media(max-width:720px){.hero{padding:44px 22px}.wrap{padding:24px 16px 56px}.stats,.grid{grid-template-columns:1fr}}
</style></head><body>
<header class="hero"><div class="eyebrow">A living historical research project</div><h1>Early Smol Web</h1>
<p>Tracing the earliest discoverable internet activity around the world — from email, networks and Gopher to online publishing and the personal web.</p>
<p><a href="https://github.com/sloev/earlysmolweb">Explore the open research repository ↗</a></p></header>
<main class="wrap"><section class="stats">
<div class="stat"><strong id="total">0</strong><span>country &amp; territory research files</span></div>
<div class="stat"><strong id="statusCount">0</strong><span>distinct research status labels</span></div>
<div class="stat"><strong>195+</strong><span>countries in scope, plus separately tracked jurisdictions</span></div>
</section>
<div class="toolbar"><input class="search" id="search" type="search" placeholder="Search countries, findings, dates or sources…" aria-label="Search research">
<select class="filter" id="statusFilter" aria-label="Filter by research status"><option value="">All statuses</option></select></div>
<p class="count" id="count" aria-live="polite"></p><section class="grid" id="results" aria-label="Research entries"></section>
<footer><p>Generated automatically from research Markdown. Last generated: __GENERATED__.</p>
<p>“Earliest” means earliest well-supported example currently documented, not proof that no earlier activity existed. Read the <a href="https://github.com/sloev/earlysmolweb/blob/main/WORK_METHOD.md">working method and evidence standards</a>.</p></footer>
</main><script>
const records=__RECORDS__;const statuses=__STATUSES__;const root=document.getElementById("results");const search=document.getElementById("search");const filter=document.getElementById("statusFilter");
document.getElementById("total").textContent=records.length;document.getElementById("statusCount").textContent=Object.keys(statuses).length;
[...new Set(records.map(x=>x.status))].sort().forEach(s=>{const o=document.createElement("option");o.value=s;o.textContent=s;filter.append(o)});
function render(){const q=search.value.toLocaleLowerCase();const s=filter.value;const shown=records.filter(r=>(!s||r.status===s)&&(!q||[r.title,r.status,r.summary,r.body,r.iso].join(" ").toLocaleLowerCase().includes(q)));
document.getElementById("count").textContent="Showing "+shown.length+" of "+records.length+" research files";root.replaceChildren();
if(!shown.length){const p=document.createElement("p");p.className="empty";p.textContent="No matching research yet. Try another search.";root.append(p);return}
shown.forEach(r=>{const article=document.createElement("article");article.className="item";const h=document.createElement("h2");h.textContent=r.title;article.append(h);
const meta=document.createElement("div");meta.className="meta";const badge=document.createElement("span");badge.className="pill";badge.textContent=r.status;meta.append(badge);
if(r.iso){const code=document.createElement("span");code.className="source";code.textContent=r.iso;meta.append(code)}article.append(meta);
if(r.summary){const p=document.createElement("p");p.className="summary";p.textContent=r.summary;article.append(p)}
const details=document.createElement("details");const summary=document.createElement("summary");summary.textContent="Read research and evidence";details.append(summary);
const content=document.createElement("div");content.className="content";content.innerHTML=r.body;details.append(content);
const link=document.createElement("p");link.className="source";const a=document.createElement("a");a.href=r.source;a.textContent="Open source Markdown on GitHub ↗";a.target="_blank";a.rel="noopener noreferrer";link.append(a);details.append(link);
article.append(details);root.append(article)})}
search.addEventListener("input",render);filter.addEventListener("change",render);render();
</script></body></html>"""
page = page.replace("__GENERATED__", generated).replace("__RECORDS__", payload).replace("__STATUSES__", status_payload)
(DOCS / "index.html").write_text(page, encoding="utf-8")
(DOCS / ".nojekyll").write_text("", encoding="utf-8")
print("Generated docs/index.html from " + str(len(records)) + " research files.")
