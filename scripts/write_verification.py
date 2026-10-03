#!/usr/bin/env python3
"""Render VERIFICATION.md from data/venues.json."""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads((ROOT / "data" / "venues.json").read_text())
V = data["venues"]
by = {v["id"]: v for v in V}
CAT = {"chop": "Chop/steak", "fine_dining": "Fine dining", "pub": "Pub", "cocktail_bar": "Cocktail bar"}

def link(text, url):
    return f"[{text}]({url})" if url else "_none_"

L = [f"# Verification\n",
     f"All checks run on **{data['generated_on']}**. Re-run phase 1 before booking anything (see PLAN.md section 9).\n",
     "## Method\n",
     "- **Official site:** fetched every website and booking URL. `scripts/check_links.py` reports 0 broken. "
     "OpenTable, Caprice and Nicholson's block scripted requests, so those links were opened by hand in a browser and all resolved.",
     f"- **Independent check:** [Hot Dinners closures tracker]({data['secondary_check']['url']}), covering Jan 2025 to Sep 2026. "
     "None of the venues below appear on it. Venue-specific sources are linked in the Evidence column where they were used.",
     "- **Pubs:** status and heritage listing from CAMRA WhatPub (the Evidence links). National Inventory (NI) listings were confirmed on CAMRA pages.",
     "- **Bars:** list placings from Time Out reports of The World's 50 Best Bars 2025 and the 2026 51-100 list.",
     "- **Coordinates:** pubs from CAMRA WhatPub; restaurants and bars from OSM Nominatim (1 request/s). Spot-checked against the venue names Nominatim returned.",
     f"- **Nearby:** up to 2 pubs and 2 bars within {data['nearby_radius_m']} m of each restaurant, as the crow flies.\n",
     "## Excluded or changed during verification\n",
     "| Venue | Finding | Action |", "|---|---|---|",
     "| FKABAM (Black Axe Mangal) | Closed 20 Dec 2025 (also on the Hot Dinners tracker) | Excluded |",
     "| Le Gavroche | Closed Jan 2024 | Excluded |",
     "| Mangal 2 | Not a chop house; chef has left | Not included |",
     "| The Game Bird (The Stafford) | Replaced by Michael Caines at The Stafford (opened 17 Sep 2025) | Dropped; replaced by Boisdale of Belgravia |",
     "| Goodman Canary Wharf | Closed Jun 2025 | Only the Mayfair and City sites are used |",
     "| Christopher's (Covent Garden) | Closing end Sep 2026 to relocate | Not included |",
     "| Kwānt (Mayfair bar) | Europe's 50 Best 2026 No. 40, but its official site shows only 'Coming Soon' | Left out until the site is back |",
     "| Oriole (bar) | Has moved from Smithfield to Covent Garden | Not used for Farringdon |",
     "| Jerusalem Tavern | Renamed Holy Tavern (2022), operator changed | Not used |",
     "| Ye Grapes, Ye Olde Watling | No NI or current GBG evidence found | Not used |",
     "| sweetingsrestaurant.com | An archive/parasite site, not Sweetings' own | Real site is sweetingsrestaurant.co.uk (HTTP only) |",
     "| Guessed URLs | Several guessed Nicholson's and pub domains turned out wrong or parked (e.g. yeoldecheshirecheese.co.uk) | Website left empty and CAMRA page used as evidence |",
     "",
     "## Restaurant scoring (30)\n",
     "Weights: food 40%, character 25%, group suitability 20%, meat 15%. Group suitability is judged for **a party of five**: "
     "how easily you get a good table (online booking, lead time, deposits, no-reservations policies). Sub-scores out of 10 are **editorial judgement** "
     "informed by guide listings (Michelin, World's 101 Best Steaks 2026, Time Out), heritage, and what each venue's own site says about booking. "
     "They are not taken from any single published rating. A total of 8.5 or more sets `highlight`.\n",
     "| # | Restaurant | Type | Area | Food | Char. | Group | Meat | **Total** | Book |",
     "|---|---|---|---|---|---|---|---|---|---|"]
R = sorted((v for v in V if v["category"] in ("chop", "fine_dining")), key=lambda v: -v["score"]["total"])
for n, v in enumerate(R, 1):
    s = v["score"]
    L.append(f"| {n} | {link(v['name'], v['website'])} | {CAT[v['category']]} | {v['area']} | {s['food']} | {s['character']} | "
             f"{s['group']} | {s['meat']} | **{s['total']}** | "
             f"{link('book', v['booking_url']) if v['booking_url'] else '⚠️ phone/email'} |")
L += ["", f"Split: {sum(v['category']=='chop' for v in R)} chop/steak, {sum(v['category']=='fine_dining' for v in R)} fine dining.\n",
      "## Trading status: every venue\n",
      "| Venue | Type | Status | Checked | Evidence | Nearby (m) |", "|---|---|---|---|---|---|"]
for v in R + sorted((v for v in V if v["category"] in ("pub", "cocktail_bar")), key=lambda v: (v["category"], v["name"])):
    near = ", ".join(f"{by[k]['name']} {d}" for k, d in v.get("nearby_distances_m", {}).items())
    star = " ★" if v["highlight"] and v["category"] == "pub" else ""
    L.append(f"| {v['name']}{star} | {CAT[v['category']]} | {v['status']} | {v['verified_on']} | {link('source', v['evidence_url'])} | {near} |")
L += ["", "## Empty fields (flagged in the UI)\n"]
for v in V:
    miss = [f for f in ("website", "booking_url") if not v[f] and not (v["category"] in ("pub", "cocktail_bar") and f == "booking_url")]
    if miss:
        L.append(f"- **{v['name']}**: no {' or '.join(miss)} confirmed. {v.get('group_notes') or 'See the CAMRA evidence link.'}")
L += ["", "## Photo credits\n",
      "Photos are freely licensed images from Wikimedia Commons, hotlinked from upload.wikimedia.org. Each one is the lead image of a "
      "Wikipedia article whose coordinates are within 250 m of the venue (`scripts/fetch_images.py`). Where a venue sits inside a larger "
      "building (hotel bars, Leadenhall Market), the photo shows that building, and the dialog says what is pictured.\n",
      "| Venue | Pictured | Credit | Licence |", "|---|---|---|---|"]
for v in sorted((v for v in V if v.get("image")), key=lambda v: v["name"]):
    im = v["image"]
    lic = f"[{im['license']}]({im['license_url']})" if im.get("license_url") else im["license"]
    L.append(f"| {v['name']} | [{im['article_title']}]({im['file_page']}) | {im['credit']} | {lic} |")
L.append(f"\n{sum(1 for v in V if not v.get('image'))} venues have no photo, because no freely licensed image of the venue itself could be confirmed.")
L += ["", "## Caveats\n",
      "- Michelin star counts are not quoted. Sources disagreed (e.g. Brat), so venues are just described as 'Michelin-starred'.",
      "- `group_notes` come from each venue's own site on the check date. Treat them as prompts to call, not as fact.",
      "- Sweetings is lunch-only and takes no bookings, so it is a weekday-lunch option, not a group dinner.",
      "- Distances are straight-line. Walking routes are 10-30% longer."]
(ROOT / "VERIFICATION.md").write_text("\n".join(L) + "\n")
print("wrote VERIFICATION.md")
