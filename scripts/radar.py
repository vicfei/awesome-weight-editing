#!/usr/bin/env python3
"""Daily arXiv radar for awesome-weight-editing.

Scrapes the public new-submission listing pages at arxiv.org/list/<cat>/new
for selected cs.* categories, keeps entries whose title matches the
weight-editing family keywords, and rewrites ``docs/radar.md`` with a rolling
archive (entries expire after ``RETENTION_DAYS``). Stdlib only.

Usage:
    python scripts/radar.py              # fetch live, rewrite docs/radar.md
    python scripts/radar.py --selftest   # parse+render an embedded fixture, no network
"""

from __future__ import annotations

import argparse
import datetime as dt
import html as html_mod
import re
import sys
import time
import urllib.request
from pathlib import Path

BASE = "https://arxiv.org/list"
CATEGORIES = ["cs.CL", "cs.LG", "cs.AI"]
RETENTION_DAYS = 21
REPO = "vicfei/awesome-weight-editing"
UA = f"Mozilla/5.0 (compatible; {REPO} radar/1.0; +https://github.com/{REPO})"

# Title keywords, precision-first. Broad terms ("machine unlearning", "model
# editing" alone) are constrained with LLM context where they flood.
STRONG = re.compile(
    r"knowledge editing|model editing|weight editing|weight-space|"
    r"task arithmetic|model merging|steering vector|representation engineering|"
    r"abliterat|weight-space programming|editing language model|"
    r"llm unlearning|language model unlearning|unlearning llm",
    re.IGNORECASE,
)
WSP = re.compile(r"weight-space|weight editing|weights? (are )?(written|read)", re.IGNORECASE)

DT_DD = re.compile(r"<dt>(.*?)</dt>\s*<dd>(.*?)</dd>", re.S)
ID_IN_DT = re.compile(r"arXiv:([0-9]{4}\.[0-9]{4,6})")
TITLE_IN_DD = re.compile(r"list-title[^>]*>\s*(?:<span[^>]*>[^<]*</span>)?\s*(.*?)\s*</div>", re.S)
TAGS = re.compile(r"<[^>]+>")

FIXTURE = """<dl>
<dt><a name='item1'>[1]</a> <a href ="/abs/2611.00001"> arXiv:2611.00001 </a></dt>
<dd><div class='meta'>
  <div class='list-title mathjax'><span class='descriptor'>Title:</span>
    Recursive Weight-Space Programming for Small Code Models
  </div>
</div></dd>
<dt><a name='item2'>[2]</a> <a href ="/abs/2611.00002"> arXiv:2611.00002 </a></dt>
<dd><div class='meta'>
  <div class='list-title mathjax'><span class='descriptor'>Title:</span>
    Boring attention-variant ablation study
  </div>
</div></dd>
<dt><a name='item3'>[3]</a> <a href ="/abs/2611.00003"> arXiv:2611.00003 </a></dt>
<dd><div class='meta'>
  <div class='list-title mathjax'><span class='descriptor'>Title:</span>
    Knowledge Editing with Steering Vectors | pipe test
  </div>
</div></dd>
</dl>
"""


def http_get(url: str, attempts: int = 3, timeout: int = 30) -> bytes:
    last_err: Exception | None = None
    for i in range(attempts):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except Exception as err:  # noqa: BLE001 - retry any transport error
            last_err = err
            time.sleep(5 * (i + 1))
    raise RuntimeError(f"GET failed after {attempts} attempts: {url} ({last_err})")


def clean_title(raw: str) -> str:
    return " ".join(html_mod.unescape(TAGS.sub("", raw)).split())


def parse_listing(page: bytes, category: str) -> tuple[list[dict[str, str]], int]:
    """Return (matches, total_parsed) for one category listing page."""
    html = page.decode("utf-8", errors="ignore")
    matches: list[dict[str, str]] = []
    total = 0
    for dt_html, dd_html in DT_DD.findall(html):
        id_m = ID_IN_DT.search(dt_html)
        title_m = TITLE_IN_DD.search(dd_html)
        if not (id_m and title_m):
            continue
        total += 1
        title = clean_title(title_m.group(1))
        if not STRONG.search(title):
            continue
        tag = "wsp+" if WSP.search(title) else "editing"
        matches.append({"id": id_m.group(1), "title": title, "category": category, "tag": tag})
    return matches, total


