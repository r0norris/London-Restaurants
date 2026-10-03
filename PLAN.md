# PLAN: London Lads' Dinner Map

Interactive map of London's top 30 chop houses and traditional fine-dining restaurants for a group of middle-aged men, with strong pubs and cocktail bars nearby. Every venue opens a dialog with deep links to its official site and booking page.

> **Claude Code: run in plan mode first.** Present the verified venue list for approval before building the UI.

---

## 1. Deliverables

| File | Purpose |
|---|---|
| `data/venues.json` | Single source of truth for every venue, plus verification evidence |
| `index.html` | Self-contained map: Leaflet + OpenStreetMap, inline CSS/JS |
| `VERIFICATION.md` | Table of each venue's trading status, source URL and check date |
| `README.md` | How to refresh data and deploy (GitHub Pages) |

**Stack:** Leaflet 1.9.x (pinned) from cdnjs, OSM tiles, vanilla JS. No build step, no framework.

**Trade-off:** Leaflet + OSM needs no API key and is free for personal-scale use. The cost is plainer styling than Google Maps and no built-in Places data such as ratings or hours. Google Maps JS would give richer data but needs a client-side API key and billing. If you go that way, restrict the key by HTTP referrer and to the Maps JS API only.

---

## 2. Data model (`venues.json`)

```json
{
  "id": "quality-chop-house",
  "name": "Quality Chop House",
  "category": "chop | fine_dining | pub | cocktail_bar",
  "highlight": true,
  "area": "Farringdon",
  "address": "",
  "lat": 0,
  "lng": 0,
  "website": "",
  "booking_url": "",
  "price_band": "££ | £££ | ££££",
  "group_notes": "private room? max table size? set menu for 8+?",
  "why": "one-line reason it made the list",
  "nearby": ["pub-id", "bar-id"],
  "status": "trading | closed | uncertain",
  "verified_on": "YYYY-MM-DD",
  "evidence_url": ""
}
```

**Hard rule:** never invent a URL, address or coordinate. If one can't be confirmed from an official or reputable source, leave it empty and set `status: "uncertain"`.

---

## 3. Verification (do this before any UI work)

For **every** venue:
1. Find the official website and confirm it's live and taking bookings or showing current menus or hours.
2. Cross-check one recent independent source, such as Hot Dinners, Time Out London, Harden's or the Michelin Guide, for closure or relocation news.
3. Check "permanently closed" signals and recent reviews from the last 3 months.
4. Record `status`, `verified_on` and `evidence_url`.
5. Exclude anything `closed`. Show `uncertain` venues greyed out with a warning badge in the dialog.

**Already checked:**
- **FKABAM (formerly Black Axe Mangal), Islington:** closed. Last service was 20 Dec 2025; the owner calls it a "pause", with occasional pop-ups. Exclude.
- **Mangal 2, Dalston:** still listed as trading, but chef Sertaç Dirik has left. Re-verify the current menu. It's a Turkish grill, not a chop house, so include it only as a "character" wildcard if at all.
- **Le Gavroche:** closed in Jan 2024 (from my knowledge, not re-checked). Do not include.

---

## 4. Restaurant selection: top 30

**Split:** about 18 chop/steak and grill venues, about 12 traditional fine-dining venues.

**Scoring (out of 10):**
- 40% food quality: Michelin, Good Food Guide or Harden's ratings
- 25% character: heritage, room, a sense of occasion
- 20% group suitability: tables of 8+, private room, takes group bookings
- 15% meat strength of the menu

**Seed candidates (unverified, so check each against section 3):**
- **Chop/steak:** Quality Chop House, St. John (Smithfield), Hawksmoor (choose the best 2–3 sites, e.g. Seven Dials, Guildhall, Borough), Blacklock (Soho, City, Shoreditch), Brat, The Guinea Grill, Goodman (Mayfair/City), Lutyens Grill at The Ned
- **Traditional fine dining:** Rules, Wiltons, The Ritz Restaurant, Simpson's in the Strand (confirm status), Scott's, Bentley's, J. Sheekey, Sweetings (lunch only; check days)

Fill the rest from current guide lists. Show the scoring table in plan mode for approval.

---

## 5. Pubs and cocktail bars

For each restaurant, find **1–2 pubs and 1–2 cocktail bars within about 10 minutes' walk (about 800 m)**. They can be shared across restaurants that are close together.

**"Really solid pub" means at least one of:**
- CAMRA Good Beer Guide (current edition)
- CAMRA National Inventory of Historic Pub Interiors
- Consistently strong recent reviews for cask beer and atmosphere

Set `highlight: true` on the standouts, which get a gold star marker. Examples to check: Ye Olde Mitre, The Lamb (Lamb's Conduit St), Ye Olde Cheshire Cheese, The Harp (Covent Garden).

**Cocktail bars:** prioritise the current World's 50 Best Bars, Top 500 Bars or Time Out lists. Same verification rules as section 3.

---

## 6. UI spec (`index.html`)

- **Map:** full-screen Leaflet, centred on central London. Marker clustering via Leaflet.markercluster (pinned, cdnjs).
- **Markers by category:**
  - Chop: red
  - Fine dining: navy
  - Pub: amber, with a star if highlighted
  - Cocktail bar: purple
- **Filter bar:** category toggles, a "highlighted only" toggle, a price band filter and an "open for groups of 8+" filter.
- **Dialog pop-out:** uses the native `<dialog>` element on marker click.
  - Name, category, area, price band, the "why" line and group notes
  - Buttons: **Website**, **Book**, **Directions** (an OSM or Google Maps link built from lat/lng)
  - All external links use `target="_blank" rel="noopener noreferrer"`
  - A "Nearby" section listing the linked pubs and bars; tapping one pans the map and opens its dialog
  - A status badge showing "Verified DD Mon YYYY" or ⚠️ Uncertain
- **List view toggle:** a sortable table of the 30 restaurants, for planning without the map.
- **Mobile-first:** viewport meta, a dialog that fills the screen on narrow widths, and touch-friendly buttons.
- **Theming:** light/dark via `prefers-color-scheme`.
- **Attribution:** keep the OSM attribution visible, as the licence requires.

---

## 7. Build phases

1. **Research and verification:** produce `venues.json` and `VERIFICATION.md`. ⛔ Stop here for approval.
2. **Geocode:** take coordinates from official sites or the OSM search page. If you script it with Nominatim, keep to 1 request per second and set a descriptive User-Agent. Spot-check 5 venues by hand.
3. **Build the UI:** create `index.html` with the data inlined at build time, or fetched from `data/venues.json` if hosted.
4. **QA:**
   - Every link resolves (scripted HEAD/GET check, logging 4xx/5xx).
   - No console errors.
   - Works at a 375 px width.
   - All 30 restaurants plus their nearby venues render.
5. **Deploy:** GitHub Pages, as a public repo or Pages from a private repo depending on your plan. No secrets are involved.

---

## 8. Acceptance criteria

- [ ] Exactly 30 restaurants, all `trading`, each with evidence dated within 30 days of build
- [ ] Every restaurant has at least 1 pub and at least 1 cocktail bar nearby
- [ ] No fabricated URLs; empty fields are flagged visibly
- [ ] Dialog deep links open the official site and booking page in a new tab
- [ ] Re-running the link checker reports zero broken links

## 9. Known limitations

- Trading status goes stale. Re-run phase 1 before any actual booking.
- Group policies change often, such as minimum spends, set menus for 8+ and deposits. Treat `group_notes` as a prompt to check with the venue, not as fact.
