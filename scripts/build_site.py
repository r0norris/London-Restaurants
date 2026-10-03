#!/usr/bin/env python3
"""Inline data/venues.json into index.html so the page works from file:// and needs no fetch.

Re-run after any change to the data:  python3 scripts/build_venues.py && python3 scripts/build_site.py
Pass --clear to empty the block (the page then fetches data/venues.json at runtime).
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
page = ROOT / "index.html"
html = page.read_text()

if "--clear" in sys.argv:
    payload = "<!-- VENUE-DATA -->"
else:
    data = json.loads((ROOT / "data" / "venues.json").read_text())
    # Escape sequences that could end the <script> element or open an HTML comment inside it.
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/").replace("<!--", "<\\!--")

pattern = re.compile(r'(<script id="venue-data" type="application/json">)(.*?)(</script>)', re.S)
if not pattern.search(html):
    sys.exit("venue-data block not found in index.html")
html = pattern.sub(lambda m: f"{m.group(1)}\n{payload}\n{m.group(3)}", html, count=1)
page.write_text(html)
print(f"index.html: {'cleared' if '--clear' in sys.argv else 'inlined %d venues' % len(data['venues'])} ({len(html)//1024} KB)")
