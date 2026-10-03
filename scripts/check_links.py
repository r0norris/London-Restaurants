#!/usr/bin/env python3
"""Check every URL in data/venues.json. Logs 4xx/5xx and connection failures.

Some booking platforms (OpenTable, SevenRooms) reject non-browser clients, and Python
cannot resolve Caprice's underscore hostname; those are reported as BLOCKED rather than
BROKEN and should be spot-checked in a browser.
"""
import json, pathlib, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
BOT_WALLED = ("opentable.", "sevenrooms.com", "rosewoodhotels.com", "nicholsonspubs.co.uk", "designmynight.com", "capricebookings.com")

def check(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
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
