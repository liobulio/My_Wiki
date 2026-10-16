#!/usr/bin/env python3
"""Fetch news leads (Investing.com) with real article URLs → data/leads.json.

  python scripts/news_leads.py                 # feeds from brief/sources.yaml (role: leads)
  python scripts/news_leads.py --hours 36      # look-back window (default 36h)

Google News RSS links are opaque redirects (news.google.com/rss/articles/…); they are decoded to
the publisher URL through Google's own batchexecute endpoint. Non-English mirrors (es./mx./…) are
dropped and stories are deduped by title, so every lead in the brief opens the original article.
Stdlib only.
"""
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from frontmatter import parse_yaml_subset  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126 Safari/537.36"}
ENGLISH_HOSTS = {"www.investing.com", "investing.com", "uk.investing.com", "ca.investing.com",
                 "au.investing.com", "in.investing.com"}
CATEGORY_RE = re.compile(r"^https?://[^/]*investing\.com/news/[a-z-]+/?$")


def _get(url, data=None, headers=None, timeout=20):
    h = dict(UA)
    h.update(headers or {})
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def is_article_url(url):
    """True for a real article link, False for a section/category page or a Google redirect."""
    return bool(url) and "news.google.com" not in url and not CATEGORY_RE.match(url) and \
        bool(re.search(r"/news/[a-z-]+/[a-z0-9-]+", url))


def is_english(url):
    return urllib.parse.urlparse(url).netloc.lower() in ENGLISH_HOSTS


def parse_rss(xml):
    items = []
    for block in re.findall(r"<item>(.*?)</item>", xml, re.S):
        def tag(name):
            m = re.search(rf"<{name}[^>]*>(.*?)</{name}>", block, re.S)
            return re.sub(r"<!\[CDATA\[|\]\]>", "", m.group(1)).strip() if m else ""
        items.append({"title": tag("title"), "link": tag("link"), "pubDate": tag("pubDate")})
    return items


def parse_date(s):
    s = (s or "").strip()
    for fn in (lambda x: parsedate_to_datetime(x),
               lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)):
        try:
            d = fn(s)
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except (TypeError, ValueError):
            continue
    return None


def extract_garturl(batch_response):
    m = re.search(r'\\"garturlres\\",\\"(https?://[^\\"]+)\\"', batch_response)
    return m.group(1) if m else None


def decode_google_news(link):
    """news.google.com/rss/articles/<id> → publisher URL (None if Google refuses)."""
    gid = link.split("/articles/")[-1].split("?")[0]
    page = _get(f"https://news.google.com/articles/{gid}")
    sg = re.search(r'data-n-a-sg="([^"]+)"', page)
    ts = re.search(r'data-n-a-ts="([^"]+)"', page)
    if not (sg and ts):
        return None
    payload = ["garturlreq", [["X", "X", ["X", "X"], None, None, 1, 1, "US:en", None, 1, None, None, None, None, None,
                               0, 1], "X", "X", 1, [1, 1, 1], 1, 1, None, 0, 0, None, 0],
               gid, int(ts.group(1)), sg.group(1)]
    body = urllib.parse.urlencode({"f.req": json.dumps([[["Fbv4je", json.dumps(payload), None, "generic"]]])}).encode()
    out = _get("https://news.google.com/_/DotsSplashUi/data/batchexecute", data=body,
               headers={"Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"})
    return extract_garturl(out)


def clean_title(t):
    return re.sub(r"\s+-\s+Investing\.com.*$", "", re.sub(r"\s+By Investing\.com", "", t)).strip()


def main(argv):
    hours = 36
    for a in argv:
        if a.startswith("--hours"):
            hours = int(a.split("=", 1)[1]) if "=" in a else int(argv[argv.index(a) + 1])
    cfg = parse_yaml_subset((ROOT / "brief" / "sources.yaml").read_text(encoding="utf-8"))
    feeds = [u for e in cfg.get("foreign", []) if e.get("role") == "leads" for u in (e.get("urls") or [])]
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    seen, out, failures = set(), [], 0
    for feed in feeds:
        try:
            items = parse_rss(_get(feed))
        except Exception as e:  # noqa: BLE001
            print(f"feed failed: {feed[:80]} ({e})")
            continue
        for it in items:
            d = parse_date(it["pubDate"])
            if d and d < since:
                continue
            title = clean_title(it["title"])
            key = re.sub(r"\W+", " ", title.lower()).strip()
            if not title or key in seen:
                continue
            url = it["link"]
            if "news.google.com" in url:
                try:
                    url = decode_google_news(url)
                except Exception:  # noqa: BLE001
                    url = None
                if not url:
                    failures += 1
                    continue
            if not (is_english(url) and is_article_url(url)):
                continue
            seen.add(key)
            out.append({"title": title, "url": url, "published": d.strftime("%Y-%m-%d %H:%M UTC") if d else "",
                        "publisher": "Investing.com", "feed": feed})
    out.sort(key=lambda x: x["published"], reverse=True)
    path = ROOT / "data" / "leads.json"
    path.write_text(json.dumps({"fetched": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "hours": hours, "leads": out}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(out)} leads → {path} ({failures} Google links could not be decoded)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
