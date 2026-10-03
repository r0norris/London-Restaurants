#!/usr/bin/env python3
"""Check every URL in data/venues.json. Logs 4xx/5xx and connection failures.

Some booking platforms (OpenTable, SevenRooms) reject non-browser clients, and Python
cannot resolve Caprice's underscore hostname; those are reported as BLOCKED rather than
BROKEN and should be spot-checked in a browser.
"""
import json, pathlib, sys, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
# Wikimedia asks scripts to identify themselves and throttles browser-like UAs
WIKI_UA = "LondonLadsDinnerMap/1.0 (https://github.com/r0norris/London-Restaurants)"
BOT_WALLED = ("opentable.", "sevenrooms.com", "rosewoodhotels.com", "nicholsonspubs.co.uk", "designmynight.com", "capricebookings.com")

def check(url):
    # Wikimedia and others answer 429 when hit in parallel: back off and retry before calling it broken
    for wait in (0, 3, 8):
        time.sleep(wait)
        status, final = _check(url)
        if status != 429:
            break
    return status, final

def _check(url):
    for method in ("HEAD", "GET"):
        try:
            ua = WIKI_UA if "wikimedia.org" in url else UA
            req = urllib.request.Request(url, method=method, headers={"User-Agent": ua, "Accept": "text/html,*/*"})
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.status, r.geturl()
        except urllib.error.HTTPError as e:
            if method == "GET":
                return e.code, url
        except Exception as e:
            if method == "GET":
                return f"ERR {type(e).__name__}", url
    return "ERR", url

data = json.loads((ROOT / "data" / "venues.json").read_text())
urls = {}
for v in data["venues"]:
    for f in ("website", "booking_url", "evidence_url"):
        if v.get(f):
            urls.setdefault(v[f], []).append(f"{v['id']}.{f}")
    for f in ("src", "file_page"):
        if v.get("image", {}).get(f):
            urls.setdefault(v["image"][f], []).append(f"{v['id']}.image.{f}")

with ThreadPoolExecutor(8) as ex:
    results = dict(zip(urls, ex.map(check, urls)))

broken = 0
for url, (status, final) in sorted(results.items(), key=lambda kv: str(kv[1][0])):
    ok = isinstance(status, int) and status < 400
    walled = any(d in url for d in BOT_WALLED)
    tag = "OK" if ok else ("BLOCKED" if walled else "BROKEN")
    broken += tag == "BROKEN"
    if tag != "OK" or "-v" in sys.argv:
        print(f"{tag:8} {status}  {url}  <- {', '.join(urls[url])}")
print(f"\n{len(urls)} unique URLs, {broken} broken")
sys.exit(1 if broken else 0)
