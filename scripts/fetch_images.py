#!/usr/bin/env python3
"""Find a freely licensed photo for each venue on Wikimedia Commons -> data/images.json.

A photo is accepted only if ALL of these hold:
  1. It is the lead image of an English Wikipedia article found by searching the venue name.
  2. That article's coordinates are within MAX_M metres of the venue's own coordinates,
     so a chain's article or a namesake elsewhere is rejected.
  3. The file is hosted on Wikimedia Commons (free licence), not a local fair-use upload.
Credit, licence and source page are stored with every image for attribution.

Entries in OVERRIDES pin a reviewed result (a specific article, or None to suppress an image).
Re-run:  python3 scripts/fetch_images.py && python3 scripts/build_venues.py && python3 scripts/build_site.py
"""
import html, json, math, pathlib, re, sys, time, urllib.parse, urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
UA = "LondonLadsDinnerMap/1.0 (https://github.com/r0norris/London-Restaurants)"
MAX_M = 250
THUMB_W = 960
# Reviewed by hand: venue id -> Wikipedia article titles to try (still distance-checked), or None for "no image".
# Used where the search picked an area/street photo or the wrong building, or missed the right article.
OVERRIDES = {
    "st-john-smithfield": ["St. John (restaurant)"],          # search found a generic Smithfield photo
    "goodman-city": None,                                     # search found "City of London"
    "j-sheekey": ["J. Sheekey"],                              # search found The Ivy
    "lamb-tavern": ["Lamb Tavern", "Leadenhall Market"],      # search found the long-gone London Tavern
    "the-audley": ["The Audley"],                             # search found a street photo
    "quality-chop-house": ["Quality Chop House"],
    "wiltons": ["Wiltons (restaurant)", "Wiltons"],
    "lutyens-grill": ["The Ned (hotel)", "The Ned"],
    "nickel-bar": ["The Ned (hotel)", "The Ned"],
    "kerridges": ["Corinthia Hotel London", "Corinthia London"],
    "connaught-bar": ["The Connaught (hotel)", "The Connaught"],
    "goring-bar": ["The Goring (hotel)", "The Goring"],
    "hawksmoor-st-pancras": ["St Pancras Renaissance London Hotel", "Midland Grand Hotel"],
    "booking-office-1869": ["St Pancras Renaissance London Hotel", "Midland Grand Hotel"],
    "donovan-bar": ["Brown's Hotel, London"],
    "the-lamb": ["The Lamb, Bloomsbury", "The Lamb, Holborn", "The Lamb (pub)"],
    "the-salisbury": ["The Salisbury, Covent Garden", "Salisbury, St Martin's Lane"],
    "red-lion-st-james": ["Red Lion, St James's", "Red Lion, Duke of York Street"],
    "euston-tap": None,                                       # only article photo shows the arch demolished in 1962
    "arlington": ["Le Caprice"],
    "zetter-parlour": ["The Zetter Townhouse", "Zetter Hotel"],
    "seed-library": ["One Hundred Shoreditch", "Ace Hotel London Shoreditch"],
}


def api(base, **params):
    params.update(format="json", formatversion=2)
    url = base + "?" + urllib.parse.urlencode(params)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30) as r:
                return json.load(r)
        except Exception as e:  # transient network errors: back off and retry
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def wp(**p):
    time.sleep(0.5)  # be polite to the API
    return api("https://en.wikipedia.org/w/api.php", **p)


def commons(**p):
    time.sleep(0.5)
    return api("https://commons.wikimedia.org/w/api.php", **p)


def dist(a, b):
    r = math.pi / 180
    h = math.sin((b[0]-a[0])*r/2)**2 + math.cos(a[0]*r)*math.cos(b[0]*r)*math.sin((b[1]-a[1])*r/2)**2
    return 2 * 6371000 * math.asin(math.sqrt(h))


def strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()


def candidates(v):
    """Article titles to try, best first."""
    if v["id"] in OVERRIDES:
        return OVERRIDES[v["id"]] or []
    names = [v["name"], re.sub(r"^(The|Ye Olde|Ye)\s+", "", v["name"])]
    seen, out = set(), []
    for q in names:
        for hit in wp(action="query", list="search", srsearch=f'{q} London', srlimit=5)["query"]["search"]:
            if hit["title"] not in seen:
                seen.add(hit["title"]); out.append(hit["title"])
    return out


def lead_image(title, here):
    q = wp(action="query", titles=title, prop="coordinates|pageimages", piprop="name", redirects=1)
    page = q["query"]["pages"][0]
    if "missing" in page or not page.get("coordinates") or not page.get("pageimage"):
        return None, "no coords or no lead image"
    c = page["coordinates"][0]
    d = dist(here, (c["lat"], c["lon"]))
    if d > MAX_M:
        return None, f"article is {int(d)} m away"
    fname = page["pageimage"]
    ii = commons(action="query", titles="File:" + fname, prop="imageinfo",
                 iiprop="url|size|extmetadata", iiurlwidth=THUMB_W)["query"]["pages"][0]
    if "missing" in ii or not ii.get("imageinfo"):
        return None, "lead image not on Commons (likely fair use)"
    info = ii["imageinfo"][0]
    meta = info.get("extmetadata", {})
    lic = strip(meta.get("LicenseShortName", {}).get("value"))
    if not lic or "fair use" in lic.lower() or "non-free" in lic.lower():
        return None, f"licence unusable: {lic!r}"
    return {
        "src": info.get("thumburl") or info["url"],
        "width": info.get("thumbwidth") or info.get("width"),
        "height": info.get("thumbheight") or info.get("height"),
        "credit": strip(meta.get("Artist", {}).get("value")) or "Unknown author",
        "license": lic,
        "license_url": strip(meta.get("LicenseUrl", {}).get("value")),
        "file_page": info.get("descriptionurl"),
        "article": "https://en.wikipedia.org/wiki/" + urllib.parse.quote(page["title"].replace(" ", "_")),
        "article_title": page["title"],
        "article_distance_m": int(d),
    }, "ok"


def main():
    venues = json.loads((ROOT / "data" / "venues.json").read_text())["venues"]
    only = set(sys.argv[1:])
    out_path = ROOT / "data" / "images.json"
    out = json.loads(out_path.read_text()) if out_path.exists() and only else {}
    for v in venues:
        if only and v["id"] not in only:
            continue
        here = (v["lat"], v["lng"])
        found, notes = None, []
        for title in candidates(v)[:6]:
            img, why = lead_image(title, here)
            notes.append(f"{title}: {why}")
            if img:
                found = img
                break
        if found:
            out[v["id"]] = found
            print(f"OK   {v['id']:26} <- {found['article_title']} ({found['article_distance_m']} m) [{found['license']}]")
        else:
            out.pop(v["id"], None)
            print(f"--   {v['id']:26} " + "; ".join(notes[:3]))
    out_path.write_text(json.dumps(dict(sorted(out.items())), indent=2, ensure_ascii=False) + "\n")
    print(f"\n{len(out)} images written to {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