def fetch_latest() -> list[dict[str, str]]:
    seen: dict[str, dict[str, str]] = {}
    for cat in CATEGORIES:
        matches, total = parse_listing(http_get(f"{BASE}/{cat}/new"), cat)
        print(f"radar: {cat}: parsed {total} listings, kept {len(matches)}")
        for e in matches:
            seen.setdefault(e["id"], e)
    return sorted(seen.values(), key=lambda e: e["id"], reverse=True)


ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*\[(.+?)\]\(https://arxiv\.org/abs/([^)]+)\)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|$")


def load_existing(rad: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    if not rad.exists():
        return entries
    for line in rad.read_text(encoding="utf-8").splitlines():
        m = ROW.match(line.strip())
        if m:
            entries.append(
                {"first_seen": m.group(1), "title": m.group(2), "id": m.group(3), "category": m.group(4), "tag": m.group(5)}
            )
    return entries


def merge(old: list[dict[str, str]], fresh: list[dict[str, str]], today: str) -> list[dict[str, str]]:
    by_id = {e["id"]: e for e in old}
    for e in fresh:
        if e["id"] not in by_id:
            by_id[e["id"]] = {"first_seen": today, **e}
    cutoff = (dt.date.fromisoformat(today) - dt.timedelta(days=RETENTION_DAYS)).isoformat()
    return [e for e in by_id.values() if e["first_seen"] >= cutoff]


def render(entries: list[dict[str, str]], now: dt.datetime) -> str:
    entries = sorted(entries, key=lambda e: (e["first_seen"], e["id"]), reverse=True)
    lines = [
        f"<!-- Auto-generated by scripts/radar.py via GitHub Actions (repo: {REPO}). Manual edits will be overwritten. -->",
        "# 🤖 arXiv Radar",
        "",
        "Papers matching this repo's [keyword filter](../scripts/radar.py), collected daily from the "
        f"arXiv new-submission listings (cs.CL / cs.LG / cs.AI) and kept for a "
        f"{RETENTION_DAYS}-day rolling window. Generated {now.strftime('%Y-%m-%d %H:%M UTC')}.",
        "",
    ]
    if not entries:
        lines += [
            "_No matches in the current window — a quiet stretch happens; if this persists, "
            "tune the keywords via a PR._",
            "",
        ]
    else:
        n = len(entries)
        lines += [f"**{n} paper{'s' if n != 1 else ''}** on radar.", "", "| First seen | Paper | Area | Match |", "|---|---|---|---|"]
        for e in entries:
            title = e["title"].replace("|", "\\|")
            lines.append(
                f"| {e['first_seen']} | [{title}](https://arxiv.org/abs/{e['id']}) | {e['category']} | {e['tag']} |"
            )
    lines += [
        "",
        "---",
        "",
        "Hand-curated sections live in the [main README](../README.md). Keywords are defined at the top "
        "of [`scripts/radar.py`](../scripts/radar.py) — PRs welcome.",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc)
    rad = Path(__file__).resolve().parent.parent / "docs" / "radar.md"
    merged = merge(load_existing(rad), fetch_latest(), now.strftime("%Y-%m-%d"))
    rad.write_text(render(merged, now), encoding="utf-8")
    print(f"radar: archive holds {len(merged)} entries -> {rad}")
    return 0


def selftest() -> int:
    matches, total = parse_listing(FIXTURE.encode(), "cs.CL")
    assert total == 3, f"expected 3 parsed listings, got {total}"
    assert len(matches) == 2, f"expected strong-filter to keep 2 of 3, got {len(matches)}: {matches}"
    assert matches[0] == {
        "id": "2611.00001",
        "title": "Recursive Weight-Space Programming for Small Code Models",
        "category": "cs.CL",
        "tag": "wsp+",
    }, matches
    assert matches[1]["id"] == "2611.00003" and matches[1]["tag"] == "editing", matches
    now = dt.datetime(2026, 11, 8, tzinfo=dt.timezone.utc)
    merged = merge([], matches, "2026-11-08")
    md = render(merged, now)
    assert "pipe test" in md and "\\|" in md, "pipe escaping wrong"
    rt_path = Path("/tmp/_radar_rt5.md")
    rt_path.write_text(md, encoding="utf-8")
    rt = load_existing(rt_path)
    assert len(rt) == 2, f"round-trip lost rows: {rt}"
    print("selftest OK — listing parse, strong/wsp tags, merge, render, archive round-trip")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true", help="run offline fixture test")
    args = ap.parse_args()
    sys.exit(selftest() if args.selftest else main())
